# G030 用户管理页面

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

用户管理页面可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G003 时区、日期输入与提交序列化, G005 HTTP 请求、会话提示与导出, G006 密码规则与记住密码适配, G007 字典获取、缓存与标签展示, G010 会话、权限与路由策略, G012 分页与列表工具栏, G013 树面板查询、选择与调整, G017 Excel 导入弹窗, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 部门树过滤禁用节点、搜索/时间范围/分页/列设置/选择/详情、完整新增编辑删除和导出均接入真实 API。
2. 用户名2–20、昵称必填、邮箱/手机号和密码规则按源表单；新增加载可选岗位/角色，编辑回填已分配值。
3. 状态开关取消或失败回滚，重置密码 prompt 使用动态规则；用户导入开关、模板与成功刷新接 Excel 弹窗。
4. 角色授权导航保留 userId 与 activeMenu；权限按钮与管理员特殊操作边界按模板原条件。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0110 | ruoyi-fastapi-frontend/src/api/system/user.js / L5-L11 完整导出 listUser | react-front/src/api/system/user.ts |
| I0111 | ruoyi-fastapi-frontend/src/api/system/user.js / L14-L19 完整导出 getUser | react-front/src/api/system/user.ts |
| I0112 | ruoyi-fastapi-frontend/src/api/system/user.js / L22-L28 完整导出 addUser | react-front/src/api/system/user.ts |
| I0113 | ruoyi-fastapi-frontend/src/api/system/user.js / L31-L37 完整导出 updateUser | react-front/src/api/system/user.ts |
| I0114 | ruoyi-fastapi-frontend/src/api/system/user.js / L40-L45 完整导出 delUser | react-front/src/api/system/user.ts |
| I0115 | ruoyi-fastapi-frontend/src/api/system/user.js / L48-L58 完整导出 resetUserPwd | react-front/src/api/system/user.ts |
| I0116 | ruoyi-fastapi-frontend/src/api/system/user.js / L61-L71 完整导出 changeUserStatus | react-front/src/api/system/user.ts |
| I0125 | ruoyi-fastapi-frontend/src/api/system/user.js / L141-L146 完整导出 deptTreeSelect | react-front/src/api/system/user.ts |
| I0126 | ruoyi-fastapi-frontend/src/api/system/user.js / 模块导入、注释及函数之间全部剩余内容 | react-front/src/api/system/user.ts |
| I0674 | ruoyi-fastapi-frontend/src/views/system/user/index.vue / L453-L767 script-setup 完整内容 | react-front/src/views/system/user/index.tsx |
| I0675 | ruoyi-fastapi-frontend/src/views/system/user/index.vue / L1-L451 template 完整内容 | react-front/src/views/system/user/index.tsx |
| I0676 | ruoyi-fastapi-frontend/src/views/system/user/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/user/index.tsx |
| I0694 | ruoyi-fastapi-frontend/src/views/system/user/view.vue / L128-L176 script-setup 完整内容 | react-front/src/views/system/user/view.tsx |
| I0695 | ruoyi-fastapi-frontend/src/views/system/user/view.vue / L1-L126 template 完整内容 | react-front/src/views/system/user/view.tsx |
| I0696 | ruoyi-fastapi-frontend/src/views/system/user/view.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/user/view.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/system/user.js

逻辑定位：listUser@L5–11, getUser@L14–19, addUser@L22–28, updateUser@L31–37, delUser@L40–45, resetUserPwd@L48–58, changeUserStatus@L61–71, deptTreeSelect@L141–146.
- URL/请求对象 L6: `'get' '/system/user/list'`; params=`query`, data=`None`
- URL/请求对象 L15: `'get' '/system/user/' + parseStrEmpty(userId)`; params=`None`, data=`None`
- URL/请求对象 L23: `'post' '/system/user'`; params=`None`, data=`data`
- URL/请求对象 L32: `'put' '/system/user'`; params=`None`, data=`data`
- URL/请求对象 L41: `'delete' '/system/user/' + userId`; params=`None`, data=`None`
- URL/请求对象 L53: `'put' '/system/user/resetPwd'`; params=`None`, data=`data`
- URL/请求对象 L66: `'put' '/system/user/changeStatus'`; params=`None`, data=`data`
- URL/请求对象 L142: `'get' '/system/user/deptTree'`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/views/system/user/index.vue

逻辑定位：getList@L548–557, getDeptTree@L559–566, filterDisabledDept@L568–578, handleNodeClick@L580–583, handleQuery@L585–588, resetQuery@L590–596, handleDelete@L598–610, handleExport@L612–620, handleStatusChange@L622–635, handleCommand@L637–648, handleAuthRole@L650–653, handleResetPwd@L655–669, handleSelectionChange@L671–675, handleViewData@L677–679, handleImport@L681–683, reset@L685–701, cancel@L703–706, handleAdd@L708–717, handleUpdate@L719–732, submitForm@L734–752.
全部模板事件/权限：node-click=handleNodeClick@L9; refresh=getDeptTree@L10; keyup=handleQuery@L28; keyup=handleQuery@L37; click=handleQuery@L67; click=resetQuery@L70; click=handleAdd@L80; =['system:user:add']@L81; click=handleUpdate@L91; =['system:user:edit']@L92; click=handleDelete@L102; =['system:user:remove']@L103; click=handleImport@L112; =['system:user:import']@L113; click=handleExport@L122; =['system:user:export']@L123; queryTable=getList@L129; selection-change=handleSelectionChange@L138; click=handleViewData(scope.row)@L159; change=handleStatusChange(scope.row)@L199; click=handleUpdate(scope.row)@L230; =['system:user:edit']@L231; click=handleDelete(scope.row)@L243; =['system:user:remove']@L244; click=handleResetPwd(scope.row)@L256; =['system:user:resetPwd']@L257; click=handleAuthRole(scope.row)@L269; =['system:user:edit']@L270; pagination=getList@L281; click=submitForm@L432; click=cancel@L433; success=getList@L448.

### ruoyi-fastapi-frontend/src/views/system/user/view.vue

逻辑定位：open@L152–167, handleClose@L169–171.
全部模板事件/权限：.
