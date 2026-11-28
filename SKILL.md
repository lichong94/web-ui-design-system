---
name: web-ui-design-system
description: 统一自适应的全端前端页面 UI 设计系统与工程规范，一套规则自动适配宽屏后台/SaaS 工作台、手机 App/小程序/H5 触屏窄屏、桌面 Agent/AI 对话工作台三类场景。当任务涉及任何网站开发、新建前端项目、页面 UI 设计与生成、界面搭建、组件选型、高保真原型还原、页面代码审查或 UI 走查验收时，必须自动调用本技能。典型触发：生成后台列表页/表单页/详情页/数据看板、开发手机 App 或小程序页面、搭建桌面 AI 对话工作台、设计组件与浮层、审查前端页面配色/圆角/边框/按钮状态/表格对齐/安全区/触控热区/软键盘/阴影裁切/输入法与滚动体验，以及响应式降级、出海多语言与 RTL 适配。规范对标 Linear 与 Apple Notes 极简克制风格，含可复用 TSX 模板、Python 规则扫描脚本与桌面阴影裁切审计脚本；另附 6 个开源 React/Vue 组件库、落地页模板、SaaS 全栈脚手架、后台仪表盘模板与动效组件的选型目录，用于从零起步时挑选外部成熟方案。
---

# 全端自适应前端 UI 设计系统

本技能是面向 AI 编程助手的可执行设计规范指令层，把资深 UI/UX 设计师与前端工程经验转化为可严格执行的生成与审查约束。**一套规范、按环境自适应**：不按端型拆成多套手册，而是先探测目标环境与任务形态，自动套用对应条款。一切对标 **Linear 官网与 Apple Notes 的极致简洁**：简单目的、简单架构、简单设计、简单实现；每个决策必须同时提升 **UX（用户体验）、DX（开发者体验）、AX（智能体体验）**。

## 何时必须调用

只要任务包含以下任意一类，即按本技能执行，无需用户再次提醒：

- **网站与项目开发**：新建前端项目、搭建官网/后台/SaaS 工作台/H5/小程序/桌面应用的页面与界面；
- **页面 UI 设计与生成**：列表、表单、详情、看板、设置、空态/异常页、信息流、详情流、对话工作台、分栏面板；
- **组件搭建与选型**：按钮、徽标、输入控件、表格、筛选、抽屉/弹窗/底部抽屉、导航、输入框、工具卡、产物面板；
- **代码审查与走查**：配色、边框、圆角、阴影、按钮状态、表格对齐、安全区、触控热区、软键盘、滚动穿透、阴影裁切、输入法误发、动效与空态覆盖；
- **响应式与出海**：跨视口断点降级、多语言短词膨胀、音标防削顶、阿拉伯语 RTL 与 LTR 特例。

> 纯后端逻辑、数据库脚本、命令行工具、无界面脚本任务不调用本技能。

## 环境自适应探测流程

动手前先按下面四个信号识别目标环境与任务形态，再从参考手册中取对应条款；同一界面跨端适配时，以主场景为基线，按响应式断点逐级降级。

```text
收到页面 UI 任务
        │
        ├── 探测信号：核心对象 / 典型视口 / 操作节奏 / 输入方式
        │
        ├── 数据密集型（宽屏后台 / SaaS 工作台）
        │       信号：表格字段批量记录；≥1024px；检索筛选批量处理；鼠标键盘
        │       套用：02 篇第二节骨架、03 篇宽屏组件、05 篇第二节附加门禁
        │
        ├── 触屏信息流型（App / 小程序 / 响应式 H5）
        │       信号：卡片条目媒体内容；≤480px 竖屏；拇指滑动浏览单点操作；触控
        │       套用：02 篇第三节骨架、03 篇窄屏浮层、04 篇触控/键盘/手势、05 篇第三节附加门禁
        │
        └── 对话工作台型（桌面 Agent / AI 应用）
                信号：会话消息工具调用产物；桌面窗口可分栏；流式等待授权介入；键鼠
                套用：02 篇第四节四层分层、04 篇输入框/视口跟随/分栏多窗口/动效、05 篇第四节附加门禁

共享视觉法则、Token、排版、按钮态、去 AI 味、i18n → 01 篇（所有场景始终适用）
```

