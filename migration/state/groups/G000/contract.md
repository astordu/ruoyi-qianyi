# G000 React 工程启动、HTML 加载入口与多环境构建

依赖：无

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00001 `ruoyi-fastapi-frontend/.env.development` env key VITE_APP_TITLE
  - 基线：环境名、标题与 API 前缀维持原值；不在报告输出变量值。压缩参数由压缩组接入。
  - 去向：由本组实施登记
- I00002 `ruoyi-fastapi-frontend/.env.development` env key VITE_APP_ENV
  - 基线：环境名、标题与 API 前缀维持原值；不在报告输出变量值。压缩参数由压缩组接入。
  - 去向：由本组实施登记
- I00003 `ruoyi-fastapi-frontend/.env.development` env key VITE_APP_BASE_API
  - 基线：环境名、标题与 API 前缀维持原值；不在报告输出变量值。压缩参数由压缩组接入。
  - 去向：由本组实施登记
- I00004 `ruoyi-fastapi-frontend/.env.docker` env key VITE_APP_TITLE
  - 基线：环境名、标题与 API 前缀维持原值；不在报告输出变量值。压缩参数由压缩组接入。
  - 去向：由本组实施登记
- I00005 `ruoyi-fastapi-frontend/.env.docker` env key VITE_APP_ENV
  - 基线：环境名、标题与 API 前缀维持原值；不在报告输出变量值。压缩参数由压缩组接入。
  - 去向：由本组实施登记
- I00006 `ruoyi-fastapi-frontend/.env.docker` env key VITE_APP_BASE_API
  - 基线：环境名、标题与 API 前缀维持原值；不在报告输出变量值。压缩参数由压缩组接入。
  - 去向：由本组实施登记
- I00008 `ruoyi-fastapi-frontend/.env.production` env key VITE_APP_TITLE
  - 基线：环境名、标题与 API 前缀维持原值；不在报告输出变量值。压缩参数由压缩组接入。
  - 去向：由本组实施登记
- I00009 `ruoyi-fastapi-frontend/.env.production` env key VITE_APP_ENV
  - 基线：环境名、标题与 API 前缀维持原值；不在报告输出变量值。压缩参数由压缩组接入。
  - 去向：由本组实施登记
- I00010 `ruoyi-fastapi-frontend/.env.production` env key VITE_APP_BASE_API
  - 基线：环境名、标题与 API 前缀维持原值；不在报告输出变量值。压缩参数由压缩组接入。
  - 去向：由本组实施登记
- I00012 `ruoyi-fastapi-frontend/.env.staging` env key VITE_APP_TITLE
  - 基线：环境名、标题与 API 前缀维持原值；不在报告输出变量值。压缩参数由压缩组接入。
  - 去向：由本组实施登记
- I00013 `ruoyi-fastapi-frontend/.env.staging` env key VITE_APP_ENV
  - 基线：环境名、标题与 API 前缀维持原值；不在报告输出变量值。压缩参数由压缩组接入。
  - 去向：由本组实施登记
- I00014 `ruoyi-fastapi-frontend/.env.staging` env key VITE_APP_BASE_API
  - 基线：环境名、标题与 API 前缀维持原值；不在报告输出变量值。压缩参数由压缩组接入。
  - 去向：由本组实施登记
- I00016 `ruoyi-fastapi-frontend/.gitignore` 完整文件（HTML 标题/meta/加载动画、IE 降级、favicon 或工程忽略规则）
  - 基线：完整读取并保留原内容；挂载点 app→root，入口 main.js→main.tsx；忽略规则增加 React 测试产物。
  - 去向：由本组实施登记
- I00025 `ruoyi-fastapi-frontend/index.html` 完整文件（HTML 标题/meta/加载动画、IE 降级、favicon 或工程忽略规则）
  - 基线：完整读取并保留原内容；挂载点 app→root，入口 main.js→main.tsx；忽略规则增加 React 测试产物。
  - 去向：由本组实施登记
- I00027 `ruoyi-fastapi-frontend/package.json` JSON name
  - 基线：保留项目描述、版本、作者、许可证和上游来源；目标命名 vfadmin-react，ESM 模式。
  - 去向：由本组实施登记
- I00028 `ruoyi-fastapi-frontend/package.json` JSON version
  - 基线：保留项目描述、版本、作者、许可证和上游来源；目标命名 vfadmin-react，ESM 模式。
  - 去向：由本组实施登记
- I00029 `ruoyi-fastapi-frontend/package.json` JSON description
  - 基线：保留项目描述、版本、作者、许可证和上游来源；目标命名 vfadmin-react，ESM 模式。
  - 去向：由本组实施登记
- I00030 `ruoyi-fastapi-frontend/package.json` JSON author
  - 基线：保留项目描述、版本、作者、许可证和上游来源；目标命名 vfadmin-react，ESM 模式。
  - 去向：由本组实施登记
