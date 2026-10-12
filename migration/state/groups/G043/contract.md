# G043 Redis 缓存概览与键维护

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

Redis 缓存概览与键维护可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G005 HTTP 请求、会话提示与导出, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 概览加载 Redis 信息/命令统计/内存 ECharts 图表，resize 与卸载销毁；无数据/失败不能伪造指标。
2. 名称→键→值联动，名称/键显示格式去旧前缀；刷新、清除某名称/键/全部的请求路径与当前选择状态保持。
3. 概览与维护两个入口共用完整缓存 API；权限、loading/空态、图表配色与页面布局按原版。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0037 | ruoyi-fastapi-frontend/src/api/monitor/cache.js / L1-L58 module 完整内容 | react-front/src/api/monitor/cache.ts |
| I0515 | ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue / L67-L132 script-setup 完整内容 | react-front/src/views/monitor/cache/index.tsx |
| I0516 | ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue / L1-L65 template 完整内容 | react-front/src/views/monitor/cache/index.tsx |
| I0517 | ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/monitor/cache/index.tsx |
| I0518 | ruoyi-fastapi-frontend/src/views/monitor/cache/list.vue / L157-L246 script-setup 完整内容 | react-front/src/views/monitor/cache/list.tsx |
| I0519 | ruoyi-fastapi-frontend/src/views/monitor/cache/list.vue / L1-L155 template 完整内容 | react-front/src/views/monitor/cache/list.tsx |
| I0520 | ruoyi-fastapi-frontend/src/views/monitor/cache/list.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/monitor/cache/list.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/monitor/cache.js

逻辑定位：getCache@L4–9, listCacheName@L12–17, listCacheKey@L20–25, getCacheValue@L28–33, clearCacheName@L36–41, clearCacheKey@L44–49, clearCacheAll@L52–57.
- URL/请求对象 L5: `'get' '/monitor/cache'`; params=`None`, data=`None`
- URL/请求对象 L13: `'get' '/monitor/cache/getNames'`; params=`None`, data=`None`
- URL/请求对象 L21: `'get' '/monitor/cache/getKeys/' + cacheName`; params=`None`, data=`None`
- URL/请求对象 L29: `'get' '/monitor/cache/getValue/' + cacheName + '/' + cacheKey`; params=`None`, data=`None`
- URL/请求对象 L37: `'delete' '/monitor/cache/clearCacheName/' + cacheName`; params=`None`, data=`None`
- URL/请求对象 L45: `'delete' '/monitor/cache/clearCacheKey/' + cacheKey`; params=`None`, data=`None`
- URL/请求对象 L53: `'delete' '/monitor/cache/clearCacheAll'`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue

逻辑定位：getList@L76–129.
全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/views/monitor/cache/list.vue

逻辑定位：getCacheNames@L171–177, refreshCacheNames@L180–183, handleClearCacheName@L186–191, getCacheKeys@L194–205, refreshCacheKeys@L208–211, handleClearCacheKey@L214–219, nameFormatter@L222–224, keyFormatter@L227–229, handleCacheValue@L232–236, handleClearCacheAll@L239–243.
全部模板事件/权限：click=refreshCacheNames()@L13; row-click=getCacheKeys@L21; click=handleClearCacheName(scope.row)@L55; click=refreshCacheKeys()@L72; row-click=handleCacheValue@L80; click=handleClearCacheKey(scope.row)@L106; click=handleClearCacheAll()@L123.