跨端响应式后台同时适配窄屏时，以宽屏骨架为基线，按 [02-layout-patterns.md](./references/02-layout-patterns.md) 第五节断点逐级降级。

## 标准执行工作流

1. **需求解构**：抽取实体角色、核心对象、操作频次、生命周期状态与目标环境；
2. **环境探测**：按上方四信号判定场景，确定骨架类型与适用条款；
3. **布局骨架**：套用对应场景骨架（宽屏 PageHeader→FilterPanel→DataSection→BulkActionBar；窄屏 TopBar→Tabs→Feed/表单；工作台 对话层→过程层→工具卡→产物层）；
4. **选型判据**：执行否定判据确定 Modal / Drawer / Popconfirm / Page，或 Bottom Sheet / ActionSheet，或分栏/产物面板；
5. **原子约束**：坚守共享基石——0.5px 微边框、同心圆角、4px 栅格、按钮六态、Badge 浅底深字、单一强调色；
6. **闭环走查**：对照 `references/05-audit-checklist.md` 通用基线 + 场景附加项逐条核对，必要时运行审计脚本，全部通过后交付。

## 必须遵守的共享硬红线（速览）

完整规则见 `references/01-foundations-and-tokens.md`，以下为任何环境都不可突破的底线：

1. **禁止粗黑边框与机械居中**：分割线/卡片边框用 0.5px 微边框；嵌套容器满足同心圆角 $R_{outer}=R_{inner}+Padding$；图标+文字按光学重心微调，弹窗垂直偏上至 38.2% 黄金分割位。
2. **主操作唯一与审批中立**：一个独立操作区最多 1 个 Primary 主按钮；审批通过/驳回均用次级样式，严禁视觉色差诱导。
3. **浮层防丢失与破坏性阻力**：含录入表单的浮层必须 `maskClosable={false}`；查看详情优先抽屉/同页展开保留上下文；删除、清空、扣费必须走确认对话框，标题中立交代对象，按钮用动宾文案。
4. **页面默认平、单一强调色、字号 ≤4 档**：常规卡片纯平用微边框切分，阴影只留给离屏浮层；全页仅一个强调色，其余收敛暖中性灰；字号严格 4 档以内，桌面最小 12px。
5. **按钮六态齐全**：Default / Hover / Active / Disabled / Loading（转圈 + 锁点击防重复提交）/ Focus-visible（键盘聚焦环，严禁裸删 `outline`）。
6. **出海防护**：按钮不写死固定像素宽度；多语言行高 ≥1.5 且不滥用 `overflow: hidden` 削音标；RTL 用逻辑属性，进度条/电话/数字/代码块强制 LTR。
7. **去 AI 味**：删除标语、占位副标题与无意义 eyebrow 标签，让布局自体自解释；低频说明用 Tooltip/Alert 折叠；规则与 Token 外置，复用成熟组件库，不从零手搓轮子。

## 参考手册导航（按主题按需读取，不要每次全量加载）

