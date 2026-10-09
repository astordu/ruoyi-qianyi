# G000 验证结果：通过

验证性质：同一 agent 实施后自检，非独立审核，非人工验收。只通过工程启动/构建组，不代表业务 Vue→React 已迁完。

| 合同条件 | 原版依据 | 实际检查与结果 |
|---|---|---|
| React 挂载及框架替换 | package.json 的 ESM/dev/build/preview 和原入口 | React19.3/TS7/Vite8；类型检查通过；Chromium 正常挂载，无 pageerror；锁文件不含 Vue/Pinia/ElementPlus |
| HTML 加载态、标题/meta | 完整原 index.html 与 baseline.json | 全 HTML/CSS 对比，仅 root/入口替换；双边冻结动画，PNG 字节相同；实际查看原加载图与目标挂载图 |
| favicon、IE 降级 | public/favicon.ico、html/ie.html | 源/目标/三套产物字节相同；开发与预览 HTTP200。IE 条件注释保留；未运行旧 IE 浏览器 |
| 环境参数 | 原四份 env 文件 | development/production/staging/docker 全键值相同；真实三套构建均成功，标题已替换 |
| 代理 | 原 vite.config.js server.proxy | 默认12580/host/open、127.0.0.1:19099及重写函数保持；本地无状态 GET probe 验证 URL/query/Host；未称真实后端互通 |
| 别名和产物 | 原 resolve/build/css 选项 | @/~ 解析及真实 main.tsx 导入成功；dist/static/js/css，无生产 source map；真实 PostCSS 去 charset 且保留声明 |
| 深链接和刷新 | 原 SPA 工程服务配置；业务路由属于后续组 | 开发和生产 preview 重放 /system/user/profile?tab=security#details，URL不变，刷新挂载；只证明服务器 fallback |
| 范围和源码完整性 | 固定339文件源快照与 round.json | 31个本组内容项有真实目标定位；源快照 check 一致；未改 Vue 或后端；只实施 G000 |

执行工作目录：`/Users/dulei/Documents/projects/ruoyi-qianyi/react-front`。

- `npm run typecheck`：通过。首次使用 baseUrl 失败后按 TS7 配置改正，再检通过。
- `npm run build:prod -- --outDir ../migration/state/evidence/G000/builds/production --emptyOutDir`：通过。
- `npm run build:stage -- --outDir ../migration/state/evidence/G000/builds/staging --emptyOutDir`：通过。
- `npm run build:docker -- --outDir ../migration/state/evidence/G000/builds/docker --emptyOutDir`：通过。
- `npm run test:foundation`：7/7通过（最终日志 attempt-3-config.log）。
- `npm run test:foundation:browser`：3/3通过（最终日志 attempt-2-command-2.log）。首次因原基线端口占用在启动前失败，保留失败报告及日志，不复用/关闭已有服务；原夹具改13581，目标开发12582/预览12583。

截图条件：Chromium，1280×720，zh-CN，Asia/Shanghai。原HTML夹具只运行原始 pre-mount 内容，不是完整 Vue 应用。双边禁用动画/过渡，仅对静态初始加载态判定截图相同；未把此证据扩大为业务页面视觉等价。目标启动诊断为白底标题/状态，实际查看符合工程基础范围。

所有命令、退出码、耗时、浏览器结果和对照元数据见 evidence/G000/summary.json 及其日志。首次基线落盘/复制的路径错误已在 baseline.md 和 progress.md 如实记录。

公共影响：此前目标为空，无已迁业务受影响。压缩变量保留但压缩插件、SVG symbol、Monaco workers、原 main.js 注册、登录、权限、路由页面、全站样式均另组 pending。生产服务器部署配置、真实 API、原 Vue 业务运行对照及31项跨组集成未执行，不计通过。

内容映射（逐项）：

