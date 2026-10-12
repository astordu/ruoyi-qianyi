# G033 角色与菜单/数据权限管理

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

角色与菜单/数据权限管理可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G003 时区、日期输入与提交序列化, G005 HTTP 请求、会话提示与导出, G007 字典获取、缓存与标签展示, G010 会话、权限与路由策略, G012 分页与列表工具栏, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 角色 CRUD、筛选/分页/导出、状态取消失败回滚与动态按钮权限完整。
2. 菜单树勾选含半选节点，回填已选与父子联动/全选/展开的差异保留；提交权限字符、顺序和菜单 IDs。
3. 数据范围非自定义清空部门，勾选部门同样包含半选；修改提交 dataScope，不混同菜单授权。
4. 分配用户导航 roleId 与返回页保持；角色名/权限字符/顺序必填，无选中项按钮状态按原模板。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0096 | ruoyi-fastapi-frontend/src/api/system/role.js / L4-L10 完整导出 listRole | react-front/src/api/system/role.ts |
| I0097 | ruoyi-fastapi-frontend/src/api/system/role.js / L13-L18 完整导出 getRole | react-front/src/api/system/role.ts |
| I0098 | ruoyi-fastapi-frontend/src/api/system/role.js / L21-L27 完整导出 addRole | react-front/src/api/system/role.ts |
| I0099 | ruoyi-fastapi-frontend/src/api/system/role.js / L30-L36 完整导出 updateRole | react-front/src/api/system/role.ts |
| I0100 | ruoyi-fastapi-frontend/src/api/system/role.js / L39-L45 完整导出 dataScope | react-front/src/api/system/role.ts |
| I0101 | ruoyi-fastapi-frontend/src/api/system/role.js / L48-L58 完整导出 changeRoleStatus | react-front/src/api/system/role.ts |
| I0102 | ruoyi-fastapi-frontend/src/api/system/role.js / L61-L66 完整导出 delRole | react-front/src/api/system/role.ts |
| I0108 | ruoyi-fastapi-frontend/src/api/system/role.js / L114-L119 完整导出 deptTreeSelect | react-front/src/api/system/role.ts |
| I0109 | ruoyi-fastapi-frontend/src/api/system/role.js / 模块导入、注释及函数之间全部剩余内容 | react-front/src/api/system/role.ts |
| I0665 | ruoyi-fastapi-frontend/src/views/system/role/index.vue / L245-L567 script-setup 完整内容 | react-front/src/views/system/role/index.tsx |
| I0666 | ruoyi-fastapi-frontend/src/views/system/role/index.vue / L1-L243 template 完整内容 | react-front/src/views/system/role/index.tsx |
| I0667 | ruoyi-fastapi-frontend/src/views/system/role/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/role/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/system/role.js

逻辑定位：listRole@L4–10, getRole@L13–18, addRole@L21–27, updateRole@L30–36, dataScope@L39–45, changeRoleStatus@L48–58, delRole@L61–66, deptTreeSelect@L114–119.
- URL/请求对象 L5: `'get' '/system/role/list'`; params=`query`, data=`None`
- URL/请求对象 L14: `'get' '/system/role/' + roleId`; params=`None`, data=`None`
- URL/请求对象 L22: `'post' '/system/role'`; params=`None`, data=`data`
- URL/请求对象 L31: `'put' '/system/role'`; params=`None`, data=`data`
- URL/请求对象 L40: `'put' '/system/role/dataScope'`; params=`None`, data=`data`
- URL/请求对象 L53: `'put' '/system/role/changeStatus'`; params=`None`, data=`data`
- URL/请求对象 L62: `'delete' '/system/role/' + roleId`; params=`None`, data=`None`
- URL/请求对象 L115: `'get' '/system/role/deptTree/' + roleId`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/views/system/role/index.vue

逻辑定位：getList@L302–309, handleQuery@L311–314, resetQuery@L316–320, handleDelete@L322–330, handleExport@L332–336, handleSelectionChange@L338–342, handleStatusChange@L344–353, handleCommand@L355–366, handleAuthUser@L368–370, getMenuTreeselect@L372–376, getDeptAllCheckedKeys@L378–385, reset@L387–408, handleAdd@L410–415, handleUpdate@L417–437, getRoleMenuTreeselect@L439–444, getDeptTree@L446–451, handleCheckedTreeExpand@L453–465, handleCheckedTreeNodeAll@L467–473, handleCheckedTreeConnect@L475–481, getMenuAllCheckedKeys@L483–490, submitForm@L492–512, cancel@L514–517, dataScopeSelectChange@L519–523, handleDataScope@L525–542, submitDataScope@L544–553, cancelDataScope@L555–558.
全部模板事件/权限：keyup=handleQuery@L10; keyup=handleQuery@L19; click=handleQuery@L49; click=resetQuery@L50; click=handleAdd@L59; =['system:role:add']@L60; click=handleUpdate@L69; =['system:role:edit']@L70; click=handleDelete@L79; =['system:role:remove']@L80; click=handleExport@L88; =['system:role:export']@L89; queryTable=getList@L92; selection-change=handleSelectionChange@L96; change=handleStatusChange(scope.row)@L108; click=handleUpdate(scope.row)@L120; =['system:role:edit']@L120; click=handleDelete(scope.row)@L123; =['system:role:remove']@L123; click=handleDataScope(scope.row)@L126; =['system:role:edit']@L126; click=handleAuthUser(scope.row)@L129; =['system:role:edit']@L129; pagination=getList@L140; change=handleCheckedTreeExpand($event, 'menu')@L173; change=handleCheckedTreeNodeAll($event, 'menu')@L174; change=handleCheckedTreeConnect($event, 'menu')@L175; click=submitForm@L193; click=cancel@L194; change=dataScopeSelectChange@L209; change=handleCheckedTreeExpand($event, 'dept')@L219; change=handleCheckedTreeNodeAll($event, 'dept')@L220; change=handleCheckedTreeConnect($event, 'dept')@L221; click=submitDataScope@L237; click=cancelDataScope@L238.
