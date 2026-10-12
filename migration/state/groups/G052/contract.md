# G052 代码生成表管理、导入与预览

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

代码生成表管理、导入与预览可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G005 HTTP 请求、会话提示与导出, G010 会话、权限与路由策略, G011 普通与分段文件下载, G012 分页与列表工具栏, G021 多标签、页面缓存与刷新, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 数据源选项按默认源选择，表查询/时间范围/分页、导入已存在数据库表与创建SQL弹窗都携带 dataSourceName。
2. 生成批次必须同一数据源，genType=1 调接口生成到自定义路径，其他下载zip；表名URL编码、空选择/多源拒绝和数据库同步确认保留。
3. 预览多个文件语法高亮和复制、删除/修改入口/返回刷新 query 保留；生成仍保持 Vue2/Vue3 产品能力，前端运行框架迁移不修改后端模板。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0127 | ruoyi-fastapi-frontend/src/api/tool/gen.js / L4-L9 完整导出 listDataSources | react-front/src/api/tool/gen.ts |
| I0128 | ruoyi-fastapi-frontend/src/api/tool/gen.js / L12-L18 完整导出 listTable | react-front/src/api/tool/gen.ts |
| I0129 | ruoyi-fastapi-frontend/src/api/tool/gen.js / L20-L26 完整导出 listDbTable | react-front/src/api/tool/gen.ts |
| I0132 | ruoyi-fastapi-frontend/src/api/tool/gen.js / L46-L52 完整导出 importTable | react-front/src/api/tool/gen.ts |
| I0133 | ruoyi-fastapi-frontend/src/api/tool/gen.js / L55-L61 完整导出 createTable | react-front/src/api/tool/gen.ts |
| I0134 | ruoyi-fastapi-frontend/src/api/tool/gen.js / L64-L69 完整导出 previewTable | react-front/src/api/tool/gen.ts |
| I0135 | ruoyi-fastapi-frontend/src/api/tool/gen.js / L72-L77 完整导出 delTable | react-front/src/api/tool/gen.ts |
| I0136 | ruoyi-fastapi-frontend/src/api/tool/gen.js / L80-L86 完整导出 genCode | react-front/src/api/tool/gen.ts |
| I0137 | ruoyi-fastapi-frontend/src/api/tool/gen.js / L89-L95 完整导出 synchDb | react-front/src/api/tool/gen.ts |
| I0138 | ruoyi-fastapi-frontend/src/api/tool/gen.js / 模块导入、注释及函数之间全部剩余内容 | react-front/src/api/tool/gen.ts |
| I0721 | ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue / L32-L76 script-setup 完整内容 | react-front/src/views/tool/gen/createTable.tsx |
| I0722 | ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue / L1-L30 template 完整内容 | react-front/src/views/tool/gen/createTable.tsx |
| I0723 | ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/tool/gen/createTable.tsx |
| I0730 | ruoyi-fastapi-frontend/src/views/tool/gen/importTable.vue / L71-L174 script-setup 完整内容 | react-front/src/views/tool/gen/importTable.tsx |
| I0731 | ruoyi-fastapi-frontend/src/views/tool/gen/importTable.vue / L1-L69 template 完整内容 | react-front/src/views/tool/gen/importTable.tsx |
| I0732 | ruoyi-fastapi-frontend/src/views/tool/gen/importTable.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/tool/gen/importTable.tsx |
| I0733 | ruoyi-fastapi-frontend/src/views/tool/gen/index.vue / L180-L353 script-setup 完整内容 | react-front/src/views/tool/gen/index.tsx |
| I0734 | ruoyi-fastapi-frontend/src/views/tool/gen/index.vue / L1-L178 template 完整内容 | react-front/src/views/tool/gen/index.tsx |
| I0735 | ruoyi-fastapi-frontend/src/views/tool/gen/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/tool/gen/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/tool/gen.js

逻辑定位：listDataSources@L4–9, listTable@L12–18, listDbTable@L20–26, importTable@L46–52, createTable@L55–61, previewTable@L64–69, delTable@L72–77, genCode@L80–86, synchDb@L89–95.
- URL/请求对象 L5: `'get' '/tool/gen/dataSources'`; params=`None`, data=`None`
- URL/请求对象 L13: `'get' '/tool/gen/list'`; params=`query`, data=`None`
- URL/请求对象 L21: `'get' '/tool/gen/db/list'`; params=`query`, data=`None`
- URL/请求对象 L47: `'post' '/tool/gen/importTable'`; params=`data`, data=`None`
- URL/请求对象 L56: `'post' '/tool/gen/createTable'`; params=`data`, data=`None`
- URL/请求对象 L65: `'get' '/tool/gen/preview/' + tableId`; params=`None`, data=`None`
- URL/请求对象 L73: `'delete' '/tool/gen/' + tableId`; params=`None`, data=`None`
- URL/请求对象 L81: `'get' '/tool/gen/genCode/' + tableName`; params=`{ dataSourceName }`, data=`None`
- URL/请求对象 L90: `'get' '/tool/gen/synchDb/' + tableName`; params=`{ dataSourceName }`, data=`None`

### ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue

逻辑定位：default@L42–42, show@L48–52, handleImportTable@L55–71.
全部模板事件/权限：click=handleImportTable@L25; click=visible = false@L26.

### ruoyi-fastapi-frontend/src/views/tool/gen/importTable.vue

逻辑定位：default@L82–82, show@L97–104, handleSourceChange@L107–112, clickRow@L115–117, handleSelectionChange@L120–122, getList@L125–135, handleQuery@L138–141, resetQuery@L144–149, handleImportTable@L152–169.
全部模板事件/权限：change=handleSourceChange@L11; keyup=handleQuery@L27; keyup=handleQuery@L36; click=handleQuery@L40; click=resetQuery@L41; row-click=clickRow@L45; selection-change=handleSelectionChange@L45; pagination=getList@L59; click=handleImportTable@L64; click=visible = false@L65.

### ruoyi-fastapi-frontend/src/views/tool/gen/index.vue

逻辑定位：getList@L232–239, getDataSources@L242–246, handleQuery@L249–252, handleGenTable@L255–280, handleSynchDb@L283–290, openImportTable@L293–295, openCreateTable@L298–300, resetQuery@L303–307, handlePreview@L310–316, copyTextSuccess@L319–321, handleSelectionChange@L324–330, handleEditTable@L333–338, handleDelete@L341–349.
全部模板事件/权限：keyup=handleQuery@L10; keyup=handleQuery@L19; click=handleQuery@L49; click=resetQuery@L50; click=handleGenTable@L61; =['tool:gen:code']@L62; click=openCreateTable@L70; =['admin']@L71; click=openImportTable@L79; =['tool:gen:import']@L80; click=handleEditTable@L89; =['tool:gen:edit']@L90; click=handleDelete@L99; =['tool:gen:remove']@L100; queryTable=getList@L103; selection-change=handleSelectionChange@L106; click=handlePreview(scope.row)@L137; =['tool:gen:preview']@L137; click=handleEditTable(scope.row)@L140; =['tool:gen:edit']@L140; click=handleDelete(scope.row)@L143; =['tool:gen:remove']@L143; click=handleSynchDb(scope.row)@L146; =['tool:gen:edit']@L146; click=handleGenTable(scope.row)@L149; =['tool:gen:code']@L149; pagination=getList@L159; ok=handleQuery@L175; ok=handleQuery@L176.
