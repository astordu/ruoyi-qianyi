# G003 时区、日期输入与提交序列化

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

时区、日期输入与提交序列化可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；整个 time.js 的状态、协作函数、选择偏移弹窗与日期控件同组；不拆成 29 个函数轮。缺失原测试是验证输入缺口，不排除该测试。

依赖：G001 React 工程、环境与部署

## 正常、异常与边界检查条件

1. auto 优先设备时区，设备无法识别时回退业务时区；自定义时区覆盖显示、筛选、导出；App focus/visibility 更新的接线在入口集成验收。
2. 秒与毫秒入口分别处理；RFC3339 带偏移的真实时刻按显示时区格式化，无偏移墙上时间、无效日历日期不能被浏览器 Date 自动修正。
3. DST gap 返回不存在时间错误；DST fold 保留所有候选偏移并让用户选择，取消选择时不提交。选择器分别保存日期和时间字符串，清空发出 null。
4. prepareTimeFields 保存原始值和原时区；未修改字段提交保持原瞬时值，修改字段按选定时区转 RFC3339；日期范围上下界保持旧规则。
5. 源 tests/time/time.test.js 的外部 contract.mjs 当前缺失。实施时需恢复可信原契约，或从旧源码建立明确输入输出用例并记录替代依据；不得宣称原测试已经运行通过。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0253 | ruoyi-fastapi-frontend/src/components/BusinessDateTimePicker/index.vue / L20-L99 script 完整内容 | react-front/src/components/BusinessDateTimePicker/index.tsx |
| I0254 | ruoyi-fastapi-frontend/src/components/BusinessDateTimePicker/index.vue / L1-L18 template 完整内容 | react-front/src/components/BusinessDateTimePicker/index.tsx |
| I0255 | ruoyi-fastapi-frontend/src/components/BusinessDateTimePicker/index.vue / L101-L123 style-1 完整内容 | react-front/src/components/BusinessDateTimePicker/index.tsx |
| I0256 | ruoyi-fastapi-frontend/src/components/BusinessDateTimePicker/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/BusinessDateTimePicker/index.tsx |
| I0485 | ruoyi-fastapi-frontend/src/utils/time.js / L1-L564 module 完整内容 | react-front/src/utils/time.ts |
| I0742 | ruoyi-fastapi-frontend/tests/time/time.test.js / L1-L4 module 完整内容 | react-front/tests/time/time.test.ts |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/components/BusinessDateTimePicker/index.vue

逻辑定位：wallValue@L52–54, timezoneName@L55–57, get@L59–61, set@L62–64, get@L67–69, set@L70–74, validationMessage@L76–85, updateValue@L93–96.
全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/utils/time.js

逻辑定位：getFormatter@L44–70, setBusinessTimezone@L78–81, getBusinessTimezone@L88–90, setUserTimezone@L98–104, getUserTimezone@L111–113, refreshDeviceTimezone@L120–134, getDeviceTimezone@L141–143, getDisplayTimezone@L150–152, getTimeFieldsTimezone@L160–162, getSupportedTimezones@L170–181, parseWallTimeMilliseconds@L190–215, parseInstantMilliseconds@L223–235, getTimezoneOffsetMinutes@L244–253, createZonedDateTime@L262–264, formatEpoch@L274–285, formatBusinessTime@L295–298, formatEpochMilliseconds@L308–313, formatEpochSeconds@L323–327, getWallTimeCandidates@L336–357, toRfc3339@L369–396, toBusinessDateTimeInput@L405–407, normalizeRangeBoundary@L415–426, prepareTimeFields@L436–454, serializeTimeFields@L464–495, resolveTimeFields@L505–521, chooseTimeOffset@L532–545, inputValidator@L539–539, serializeTimeFieldsForSubmit@L554–563.

### ruoyi-fastapi-frontend/tests/time/time.test.js
