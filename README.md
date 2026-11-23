# web-ui-design-system · 全端自适应前端 UI 设计系统

一套面向 AI 编程助手与前端开发者的**可执行设计规范与工程约束**：不按端型拆成多套手册，而是先探测目标环境与任务形态，自动套用对应条款，一套规则同时适配宽屏后台 / SaaS 工作台、手机 App / 小程序 / H5 触屏窄屏、桌面 Agent / AI 对话工作台三类场景。规范对标 Linear 官网与 Apple Notes 的极简克制风格。

## 特性

- **一套规范按环境自适应**：通过核心对象、典型视口、操作节奏、输入方式四个信号判定场景，再套用对应骨架与条款；跨端界面以主场景为基线，按响应式断点逐级降级。
- **共享视觉基石**：0.5px 微边框、同心圆角、4px 间距栅格、自适应字阶、按钮六态、Badge 浅底深字、单一强调色、去 AI 味四纯粹性。
- **组件与浮层选型**：否定判据与决策树，区分 Modal / Drawer / Popconfirm / 页面跳转、Bottom Sheet / ActionSheet / 分栏面板。
- **交互、动效与工程避坑**：触控热区、安全区、软键盘、手势与滚动、穿透锁死、中文输入法守卫、增高输入框、视口跟随、分栏多窗口；16 种常见动效 + 15 种加载态动效词典；弱网、低算力与户外降级。
- **可访问性与工程架构**：WCAG 2.1 AA / ARIA、组件拆分与职责、状态管理最简阶梯、参考图转设计契约。
- **交付门禁**：102 项自查清单（通用基线 48、宽屏后台 10、触屏窄屏 22、桌面 Agent 22），配规则扫描脚本与阴影裁切审计脚本。

## 目录结构

```text
web-ui-design-system/
├── SKILL.md                          # 元数据、核心指令、工作流、硬红线与导航
├── references/
│   ├── 01-foundations-and-tokens.md   # 视觉基石、设计 Token、按钮六态、去 AI 味、i18n/RTL、WCAG/ARIA
│   ├── 02-layout-patterns.md         # 自适应骨架、布局模式、落地页 Bento、参考图转设计契约
│   ├── 03-components-and-overlays.md # 组件选型、浮层决策树、弹层原点与 Tooltip 时机
│   ├── 04-interaction-and-engineering.md # 交互手感、动效决策、手势细节、组件架构与状态阶梯
│   ├── 05-audit-checklist.md         # 交付前自查门禁清单
│   ├── 06~11-opensource-*.md         # 6 篇开源组件库 / 模板 / 脚手架选型目录
├── scripts/
│   ├── audit_web_design.py           # Python 规则扫描脚本（仅标准库，无需 pip 安装）
│   └── clip-audit.js                 # 桌面阴影裁切审计脚本
└── templates/
    ├── web-admin/（4 个 TSX：列表 / 表单 / 详情 / 看板）
    └── mobile/（4 个 TSX：信息流 / 底部抽屉 / 紧凑表单 / 标签栏外壳）
```

## 适用与不适用

**适用**：新建前端项目、官网 / 后台 / SaaS 工作台 / H5 / 小程序 / 桌面应用页面；页面 UI 设计与生成；组件搭建与选型；代码审查与 UI 走查；响应式降级、多语言与 RTL 适配。

**不适用**：纯后端逻辑、数据库脚本、命令行工具、无界面脚本任务；不负责后端接口实现、数据建模与部署运维；不绑定特定组件库，也不提供 `package.json`、开发服务器、CSS 入口或 Tailwind 配置。

## 模板与脚本前提

- 模板为 React + TypeScript 的 TSX 组件，接入项目需已有 JSX/TSX 编译环境；图标使用 `lucide-react`，样式基于 Tailwind CSS。
- Python 扫描脚本仅用 Python 3 标准库；JS 审计脚本在浏览器 DevTools 或 Playwright 评估环境中运行。
- 规则扫描为正则初筛，不能替代完整人工设计走查。

## 技术栈中立

本技能不预设、不绑定任何组件库或设计系统：shadcn/ui、Ant Design、Radix UI、Tailwind CSS、原生自绘均可适配。已有项目直接沿用其成熟设计系统与组件库，不为风格统一强行引入第二套重复库。

## 作为豆包技能使用

将本目录整体放入豆包技能目录（`.user_skills/`），保留根级 `SKILL.md`；技能按 `SKILL.md` 中的探测流程与参考手册导航按需读取条款。

## 许可

[MIT License](./LICENSE)
