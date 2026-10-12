# G036 菜单树、路由信息与排序

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

菜单树、路由信息与排序可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G005 HTTP 请求、会话提示与导出, G007 字典获取、缓存与标签展示, G008 SVG 图标与图标选择器, G010 会话、权限与路由策略, G012 分页与列表工具栏, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 目录/菜单/按钮三种类型显示不同字段，父树、图标筛选、路由 path/component/query/权限/外链/缓存/可见性按源模板可编辑。
2. 树展开收起、CRUD 与递归只保存变化的排序，空变化不请求；禁用/隐藏项回显不丢失。
3. roleMenuTreeselect/treeselect 公共接口归只读 menu-read.ts，角色页不依赖先完成菜单编辑页面；新增菜单后登录/重新加载路由能找到目标页面。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0075 | ruoyi-fastapi-frontend/src/api/system/menu.js / L4-L10 完整导出 listMenu | react-front/src/api/system/menu.ts |
| I0076 | ruoyi-fastapi-frontend/src/api/system/menu.js / L13-L18 完整导出 getMenu | react-front/src/api/system/menu.ts |
| I0079 | ruoyi-fastapi-frontend/src/api/system/menu.js / L37-L43 完整导出 addMenu | react-front/src/api/system/menu.ts |
| I0080 | ruoyi-fastapi-frontend/src/api/system/menu.js / L46-L52 完整导出 updateMenu | react-front/src/api/system/menu.ts |
| I0081 | ruoyi-fastapi-frontend/src/api/system/menu.js / L55-L61 完整导出 updateMenuSort | react-front/src/api/system/menu.ts |
| I0082 | ruoyi-fastapi-frontend/src/api/system/menu.js / L64-L69 完整导出 delMenu | react-front/src/api/system/menu.ts |
| I0083 | ruoyi-fastapi-frontend/src/api/system/menu.js / 模块导入、注释及函数之间全部剩余内容 | react-front/src/api/system/menu.ts |
| I0625 | ruoyi-fastapi-frontend/src/views/system/menu/index.vue / L308-L497 script-setup 完整内容 | react-front/src/views/system/menu/index.tsx |
| I0626 | ruoyi-fastapi-frontend/src/views/system/menu/index.vue / L1-L306 template 完整内容 | react-front/src/views/system/menu/index.tsx |
| I0627 | ruoyi-fastapi-frontend/src/views/system/menu/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/menu/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/system/menu.js

逻辑定位：listMenu@L4–10, getMenu@L13–18, addMenu@L37–43, updateMenu@L46–52, updateMenuSort@L55–61, delMenu@L64–69.
- URL/请求对象 L5: `'get' '/system/menu/list'`; params=`query`, data=`None`
- URL/请求对象 L14: `'get' '/system/menu/' + menuId`; params=`None`, data=`None`
- URL/请求对象 L38: `'post' '/system/menu'`; params=`None`, data=`data`
- URL/请求对象 L47: `'put' '/system/menu'`; params=`None`, data=`data`
- URL/请求对象 L56: `'put' '/system/menu/updateSort'`; params=`None`, data=`data`
- URL/请求对象 L65: `'delete' '/system/menu/' + menuId`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/views/system/menu/index.vue

逻辑定位：getList@L343–350, getTreeselect@L352–359, cancel@L361–364, reset@L366–381, showSelectIcon@L383–385, selected@L387–389, handleQuery@L391–393, resetQuery@L395–398, handleAdd@L400–410, toggleExpandAll@L412–418, handleUpdate@L420–428, submitForm@L430–448, recordOriginalOrders@L451–458, handleSaveSort@L461–484, collectChanged@L464–474, handleDelete@L487–494.
全部模板事件/权限：keyup=handleQuery@L10; click=handleQuery@L24; click=resetQuery@L25; click=handleAdd@L35; =['system:menu:add']@L36; click=handleSaveSort@L44; =['system:menu:edit']@L45; click=toggleExpandAll@L53; queryTable=getList@L56; click=handleUpdate(scope.row)@L96; =['system:menu:edit']@L96; click=handleAdd(scope.row)@L97; =['system:menu:add']@L97; click=handleDelete(scope.row)@L98; =['system:menu:remove']@L98; blur=showSelectIcon@L136; selected=selected@L148; click=submitForm@L300; click=cancel@L301.
