# G050 传输加密监控与联动图表

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

传输加密监控与联动图表可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G004 传输加密策略与请求响应协议, G005 HTTP 请求、会话提示与导出, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 加载真实监控策略、密钥kid/支持版本、启用/强制/排除路径、统计范围与近期失败；缺省数组防止图表崩溃。
2. 失败原因和kid柱图点击与表格行选择相互联动、二次点击取消；零分母率显示不为 Infinity/NaN，数字格式按源码。
3. 自动刷新开关重置timer；主题/resize 更新图表，卸载清除interval与ECharts实例，错误关闭loading。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0056 | ruoyi-fastapi-frontend/src/api/monitor/transportCrypto.js / L1-L10 module 完整内容 | react-front/src/api/monitor/transportCrypto.ts |
| I0554 | ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue / L332-L878 script-setup 完整内容 | react-front/src/views/monitor/transportCrypto/index.tsx |
| I0555 | ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue / L1-L330 template 完整内容 | react-front/src/views/monitor/transportCrypto/index.tsx |
| I0556 | ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue / L880-L1011 style-1 完整内容 | react-front/src/views/monitor/transportCrypto/index.tsx |
| I0557 | ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/monitor/transportCrypto/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/monitor/transportCrypto.js

逻辑定位：getTransportCryptoMonitor@L4–9.
- URL/请求对象 L5: `'get' '/transport/crypto/monitor'`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue

逻辑定位：formatMonitorTime@L502–504, loadMonitorData@L506–532, resetRefreshTimer@L534–544, formatCount@L546–548, formatPercent@L550–555, formatRate@L557–559, getRate@L561–566, getFailureTagType@L568–579, getFailureChartColor@L581–590, buildKidChartBarData@L592–601, bindFailureReasonChartEvents@L603–612, bindKidStatsChartEvents@L614–623, initFailureReasonChart@L625–638, initKidStatsChart@L640–653, renderFailureReasonChart@L655–727, formatter@L683–690, renderKidStatsChart@L729–804, resizeCharts@L806–809, destroyCharts@L811–820, clearFailureReasonSelection@L822–824, clearKidSelection@L826–828, handleFailureReasonRowClick@L830–833, handleKidStatRowClick@L835–838, getFailureReasonRowClassName@L840–842, getKidStatRowClassName@L844–846.
全部模板事件/权限：click=loadMonitorData@L74; close=clearFailureReasonSelection@L205; row-click=handleFailureReasonRowClick@L221; close=clearKidSelection@L247; row-click=handleKidStatRowClick@L263.
