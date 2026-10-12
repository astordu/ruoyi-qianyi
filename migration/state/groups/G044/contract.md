# G044 定时任务配置、运行与同步

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

定时任务配置、运行与同步可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；任务配置与运行、同步共用变更状态与刷新，同组；日志查询是独立入口，可另组交付。previewJob API 已在 cron 组，不能重复迁。

依赖：G002 共用数据与表单适配, G003 时区、日期输入与提交序列化, G005 HTTP 请求、会话提示与导出, G007 字典获取、缓存与标签展示, G010 会话、权限与路由策略, G012 分页与列表工具栏, G014 Cron 编辑与运行时间预览, G016 JSON 编辑器校验与主题, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 任务 CRUD/状态/立即执行/导出与 Cron 生成器真实接入；jobArgs 必须 JSON 数组，jobKwargs 非null非数组对象，拒绝非有限数字；最大并发/允许延迟等规则不丢失。
2. 变更结果 failed→warning、pending→普通消息、其他→success，失败同步可打开 runtime 检查并 retrySync；runningIds/changingIds/submitting 防重入，取消状态回滚。
3. 列表 pending/failed 同步状态自动轮询，版本号与 AbortController 防旧响应覆盖；页面不可见/卸载停止，恢复可见重查。
4. runtime 在 execution/sync 两类记录间切换，jobId/executionId 定位与显示全部，有限状态刷新、重试、隐藏/卸载终止请求；详情job/log两种模式复用。
5. 原 job-form.test.js 全部断言与 payload 保留；跳日志页携 jobId/executionId，真实执行日志联调后验收。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0039 | ruoyi-fastapi-frontend/src/api/monitor/job.js / L16-L23 完整导出 listJob | react-front/src/api/monitor/job.ts |
| I0040 | ruoyi-fastapi-frontend/src/api/monitor/job.js / L26-L31 完整导出 getJob | react-front/src/api/monitor/job.ts |
| I0041 | ruoyi-fastapi-frontend/src/api/monitor/job.js / L34-L40 完整导出 addJob | react-front/src/api/monitor/job.ts |
| I0042 | ruoyi-fastapi-frontend/src/api/monitor/job.js / L43-L49 完整导出 updateJob | react-front/src/api/monitor/job.ts |
| I0043 | ruoyi-fastapi-frontend/src/api/monitor/job.js / L52-L57 完整导出 delJob | react-front/src/api/monitor/job.ts |
| I0044 | ruoyi-fastapi-frontend/src/api/monitor/job.js / L60-L70 完整导出 changeJobStatus | react-front/src/api/monitor/job.ts |
| I0045 | ruoyi-fastapi-frontend/src/api/monitor/job.js / L74-L83 完整导出 runJob | react-front/src/api/monitor/job.ts |
| I0046 | ruoyi-fastapi-frontend/src/api/monitor/job.js / L86-L93 完整导出 listJobExecutions | react-front/src/api/monitor/job.ts |
| I0047 | ruoyi-fastapi-frontend/src/api/monitor/job.js / L96-L102 完整导出 getJobExecution | react-front/src/api/monitor/job.ts |
| I0048 | ruoyi-fastapi-frontend/src/api/monitor/job.js / L105-L112 完整导出 listJobSync | react-front/src/api/monitor/job.ts |
| I0049 | ruoyi-fastapi-frontend/src/api/monitor/job.js / L115-L120 完整导出 retryJobSync | react-front/src/api/monitor/job.ts |
| I0050 | ruoyi-fastapi-frontend/src/api/monitor/job.js / 模块导入、注释及函数之间全部剩余内容 | react-front/src/api/monitor/job.ts |
| I0475 | ruoyi-fastapi-frontend/src/utils/job.js / L1-L62 module 完整内容 | react-front/src/utils/job.ts |
| I0524 | ruoyi-fastapi-frontend/src/views/monitor/job/detail.vue / L292-L314 script-setup 完整内容 | react-front/src/views/monitor/job/detail.tsx |
| I0525 | ruoyi-fastapi-frontend/src/views/monitor/job/detail.vue / L1-L290 template 完整内容 | react-front/src/views/monitor/job/detail.tsx |
| I0526 | ruoyi-fastapi-frontend/src/views/monitor/job/detail.vue / L316-L321 style-1 完整内容 | react-front/src/views/monitor/job/detail.tsx |
| I0527 | ruoyi-fastapi-frontend/src/views/monitor/job/detail.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/monitor/job/detail.tsx |
| I0528 | ruoyi-fastapi-frontend/src/views/monitor/job/index.vue / L310-L617 script-setup 完整内容 | react-front/src/views/monitor/job/index.tsx |
| I0529 | ruoyi-fastapi-frontend/src/views/monitor/job/index.vue / L1-L308 template 完整内容 | react-front/src/views/monitor/job/index.tsx |
| I0530 | ruoyi-fastapi-frontend/src/views/monitor/job/index.vue / L619-L629 style-1 完整内容 | react-front/src/views/monitor/job/index.tsx |
| I0531 | ruoyi-fastapi-frontend/src/views/monitor/job/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/monitor/job/index.tsx |
| I0535 | ruoyi-fastapi-frontend/src/views/monitor/job/runtime.vue / L89-L228 script-setup 完整内容 | react-front/src/views/monitor/job/runtime.tsx |
| I0536 | ruoyi-fastapi-frontend/src/views/monitor/job/runtime.vue / L1-L87 template 完整内容 | react-front/src/views/monitor/job/runtime.tsx |
| I0537 | ruoyi-fastapi-frontend/src/views/monitor/job/runtime.vue / L230-L262 style-1 完整内容 | react-front/src/views/monitor/job/runtime.tsx |
| I0538 | ruoyi-fastapi-frontend/src/views/monitor/job/runtime.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/monitor/job/runtime.tsx |
| I0739 | ruoyi-fastapi-frontend/tests/job/job-form.test.js / L1-L37 module 完整内容 | react-front/tests/job/job-form.test.ts |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/monitor/job.js