| 手册 | 内容 | 何时读 |
| --- | --- | --- |
| [01-foundations-and-tokens.md](./references/01-foundations-and-tokens.md) | 色彩/圆角/阴影/间距 Token、0.5px 边框、同心圆角、自适应字阶、按钮六态与五档层级、点赞爆粒子/提交三连变/果冻开关/长按确认四模式契约、Badge 映射、去 AI 味四纯粹性与观感对照、i18n/RTL、AX 协作协议、WCAG 2.1 AA / ARIA 可访问性 | 所有 UI 任务的共享底线；写组件、定视觉规范、设计按钮与控件微交互、补齐可访问性时查阅 |
| [02-layout-patterns.md](./references/02-layout-patterns.md) | 环境探测与骨架选型；宽屏列表/表单/详情/看板/设置/登录认证页骨架（含图表聚焦与直接标注、行业场景分栏）；窄屏信息流/详情/向导/个人中心骨架；工作台四层正交分层；演示页一页一观点骨架；官网落地页与 Bento 便当盒布局；响应式降级断点；五态覆盖；参考图转设计契约 | 确定页面结构、布局拓扑、看板图表、登录页、演示页、跨端降级与参考稿提炼时 |
| [03-components-and-overlays.md](./references/03-components-and-overlays.md) | 六大否定判据、输入选择控件选型、浮层决策树与尺寸、Modal/AlertDialog 阻断分级、Bottom Sheet 分档吸附、ActionSheet、Snackbar 撤销条、Tour 引导、Inline Alert 行内校验、Lightbox 灯箱、复合组件、导航选型与侧边栏分组/高亮/低频项固定细则 | 选组件、定浮层形态、处理反馈提示、表格、导航与侧边栏整理时 |
| [04-interaction-and-engineering.md](./references/04-interaction-and-engineering.md) | 触控热区与拇指区、安全区、软键盘、手势与滚动手感（速度阈值/指针捕获/多点保护/边界阻尼）、穿透锁死、CJK 输入法守卫、自适应增高输入框、视口跟随、分栏多窗口、阴影裁切/滚动槽位/原生语义避坑、动效频率决策、时长/缓动/性能铁律、16 种常见动效模式词典、15 种加载态动效词典、骨架屏双模、组件架构与状态管理阶梯、弱网低算力降级 | 处理交互手感、输入体验、滚动窗口工程、动效与加载等待态选型、组件拆分与状态选型时 |
| [05-audit-checklist.md](./references/05-audit-checklist.md) | 通用基线 48 项 + 宽屏后台 12 项 + 触屏窄屏 22 项 + 桌面 Agent 22 项交付门禁、复核三列表格格式与最小交付证明记录 | 代码生成后自查、评审、交付验收时逐条核对 |

## 开源 UI 套件选型参考（从零起步时查阅）

下列 6 个项目为 GitHub 星标筛选的开源外部方案，仅用于**从零起步、尚未建立技术栈**时挑选组件库/模板/脚手架；**已有项目一律沿用其现有设计系统与组件库**，不为风格统一强行引入第二套重复库。每份文档含仓库链接、技术栈、协议、功能要点、上手命令与注意事项，按需读取，不要全量加载。星标为 2026-11-21 检索时点近似值，组件清单与协议以各仓库实时信息为准。

| 场景 | 项目 | 技术栈 | 参考文档 |
| --- | --- | --- | --- |
| React/Next.js 产品站、中后台，需可自主改造的组件 | shadcn/ui | React + Tailwind + Radix | `references/06-opensource-shadcn-ui.md` |
| 公司官网、产品/营销落地页，改文案图片即可上线 | Cruip Simple Light | React/Next.js + Tailwind（GPL，不可转售模板） | `references/07-opensource-cruip-landing.md` |
| 带登录、团队/多租户、权限、国际化的付费 SaaS 产品 | SaaS-Boilerplate | Next.js + React 19 + Tailwind + Shadcn | `references/08-opensource-saas-boilerplate.md` |
| Vue 3 中后台、数据密集型系统 | Naive UI | Vue 3 + TypeScript | `references/09-opensource-naive-ui.md` |
| 官网/首页需滚动动画、氛围感动效组件 | Magic UI | React + Tailwind + Framer Motion | `references/10-opensource-magicui.md` |
| 快速搭建 Material 风格后台仪表盘骨架 | Devias Kit - React | React + Next.js + MUI | `references/11-opensource-material-kit-react.md` |

组合建议：官网/宣传页先用 Cruip 模板，缺动效补 Magic UI；React 中后台组件选 shadcn/ui，仪表盘布局参考 Devias Kit；Vue 中后台选 Naive UI；完整 SaaS 产品基于 SaaS-Boilerplate 二次开发。除 Naive UI 属 Vue 外，其余均为 React/Next.js 工程化项目；PHP/ThinkPHP 传统页面不能直接安装其中组件，只能参考版式与交互。

## 开箱即用模板

`templates/` 目录提供参考 TSX 组件，按目标场景选用，可直接复制改造。**模板前提**：业务应用需已有 React + TypeScript 与 JSX/TSX 编译，安装 `lucide-react`，并配置 Tailwind CSS；本技能不提供 `package.json`、开发服务器、CSS 入口或 Tailwind 配置。接入真实业务数据前，检查示例数据、操作处理与校验逻辑，并运行业务项目已有构建检查确认图标与样式正确呈现。

