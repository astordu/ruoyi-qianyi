# G037 岗位管理页面

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

岗位管理页面可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G005 HTTP 请求、会话提示与导出, G007 字典获取、缓存与标签展示, G010 会话、权限与路由策略, G012 分页与列表工具栏, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 编码/名称/状态筛选和分页，完整新增修改删除、批量选择与 Excel 导出按原 endpoint/method 发送。
2. 编码/名称/岗位顺序必填，新增清空、编辑回填、取消不提交；错误时加载/表单反馈与源码对照。
3. 操作权限、状态标签、排序与时间显示按旧页面视觉验证。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0095 | ruoyi-fastapi-frontend/src/api/system/post.js / L1-L45 module 完整内容 | react-front/src/api/system/post.ts |
| I0659 | ruoyi-fastapi-frontend/src/views/system/post/index.vue / L147-L277 script-setup 完整内容 | react-front/src/views/system/post/index.tsx |
| I0660 | ruoyi-fastapi-frontend/src/views/system/post/index.vue / L1-L145 template 完整内容 | react-front/src/views/system/post/index.tsx |
| I0661 | ruoyi-fastapi-frontend/src/views/system/post/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/post/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/system/post.js

逻辑定位：listPost@L4–10, getPost@L13–18, addPost@L21–27, updatePost@L30–36, delPost@L39–44.
- URL/请求对象 L5: `'get' '/system/post/list'`; params=`query`, data=`None`
- URL/请求对象 L14: `'get' '/system/post/' + postId`; params=`None`, data=`None`
- URL/请求对象 L22: `'post' '/system/post'`; params=`None`, data=`data`
- URL/请求对象 L31: `'put' '/system/post'`; params=`None`, data=`data`
- URL/请求对象 L40: `'delete' '/system/post/' + postId`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/views/system/post/index.vue

逻辑定位：getList@L182–189, cancel@L191–194, reset@L196–206, handleQuery@L208–211, resetQuery@L213–216, handleSelectionChange@L218–222, handleAdd@L224–228, handleUpdate@L230–238, submitForm@L240–258, handleDelete@L260–268, handleExport@L270–274.
全部模板事件/权限：keyup=handleQuery@L10; keyup=handleQuery@L19; click=handleQuery@L33; click=resetQuery@L34; click=handleAdd@L44; =['system:post:add']@L45; click=handleUpdate@L54; =['system:post:edit']@L55; click=handleDelete@L64; =['system:post:remove']@L65; click=handleExport@L73; =['system:post:export']@L74; queryTable=getList@L77; selection-change=handleSelectionChange@L80; click=handleUpdate(scope.row)@L98; =['system:post:edit']@L98; click=handleDelete(scope.row)@L99; =['system:post:remove']@L99; pagination=getList@L109; click=submitForm@L139; click=cancel@L140.