逻辑定位：listJob@L16–23, getJob@L26–31, addJob@L34–40, updateJob@L43–49, delJob@L52–57, changeJobStatus@L60–70, runJob@L74–83, listJobExecutions@L86–93, getJobExecution@L96–102, listJobSync@L105–112, retryJobSync@L115–120.
- URL/请求对象 L17: `'get' '/monitor/job/list'`; params=`query`, data=`None`
- URL/请求对象 L27: `'get' '/monitor/job/' + jobId`; params=`None`, data=`None`
- URL/请求对象 L35: `'post' '/monitor/job'`; params=`None`, data=`data`
- URL/请求对象 L44: `'put' '/monitor/job'`; params=`None`, data=`data`
- URL/请求对象 L53: `'delete' '/monitor/job/' + jobId`; params=`None`, data=`None`
- URL/请求对象 L65: `'put' '/monitor/job/changeStatus'`; params=`None`, data=`data`
- URL/请求对象 L78: `'put' '/monitor/job/run'`; params=`None`, data=`data`
- URL/请求对象 L87: `'get' '/monitor/job/execution/list'`; params=`query`, data=`None`
- URL/请求对象 L97: `'get' '/monitor/job/execution/' + executionId`; params=`None`, data=`None`
- URL/请求对象 L106: `'get' '/monitor/job/sync/list'`; params=`query`, data=`None`
- URL/请求对象 L116: `'post' '/monitor/job/sync/' + jobId`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/utils/job.js

逻辑定位：parseJobParameter@L2–21, buildJobPayload@L24–30, notifyJobMutation@L53–61.

### ruoyi-fastapi-frontend/src/views/monitor/job/detail.vue

逻辑定位：default@L297–297, get@L305–305, set@L306–306.
全部模板事件/权限：click=dialogVisible = false@L286.

### ruoyi-fastapi-frontend/src/views/monitor/job/index.vue

逻辑定位：validateParameter@L352–359, validateGraceTime@L362–365, get@L392–392, set@L393–395, getList@L399–421, handleRuntime@L424–428, showMutationResult@L431–437, cancel@L439–442, reset@L444–462, handleQuery@L464–467, resetQuery@L469–472, handleSelectionChange@L474–478, handleStatusChange@L480–494, handleRun@L496–509, handleView@L511–516, handleShowCron@L518–521, crontabFill@L523–525, handleJobLog@L527–530, handleAdd@L532–536, handleUpdate@L538–550, submitForm@L552–568, handleDelete@L570–578, handleExport@L580–584, stopListRefresh@L587–592, handlePageVisibility@L595–598.
全部模板事件/权限：keyup=handleQuery@L10; keyup=handleQuery@L14; click=handleQuery@L27; click=resetQuery@L28; click=handleAdd@L38; =['monitor:job:add']@L39; click=handleUpdate@L48; =['monitor:job:edit']@L49; click=handleDelete@L58; =['monitor:job:remove']@L59; click=handleExport@L67; =['monitor:job:export']@L68; click=handleJobLog@L76; =['monitor:job:query']@L77; click=handleRuntime('executions')@L81; =['monitor:job:query']@L82; queryTable=getList@L84; selection-change=handleSelectionChange@L87; click=handleView(scope.row)@L92; click=handleRuntime('sync', scope.row)@L106; change=handleStatusChange(scope.row)@L120; click=handleUpdate(scope.row)@L127; =['monitor:job:edit']@L127; click=handleDelete(scope.row)@L130; =['monitor:job:remove']@L130; click=handleRun(scope.row)@L134; =['monitor:job:changeStatus']@L135; click=handleJobLog(scope.row)@L138; =['monitor:job:query']@L138; pagination=getList@L149; click=handleShowCron@L234; click=submitForm@L287; click=cancel@L288; hide=openCron=false@L298; fill=crontabFill@L299; sync-updated=getList@L306.

### ruoyi-fastapi-frontend/src/views/monitor/job/runtime.vue

逻辑定位：get@L102–102, set@L103–103, stopRequests@L123–128, scheduleRefresh@L131–139, loadRecords@L142–172, resetPage@L175–180, showAllExecutions@L183–186, retrySync@L189–201, handleVisibility@L204–207.
全部模板事件/权限：tab-change=resetPage@L3; submit=resetPage@L7; click=loadRecords()@L13; click=showAllExecutions@L18; =['monitor:job:edit']@L76; click=retrySync(scope.row)@L78; pagination=loadRecords()@L82; click=dialogVisible = false@L84.

### ruoyi-fastapi-frontend/tests/job/job-form.test.js
