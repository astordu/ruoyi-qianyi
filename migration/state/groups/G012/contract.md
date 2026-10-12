# G012 分页与列表工具栏

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

分页与列表工具栏可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G009 系统主题与布局偏好

## 正常、异常与边界检查条件

1. page/limit 受控绑定，改变 pageSize 使当前页超总数时回 1，再发送含 page/limit 的 pagination 回调；autoScroll 控制滚动。
2. 搜索显示/隐藏与过渡、queryTable 刷新、列显示/全选/清除同时可用；columns 数组/对象两类输入和 storageKey 持久化按原处理。
3. 相邻不同页面的分页、列配置与搜索状态互不污染；无 storageKey 不写缓存，卸载清理动画/定时器。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0337 | ruoyi-fastapi-frontend/src/components/Pagination/index.vue / L17-L95 script-setup 完整内容 | react-front/src/components/Pagination/index.tsx |
| I0338 | ruoyi-fastapi-frontend/src/components/Pagination/index.vue / L1-L15 template 完整内容 | react-front/src/components/Pagination/index.tsx |
| I0339 | ruoyi-fastapi-frontend/src/components/Pagination/index.vue / L97-L104 style-1 完整内容 | react-front/src/components/Pagination/index.tsx |
| I0340 | ruoyi-fastapi-frontend/src/components/Pagination/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/Pagination/index.tsx |
| I0343 | ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue / L42-L228 script-setup 完整内容 | react-front/src/components/RightToolbar/index.tsx |
| I0344 | ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue / L1-L40 template 完整内容 | react-front/src/components/RightToolbar/index.tsx |
| I0345 | ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue / L230-L249 style-1 完整内容 | react-front/src/components/RightToolbar/index.tsx |
| I0346 | ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/RightToolbar/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/components/Pagination/index.vue

逻辑定位：default@L35–37, get@L64–66, set@L67–69, get@L72–74, set@L75–77, handleSizeChange@L79–87, handleCurrentChange@L88–93.
全部模板事件/权限：size-change=handleSizeChange@L11; current-change=handleCurrentChange@L12.

### ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue

逻辑定位：default@L54–54, get@L97–97, set@L98–98, toggleSearch@L105–113, animateSearch@L114–133, clear@L117–117, refresh@L136–138, dataChange@L141–153, showColumn@L156–158, checkboxChange@L195–202, toggleCheckAll@L205–213, saveStorage@L216–227.
全部模板事件/权限：click=toggleSearch()@L5; click=refresh()@L8; click=showColumn()@L11; change=toggleCheckAll@L18; change=checkboxChange($event, key)@L23; change=dataChange@L36.
