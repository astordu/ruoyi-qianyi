# G034 按角色分配与取消用户

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

按角色分配与取消用户可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G005 HTTP 请求、会话提示与导出, G007 字典获取、缓存与标签展示, G010 会话、权限与路由策略, G012 分页与列表工具栏, G021 多标签、页面缓存与刷新, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 路由 roleId 下已授权用户分页查询，单个与批量取消确认后刷新，取消不发送。
2. 选择弹窗分页加载未授权用户、点击行切换勾选，无选择提示；选择多个 userIds 逗号串提交后发成功事件刷新父页。
3. 手机/用户名筛选、回退标签页、权限与请求错误反馈全部接线。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0103 | ruoyi-fastapi-frontend/src/api/system/role.js / L69-L75 完整导出 allocatedUserList | react-front/src/api/system/role-roleusers.ts |
| I0104 | ruoyi-fastapi-frontend/src/api/system/role.js / L78-L84 完整导出 unallocatedUserList | react-front/src/api/system/role-roleusers.ts |
| I0105 | ruoyi-fastapi-frontend/src/api/system/role.js / L87-L93 完整导出 authUserCancel | react-front/src/api/system/role-roleusers.ts |
| I0106 | ruoyi-fastapi-frontend/src/api/system/role.js / L96-L102 完整导出 authUserCancelAll | react-front/src/api/system/role-roleusers.ts |
| I0107 | ruoyi-fastapi-frontend/src/api/system/role.js / L105-L111 完整导出 authUserSelectAll | react-front/src/api/system/role-roleusers.ts |
| I0662 | ruoyi-fastapi-frontend/src/views/system/role/authUser.vue / L94-L172 script-setup 完整内容 | react-front/src/views/system/role/authUser.tsx |
| I0663 | ruoyi-fastapi-frontend/src/views/system/role/authUser.vue / L2-L92 template 完整内容 | react-front/src/views/system/role/authUser.tsx |
| I0664 | ruoyi-fastapi-frontend/src/views/system/role/authUser.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/role/authUser.tsx |
| I0668 | ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue / L63-L138 script-setup 完整内容 | react-front/src/views/system/role/selectUser.tsx |
| I0669 | ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue / L1-L61 template 完整内容 | react-front/src/views/system/role/selectUser.tsx |
| I0670 | ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/role/selectUser.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/system/role.js

逻辑定位：allocatedUserList@L69–75, unallocatedUserList@L78–84, authUserCancel@L87–93, authUserCancelAll@L96–102, authUserSelectAll@L105–111.
- URL/请求对象 L70: `'get' '/system/role/authUser/allocatedList'`; params=`query`, data=`None`
- URL/请求对象 L79: `'get' '/system/role/authUser/unallocatedList'`; params=`query`, data=`None`
- URL/请求对象 L88: `'put' '/system/role/authUser/cancel'`; params=`None`, data=`data`
- URL/请求对象 L97: `'put' '/system/role/authUser/cancelAll'`; params=`data`, data=`None`
- URL/请求对象 L106: `'put' '/system/role/authUser/selectAll'`; params=`data`, data=`None`

### ruoyi-fastapi-frontend/src/views/system/role/authUser.vue

逻辑定位：getList@L118–125, handleClose@L127–130, handleQuery@L132–135, resetQuery@L137–140, handleSelectionChange@L142–145, openSelectUser@L147–149, cancelAuthUser@L151–158, cancelAuthUserAll@L160–169.
全部模板事件/权限：keyup=handleQuery@L11; keyup=handleQuery@L20; click=handleQuery@L24; click=resetQuery@L25; click=openSelectUser@L35; =['system:role:add']@L36; click=cancelAuthUserAll@L45; =['system:role:remove']@L46; click=handleClose@L54; queryTable=getList@L57; selection-change=handleSelectionChange@L60; click=cancelAuthUser(scope.row)@L78; =['system:role:remove']@L78; pagination=getList@L88; ok=handleQuery@L90.

### ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue

逻辑定位：show@L89–93, clickRow@L95–97, handleSelectionChange@L99–101, getList@L103–108, handleQuery@L110–113, resetQuery@L115–118, handleSelectUser@L121–133.
全部模板事件/权限：keyup=handleQuery@L11; keyup=handleQuery@L20; click=handleQuery@L24; click=resetQuery@L25; row-click=clickRow@L29; selection-change=handleSelectionChange@L29; pagination=getList@L51; click=handleSelectUser@L56; click=visible = false@L57.