### 宽屏后台模板（`templates/web-admin/`）

| 文件 | 内容 |
| --- | --- |
| `list-page-template.tsx` | 标准查询表格 + 批量浮条 + 抽屉轻编辑 + 确认删除弹窗 |
| `form-page-template.tsx` | Top-aligned 标签置顶 + 卡片语义分组 + 离开防丢脏检查 |
| `detail-page-template.tsx` | DetailHeader + DescriptionGrid + Tabs 辅助页签 + 审计时间线 |
| `dashboard-page-template.tsx` | 问候语 + 4 个核心 KPI 趋势卡 + 轻量原生柱状图 + 快捷直通 |
| `login-page-template.tsx` | 宽屏左右分栏：行业场景面板 + 登录表单；密码可见切换、行内校验、加载锁按钮、窄屏降级 |

### 触屏窄屏模板（`templates/mobile/`）

| 文件 | 内容 |
| --- | --- |
| `mobile-feed-list-template.tsx` | 安全区避让 + 搜索吸顶 + 16:9 裁切 + 下拉刷新与触底加载流 |
| `mobile-bottom-sheet-template.tsx` | 顶部拖拽条 + 三分屏高度 + 底层滚动彻底锁死 + 确定取消动作 |
| `mobile-compact-form-template.tsx` | 聚焦居中防遮挡 + inputmode 精准映射 + 底部全宽主按钮 |
| `mobile-tabbar-app-shell.tsx` | 标准 4 槽位 TabBar + 未读数红点 + 毛玻璃材质外壳 |

## 自动化校验脚本

### Python 规则扫描（宽屏 / 触屏代码）

扫描 `.tsx / .jsx / .vue / .html`，按场景分组检查粗边框、按钮固定宽度、紧缩行高、卡片大阴影、缺失聚焦环、危险按钮样式、弹窗防丢、数值右对齐、安全区、键盘声明、表格暴力移植等规则。使用脚本安装目录的绝对路径执行：

```bash
# 全场景规则
python3 "<技能目录>/scripts/audit_web_design.py" "<待扫描项目目录>"

# 仅宽屏后台规则（含共享规则）
python3 "<技能目录>/scripts/audit_web_design.py" "<项目目录>" --platform b-end

# 仅触屏窄屏规则（含共享规则）
python3 "<技能目录>/scripts/audit_web_design.py" "<项目目录>" --platform mobile
```

退出码：`0` 已检查且无违规；`1` 检测到违规或读取失败；`2` 目标不存在、类型不支持或无受支持文件。正则检查仅覆盖已实现规则，不能替代完整人工设计走查。脚本仅用 Python 3 标准库，无需 pip 安装。

### 桌面阴影裁切审计（`scripts/clip-audit.js`）

涉及 `box-shadow`、`drop-shadow`、无边框透明窗口或带 `overflow: hidden` / `clip-path` 容器时，在浏览器 DevTools `evaluate_script` 或 Playwright `browser_evaluate` 中运行；透明/无边框窗口传 `{ viewport: true }`，指定范围传 `{ root: '.screen' }`。默认静态态、hover 态、展开态、动效落点态分别运行，**硬门禁为 `cut === 0`**。注意脚本不检查 root 容器自身投影，检查某卡片时 root 须指定为其父级容器。详见 [04-interaction-and-engineering.md](./references/04-interaction-and-engineering.md) 第十节。

## 技术栈与设计系统中立原则

- 本技能不预设、不绑定任何特定组件库或设计系统：shadcn/ui、Ant Design、Radix UI、Tailwind CSS、原生自绘均通用；
- **已有项目直接沿用其成熟设计系统与组件库**，严禁为“风格统一”强行引入第二套重复库或重构；
- 从零起步且未检测到既定设计系统时，先询问用户偏好；若需复刻 Claude 桌面设计风格，指引至上游 `github.com/Caho1/open-claude-ui` 与 openclaudeui.com 获取 Token 与参考组件。