- I00031 `ruoyi-fastapi-frontend/package.json` JSON license
  - 基线：保留项目描述、版本、作者、许可证和上游来源；目标命名 vfadmin-react，ESM 模式。
  - 去向：由本组实施登记
- I00032 `ruoyi-fastapi-frontend/package.json` JSON type
  - 基线：保留项目描述、版本、作者、许可证和上游来源；目标命名 vfadmin-react，ESM 模式。
  - 去向：由本组实施登记
- I00033 `ruoyi-fastapi-frontend/package.json` JSON scripts.dev
  - 基线：保留 dev 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：由本组实施登记
- I00034 `ruoyi-fastapi-frontend/package.json` JSON scripts.build:prod
  - 基线：保留 build:prod 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：由本组实施登记
- I00035 `ruoyi-fastapi-frontend/package.json` JSON scripts.build:docker
  - 基线：保留 build:docker 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：由本组实施登记
- I00036 `ruoyi-fastapi-frontend/package.json` JSON scripts.build:stage
  - 基线：保留 build:stage 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：由本组实施登记
- I00039 `ruoyi-fastapi-frontend/package.json` JSON scripts.preview
  - 基线：保留 preview 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：由本组实施登记
- I00040 `ruoyi-fastapi-frontend/package.json` JSON repository
  - 基线：保留项目描述、版本、作者、许可证和上游来源；目标命名 vfadmin-react，ESM 模式。
  - 去向：由本组实施登记
- I00070 `ruoyi-fastapi-frontend/package.json` JSON dependencies.vue
  - 基线：保留 vue 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：由本组实施登记
- I00074 `ruoyi-fastapi-frontend/package.json` JSON devDependencies.@vitejs/plugin-vue
  - 基线：保留 @vitejs/plugin-vue 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：由本组实施登记
- I00079 `ruoyi-fastapi-frontend/package.json` JSON devDependencies.vite
  - 基线：保留 vite 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：由本组实施登记
- I00440 `ruoyi-fastapi-frontend/public/favicon.ico` 完整文件（HTML 标题/meta/加载动画、IE 降级、favicon 或工程忽略规则）
  - 基线：完整读取并保留原内容；挂载点 app→root，入口 main.js→main.tsx；忽略规则增加 React 测试产物。
  - 去向：由本组实施登记
- I08738 `ruoyi-fastapi-frontend/vite.config.js` defineConfig: base/resolve/build/server/css（plugins 单独登记）
  - 基线：base=/；~ 根别名、@ src 别名；dist/static 名称；12580 host/open；dev-api→19099 去前缀；移除 @charset。
  - 去向：由本组实施登记

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。

## 本轮具体验收条件（取自原入口和 Vite 配置）

1. React + TypeScript + Vite 可启动并挂载；旧业务注册、登录和菜单均不属于本组，不计完成。
2. 原 index.html 的中文加载文案、三层旋转动画、#7171C6 背景、viewport/meta/title、favicon 与 IE 降级文件保持。仅挂载点改为 root、脚本改为 main.tsx；JS 阻止时原/新加载界面截图逐像素相同。
3. 开发监听仍默认 12580、host/open；测试用独立 12582，不能占用用户实例。/dev-api 请求去前缀、changeOrigin，转发到 127.0.0.1:19099。可通过不写业务数据的临时只读 probe server 验证真实转发；非真实后端互通结论。
4. development/production/staging/docker 的标题、环境名与 API 前缀保留；三个构建命令正常结束，标题完成占位符替换。压缩变量保留但插件实施属另一组，本组不宣称 gzip/brotli 已完成。
5. ~ 根别名与 @ src 别名；JS/TS/JSX/TSX/JSON 导入可解析，Vue 编译插件替换为 React 插件；Vue-only .vue 扩展由目标移除。构建输出 dist/static/js 与 dist/static/css，不生成生产 source maps；CSS @charset 去除。
6. 真实浏览器加载根路径与多级深链接（含 query/hash），保持 URL；刷新仍能挂载。该条件只证明 SPA 服务器 fallback，不证明业务路由已经迁移。
7. 依赖树不含 Vue/Pinia/ElementPlus；源快照检查仍一致。favicon 和 IE 降级文件内容哈希与原文件相同。

证据：源码基线与配置解析 → 类型检查/多环境构建 → Node 配置/产物检查 → Playwright 原/新启动加载截图及 React 挂载/刷新 → 本组验证报告。所有验证由同一 agent 执行，记为自检。

适用环境：Node 22；Chromium；viewport 1280×720、zh-CN、Asia/Shanghai；加载动画截图冻结在同一时刻，分别冻结两边全部动画，不只处理目标图。

框架 API 依据：[React createRoot](https://react.dev/reference/react-dom/client/createRoot)、[Vite 构建选项](https://vite.dev/config/build-options)、[Vite 代理配置](https://vite.dev/config/server-options)。Vite 8 的 rolldownOptions 与旧 rollupOptions 对应。
