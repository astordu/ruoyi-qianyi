# G046 登录日志与账号解锁

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

登录日志与账号解锁可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G003 时区、日期输入与提交序列化, G005 HTTP 请求、会话提示与导出, G007 字典获取、缓存与标签展示, G010 会话、权限与路由策略, G012 分页与列表工具栏, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 登录地址/用户名/状态/时间范围、分页与排序参数，登录状态标签及设备信息展示。
2. 选中删除、清空、选中用户名解锁各自确认，取消不发送；导出包含当前查询，按钮权限按模板。
3. 时间范围、日期排序、空结果和接口错误按旧版可验证。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0052 | ruoyi-fastapi-frontend/src/api/monitor/logininfor.js / L1-L35 module 完整内容 | react-front/src/api/monitor/logininfor.ts |
| I0539 | ruoyi-fastapi-frontend/src/views/monitor/logininfor/index.vue / L127-L232 script-setup 完整内容 | react-front/src/views/monitor/logininfor/index.tsx |
| I0540 | ruoyi-fastapi-frontend/src/views/monitor/logininfor/index.vue / L1-L125 template 完整内容 | react-front/src/views/monitor/logininfor/index.tsx |
| I0541 | ruoyi-fastapi-frontend/src/views/monitor/logininfor/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/monitor/logininfor/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/monitor/logininfor.js

逻辑定位：list@L4–10, delLogininfor@L13–18, unlockLogininfor@L21–26, cleanLogininfor@L29–34.
- URL/请求对象 L5: `'get' '/monitor/logininfor/list'`; params=`query`, data=`None`
- URL/请求对象 L14: `'delete' '/monitor/logininfor/' + infoId`; params=`None`, data=`None`
- URL/请求对象 L22: `'get' '/monitor/logininfor/unlock/' + userName`; params=`None`, data=`None`
- URL/请求对象 L30: `'delete' '/monitor/logininfor/clean'`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/views/monitor/logininfor/index.vue

逻辑定位：getList@L157–164, handleQuery@L166–169, resetQuery@L171–176, handleSelectionChange@L178–183, handleSortChange@L185–189, handleDelete@L191–199, handleClean@L201–208, handleUnlock@L210–217, handleExport@L219–223.
全部模板事件/权限：keyup=handleQuery@L10; keyup=handleQuery@L19; click=handleQuery@L49; click=resetQuery@L50; click=handleDelete@L61; =['monitor:logininfor:remove']@L62; click=handleClean@L70; =['monitor:logininfor:remove']@L71; click=handleUnlock@L80; =['monitor:logininfor:unlock']@L81; click=handleExport@L89; =['monitor:logininfor:export']@L90; queryTable=getList@L93; selection-change=handleSelectionChange@L96; sort-change=handleSortChange@L96; pagination=getList@L122.
