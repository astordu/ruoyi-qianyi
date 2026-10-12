# G047 在线会话与强退

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

在线会话与强退可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G005 HTTP 请求、会话提示与导出, G010 会话、权限与路由策略, G012 分页与列表工具栏, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 按IP和用户查询在线会话，行序号/部门/浏览器/登录时间显示，返回的数据切片/total规则按原列表逻辑。
2. 强退针对 tokenId，确认后删除并刷新，取消不请求；当前用户与其他用户真实会话联调。
3. 空状态与无强退权限隐藏按钮，网络失败保留原列表并按统一错误反馈。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0053 | ruoyi-fastapi-frontend/src/api/monitor/online.js / L1-L19 module 完整内容 | react-front/src/api/monitor/online.ts |
| I0542 | ruoyi-fastapi-frontend/src/views/monitor/online/index.vue / L60-L106 script-setup 完整内容 | react-front/src/views/monitor/online/index.tsx |
| I0543 | ruoyi-fastapi-frontend/src/views/monitor/online/index.vue / L1-L58 template 完整内容 | react-front/src/views/monitor/online/index.tsx |
| I0544 | ruoyi-fastapi-frontend/src/views/monitor/online/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/monitor/online/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/monitor/online.js

逻辑定位：list@L4–10, forceLogout@L13–18.
- URL/请求对象 L5: `'get' '/monitor/online/list'`; params=`query`, data=`None`
- URL/请求对象 L14: `'delete' '/monitor/online/' + tokenId`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/views/monitor/online/index.vue

逻辑定位：getList@L77–84, handleQuery@L86–89, resetQuery@L91–94, handleForceLogout@L96–103.
全部模板事件/权限：keyup=handleQuery@L10; keyup=handleQuery@L19; click=handleQuery@L23; click=resetQuery@L24; click=handleForceLogout(scope.row)@L51; =['monitor:online:forceLogout']@L51.
