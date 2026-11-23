# Naive UI（Vue 3 组件库）

## 基本信息

| 项目 | 内容 |
| --- | --- |
| 仓库 | https://github.com/tusen-ai/naive-ui |
| 官方文档 | https://www.naiveui.com |
| 默认分支 | main |
| 主要语言 | TypeScript |
| 协议 | MIT（`result` 组件图形资源为 CC-BY 4.0，来自 Twemoji） |
| 星标（2026-11-21 检索值，会随时间变动） | 约 1.86 万 |
| 技术栈 | Vue 3 + TypeScript |

## 定位

一套 Vue 3 组件库，官方关键词：相当完整、主题可定制、使用 TypeScript、性能快（Fairly Complete, Theme Customizable, Uses TypeScript, Fast）。

## 核心特点（来自官方 README）

- **组件较全**：提供 90+ 组件，全部支持 Tree Shaking（按需打包）。
- **主题可定制**：基于 TypeScript 构建类型安全的高级主题系统，只需传入主题覆盖对象即可；不依赖 less/sass/css 变量，也不需要 webpack loader。
- **全 TypeScript**：库内全部用 TypeScript 编写，可与 TS 项目无缝配合；使用组件无需额外导入 CSS。
- **性能**：数据类组件默认使用虚拟列表。

## 安装与配套（README 命令）

```bash
# 安装组件库
npm i naive-ui

# 字体
npm i vfonts
```

- 图标推荐使用 [xicons](https://www.xicons.org)。
- 提供 Sketch 设计资源（见 README 链接）。

## 适用场景

- Vue 3 中后台、内部管理系统、数据密集型页面。
- 需要类型安全、主题可定制、组件按需加载的 Vue 项目。

## 注意事项

- 属 Vue 3 技术栈；React 项目与 PHP 传统页面不能直接安装使用。
- 文档与组件清单以官网 https://www.naiveui.com 实时信息为准；本文件星标为检索时点近似值。
- 仓库另有中文 README（README.zh-CN.md）与社区合集 awesome-naive。
