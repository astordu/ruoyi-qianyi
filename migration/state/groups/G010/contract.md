# G010 会话、权限与路由策略

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

会话、权限与路由策略可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；用户、权限、锁状态与守卫有直接协作，合为同组。页面组件使用注入的视图注册表解析；策略可单独验证，真实入口和全部路由接线在 J002/J010 验收。

依赖：G002 共用数据与表单适配, G003 时区、日期输入与提交序列化, G005 HTTP 请求、会话提示与导出, G006 密码规则与记住密码适配, G009 系统主题与布局偏好

## 正常、异常与边界检查条件

1. 登录仅 trim username，成功保存 Token 并解除屏幕锁；getInfo 处理头像空值/相对地址/外链、角色缺省 ROLE_DEFAULT、权限、业务/账号时区及密码修改/过期提示的优先级。
2. 无 token 仅 /login 与 /register 放行；已登录访问 /login 回首页；锁定会话跳 /lock，解锁状态访问 /lock 返回首页，记录并恢复原 lockPath。
3. roles 未加载时获取 getInfo/getRouters 并注册路由后 replace 重进；权限 OR/角色 OR、超级管理员与 *:*:*、按钮权限按源规则判断。
4. Layout/ParentView/InnerLink 的服务端组件标记、children 路径扁平化、外链处理、query/meta/hidden/noCache/activeMenu、6 类隐藏业务入口和兜底路由均保持可解析。
5. builtin 与 plugins glob 注册全部视图；plugin/ai/... 标识不改变。插件路径拒绝非法 pluginId/段与目录穿越，缺失插件视图回 404；原插件测试的输入逐个保留，目标索引改为 .tsx。
6. 注销 API 成功才清理旧状态的行为、getRouters 失败时原 Promise 无 reject、原 redirect 查询串拼接的歧义均列为基线差异观察点；不得通过永久挂起或静默忽略错误伪装完成。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0035 | ruoyi-fastapi-frontend/src/api/login.js / L1-L71 module 完整内容 | react-front/src/api/login.ts |
| I0036 | ruoyi-fastapi-frontend/src/api/menu.js / L1-L9 module 完整内容 | react-front/src/api/menu.ts |
| I0077 | ruoyi-fastapi-frontend/src/api/system/menu.js / L21-L26 完整导出 treeselect | react-front/src/api/system/menu-session.ts |
| I0078 | ruoyi-fastapi-frontend/src/api/system/menu.js / L29-L34 完整导出 roleMenuTreeselect | react-front/src/api/system/menu-session.ts |
| I0239 | ruoyi-fastapi-frontend/src/assets/images/profile.jpg / L1-L1 asset 完整内容 | react-front/src/assets/images/profile.jpg |
| I0375 | ruoyi-fastapi-frontend/src/directive/permission/hasPermi.js / L1-L28 module 完整内容 | react-front/src/directive/permission/hasPermi.ts |
| I0376 | ruoyi-fastapi-frontend/src/directive/permission/hasRole.js / L1-L28 module 完整内容 | react-front/src/directive/permission/hasRole.ts |
| I0446 | ruoyi-fastapi-frontend/src/permission.js / L1-L77 module 完整内容 | react-front/src/permission.ts |
| I0447 | ruoyi-fastapi-frontend/src/plugins/auth.js / L1-L61 module 完整内容 | react-front/src/plugins/auth.ts |
| I0453 | ruoyi-fastapi-frontend/src/router/index.js / L1-L181 module 完整内容 | react-front/src/router/index.ts |
| I0458 | ruoyi-fastapi-frontend/src/store/modules/lock.js / L1-L28 module 完整内容 | react-front/src/store/modules/lock.ts |
| I0459 | ruoyi-fastapi-frontend/src/store/modules/permission.js / L1-L145 module 完整内容 | react-front/src/store/modules/permission.ts |
| I0462 | ruoyi-fastapi-frontend/src/store/modules/user.js / L1-L108 module 完整内容 | react-front/src/store/modules/user.ts |
| I0478 | ruoyi-fastapi-frontend/src/utils/permission.js / L1-L51 module 完整内容 | react-front/src/utils/permission.ts |
| I0480 | ruoyi-fastapi-frontend/src/utils/pluginViewResolver.js / L1-L27 module 完整内容 | react-front/src/utils/pluginViewResolver.ts |
| I0740 | ruoyi-fastapi-frontend/tests/plugins/pluginViewResolver.test.js / L1-L15 module 完整内容 | react-front/tests/plugins/pluginViewResolver.test.ts |
| I0741 | ruoyi-fastapi-frontend/tests/plugins/run-plugin-tests.js / L1-L54 module 完整内容 | react-front/tests/plugins/run-plugin-tests.ts |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/login.js

