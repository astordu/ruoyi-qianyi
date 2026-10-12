# G001 React 工程、环境与部署

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

空 React 工程可启动、按四种环境构建并部署；业务迁移有统一工具链

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：无

## 正常、异常与边界检查条件

1. 开发代理 /dev-api 去掉前缀后指向原后端；多环境 API 前缀、标题、端口与源码键名保持对应，报告不保存环境变量值。
2. dev、production、stage、docker 模式能启动或构建；产物入口、static/js 与 static/[ext] 路径、原压缩开关按旧配置核对。
3. 深层 history URL 在 MySQL/PostgreSQL 两种 Nginx 配置刷新可回到 index.html，/docker-api/ 转发仍匹配各自服务。
4. React+TypeScript+Vite+React Router+Ant Design+Context 工程显式导入依赖；替换 Vue 自动导入/setup 插件，SVG/Monaco/压缩能力按真实需要接入。
5. 启动加载动画、favicon、IE 提示页、许可证和 Windows 启动/打包脚本都有去向；Vue npm 锁文件仅登记排除，React 根据新 manifest 生成自己的锁文件。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0001 | ruoyi-fastapi-frontend/.env.development / L1-L9 environment 完整内容 | react-front/.env.development |
| I0002 | ruoyi-fastapi-frontend/.env.docker / L1-L11 environment 完整内容 | react-front/.env.docker |
| I0003 | ruoyi-fastapi-frontend/.env.production / L1-L11 environment 完整内容 | react-front/.env.production |
| I0004 | ruoyi-fastapi-frontend/.env.staging / L1-L11 environment 完整内容 | react-front/.env.staging |
| I0005 | ruoyi-fastapi-frontend/.gitignore / L1-L24 document-or-config 完整内容 | react-front/.gitignore |
| I0006 | ruoyi-fastapi-frontend/Dockerfile / L1-L31 document-or-config 完整内容 | react-front/Dockerfile |
| I0007 | ruoyi-fastapi-frontend/LICENSE / L1-L20 document-or-config 完整内容 | react-front/LICENSE |
| I0008 | ruoyi-fastapi-frontend/bin/build.bat / L1-L12 document-or-config 完整内容 | react-front/bin/build.bat |
| I0009 | ruoyi-fastapi-frontend/bin/nginx.dockermy.conf / L1-L24 document-or-config 完整内容 | react-front/bin/nginx.dockermy.conf |
| I0010 | ruoyi-fastapi-frontend/bin/nginx.dockerpg.conf / L1-L24 document-or-config 完整内容 | react-front/bin/nginx.dockerpg.conf |
| I0011 | ruoyi-fastapi-frontend/bin/package.bat / L1-L12 document-or-config 完整内容 | react-front/bin/package.bat |
| I0012 | ruoyi-fastapi-frontend/bin/run-web.bat / L1-L12 document-or-config 完整内容 | react-front/bin/run-web.bat |
| I0013 | ruoyi-fastapi-frontend/html/ie.html / L1-L46 document-or-config 完整内容 | react-front/html/ie.html |
| I0014 | ruoyi-fastapi-frontend/index.html / L1-L215 document-or-config 完整内容 | react-front/index.html |
| I0016 | ruoyi-fastapi-frontend/package.json / L1-L71 configuration 完整内容 | react-front/package.json |
| I0031 | ruoyi-fastapi-frontend/public/favicon.ico / L1-L1 asset 完整内容 | react-front/public/favicon.ico |
| I0743 | ruoyi-fastapi-frontend/vite.config.js / L1-L74 module 完整内容 | react-front/vite.config.ts |
| I0744 | ruoyi-fastapi-frontend/vite/plugins/auto-import.js / L1-L13 module 完整内容 | react-front/vite.config.ts |
| I0745 | ruoyi-fastapi-frontend/vite/plugins/compression.js / L1-L29 module 完整内容 | react-front/vite.config.ts |
| I0746 | ruoyi-fastapi-frontend/vite/plugins/index.js / L1-L44 module 完整内容 | react-front/vite.config.ts |
| I0747 | ruoyi-fastapi-frontend/vite/plugins/setup-extend.js / L1-L6 module 完整内容 | react-front/vite.config.ts |
| I0748 | ruoyi-fastapi-frontend/vite/plugins/svg-icon.js / L1-L11 module 完整内容 | react-front/vite.config.ts |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/.env.development


### ruoyi-fastapi-frontend/.env.docker


### ruoyi-fastapi-frontend/.env.production


### ruoyi-fastapi-frontend/.env.staging


### ruoyi-fastapi-frontend/.gitignore


### ruoyi-fastapi-frontend/Dockerfile


### ruoyi-fastapi-frontend/LICENSE


### ruoyi-fastapi-frontend/bin/build.bat


### ruoyi-fastapi-frontend/bin/nginx.dockermy.conf


### ruoyi-fastapi-frontend/bin/nginx.dockerpg.conf


### ruoyi-fastapi-frontend/bin/package.bat


### ruoyi-fastapi-frontend/bin/run-web.bat


### ruoyi-fastapi-frontend/html/ie.html


### ruoyi-fastapi-frontend/index.html


### ruoyi-fastapi-frontend/package.json


### ruoyi-fastapi-frontend/public/favicon.ico


### ruoyi-fastapi-frontend/vite.config.js

逻辑定位：rewrite@L51–51, charset@L62–66.

### ruoyi-fastapi-frontend/vite/plugins/auto-import.js

逻辑定位：createAutoImport@L3–12.

### ruoyi-fastapi-frontend/vite/plugins/compression.js

逻辑定位：createCompression@L3–28.

### ruoyi-fastapi-frontend/vite/plugins/index.js

逻辑定位：createVitePlugins@L32–43.

### ruoyi-fastapi-frontend/vite/plugins/setup-extend.js

逻辑定位：createSetupExtend@L3–5.

### ruoyi-fastapi-frontend/vite/plugins/svg-icon.js

逻辑定位：createSvgIcon@L4–10.

## 源循环/延后装配的明确接口

- `ruoyi-fastapi-frontend/index.html` → `ruoyi-fastapi-frontend/src/main.js` (G023): index.html 的运行入口随 shell 装配；工程组先验证实际空React启动入口，J001/J010检查最终入口。

这些源关系保留在 dependency-review.json；只是将运行依赖改为显式接口注入，未删除功能。最终必须以真实页面/服务接线验收。