- I00001 `ruoyi-fastapi-frontend/.env.development` env key VITE_APP_TITLE → `react-front/.env.development`；定位：env key VITE_APP_TITLE：目标对应完整文件/环境键；合同条件已覆盖。
- I00002 `ruoyi-fastapi-frontend/.env.development` env key VITE_APP_ENV → `react-front/.env.development`；定位：env key VITE_APP_ENV：目标对应完整文件/环境键；合同条件已覆盖。
- I00003 `ruoyi-fastapi-frontend/.env.development` env key VITE_APP_BASE_API → `react-front/.env.development`；定位：env key VITE_APP_BASE_API：目标对应完整文件/环境键；合同条件已覆盖。
- I00004 `ruoyi-fastapi-frontend/.env.docker` env key VITE_APP_TITLE → `react-front/.env.docker`；定位：env key VITE_APP_TITLE：目标对应完整文件/环境键；合同条件已覆盖。
- I00005 `ruoyi-fastapi-frontend/.env.docker` env key VITE_APP_ENV → `react-front/.env.docker`；定位：env key VITE_APP_ENV：目标对应完整文件/环境键；合同条件已覆盖。
- I00006 `ruoyi-fastapi-frontend/.env.docker` env key VITE_APP_BASE_API → `react-front/.env.docker`；定位：env key VITE_APP_BASE_API：目标对应完整文件/环境键；合同条件已覆盖。
- I00008 `ruoyi-fastapi-frontend/.env.production` env key VITE_APP_TITLE → `react-front/.env.production`；定位：env key VITE_APP_TITLE：目标对应完整文件/环境键；合同条件已覆盖。
- I00009 `ruoyi-fastapi-frontend/.env.production` env key VITE_APP_ENV → `react-front/.env.production`；定位：env key VITE_APP_ENV：目标对应完整文件/环境键；合同条件已覆盖。
- I00010 `ruoyi-fastapi-frontend/.env.production` env key VITE_APP_BASE_API → `react-front/.env.production`；定位：env key VITE_APP_BASE_API：目标对应完整文件/环境键；合同条件已覆盖。
- I00012 `ruoyi-fastapi-frontend/.env.staging` env key VITE_APP_TITLE → `react-front/.env.staging`；定位：env key VITE_APP_TITLE：目标对应完整文件/环境键；合同条件已覆盖。
- I00013 `ruoyi-fastapi-frontend/.env.staging` env key VITE_APP_ENV → `react-front/.env.staging`；定位：env key VITE_APP_ENV：目标对应完整文件/环境键；合同条件已覆盖。
- I00014 `ruoyi-fastapi-frontend/.env.staging` env key VITE_APP_BASE_API → `react-front/.env.staging`；定位：env key VITE_APP_BASE_API：目标对应完整文件/环境键；合同条件已覆盖。
- I00016 `ruoyi-fastapi-frontend/.gitignore` 完整文件（HTML 标题/meta/加载动画、IE 降级、favicon 或工程忽略规则） → `react-front/.gitignore`；定位：完整文件（HTML 标题/meta/加载动画、IE 降级、favicon 或工程忽略规则）：目标对应完整文件/环境键；合同条件已覆盖。
- I00025 `ruoyi-fastapi-frontend/index.html` 完整文件（HTML 标题/meta/加载动画、IE 降级、favicon 或工程忽略规则） → `react-front/index.html`, `react-front/src/main.tsx`, `react-front/public/html/ie.html`；定位：HTML 全部 meta/title/loader CSS 和 DOM；#root；main.tsx createRoot；IE fallback 静态页；合同条件已覆盖。
- I00027 `ruoyi-fastapi-frontend/package.json` JSON name → `react-front/package.json`, `react-front/package-lock.json`；定位：JSON name；Vue/plugin-vue 替换 React/react-dom/plugin-react，锁文件由 npm install 生成；合同条件已覆盖。
- I00028 `ruoyi-fastapi-frontend/package.json` JSON version → `react-front/package.json`, `react-front/package-lock.json`；定位：JSON version；Vue/plugin-vue 替换 React/react-dom/plugin-react，锁文件由 npm install 生成；合同条件已覆盖。
- I00029 `ruoyi-fastapi-frontend/package.json` JSON description → `react-front/package.json`, `react-front/package-lock.json`；定位：JSON description；Vue/plugin-vue 替换 React/react-dom/plugin-react，锁文件由 npm install 生成；合同条件已覆盖。
- I00030 `ruoyi-fastapi-frontend/package.json` JSON author → `react-front/package.json`, `react-front/package-lock.json`；定位：JSON author；Vue/plugin-vue 替换 React/react-dom/plugin-react，锁文件由 npm install 生成；合同条件已覆盖。
- I00031 `ruoyi-fastapi-frontend/package.json` JSON license → `react-front/package.json`, `react-front/package-lock.json`；定位：JSON license；Vue/plugin-vue 替换 React/react-dom/plugin-react，锁文件由 npm install 生成；合同条件已覆盖。
- I00032 `ruoyi-fastapi-frontend/package.json` JSON type → `react-front/package.json`, `react-front/package-lock.json`；定位：JSON type；Vue/plugin-vue 替换 React/react-dom/plugin-react，锁文件由 npm install 生成；合同条件已覆盖。
- I00033 `ruoyi-fastapi-frontend/package.json` JSON scripts.dev → `react-front/package.json`, `react-front/package-lock.json`；定位：JSON scripts.dev；Vue/plugin-vue 替换 React/react-dom/plugin-react，锁文件由 npm install 生成；合同条件已覆盖。
- I00034 `ruoyi-fastapi-frontend/package.json` JSON scripts.build:prod → `react-front/package.json`, `react-front/package-lock.json`；定位：JSON scripts.build:prod；Vue/plugin-vue 替换 React/react-dom/plugin-react，锁文件由 npm install 生成；合同条件已覆盖。
- I00035 `ruoyi-fastapi-frontend/package.json` JSON scripts.build:docker → `react-front/package.json`, `react-front/package-lock.json`；定位：JSON scripts.build:docker；Vue/plugin-vue 替换 React/react-dom/plugin-react，锁文件由 npm install 生成；合同条件已覆盖。
- I00036 `ruoyi-fastapi-frontend/package.json` JSON scripts.build:stage → `react-front/package.json`, `react-front/package-lock.json`；定位：JSON scripts.build:stage；Vue/plugin-vue 替换 React/react-dom/plugin-react，锁文件由 npm install 生成；合同条件已覆盖。
- I00039 `ruoyi-fastapi-frontend/package.json` JSON scripts.preview → `react-front/package.json`, `react-front/package-lock.json`；定位：JSON scripts.preview；Vue/plugin-vue 替换 React/react-dom/plugin-react，锁文件由 npm install 生成；合同条件已覆盖。
- I00040 `ruoyi-fastapi-frontend/package.json` JSON repository → `react-front/package.json`, `react-front/package-lock.json`；定位：JSON repository；Vue/plugin-vue 替换 React/react-dom/plugin-react，锁文件由 npm install 生成；合同条件已覆盖。
- I00070 `ruoyi-fastapi-frontend/package.json` JSON dependencies.vue → `react-front/package.json`, `react-front/package-lock.json`；定位：JSON dependencies.vue；Vue/plugin-vue 替换 React/react-dom/plugin-react，锁文件由 npm install 生成；合同条件已覆盖。
- I00074 `ruoyi-fastapi-frontend/package.json` JSON devDependencies.@vitejs/plugin-vue → `react-front/package.json`, `react-front/package-lock.json`；定位：JSON devDependencies.@vitejs/plugin-vue；Vue/plugin-vue 替换 React/react-dom/plugin-react，锁文件由 npm install 生成；合同条件已覆盖。
- I00079 `ruoyi-fastapi-frontend/package.json` JSON devDependencies.vite → `react-front/package.json`, `react-front/package-lock.json`；定位：JSON devDependencies.vite；Vue/plugin-vue 替换 React/react-dom/plugin-react，锁文件由 npm install 生成；合同条件已覆盖。
- I00440 `ruoyi-fastapi-frontend/public/favicon.ico` 完整文件（HTML 标题/meta/加载动画、IE 降级、favicon 或工程忽略规则） → `react-front/public/favicon.ico`；定位：完整文件（HTML 标题/meta/加载动画、IE 降级、favicon 或工程忽略规则）：目标对应完整文件/环境键；合同条件已覆盖。
- I08738 `ruoyi-fastapi-frontend/vite.config.js` defineConfig: base/resolve/build/server/css（plugins 单独登记） → `react-front/vite.config.ts`；定位：defineConfig：base/resolve/build/server/css（保留 charset-removal）；合同条件已覆盖。

## 复验（G253 接入 dayjs 后）

触发：G253 实施向 `react-front/package.json` 增加 `dayjs@1.11.23`（依赖接口必要接入），本组目标文件哈希变化导致原验证失效（check: invalidated_groups=[G000]）。按协议"单纯共享文件变化也必须记录复验"，重新执行本组检查：

- `npm run typecheck`：通过（exit 0，G253 证据 typecheck.log）。
- 三套构建 `build:prod/stage/docker`：全部通过（evidence/G000/revalidation-build-*.log）。
- `npm run test:foundation`：7/7 通过（revalidation-foundation.log）。
- `npx playwright test`：3/3 通过（revalidation-browser.log）；原/新加载态像素一致、深链接刷新挂载不变。
- 锁文件检查：package-lock.json 无 vue/pinia/element-plus/@vitejs/plugin-vue/ant-design-vue，dayjs 接入未带入 Vue 依赖。

复验结论：dayjs 为普通 JS 库按实际引用接入，不影响本组工程基础结论；原通过结论维持，快照按当前目标哈希重新冻结。dayjs 内容项（I00051）归属 G016，届时核对本接入。
