# vfadmin React

Vue → React 逐组迁移的目标工程。当前只完成 G000 工程基础；首页显示启动诊断，业务路由、登录、组件和 API 仍待迁移。

需要 Node.js 22.12+。运行 `npm ci`，然后 `npm run dev`，默认端口 12580。已有服务占用该端口时可传 `-- --port 12582`。

`npm run typecheck` 检查类型；`npm run build:prod`、`npm run build:stage`、`npm run build:docker` 对应三个原环境构建命令。`npm run preview` 预览产物。

本组检查：`npm run test:foundation`；首次运行浏览器检查需 `npx playwright install chromium`，再运行 `npm run test:foundation:browser`。

完整清单、每轮合同及验证在 `../migration/state/`。压缩、SVG symbol 与 Monaco workers 已登记为后续组，保留环境参数不代表这些插件已实现。生产服务器的 history fallback、真实后端互通由后续部署/页面集成验证。
