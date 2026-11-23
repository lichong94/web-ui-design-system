# SaaS-Boilerplate（Next.js 全栈 SaaS 起步脚手架）

## 基本信息

| 项目 | 内容 |
| --- | --- |
| 仓库 | https://github.com/ixartz/SaaS-Boilerplate |
| 在线演示 | https://react-saas.com |
| 默认分支 | main |
| 主要语言 | TypeScript |
| 协议 | MIT |
| 星标（2026-11-21 检索值，会随时间变动） | 约 7.50 千 |
| 技术栈 | Next.js（App Router）+ React 19 + Tailwind CSS + Shadcn UI + TypeScript；Drizzle ORM；Clerk 认证；Vitest / Playwright |

## 定位

一套可高度定制的开源 SaaS 起步模板，用于以最少成本快速搭建并上线 SaaS 应用。内置认证、多租户与团队、角色权限、数据库、国际化、落地页、用户仪表盘、表单、SEO、日志、错误监控、测试等生产级能力。

## 内置功能（来自官方 README）

- Next.js App Router，TypeScript 严格模式，React 19。
- 认证（Clerk）：注册、登录、登出、忘记密码、重置密码；魔法链接无密码登录、多因素认证（MFA）、社交登录（Google/Facebook/Twitter/GitHub/Apple 等）、Passkey、用户冒充（Impersonation）。
- 多租户与团队：创建、切换、更新组织，邀请团队成员。
- 基于角色的访问控制（RBAC）与权限。
- 类型安全 ORM：DrizzleORM，兼容 PostgreSQL、SQLite、MySQL；本地开发库 PGlite；可接 Neon 等远程 PostgreSQL。
- 国际化 i18n：next-intl + Crowdin。
- 表单：React Hook Form；校验：Zod。
- 代码质量：ESLint、Prettier、Lefthook、Commitlint、Commitizen。
- 测试：Vitest（单元/浏览器模式）、Playwright（集成与 E2E）、GitHub Actions、Storybook、视觉回归测试。
- 监控与日志：Sentry 错误监控、Codecov 覆盖率、LogTape/Better Stack 日志、Checkly 监控即代码。
- SEO：SEO 元数据、JSON-LD、Open Graph、sitemap.xml、robots.txt。
- 环境变量类型安全（T3 Env）、`@` 绝对路径导入、VSCode 配置、Lighthouse 高分。

## 运行要求与起步命令（README）

- 要求：Node.js 24+ 与 npm。

```bash
git clone --depth=1 https://github.com/ixartz/SaaS-Boilerplate.git my-project-name
cd my-project-name
npm install
npm run dev
```

`npm run dev` 会同时启动 Next.js、本地 PostgreSQL 兼容库 PGlite、Sentry Spotlight；浏览器打开 http://localhost:3000 查看。

## 关键配置与定制入口（README）

- 认证：在 Clerk 后台创建应用，把 `NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY`、`CLERK_SECRET_KEY` 写入 `.env.local`；并在 Organization management > Settings 中开启 Organization。
- 远程数据库：准备 PostgreSQL 连接串（推荐 Neon 免费库），项目通过 DrizzleORM 接入。
- 国际化：注册 Crowdin 项目，配置 `CROWDIN_PROJECT_ID` 与 `CROWDIN_PERSONAL_TOKEN`，推送 main 分支时自动同步翻译。
- 常见定制文件：`public/` 下图标、`src/utils/AppConfig.ts`、`src/templates/BaseTemplate.tsx`、`next.config.mjs`、`.env`。
- 修改数据库表结构：编辑 `./src/models/Schema.ts`（Drizzle），然后运行 `npm run db:generate` 生成迁移。
- 测试：`npm run test`（单元）；`npx playwright install` 后 `npm run test:e2e`（E2E）。
- 生产构建：`npm run build`，本地预览 `npm run start`；需在环境变量中配置 `DATABASE_URL` 与 `CLERK_SECRET_KEY`。

## 项目结构（README 摘录）

```text
src/
├── app            # Next.js App Router
├── components     # 可复用组件
├── features       # 功能专属组件
├── libs           # 第三方库配置
├── locales        # i18n 文案
├── models         # 数据模型
├── styles         # 样式
├── templates      # 模板
├── types          # 类型定义
└── utils          # 工具函数
tests/
├── e2e            # E2E 与监控即代码
└── integration    # 集成测试
```

## 版本说明（README）

项目分免费开源版与付费 Plus/Pro/Max 版。免费版已含认证、社交登录、MFA、多租户、RBAC、落地页、i18n、Drizzle ORM、GitHub Actions、Sentry、Shadcn UI 等；付费版额外提供自托管认证（Better Auth）、事务邮件、Bun、Stripe 支付、oRPC 端到端类型安全、暗色模式、完整仪表盘扩展、视觉回归测试等。具体差异以官方版本对比表为准。

## 适用场景

- 带账号体系、团队/多租户、权限管理的付费工具站或 SaaS 产品。
- 希望直接在生产级脚手架上二次开发，省去登录、权限、国际化、测试、监控等重复工作。

## 注意事项

- 属 Next.js/React 工程化项目，不能直接用于 PHP/ThinkPHP 传统页面。
- 免费版部分高级能力（暗色模式、Stripe 支付、邮件等）在付费版，选型前先对照官方对比表。
- README 另提供 `saas-builder` Agent Skill（`npx skills add ixartz/saas-boilerplate`），供 AI 编码 Agent 克隆并搭建项目；本集合不自动安装该 Skill。
