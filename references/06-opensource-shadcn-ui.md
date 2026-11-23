# shadcn/ui（React 可复制式组件库）

## 基本信息

| 项目 | 内容 |
| --- | --- |
| 仓库 | https://github.com/shadcn-ui/ui |
| 官方文档 | https://ui.shadcn.com |
| 默认分支 | main |
| 主要语言 | TypeScript |
| 协议 | MIT |
| 星标（2026-11-21 检索值，会随时间变动） | 约 12.87 万 |
| 技术栈 | React + Tailwind CSS + Radix UI，支持 Next.js / Vite 等 |

## 定位

一套设计精美、可自定义、可扩展、可在其之上搭建自有组件库的组件集合。
与传统“安装一个 npm 包再调用”的组件库不同，shadcn/ui 的模式是把组件源码直接复制进项目，开发者可以随意修改、扩展，组件代码归项目自己所有。官方原话：“Open Source. Open Code. Use this to build your own component library.”

## 核心特点（来自官方 README 与仓库元数据）

- 组合式、可访问性（无障碍）良好的组件，默认设计经过考量。
- 基于 Radix UI 无头原语与 Tailwind CSS，样式可深度定制。
- 生态活跃，文档、示例、第三方集成（Next.js、Vite、Laravel、TanStack 等）齐全。
- 主题、暗色模式、表单、表格、弹窗、导航等常见界面组件覆盖较全。

## 适用场景

- React / Next.js 产品站、中后台、管理系统。
- 希望组件代码可自主掌控、便于二次改造的项目。
- 需要一套现代、Tailwind 风格且社区资料丰富的组件基础。

## 上手要点

- 文档站点：https://ui.shadcn.com/docs 。
- 典型集成方式：在已有 React + Tailwind 项目中按文档初始化 shadcn，再按需把单个组件添加进项目源码。
- 组件不是作为封闭依赖发布，而是复制进项目后由项目自行维护。

## 注意事项

- 属于 React 技术栈；Vue、PHP 传统页面不能直接安装使用，只能参考其版式与交互设计。
- 星标与组件数量以官方文档和仓库实时信息为准，本文件记录的是检索时点的近似值。
