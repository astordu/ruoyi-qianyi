# G021 多标签、页面缓存与刷新

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

多标签、页面缓存与刷新可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G008 SVG 图标与图标选择器, G009 系统主题与布局偏好, G010 会话、权限与路由策略

## 正常、异常与边界检查条件

1. visited/cached/iframeViews 分别管理，路由 path 去重、affix 保留、noCache 排除；标签持久化受设置控制，刷新恢复次序。
2. 关闭当前/左/右/其他/全部及刷新后打开正确目标，保留 affix；最后页面兜底首页，iframe 刷新/移除不同于普通组件。
3. 滚轮/左右按钮/当前标签滚入视野、上下文菜单、card/chrome 两种样式、全屏操作按旧事件处理；卸载清理监听。
4. React 必须提供可验证的缓存保活机制以替代 KeepAlive，页面保留与退出清理需要真页面集成；不只复制标签 DOM。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0423 | ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue / L12-L139 script-setup 完整内容 | react-front/src/layout/components/TagsView/ScrollPane.tsx |
| I0424 | ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue / L1-L10 template 完整内容 | react-front/src/layout/components/TagsView/ScrollPane.tsx |
| I0425 | ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue / L141-L156 style-1 完整内容 | react-front/src/layout/components/TagsView/ScrollPane.tsx |
| I0426 | ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/layout/components/TagsView/ScrollPane.tsx |
| I0427 | ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue / L68-L319 script-setup 完整内容 | react-front/src/layout/components/TagsView/index.tsx |
| I0428 | ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue / L1-L66 template 完整内容 | react-front/src/layout/components/TagsView/index.tsx |
| I0429 | ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue / L321-L585 style-1 完整内容 | react-front/src/layout/components/TagsView/index.tsx |
| I0430 | ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue / L587-L661 style-2 完整内容 | react-front/src/layout/components/TagsView/index.tsx |
| I0431 | ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/layout/components/TagsView/index.tsx |
| I0452 | ruoyi-fastapi-frontend/src/plugins/tab.js / L1-L76 module 完整内容 | react-front/src/plugins/tab.ts |
| I0461 | ruoyi-fastapi-frontend/src/store/modules/tagsView.js / L1-L227 module 完整内容 | react-front/src/store/modules/tagsView.ts |
| I0558 | ruoyi-fastapi-frontend/src/views/redirect/index.vue / L5-L14 script-setup 完整内容 | react-front/src/views/redirect/index.tsx |
| I0559 | ruoyi-fastapi-frontend/src/views/redirect/index.vue / L1-L3 template 完整内容 | react-front/src/views/redirect/index.tsx |
| I0560 | ruoyi-fastapi-frontend/src/views/redirect/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/redirect/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue

逻辑定位：emitScroll@L28–31, smoothScrollTo@L33–60, ease@L40–45, step@L47–57, handleScroll@L62–67, moveToTarget@L72–114, scrollToStart@L116–118, scrollToEnd@L120–123, getScrollState@L125–131.
全部模板事件/权限：wheel=handleScroll@L6.

### ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue

逻辑定位：isActive@L125–127, tagActiveStyle@L128–134, isAffix@L135–137, isFirstView@L138–145, isLastView@L146–153, filterAffixTags@L154–174, initTags@L175–186, addTags@L187–192, moveToCurrentTag@L193–204, scrollLeft@L205–208, scrollRight@L209–212, updateArrowState@L213–221, toggleFullscreen@L222–231, onFullscreenChange@L232–239, handleDropdownCommand@L240–252, refreshSelectedTag@L253–258, closeSelectedTag@L259–265, closeRightTags@L266–272, closeLeftTags@L273–279, closeOthersTags@L280–285, closeAllTags@L286–293, toLastView@L294–305, openMenu@L306–311, closeMenu@L312–314, handleScroll@L315–318.
全部模板事件/权限：click=scrollLeft@L4; scroll=handleScroll@L9; update-arrows=updateArrowState@L9; click=!isAffix(tag) ? closeSelectedTag(tag) : ''@L18; contextmenu=openMenu(tag, $event)@L19; click=closeSelectedTag(tag)@L23; click=scrollRight@L30; command=handleDropdownCommand@L35; click=refreshSelectedTag(selectedDropdownTag)@L52; click=refreshSelectedTag(selectedTag)@L58; click=closeSelectedTag(selectedTag)@L59; click=closeOthersTags@L60; click=closeLeftTags@L61; click=closeRightTags@L62; click=closeAllTags(selectedTag)@L63.

### ruoyi-fastapi-frontend/src/plugins/tab.js

逻辑定位：refreshPage@L6–28, closeOpenPage@L30–35, closePage@L37–48, closeAllPage@L50–52, closeLeftPage@L54–56, closeRightPage@L58–60, closeOtherPage@L62–64, openPage@L66–70, updatePage@L72–74.

### ruoyi-fastapi-frontend/src/store/modules/tagsView.js

逻辑定位：isPersistEnabled@L6–8, saveVisitedViews@L10–14, loadVisitedViews@L16–18, clearVisitedViews@L20–22, state@L27–31, addView@L33–36, addIframeView@L37–44, addVisitedView@L45–53, addAffixView@L54–61, addCachedView@L62–67, delView@L68–77, delVisitedView@L78–90, delIframeView@L91–96, delCachedView@L97–103, delOthersViews@L104–113, delOthersVisitedViews@L114–123, delOthersCachedViews@L124–134, delAllViews@L135–144, delAllVisitedViews@L145–153, delAllCachedViews@L154–159, updateVisitedView@L160–167, delRightTags@L168–191, delLeftTags@L192–215, loadPersistedViews@L217–222.

### ruoyi-fastapi-frontend/src/views/redirect/index.vue

全部模板事件/权限：.
