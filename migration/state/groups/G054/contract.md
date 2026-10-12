# G054 AI 模型管理

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

AI 模型管理可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G005 HTTP 请求、会话提示与导出, G007 字典获取、缓存与标签展示, G010 会话、权限与路由策略, G012 分页与列表工具栏, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 模型 CRUD/筛选/分页/选择，provider字典、模型编码/名称/状态必填，推理/图片支持、温度/最大输出、BaseURL/APIKey等字段完整。
2. 凭证由后端管理，报告/测试日志脱敏；新增与编辑分别 POST/PUT，取消删除不调用。
3. all接口供聊天模型选择，plugin/ai/model/index 标识与后端 ai:model:* 权限不改变；README 改为 React 目录与验证命令。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0017 | ruoyi-fastapi-frontend/plugins/ai/README.md / L1-L84 document-or-config 完整内容 | react-front/plugins/ai/README.md |
| I0019 | ruoyi-fastapi-frontend/plugins/ai/api/model.js / L1-L53 module 完整内容 | react-front/plugins/ai/api/model.ts |
| I0028 | ruoyi-fastapi-frontend/plugins/ai/views/model/index.vue / L312-L473 script-setup 完整内容 | react-front/plugins/ai/views/model/index.tsx |
| I0029 | ruoyi-fastapi-frontend/plugins/ai/views/model/index.vue / L1-L310 template 完整内容 | react-front/plugins/ai/views/model/index.tsx |
| I0030 | ruoyi-fastapi-frontend/plugins/ai/views/model/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/plugins/ai/views/model/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/plugins/ai/README.md


### ruoyi-fastapi-frontend/plugins/ai/api/model.js

逻辑定位：listModel@L4–10, listModelAll@L13–18, getModel@L21–26, addModel@L29–35, updateModel@L38–44, delModel@L47–52.
- URL/请求对象 L5: `"get" "/ai/model/list"`; params=`query`, data=`None`
- URL/请求对象 L14: `"get" "/ai/model/all"`; params=`None`, data=`None`
- URL/请求对象 L22: `"get" "/ai/model/" + modelId`; params=`None`, data=`None`
- URL/请求对象 L30: `"post" "/ai/model"`; params=`None`, data=`data`
- URL/请求对象 L39: `"put" "/ai/model"`; params=`None`, data=`data`
- URL/请求对象 L48: `"delete" "/ai/model/" + modelId`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/plugins/ai/views/model/index.vue

逻辑定位：getList@L363–370, cancel@L373–376, reset@L379–397, handleQuery@L400–403, resetQuery@L406–409, handleSelectionChange@L412–416, handleAdd@L419–423, handleUpdate@L426–434, submitForm@L437–455, handleDelete@L458–470.
全部模板事件/权限：keyup=handleQuery@L15; keyup=handleQuery@L24; click=handleQuery@L50; click=resetQuery@L53; click=handleAdd@L63; =['ai:model:add']@L64; click=handleUpdate@L74; =['ai:model:edit']@L75; click=handleDelete@L85; =['ai:model:remove']@L86; queryTable=getList@L92; selection-change=handleSelectionChange@L99; click=handleUpdate(scope.row)@L145; =['ai:model:edit']@L146; click=handleDelete(scope.row)@L153; =['ai:model:remove']@L154; pagination=getList@L166; click=submitForm@L304; click=cancel@L305.
