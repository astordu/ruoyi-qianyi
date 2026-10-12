# G045 调度日志查询与清理

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

调度日志查询与清理可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G003 时区、日期输入与提交序列化, G005 HTTP 请求、会话提示与导出, G007 字典获取、缓存与标签展示, G010 会话、权限与路由策略, G012 分页与列表工具栏, G021 多标签、页面缓存与刷新, G023 应用入口与响应式导航布局, G044 定时任务配置、运行与同步

## 正常、异常与边界检查条件

1. route.params.jobId=0 代表所有任务，query.executionId 可定位执行；切换参数清旧任务名/分页，日期范围按显示时区。
2. 分页查询、详情复用 job detail 的 log 模式、批量删除/全部清理/导出；取消不请求，成功刷新。
3. 关闭日志标签返回正确页面，时区变化下已有范围重查，loading finally 恢复。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0051 | ruoyi-fastapi-frontend/src/api/monitor/jobLog.js / L1-L27 module 完整内容 | react-front/src/api/monitor/jobLog.ts |
| I0532 | ruoyi-fastapi-frontend/src/views/monitor/job/log.vue / L136-L251 script-setup 完整内容 | react-front/src/views/monitor/job/log.tsx |
| I0533 | ruoyi-fastapi-frontend/src/views/monitor/job/log.vue / L1-L134 template 完整内容 | react-front/src/views/monitor/job/log.tsx |
| I0534 | ruoyi-fastapi-frontend/src/views/monitor/job/log.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/monitor/job/log.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/monitor/jobLog.js

逻辑定位：listJobLog@L4–10, delJobLog@L13–18, cleanJobLog@L21–26.
- URL/请求对象 L5: `'get' '/monitor/jobLog/list'`; params=`query`, data=`None`
- URL/请求对象 L14: `'delete' '/monitor/jobLog/' + jobLogId`; params=`None`, data=`None`
- URL/请求对象 L22: `'delete' '/monitor/jobLog/clean'`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/views/monitor/job/log.vue

逻辑定位：getList@L170–183, handleClose@L185–188, handleQuery@L190–193, resetQuery@L195–199, handleSelectionChange@L201–204, handleView@L206–209, handleDelete@L211–218, handleClean@L220–227, handleExport@L229–235.
全部模板事件/权限：keyup=handleQuery@L10; keyup=handleQuery@L14; keyup=handleQuery@L17; keyup=handleQuery@L20; click=handleQuery@L49; click=resetQuery@L50; click=handleDelete@L61; =['monitor:job:remove']@L62; click=handleClean@L70; =['monitor:job:remove']@L71; click=handleExport@L79; =['monitor:job:export']@L80; click=handleClose@L88; queryTable=getList@L91; selection-change=handleSelectionChange@L94; click=handleView(scope.row)@L118; =['monitor:job:query']@L118; pagination=getList@L128.
