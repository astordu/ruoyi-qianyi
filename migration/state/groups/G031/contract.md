# G031 按用户分配角色

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

按用户分配角色可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G005 HTTP 请求、会话提示与导出, G012 分页与列表工具栏, G021 多标签、页面缓存与刷新, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 按路由 userId 读取当前用户和已分配角色，rowKey=roleId，禁用角色不可选择，点击行只切换可选角色。
2. 保存 roleIds 逗号串用 PUT params 提交，成功关闭并回正确原页；请求失败不展示成功。
3. 直接 URL、刷新、取消/关闭与权限隐藏入口接真实路由。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0123 | ruoyi-fastapi-frontend/src/api/system/user.js / L124-L129 完整导出 getAuthRole | react-front/src/api/system/user-userroles.ts |
| I0124 | ruoyi-fastapi-frontend/src/api/system/user.js / L132-L138 完整导出 updateAuthRole | react-front/src/api/system/user-userroles.ts |
| I0671 | ruoyi-fastapi-frontend/src/views/system/user/authRole.vue / L48-L123 script-setup 完整内容 | react-front/src/views/system/user/authRole.tsx |
| I0672 | ruoyi-fastapi-frontend/src/views/system/user/authRole.vue / L1-L46 template 完整内容 | react-front/src/views/system/user/authRole.tsx |
| I0673 | ruoyi-fastapi-frontend/src/views/system/user/authRole.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/user/authRole.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/system/user.js

逻辑定位：getAuthRole@L124–129, updateAuthRole@L132–138.
- URL/请求对象 L125: `'get' '/system/user/authRole/' + userId`; params=`None`, data=`None`
- URL/请求对象 L133: `'put' '/system/user/authRole'`; params=`data`, data=`None`

### ruoyi-fastapi-frontend/src/views/system/user/authRole.vue

逻辑定位：clickRow@L67–71, handleSelectionChange@L74–76, getRowKey@L79–81, checkSelectable@L84–86, close@L89–92, submitForm@L95–102.
全部模板事件/权限：row-click=clickRow@L20; selection-change=handleSelectionChange@L20; click=submitForm()@L41; click=close()@L42.