逻辑定位：login@L4–21, register@L24–33, getInfo@L36–41, unlockScreen@L44–50, logout@L53–58, getCodeImg@L61–70.
- URL/请求对象 L11: `'post' '/login'`; params=`None`, data=`data`
- URL/请求对象 L25: `'post' '/register'`; params=`None`, data=`data`
- URL/请求对象 L37: `'get' '/getInfo'`; params=`None`, data=`None`
- URL/请求对象 L45: `'post' '/unlockscreen'`; params=`None`, data=`{ password }`
- URL/请求对象 L54: `'post' '/logout'`; params=`None`, data=`None`
- URL/请求对象 L62: `'get' '/captchaImage'`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/api/menu.js

逻辑定位：getRouters@L4–9.
- URL/请求对象 L5: `'get' '/getRouters'`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/api/system/menu.js

逻辑定位：treeselect@L21–26, roleMenuTreeselect@L29–34.
- URL/请求对象 L22: `'get' '/system/menu/treeselect'`; params=`None`, data=`None`
- URL/请求对象 L30: `'get' '/system/menu/roleMenuTreeselect/' + roleId`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/assets/images/profile.jpg


### ruoyi-fastapi-frontend/src/directive/permission/hasPermi.js

逻辑定位：mounted@L8–26.

### ruoyi-fastapi-frontend/src/directive/permission/hasRole.js

逻辑定位：mounted@L8–26.

### ruoyi-fastapi-frontend/src/permission.js

逻辑定位：isWhiteList@L17–19.

### ruoyi-fastapi-frontend/src/plugins/auth.js

逻辑定位：authPermission@L3–13, authRole@L15–25, hasPermi@L29–31, hasPermiOr@L33–37, hasPermiAnd@L39–43, hasRole@L45–47, hasRoleOr@L49–53, hasRoleAnd@L55–59.

### ruoyi-fastapi-frontend/src/router/index.js

逻辑定位：component@L36–36, component@L42–42, component@L47–47, component@L52–52, component@L57–57, component@L67–67, component@L75–75, component@L87–87, component@L105–105, component@L119–119, component@L133–133, component@L147–147, component@L161–161, scrollBehavior@L172–177.

### ruoyi-fastapi-frontend/src/store/modules/lock.js

逻辑定位：state@L5–8, lockScreen@L11–16, unlockScreen@L18–23.

### ruoyi-fastapi-frontend/src/store/modules/permission.js

逻辑定位：missingView@L12–12, state@L17–23, setRoutes@L25–28, setDefaultRoutes@L29–31, setTopbarRoutes@L32–34, setSidebarRouters@L35–37, generateRoutes@L38–57, filterAsyncRouter@L62–87, filterChildren@L89–100, filterDynamicRoutes@L103–117, loadView@L124–142.

### ruoyi-fastapi-frontend/src/store/modules/user.js

逻辑定位：state@L14–24, applyTimezone@L27–30, login@L32–47, getInfo@L49–88, logOut@L90–103.

### ruoyi-fastapi-frontend/src/utils/permission.js

逻辑定位：checkPermi@L8–26, checkRole@L33–51.

### ruoyi-fastapi-frontend/src/utils/pluginViewResolver.js

逻辑定位：resolvePluginViewPath@L9–26.

### ruoyi-fastapi-frontend/tests/plugins/pluginViewResolver.test.js


### ruoyi-fastapi-frontend/tests/plugins/run-plugin-tests.js

逻辑定位：collectTestFiles@L8–24.

## 源循环/延后装配的明确接口

