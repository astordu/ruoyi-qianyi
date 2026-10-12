# G023 应用入口与响应式导航布局

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

应用入口与响应式导航布局可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；主入口接线集中在此组；业务页面由注册表懒加载，尚未迁的业务不能标通过，最终全部页面接入由 J010 验收。

依赖：G002 共用数据与表单适配, G003 时区、日期输入与提交序列化, G005 HTTP 请求、会话提示与导出, G007 字典获取、缓存与标签展示, G008 SVG 图标与图标选择器, G009 系统主题与布局偏好, G010 会话、权限与路由策略, G011 普通与分段文件下载, G012 分页与列表工具栏, G013 树面板查询、选择与调整, G014 Cron 编辑与运行时间预览, G015 富文本编辑与图片粘贴, G016 JSON 编辑器校验与主题, G017 Excel 导入弹窗, G018 通用文件附件上传, G019 业务文件上传、进度与重试, G020 图片上传与预览, G021 多标签、页面缓存与刷新, G022 顶部公告阅读与详情, G029 内嵌页面与接口/数据源控制台

## 正常、异常与边界检查条件

1. main 所有全局组件/helpers/plugins/directives 逐项改显式 React 导入与 Context，入口 mount/日期时区焦点监听/主题初始化及卸载清理完整。
2. 横向、混合、侧边导航的菜单过滤、单子节点折叠、alwaysShow/hidden/query/external/activeMenu 与面包屑 noRedirect 保持；小屏遮罩、侧边栏 Cookie、控件 size 保留。
3. HeaderSearch Fuse 按标题/路径检索，↑↓/Enter/Esc、无结果、匹配高亮、路由 query 与外链打开均验收；监听主题和尺寸更新。
4. Navbar 个人中心、设置抽屉、锁屏、退出与主题切换都接真实能力；文档/Git快捷入口的链接与打开方式保留；所有全局表单/上传/列表组件注册引用有效，版权与 Logo 可见。
5. AppMain 普通页面缓存和 iframeViews 接真实标签/内嵌服务；focus/visibilitychange 刷新设备时区，不遗留重复 listener。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0032 | ruoyi-fastapi-frontend/src/App.vue / L5-L29 script-setup 完整内容 | react-front/src/App.tsx |
| I0033 | ruoyi-fastapi-frontend/src/App.vue / L1-L3 template 完整内容 | react-front/src/App.tsx |
| I0034 | ruoyi-fastapi-frontend/src/App.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/App.tsx |
| I0240 | ruoyi-fastapi-frontend/src/assets/logo/logo.png / L1-L1 asset 完整内容 | react-front/src/assets/logo/logo.png |
| I0249 | ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue / L12-L84 script-setup 完整内容 | react-front/src/components/Breadcrumb/index.tsx |
| I0250 | ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue / L1-L10 template 完整内容 | react-front/src/components/Breadcrumb/index.tsx |
| I0251 | ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue / L86-L97 style-1 完整内容 | react-front/src/components/Breadcrumb/index.tsx |
| I0252 | ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/Breadcrumb/index.tsx |
| I0312 | ruoyi-fastapi-frontend/src/components/Hamburger/index.vue / L17-L29 script-setup 完整内容 | react-front/src/components/Hamburger/index.tsx |
| I0313 | ruoyi-fastapi-frontend/src/components/Hamburger/index.vue / L1-L15 template 完整内容 | react-front/src/components/Hamburger/index.tsx |
| I0314 | ruoyi-fastapi-frontend/src/components/Hamburger/index.vue / L31-L42 style-1 完整内容 | react-front/src/components/Hamburger/index.tsx |
| I0315 | ruoyi-fastapi-frontend/src/components/Hamburger/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/Hamburger/index.tsx |
| I0316 | ruoyi-fastapi-frontend/src/components/HeaderSearch/index.vue / L79-L246 script-setup 完整内容 | react-front/src/components/HeaderSearch/index.tsx |
| I0317 | ruoyi-fastapi-frontend/src/components/HeaderSearch/index.vue / L1-L77 template 完整内容 | react-front/src/components/HeaderSearch/index.tsx |
| I0318 | ruoyi-fastapi-frontend/src/components/HeaderSearch/index.vue / L248-L397 style-1 完整内容 | react-front/src/components/HeaderSearch/index.tsx |
| I0319 | ruoyi-fastapi-frontend/src/components/HeaderSearch/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/HeaderSearch/index.tsx |
| I0341 | ruoyi-fastapi-frontend/src/components/ParentView/index.vue / L1-L3 template 完整内容 | react-front/src/components/ParentView/index.tsx |
| I0342 | ruoyi-fastapi-frontend/src/components/ParentView/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/ParentView/index.tsx |
| I0347 | ruoyi-fastapi-frontend/src/components/RuoYi/Doc/index.vue / L7-L13 script-setup 完整内容 | react-front/src/components/RuoYi/Doc/index.tsx |
| I0348 | ruoyi-fastapi-frontend/src/components/RuoYi/Doc/index.vue / L1-L5 template 完整内容 | react-front/src/components/RuoYi/Doc/index.tsx |
| I0349 | ruoyi-fastapi-frontend/src/components/RuoYi/Doc/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/RuoYi/Doc/index.tsx |
| I0350 | ruoyi-fastapi-frontend/src/components/RuoYi/Git/index.vue / L7-L13 script-setup 完整内容 | react-front/src/components/RuoYi/Git/index.tsx |
| I0351 | ruoyi-fastapi-frontend/src/components/RuoYi/Git/index.vue / L1-L5 template 完整内容 | react-front/src/components/RuoYi/Git/index.tsx |
| I0352 | ruoyi-fastapi-frontend/src/components/RuoYi/Git/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/RuoYi/Git/index.tsx |
| I0353 | ruoyi-fastapi-frontend/src/components/Screenfull/index.vue / L7-L11 script-setup 完整内容 | react-front/src/components/Screenfull/index.tsx |
| I0354 | ruoyi-fastapi-frontend/src/components/Screenfull/index.vue / L1-L5 template 完整内容 | react-front/src/components/Screenfull/index.tsx |
| I0355 | ruoyi-fastapi-frontend/src/components/Screenfull/index.vue / L13-L22 style-1 完整内容 | react-front/src/components/Screenfull/index.tsx |
| I0356 | ruoyi-fastapi-frontend/src/components/Screenfull/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/Screenfull/index.tsx |
| I0357 | ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue / L18-L35 script-setup 完整内容 | react-front/src/components/SizeSelect/index.tsx |
| I0358 | ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue / L1-L16 template 完整内容 | react-front/src/components/SizeSelect/index.tsx |
| I0359 | ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue / L37-L43 style-1 完整内容 | react-front/src/components/SizeSelect/index.tsx |
| I0360 | ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/SizeSelect/index.tsx |
| I0374 | ruoyi-fastapi-frontend/src/directive/index.js / L1-L9 module 完整内容 | react-front/src/directive/index.ts |
| I0377 | ruoyi-fastapi-frontend/src/layout/components/AppMain.vue / L15-L36 script-setup 完整内容 | react-front/src/layout/components/AppMain.tsx |
| I0378 | ruoyi-fastapi-frontend/src/layout/components/AppMain.vue / L1-L13 template 完整内容 | react-front/src/layout/components/AppMain.tsx |
| I0379 | ruoyi-fastapi-frontend/src/layout/components/AppMain.vue / L38-L107 style-1 完整内容 | react-front/src/layout/components/AppMain.tsx |
| I0380 | ruoyi-fastapi-frontend/src/layout/components/AppMain.vue / L109-L123 style-2 完整内容 | react-front/src/layout/components/AppMain.tsx |
| I0381 | ruoyi-fastapi-frontend/src/layout/components/AppMain.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/layout/components/AppMain.tsx |
| I0382 | ruoyi-fastapi-frontend/src/layout/components/Copyright/index.vue / L7-L14 script-setup 完整内容 | react-front/src/layout/components/Copyright/index.tsx |
| I0383 | ruoyi-fastapi-frontend/src/layout/components/Copyright/index.vue / L1-L5 template 完整内容 | react-front/src/layout/components/Copyright/index.tsx |
| I0384 | ruoyi-fastapi-frontend/src/layout/components/Copyright/index.vue / L16-L31 style-1 完整内容 | react-front/src/layout/components/Copyright/index.tsx |
| I0385 | ruoyi-fastapi-frontend/src/layout/components/Copyright/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/layout/components/Copyright/index.tsx |
| I0401 | ruoyi-fastapi-frontend/src/layout/components/Navbar.vue / L67-L174 script-setup 完整内容 | react-front/src/layout/components/Navbar.tsx |
| I0402 | ruoyi-fastapi-frontend/src/layout/components/Navbar.vue / L1-L65 template 完整内容 | react-front/src/layout/components/Navbar.tsx |
| I0403 | ruoyi-fastapi-frontend/src/layout/components/Navbar.vue / L176-L308 style-1 完整内容 | react-front/src/layout/components/Navbar.tsx |
| I0404 | ruoyi-fastapi-frontend/src/layout/components/Navbar.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/layout/components/Navbar.tsx |
| I0409 | ruoyi-fastapi-frontend/src/layout/components/Sidebar/Link.vue / L7-L40 script-setup 完整内容 | react-front/src/layout/components/Sidebar/Link.tsx |
| I0410 | ruoyi-fastapi-frontend/src/layout/components/Sidebar/Link.vue / L1-L5 template 完整内容 | react-front/src/layout/components/Sidebar/Link.tsx |
| I0411 | ruoyi-fastapi-frontend/src/layout/components/Sidebar/Link.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/layout/components/Sidebar/Link.tsx |
| I0412 | ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue / L16-L53 script-setup 完整内容 | react-front/src/layout/components/Sidebar/Logo.tsx |
| I0413 | ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue / L1-L14 template 完整内容 | react-front/src/layout/components/Sidebar/Logo.tsx |
| I0414 | ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue / L55-L102 style-1 完整内容 | react-front/src/layout/components/Sidebar/Logo.tsx |
| I0415 | ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/layout/components/Sidebar/Logo.tsx |
| I0416 | ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue / L30-L100 script-setup 完整内容 | react-front/src/layout/components/Sidebar/SidebarItem.tsx |
| I0417 | ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue / L1-L28 template 完整内容 | react-front/src/layout/components/Sidebar/SidebarItem.tsx |
| I0418 | ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/layout/components/Sidebar/SidebarItem.tsx |
| I0419 | ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue / L27-L69 script-setup 完整内容 | react-front/src/layout/components/Sidebar/index.tsx |
| I0420 | ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue / L1-L25 template 完整内容 | react-front/src/layout/components/Sidebar/index.tsx |
| I0421 | ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue / L71-L104 style-1 完整内容 | react-front/src/layout/components/Sidebar/index.tsx |
| I0422 | ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/layout/components/Sidebar/index.tsx |
| I0432 | ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue / L14-L58 script-setup 完整内容 | react-front/src/layout/components/TopBar/index.tsx |
| I0433 | ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue / L1-L12 template 完整内容 | react-front/src/layout/components/TopBar/index.tsx |
| I0434 | ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue / L60-L99 style-1 完整内容 | react-front/src/layout/components/TopBar/index.tsx |
| I0435 | ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/layout/components/TopBar/index.tsx |
| I0436 | ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue / L35-L171 script-setup 完整内容 | react-front/src/layout/components/TopNav/index.tsx |
| I0437 | ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue / L1-L33 template 完整内容 | react-front/src/layout/components/TopNav/index.tsx |
| I0438 | ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue / L173-L220 style-1 完整内容 | react-front/src/layout/components/TopNav/index.tsx |
| I0439 | ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/layout/components/TopNav/index.tsx |
| I0440 | ruoyi-fastapi-frontend/src/layout/components/index.js / L1-L5 module 完整内容 | react-front/src/layout/components/index.ts |
| I0441 | ruoyi-fastapi-frontend/src/layout/index.vue / L16-L63 script-setup 完整内容 | react-front/src/layout/index.tsx |
| I0442 | ruoyi-fastapi-frontend/src/layout/index.vue / L1-L14 template 完整内容 | react-front/src/layout/index.tsx |
| I0443 | ruoyi-fastapi-frontend/src/layout/index.vue / L65-L116 style-1 完整内容 | react-front/src/layout/index.tsx |
| I0444 | ruoyi-fastapi-frontend/src/layout/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/layout/index.tsx |
| I0445 | ruoyi-fastapi-frontend/src/main.js / L1-L88 module 完整内容 | react-front/src/main.tsx |
| I0450 | ruoyi-fastapi-frontend/src/plugins/index.js / L1-L19 module 完整内容 | react-front/src/plugins/index.ts |
| I0455 | ruoyi-fastapi-frontend/src/store/index.js / L1-L3 module 完整内容 | react-front/src/store/index.ts |
| I0456 | ruoyi-fastapi-frontend/src/store/modules/app.js / L1-L47 module 完整内容 | react-front/src/store/modules/app.ts |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/App.vue

