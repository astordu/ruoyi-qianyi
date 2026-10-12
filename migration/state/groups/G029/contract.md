# G029 内嵌页面与接口/数据源控制台

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

内嵌页面与接口/数据源控制台可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；内嵌载体和两个简单入口按同一内嵌/文档展示能力交付；保留 Druid 的原文字页。标签状态由 tabs 提供接口，避免互相静态导入。

依赖：G001 React 工程、环境与部署, G002 共用数据与表单适配, G009 系统主题与布局偏好

## 正常、异常与边界检查条件

1. iframe src/height/scroll/loading 按旧 props 渲染；InnerLink 使用 route.meta.link，IframeToggle 序列化 query 后在新窗口打开。
2. Swagger 通过 baseAPI+/proxy-docs 打开实际文档。Druid 当前模板只显示“我是数据监控”，iframe 被注释，保留这项原行为；不擅自启用 /druid/login.html。
3. 同路由 iframe 缓存和关闭由注入标签服务协作；Swagger 的后台登录/跨源/代理失败需真实环境证据，不能靠 mock 冒充文档已接通。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0370 | ruoyi-fastapi-frontend/src/components/iFrame/index.vue / L11-L31 script-setup 完整内容 | react-front/src/components/iFrame/index.tsx |
| I0371 | ruoyi-fastapi-frontend/src/components/iFrame/index.vue / L1-L9 template 完整内容 | react-front/src/components/iFrame/index.tsx |
| I0372 | ruoyi-fastapi-frontend/src/components/iFrame/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/iFrame/index.tsx |
| I0395 | ruoyi-fastapi-frontend/src/layout/components/IframeToggle/index.vue / L11-L25 script-setup 完整内容 | react-front/src/layout/components/IframeToggle/index.tsx |
| I0396 | ruoyi-fastapi-frontend/src/layout/components/IframeToggle/index.vue / L1-L9 template 完整内容 | react-front/src/layout/components/IframeToggle/index.tsx |
| I0397 | ruoyi-fastapi-frontend/src/layout/components/IframeToggle/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/layout/components/IframeToggle/index.tsx |
| I0398 | ruoyi-fastapi-frontend/src/layout/components/InnerLink/index.vue / L13-L35 script-setup 完整内容 | react-front/src/layout/components/InnerLink/index.tsx |
| I0399 | ruoyi-fastapi-frontend/src/layout/components/InnerLink/index.vue / L1-L11 template 完整内容 | react-front/src/layout/components/InnerLink/index.tsx |
| I0400 | ruoyi-fastapi-frontend/src/layout/components/InnerLink/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/layout/components/InnerLink/index.tsx |
| I0521 | ruoyi-fastapi-frontend/src/views/monitor/druid/index.vue / L8-L14 script-setup 完整内容 | react-front/src/views/monitor/druid/index.tsx |
| I0522 | ruoyi-fastapi-frontend/src/views/monitor/druid/index.vue / L1-L6 template 完整内容 | react-front/src/views/monitor/druid/index.tsx |
| I0523 | ruoyi-fastapi-frontend/src/views/monitor/druid/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/monitor/druid/index.tsx |
| I0736 | ruoyi-fastapi-frontend/src/views/tool/swagger/index.vue / L5-L9 script-setup 完整内容 | react-front/src/views/tool/swagger/index.tsx |
| I0737 | ruoyi-fastapi-frontend/src/views/tool/swagger/index.vue / L1-L3 template 完整内容 | react-front/src/views/tool/swagger/index.tsx |
| I0738 | ruoyi-fastapi-frontend/src/views/tool/swagger/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/tool/swagger/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/components/iFrame/index.vue

逻辑定位：temp@L27–29.
全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/layout/components/IframeToggle/index.vue

逻辑定位：iframeUrl@L18–24.
全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/layout/components/InnerLink/index.vue

全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/views/monitor/druid/index.vue

全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/views/tool/swagger/index.vue

全部模板事件/权限：.

## 源循环/延后装配的明确接口

- `ruoyi-fastapi-frontend/src/layout/components/IframeToggle/index.vue` → `ruoyi-fastapi-frontend/src/store/modules/tagsView.js` (G021): 内嵌组件接收 iframeViews 查询/关闭接口；tabs提供真实状态，shell装配，J002/J007验收。

这些源关系保留在 dependency-review.json；只是将运行依赖改为显式接口注入，未删除功能。最终必须以真实页面/服务接线验收。