- `ruoyi-fastapi-frontend/src/router/index.js` → `ruoyi-fastapi-frontend/src/layout/index.vue` (G023): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/router/index.js` → `ruoyi-fastapi-frontend/src/views/redirect/index.vue` (G021): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/router/index.js` → `ruoyi-fastapi-frontend/src/views/login.vue` (G024): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/router/index.js` → `ruoyi-fastapi-frontend/src/views/register.vue` (G025): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/router/index.js` → `ruoyi-fastapi-frontend/src/views/error/404.vue` (G028): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/router/index.js` → `ruoyi-fastapi-frontend/src/views/error/401.vue` (G028): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/router/index.js` → `ruoyi-fastapi-frontend/src/views/dashboard/index.vue` (G027): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/router/index.js` → `ruoyi-fastapi-frontend/src/views/lock.vue` (G026): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/router/index.js` → `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` (G032): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/router/index.js` → `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` (G031): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/router/index.js` → `ruoyi-fastapi-frontend/src/views/system/role/authUser.vue` (G034): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/router/index.js` → `ruoyi-fastapi-frontend/src/views/system/dict/data.vue` (G038): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/router/index.js` → `ruoyi-fastapi-frontend/src/views/monitor/job/log.vue` (G045): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/router/index.js` → `ruoyi-fastapi-frontend/src/views/tool/gen/editTable.vue` (G053): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/layout/index.vue` (G023): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/components/ParentView/index.vue` (G023): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/layout/components/InnerLink/index.vue` (G029): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/dashboard/editable-link-group.vue` (G027): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/dashboard/index.vue` (G027): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/error/401.vue` (G028): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/error/404.vue` (G028): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/lock.vue` (G026): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/login.vue` (G024): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` (G043): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/monitor/cache/list.vue` (G043): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/monitor/druid/index.vue` (G029): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/monitor/job/detail.vue` (G044): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` (G044): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/monitor/job/log.vue` (G045): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/monitor/job/runtime.vue` (G044): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/monitor/logininfor/index.vue` (G046): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` (G047): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` (G048): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/monitor/operlog/index.vue` (G048): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/monitor/server/index.vue` (G049): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` (G050): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/redirect/index.vue` (G021): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/register.vue` (G025): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/config/index.vue` (G039): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/dept/index.vue` (G035): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/dict/data.vue` (G038): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` (G038): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/dict/index.vue` (G038): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/file/components/FileAclDrawer.vue` (G041): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/file/components/FileAuditDrawer.vue` (G041): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` (G041): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` (G041): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` (G041): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/file/components/FileRetentionPolicyDrawer.vue` (G041): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/file/components/FileRetentionReminderDrawer.vue` (G041): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` (G041): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue` (G041): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/file/components/FileTable.vue` (G041): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` (G041): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/file/index.vue` (G041): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/menu/index.vue` (G036): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` (G040): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/notice/index.vue` (G040): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginConfigDialog.vue` (G042): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginDependencyDialog.vue` (G042): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginDetailDialog.vue` (G042): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginDiagnosticDialog.vue` (G042): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginPlanDialog.vue` (G042): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/plugin/index.vue` (G042): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/post/index.vue` (G037): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/role/authUser.vue` (G034): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/role/index.vue` (G033): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` (G034): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` (G031): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/user/index.vue` (G030): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` (G032): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` (G032): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/user/profile/timezoneSettings.vue` (G032): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/user/profile/userAvatar.vue` (G032): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` (G032): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/system/user/view.vue` (G030): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` (G051): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` (G051): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` (G051): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/tool/build/RightPanel.vue` (G051): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` (G051): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/tool/build/index.vue` (G051): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/tool/gen/basicInfoForm.vue` (G053): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` (G052): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/tool/gen/editTable.vue` (G053): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/tool/gen/genInfoForm.vue` (G053): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/tool/gen/importTable.vue` (G052): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/tool/gen/index.vue` (G052): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/tool/swagger/index.vue` (G029): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` (G055): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` (G055): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/plugins/ai/views/model/index.vue` (G054): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。
- `ruoyi-fastapi-frontend/src/store/modules/permission.js` → `ruoyi-fastapi-frontend/src/views/error/404.vue` (G028): 路由策略接收 builtin/plugin/Layout/ParentView/InnerLink 视图注册表；shell与业务组注册真实TSX，J002/J006/J010验收，不能靠空页面通过。

这些源关系保留在 dependency-review.json；只是将运行依赖改为显式接口注入，未删除功能。最终必须以真实页面/服务接线验收。