逻辑定位：refreshTimezoneOnVisible@L11–15.
全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/assets/logo/logo.png


### ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue

逻辑定位：getBreadcrumb@L20–40, findPathNum@L41–49, getMatched@L50–59, isDashboard@L60–66, handleLink@L67–74.
全部模板事件/权限：click=handleLink(item)@L6.

### ruoyi-fastapi-frontend/src/components/Hamburger/index.vue

逻辑定位：toggleClick@L26–28.
全部模板事件/权限：click=toggleClick@L2.

### ruoyi-fastapi-frontend/src/components/HeaderSearch/index.vue

逻辑定位：click@L97–102, onDialogOpened@L104–108, close@L110–116, change@L118–137, initFuse@L139–153, generateRoutes@L155–183, querySearch@L185–203, activeStyle@L205–211, navigateResult@L213–219, selectActiveResult@L221–225, highlightText@L227–233, escapeRegExp@L235–237.
全部模板事件/权限：click=click@L3; close=close@L7; opened=onDialogOpened@L8; input=querySearch@L16; keyup=selectActiveResult@L20; keydown=navigateResult('up')@L21; keydown=navigateResult('down')@L22; mouseenter=activeIndex = index@L41; mouseleave=activeIndex = -1@L42; click=change(item)@L47.

