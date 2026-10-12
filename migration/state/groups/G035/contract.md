# G035 部门树管理

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

部门树管理可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G005 HTTP 请求、会话提示与导出, G007 字典获取、缓存与标签展示, G010 会话、权限与路由策略, G012 分页与列表工具栏, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 树列表查询、展开收起、父部门新增/编辑，编辑父候选排除当前子树；数据用源 handleTree 规则。
2. 递归记录原顺序，只提交有变化的 deptIds/orderNums 逗号串；无变化提示不请求，成功刷新基线。
3. 名称/排序/负责人/手机/邮箱/状态校验与确认删除、取消、错误反馈保留。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0065 | ruoyi-fastapi-frontend/src/api/system/dept.js / L1-L61 module 完整内容 | react-front/src/api/system/dept.ts |
| I0568 | ruoyi-fastapi-frontend/src/views/system/dept/index.vue / L156-L326 script-setup 完整内容 | react-front/src/views/system/dept/index.tsx |
| I0569 | ruoyi-fastapi-frontend/src/views/system/dept/index.vue / L1-L154 template 完整内容 | react-front/src/views/system/dept/index.tsx |
| I0570 | ruoyi-fastapi-frontend/src/views/system/dept/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/dept/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/system/dept.js

逻辑定位：listDept@L4–10, listDeptExcludeChild@L13–18, getDept@L21–26, addDept@L29–35, updateDept@L38–44, updateDeptSort@L47–53, delDept@L56–61.
- URL/请求对象 L5: `'get' '/system/dept/list'`; params=`query`, data=`None`
- URL/请求对象 L14: `'get' '/system/dept/list/exclude/' + deptId`; params=`None`, data=`None`
- URL/请求对象 L22: `'get' '/system/dept/' + deptId`; params=`None`, data=`None`
- URL/请求对象 L30: `'post' '/system/dept'`; params=`None`, data=`data`
- URL/请求对象 L39: `'put' '/system/dept'`; params=`None`, data=`data`
- URL/请求对象 L48: `'put' '/system/dept/updateSort'`; params=`None`, data=`data`
- URL/请求对象 L57: `'delete' '/system/dept/' + deptId`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/views/system/dept/index.vue

逻辑定位：getList@L190–197, cancel@L199–202, reset@L204–216, handleQuery@L218–220, resetQuery@L222–225, handleAdd@L227–237, toggleExpandAll@L239–245, handleUpdate@L247–257, submitForm@L259–277, recordOriginalOrders@L280–287, handleSaveSort@L290–313, collectChanged@L293–303, handleDelete@L316–323.
全部模板事件/权限：keyup=handleQuery@L10; click=handleQuery@L24; click=resetQuery@L25; click=handleAdd@L35; =['system:dept:add']@L36; click=handleSaveSort@L44; =['system:dept:edit']@L45; click=toggleExpandAll@L53; queryTable=getList@L56; click=handleUpdate(scope.row)@L85; =['system:dept:edit']@L85; click=handleAdd(scope.row)@L86; =['system:dept:add']@L86; click=handleDelete(scope.row)@L87; =['system:dept:remove']@L87; click=submitForm@L148; click=cancel@L149.
