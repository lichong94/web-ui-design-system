#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统一 Web 前端设计规范自动化审计脚本 (Web Design Linter)

合并自 B 端设计规范、移动端设计规范两套规则，覆盖 React / Vue / TSX / H5 / HTML。
规则分三组：
- shared：三端通用（粗边框、按钮固定宽度、紧缩行高、卡片大阴影、缺失聚焦环等）
- b-end：企业后台专属（危险按钮样式、弹窗防丢、数值右对齐、占位废话等）
- mobile：移动端专属（安全区避让、键盘 inputmode、滚动穿透、表格暴力移植等）

用法：
    python audit_web_design.py <目标目录或文件> [--platform all|b-end|mobile]

退出码：
    0  已检查且未检测到违规
    1  检测到违规，或文件/目录读取失败
    2  目标不存在、文件类型不受支持，或目录中没有受支持的源码文件
"""

import sys
import os
import re
from pathlib import Path

# ---------------------------------------------------------------------------
# 规则定义：id / name / severity / group / pattern / message
# group 取值：shared（三端通用）、b-end（B 端）、mobile（移动端）
# ---------------------------------------------------------------------------
RULES = [
    # ===== 三端通用规则 =====
    {
        "id": "WEB-001",
        "group": "shared",
        "name": "粗黑边框与硬编码纯黑",
        "severity": "WARNING",
        "pattern": r"(border-(?:black|gray-800|gray-900)|1px\s+solid\s+#000000|1px\s+solid\s+black)",
        "message": "检测到粗黑或深黑硬编码边框。现代界面推荐使用 0.5px 精细微边框或半透明边框（如 border-slate-200/70）。",
    },
    {
        "id": "WEB-002",
        "group": "shared",
        "name": "操作按钮写死固定宽度（出海短词膨胀隐患）",
        "severity": "WARNING",
        "pattern": r"<(?:button|Button)[^>]*?\b(?:w-20|w-16|w-24|w-\[80px\]|w-\[72px\])\b",
        "message": "检测到操作按钮写死固定像素宽度。欧系多语言短词翻译后长度暴涨 2-3 倍（短词膨胀定律），按钮应使用弹性填充（flex-1）或 min-w + px 自适应。",
    },
    {
        "id": "WEB-003",
        "group": "shared",
        "name": "紧缩行高导致多语言变音符号削顶隐患",
        "severity": "WARNING",
        "pattern": r"\b(?:leading-none|leading-tight|line-height:\s*1(?:px|rem|em|;)|\bleading-\[1\])\b",
        "message": "检测到紧缩行高。泰语、越南语、阿拉伯语等带有上下变音符号，过紧行高会被削顶削底，出海多语言建议行高 >= 1.5。",
    },
    {
        "id": "WEB-004",
        "group": "shared",
        "name": "常规内容卡片滥用大阴影（违背页面默认平原则）",
        "severity": "WARNING",
        "pattern": r"<(?:Card|\w+Card)[^>]*?\b(?:shadow-lg|shadow-xl|shadow-2xl)\b",
        "message": "检测到常规卡片使用了大阴影。根据页面默认平原则，卡片应默认纯平用 0.5px/1px 微边框切分，大阴影仅留给真实浮层（Modal/Popover/Drawer/BottomSheet）。",
    },
    {
        "id": "WEB-005",
        "group": "shared",
        "name": "裸写 outline-none 且缺失键盘聚焦外框（违反按钮完整态与 WCAG）",
        "severity": "WARNING",
        "pattern": r"<(?:button|Button|a|input|select)[^>]*?\b(?:outline-none|focus:outline-none)\b(?![^>]*?\b(?:focus-visible:ring|focus:ring)\b)",
        "message": "检测到清除了默认 outline 但未补充 focus-visible:ring 聚焦环。键盘 Tab 导航用户将彻底丢失焦点位置，必须为交互控件补齐 Focus 态。",
    },

    # ===== B 端后台专属规则 =====
    {
        "id": "BE-001",
        "group": "b-end",
        "name": "危险操作样式违规",
        "severity": "ERROR",
        "pattern": r'(?:variant=["\']primary["\'][^>]*?(?:bg-red|text-red|bg-rose)|btn-primary[^>]*?(?:danger|delete))',
        "message": "检测到危险操作试图通过 primary 按钮涂红实现。必须使用标准 variant=\"danger\"，且高危操作需配二次确认。",
    },
    {
        "id": "BE-002",
        "group": "b-end",
        "name": "表单弹窗误触遮罩易丢数据",
        "severity": "ERROR",
        "pattern": r'(?:<Dialog|<Modal|<ConfirmDialog)[^>]*?maskClosable\s*=\s*\{?true\}?',
        "message": "含录入或确认的弹窗开启了 maskClosable={true}，用户误触空白处易造成数据丢失。必须显式设为 false。",
    },
    {
        "id": "BE-003",
        "group": "b-end",
        "name": "占位说明废话",
        "severity": "WARNING",
        "pattern": r'(?:这里展示了所有|请在这里输入该|用于展示.*?列表的信息)',
        "message": "检测到冗余占位废话。卡片与表单应去除无意义副标题，依靠排版层级与精准标签本身说话。",
    },
    {
        "id": "BE-004",
        "group": "b-end",
        "name": "表格金额或数值未右对齐",
        "severity": "WARNING",
        "pattern": r'(?:金额|价格|签约额|收入|支出|总额)[^<]*?</th>\s*<td(?![^>]*?text-right)',
        "message": "检测到金额或财务数值列未采用 text-right 右对齐。必须右对齐以保证个十百千数位垂直对齐。",
    },

    # ===== 移动端专属规则 =====
    {
        "id": "MB-001",
        "group": "mobile",
        "name": "底部安全区丢失",
        "severity": "ERROR",
        "pattern": r'fixed\b[^>]*?\bbottom-0\b',
        "message": "检测到底部固定定位吸底容器 (fixed bottom-0) 未配置 env(safe-area-inset-bottom) 安全区避让。在全面屏上会导致主按钮被系统 Home Bar 遮挡并引发误触。",
    },
    {
        "id": "MB-002",
        "group": "mobile",
        "name": "移动端输入框缺少精准键盘声明",
        "severity": "WARNING",
        "pattern": r'<input\b',
        "message": "手机号/验证码/金额字段需配置对应 inputmode：tel、numeric、decimal、email、search；验证码追加 autocomplete=\"one-time-code\"。",
    },
    {
        "id": "MB-003",
        "group": "mobile",
        "name": "浮层开启遮罩点击易丢失数据",
        "severity": "ERROR",
        "pattern": r'(?:<BottomSheet|<Drawer|<Modal|<Dialog)[^>]*?maskClosable\s*=\s*\{?true\}?',
        "message": "移动端浮层开启了 maskClosable={true}。用户手滑极易误触背景导致正在录入或核对的数据丢失。",
    },
    {
        "id": "MB-004",
        "group": "mobile",
        "name": "移动端暴力移植复杂表格",
        "severity": "WARNING",
        "pattern": r'<table\b[^>]*>',
        "message": "检测到移动端代码直接使用了 <table> 标签。移动端屏幕极窄，强塞表格会导致整屏横向晃动；必须转换为纵向结构化信息卡片 (Card)。",
    },
]

# MB-002 需要二次判断：仅当字段名像手机号/验证码时才告警
MOB_INPUT_PATTERN = re.compile(r'(?:phone|mobile|tel|otp|verify|sms)', re.IGNORECASE)
MOB_INPUTMODE_PATTERN = re.compile(r'inputmode\s*=\s*["\'](?:tel|numeric|decimal|email|search)["\']', re.IGNORECASE)


def select_rules(platform: str):
    """根据平台参数筛选规则组。"""
    if platform == "b-end":
        groups = {"shared", "b-end"}
    elif platform == "mobile":
        groups = {"shared", "mobile"}
    else:
        groups = {"shared", "b-end", "mobile"}
    return [rule for rule in RULES if rule["group"] in groups]


def audit_file(file_path: Path, rules):
    violations = []
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return [{"id": "IO-ERR", "line": 0, "rule": "读取失败", "severity": "ERROR", "message": str(e)}]

    lines = content.splitlines()
    for rule in rules:
        for idx, line in enumerate(lines, start=1):
            # MB-002 二次判断：字段名不匹配则跳过
            if rule["id"] == "MB-002":
                if not MOB_INPUT_PATTERN.search(line) or MOB_INPUTMODE_PATTERN.search(line):
                    continue
            if re.search(rule["pattern"], line, re.IGNORECASE):
                violations.append({
                    "id": rule["id"],
                    "line": idx,
                    "rule": rule["name"],
                    "severity": rule["severity"],
                    "message": rule["message"],
                    "code_snippet": line.strip()[:80],
                })
    return violations


def main():
    platform = "all"
    args = []
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg.startswith("--platform="):
            platform = arg.split("=", 1)[1]
        elif arg == "--platform":
            platform = sys.argv[i + 1]
            i += 1
        else:
            args.append(arg)
        i += 1

    target = args[0] if args else "."
    target_path = Path(target).resolve()

    if not target_path.exists():
        print(f"目标不存在：{target_path}", file=sys.stderr)
        sys.exit(2)

    extensions = (".tsx", ".jsx", ".vue", ".html")
    files_to_check = []
    if target_path.is_file():
        if target_path.suffix.lower() not in extensions:
            print(f"不支持的源码文件类型：{target_path}", file=sys.stderr)
            sys.exit(2)
        files_to_check.append(target_path)
    else:
        scan_errors = []
        for directory, _, filenames in os.walk(target_path, onerror=scan_errors.append):
            files_to_check.extend(
                Path(directory) / name for name in filenames
                if Path(name).suffix.lower() in extensions
            )
        if scan_errors:
            for error in scan_errors:
                print(f"目录扫描失败：{error}", file=sys.stderr)
            sys.exit(1)

    rules = select_rules(platform)
    total_violations = 0
    print(f"[Web Design Linter] 走查设计规范（平台：{platform}）：{target_path}")
    print(f"发现目标待测代码文件：{len(files_to_check)} 个\n")

    if not files_to_check:
        print("未找到受支持的源码文件（.tsx、.jsx、.vue、.html）。", file=sys.stderr)
        sys.exit(2)

    for f in files_to_check:
        results = audit_file(f, rules)
        if results:
            print(f"文件：{f.relative_to(target_path) if target_path.is_dir() else f.name}")
            for r in results:
                total_violations += 1
                color_tag = "[ERROR]" if r["severity"] == "ERROR" else "[WARN]"
                print(f"  Line {r['line']} {color_tag} ({r['id']} {r['rule']})：{r['message']}")
                if "code_snippet" in r:
                    print(f"    代码片段：`{r['code_snippet']}`")
            print()

    if total_violations == 0:
        print("走查完成，未检测到已实现规则覆盖的违规项；仍需人工设计走查。")
        sys.exit(0)
    else:
        print(f"走查完成，共发现 {total_violations} 处需优化的设计或交互项。")
        sys.exit(1)


if __name__ == "__main__":
    main()