### ruoyi-fastapi-frontend/src/components/ParentView/index.vue

全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/components/RuoYi/Doc/index.vue

逻辑定位：goto@L10–12.
全部模板事件/权限：click=goto@L3.

### ruoyi-fastapi-frontend/src/components/RuoYi/Git/index.vue

逻辑定位：goto@L10–12.
全部模板事件/权限：click=goto@L3.

### ruoyi-fastapi-frontend/src/components/Screenfull/index.vue

全部模板事件/权限：click=toggle@L3.

### ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue

逻辑定位：handleSetSize@L30–34.
全部模板事件/权限：command=handleSetSize@L3.

### ruoyi-fastapi-frontend/src/directive/index.js

逻辑定位：directive@L5–9.

### ruoyi-fastapi-frontend/src/layout/components/AppMain.vue

逻辑定位：addIframe@L31–35.
全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/layout/components/Copyright/index.vue

全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/layout/components/Navbar.vue

逻辑定位：toggleSideBar@L92–94, handleCommand@L96–110, logout@L112–122, setLayout@L125–127, lockScreen@L129–133, toggleTheme@L135–173.
全部模板事件/权限：toggleClick=toggleSideBar@L3; click=toggleTheme@L26; command=handleCommand@L41.

### ruoyi-fastapi-frontend/src/layout/components/Sidebar/Link.vue

逻辑定位：linkProps@L28–39.
全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue

全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue

逻辑定位：hasOneShowingChild@L53–77, resolvePath@L79–91, hasTitle@L93–99.
全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue

全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue

逻辑定位：setVisibleNumber@L43–46.
全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue

逻辑定位：setVisibleNumber@L115–118, handleSelect@L120–141, activeRoutes@L143–158.
全部模板事件/权限：select=handleSelect@L5.

### ruoyi-fastapi-frontend/src/layout/components/index.js


### ruoyi-fastapi-frontend/src/layout/index.vue

逻辑定位：handleClickOutside@L55–57, setLayout@L60–62.
全部模板事件/权限：click=handleClickOutside@L3; setLayout=setLayout@L7.

### ruoyi-fastapi-frontend/src/main.js


### ruoyi-fastapi-frontend/src/plugins/index.js

逻辑定位：installPlugins@L7–18.

### ruoyi-fastapi-frontend/src/store/index.js


### ruoyi-fastapi-frontend/src/store/modules/app.js

逻辑定位：state@L6–14, toggleSideBar@L16–27, closeSideBar@L28–32, toggleDevice@L33–35, setSize@L36–39, toggleSideBarHide@L40–42.
