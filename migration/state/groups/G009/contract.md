# G009 系统主题与布局偏好

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

系统主题与布局偏好可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G001 React 工程、环境与部署, G002 共用数据与表单适配, G005 HTTP 请求、会话提示与导出

## 正常、异常与边界检查条件

1. 深/浅主题、primary 颜色的明暗派生、navType 三种布局、侧边栏主题使用源默认设置；Element 样式选择器适配到 Ant Design 后按视觉基线核对。
2. tagsView/tagsViewPersist/tagsIcon/card或chrome/fixedHeader/sidebarLogo/dynamicTitle/footerVisible 设置和本地保存、重置保持旧结果。
3. 动态标题开关影响 document.title；刷新恢复偏好，关闭标签持久化清除缓存通过注入标签服务接线，不使主题组反向依赖标签实现。
4. settings 抽屉 openSetting 和事件接口完整提供；全局、过渡、按钮、菜单、mixin 与变量模块全部覆盖，不能只保留首页样式。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0236 | ruoyi-fastapi-frontend/src/assets/images/dark.svg / L1-L39 asset 完整内容 | react-front/src/assets/images/dark.svg |
| I0237 | ruoyi-fastapi-frontend/src/assets/images/light.svg / L1-L39 asset 完整内容 | react-front/src/assets/images/light.svg |
| I0241 | ruoyi-fastapi-frontend/src/assets/styles/btn.scss / L1-L100 style 完整内容 | react-front/src/assets/styles/btn.scss |
| I0242 | ruoyi-fastapi-frontend/src/assets/styles/element-ui.scss / L1-L96 style 完整内容 | react-front/src/assets/styles/element-ui.scss |
| I0243 | ruoyi-fastapi-frontend/src/assets/styles/index.scss / L1-L180 style 完整内容 | react-front/src/assets/styles/index.scss |
| I0244 | ruoyi-fastapi-frontend/src/assets/styles/mixin.scss / L1-L67 style 完整内容 | react-front/src/assets/styles/mixin.scss |
| I0245 | ruoyi-fastapi-frontend/src/assets/styles/ruoyi.scss / L1-L495 style 完整内容 | react-front/src/assets/styles/ruoyi.scss |
| I0246 | ruoyi-fastapi-frontend/src/assets/styles/sidebar.scss / L1-L329 style 完整内容 | react-front/src/assets/styles/sidebar.scss |
| I0247 | ruoyi-fastapi-frontend/src/assets/styles/transition.scss / L1-L81 style 完整内容 | react-front/src/assets/styles/transition.scss |
| I0248 | ruoyi-fastapi-frontend/src/assets/styles/variables.module.scss / L1-L449 style 完整内容 | react-front/src/assets/styles/variables.module.scss |
| I0405 | ruoyi-fastapi-frontend/src/layout/components/Settings/index.vue / L126-L224 script-setup 完整内容 | react-front/src/layout/components/Settings/index.tsx |
| I0406 | ruoyi-fastapi-frontend/src/layout/components/Settings/index.vue / L1-L124 template 完整内容 | react-front/src/layout/components/Settings/index.tsx |
| I0407 | ruoyi-fastapi-frontend/src/layout/components/Settings/index.vue / L226-L344 style-1 完整内容 | react-front/src/layout/components/Settings/index.tsx |
| I0408 | ruoyi-fastapi-frontend/src/layout/components/Settings/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/layout/components/Settings/index.tsx |
| I0454 | ruoyi-fastapi-frontend/src/settings.js / L1-L67 module 完整内容 | react-front/src/settings.ts |
| I0460 | ruoyi-fastapi-frontend/src/store/modules/settings.js / L1-L58 module 完整内容 | react-front/src/store/modules/settings.ts |
| I0465 | ruoyi-fastapi-frontend/src/utils/dynamicTitle.js / L1-L14 module 完整内容 | react-front/src/utils/dynamicTitle.ts |
| I0484 | ruoyi-fastapi-frontend/src/utils/theme.js / L1-L65 module 完整内容 | react-front/src/utils/theme.ts |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/assets/images/dark.svg


### ruoyi-fastapi-frontend/src/assets/images/light.svg


### ruoyi-fastapi-frontend/src/assets/styles/btn.scss


### ruoyi-fastapi-frontend/src/assets/styles/element-ui.scss


### ruoyi-fastapi-frontend/src/assets/styles/index.scss


### ruoyi-fastapi-frontend/src/assets/styles/mixin.scss


### ruoyi-fastapi-frontend/src/assets/styles/ruoyi.scss


### ruoyi-fastapi-frontend/src/assets/styles/sidebar.scss


### ruoyi-fastapi-frontend/src/assets/styles/transition.scss


### ruoyi-fastapi-frontend/src/assets/styles/variables.module.scss


### ruoyi-fastapi-frontend/src/layout/components/Settings/index.vue

逻辑定位：dynamicTitleChange@L145–147, tagsViewPersistChange@L149–152, themeChange@L154–157, handleTheme@L159–162, handleNavType@L164–167, saveSetting@L188–208, resetSetting@L210–215, openSetting@L217–219.
全部模板事件/权限：click=handleNavType(1)@L8; click=handleNavType(2)@L14; click=handleNavType(3)@L19; click=handleTheme('theme-dark')@L28; click=handleTheme('theme-light')@L38; change=themeChange@L52; change=tagsViewPersistChange@L69; change=dynamicTitleChange@L107; click=saveSetting@L120; click=resetSetting@L121.

### ruoyi-fastapi-frontend/src/settings.js


### ruoyi-fastapi-frontend/src/store/modules/settings.js

逻辑定位：state@L16–32, changeSetting@L35–40, setTitle@L42–45, toggleTheme@L47–53.

### ruoyi-fastapi-frontend/src/utils/dynamicTitle.js

逻辑定位：useDynamicTitle@L7–14.

### ruoyi-fastapi-frontend/src/utils/theme.js

逻辑定位：handleThemeStyle@L2–12, mixHexColors@L15–20, softenPrimaryForDark@L23–25, hexToRgb@L28–35, rgbToHex@L38–46, getLightColor@L49–55, getDarkColor@L58–64.

## 源循环/延后装配的明确接口

- `ruoyi-fastapi-frontend/src/layout/components/Settings/index.vue` → `ruoyi-fastapi-frontend/src/store/modules/app.js` (G023): 设置抽屉接收导航状态/重置侧边路由/标签清理回调；主题状态独立，shell接真实实现，J002/J009验收。
- `ruoyi-fastapi-frontend/src/layout/components/Settings/index.vue` → `ruoyi-fastapi-frontend/src/store/modules/permission.js` (G010): 设置抽屉接收导航状态/重置侧边路由/标签清理回调；主题状态独立，shell接真实实现，J002/J009验收。

这些源关系保留在 dependency-review.json；只是将运行依赖改为显式接口注入，未删除功能。最终必须以真实页面/服务接线验收。
