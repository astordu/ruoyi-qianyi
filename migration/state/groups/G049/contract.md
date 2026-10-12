# G049 服务与主机监控

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

服务与主机监控可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G005 HTTP 请求、会话提示与导出, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 真实 getServer 数据中的 CPU/内存/服务器/磁盘字段依模板呈现，百分比和容量单位与源码一致。
2. 加载时遮罩，完成/失败关闭；无服务器数据不以静态数值冒充。
3. 磁盘长路径、空数组、各单位精度与旧页面截图对照。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0055 | ruoyi-fastapi-frontend/src/api/monitor/server.js / L1-L9 module 完整内容 | react-front/src/api/monitor/server.ts |
| I0551 | ruoyi-fastapi-frontend/src/views/monitor/server/index.vue / L168-L183 script-setup 完整内容 | react-front/src/views/monitor/server/index.tsx |
| I0552 | ruoyi-fastapi-frontend/src/views/monitor/server/index.vue / L1-L166 template 完整内容 | react-front/src/views/monitor/server/index.tsx |
| I0553 | ruoyi-fastapi-frontend/src/views/monitor/server/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/monitor/server/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/monitor/server.js

逻辑定位：getServer@L4–9.
- URL/请求对象 L5: `'get' '/monitor/server'`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/views/monitor/server/index.vue

逻辑定位：getList@L174–180.
全部模板事件/权限：.
