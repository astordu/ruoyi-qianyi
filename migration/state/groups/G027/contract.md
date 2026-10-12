# G027 首页工作台

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

首页工作台可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G009 系统主题与布局偏好, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 项目数/团队排名/访问统计、项目网格、动态、快捷链接、团队与雷达图使用当前源码数据与导航，不能添加假后端接口替换静态内容。
2. G2Plot Radar 挂载渲染、主题与容器尺寸适配、卸载 destroy；Ant Design 卡片/统计/列表布局与源图表对照。
3. editable-link-group 中快捷链接与编辑/更多入口按原版实际存在行为保留。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0489 | ruoyi-fastapi-frontend/src/views/dashboard/editable-link-group.vue / L12-L20 script 完整内容 | react-front/src/views/dashboard/editable-link-group.tsx |
| I0490 | ruoyi-fastapi-frontend/src/views/dashboard/editable-link-group.vue / L22-L51 script-setup 完整内容 | react-front/src/views/dashboard/editable-link-group.tsx |
| I0491 | ruoyi-fastapi-frontend/src/views/dashboard/editable-link-group.vue / L1-L10 template 完整内容 | react-front/src/views/dashboard/editable-link-group.tsx |
| I0492 | ruoyi-fastapi-frontend/src/views/dashboard/editable-link-group.vue / L53-L68 style-1 完整内容 | react-front/src/views/dashboard/editable-link-group.tsx |
| I0493 | ruoyi-fastapi-frontend/src/views/dashboard/editable-link-group.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/dashboard/editable-link-group.tsx |
| I0494 | ruoyi-fastapi-frontend/src/views/dashboard/index.vue / L169-L201 script 完整内容 | react-front/src/views/dashboard/index.tsx |
| I0495 | ruoyi-fastapi-frontend/src/views/dashboard/index.vue / L203-L499 script-setup 完整内容 | react-front/src/views/dashboard/index.tsx |
| I0496 | ruoyi-fastapi-frontend/src/views/dashboard/index.vue / L1-L167 template 完整内容 | react-front/src/views/dashboard/index.tsx |
| I0497 | ruoyi-fastapi-frontend/src/views/dashboard/index.vue / L501-L752 style-1 完整内容 | react-front/src/views/dashboard/index.tsx |
| I0498 | ruoyi-fastapi-frontend/src/views/dashboard/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/dashboard/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/views/dashboard/editable-link-group.vue

全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/views/dashboard/index.vue

全部模板事件/权限：.
