# G014 Cron 编辑与运行时间预览

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

Cron 编辑与运行时间预览可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；九个内部 Vue 文件同组；预览 API 适配随本组迁，不依赖整个任务页面。

依赖：G003 时区、日期输入与提交序列化, G005 HTTP 请求、会话提示与导出

## 正常、异常与边界检查条件

1. 秒/分/时/日/月/周/年全部编辑方式及 *,?,/,L,W,# 范围和互斥规则按源 resolveExp/tabCheck/updateCrontabValue 执行。
2. 表达式反解恢复面板，确定填充完整表达式、重置与取消不同；hideComponent 隐藏字段保持其原表达式规则。
3. 最近 5 次运行时间来自任务 preview API 与时区/任务设置，不用前端猜测。无结果显示没有未来时间，请求中 loading 与失败显示保持源码。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0038 | ruoyi-fastapi-frontend/src/api/monitor/job.js / L4-L13 完整导出 previewJob | react-front/src/api/monitor/job-cron.ts |
| I0261 | ruoyi-fastapi-frontend/src/components/Crontab/day.vue / L54-L165 script-setup 完整内容 | react-front/src/components/Crontab/day.tsx |
| I0262 | ruoyi-fastapi-frontend/src/components/Crontab/day.vue / L1-L53 template 完整内容 | react-front/src/components/Crontab/day.tsx |
| I0263 | ruoyi-fastapi-frontend/src/components/Crontab/day.vue / L167-L174 style-1 完整内容 | react-front/src/components/Crontab/day.tsx |
| I0264 | ruoyi-fastapi-frontend/src/components/Crontab/day.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/Crontab/day.tsx |
| I0265 | ruoyi-fastapi-frontend/src/components/Crontab/hour.vue / L36-L124 script-setup 完整内容 | react-front/src/components/Crontab/hour.tsx |
| I0266 | ruoyi-fastapi-frontend/src/components/Crontab/hour.vue / L1-L34 template 完整内容 | react-front/src/components/Crontab/hour.tsx |
| I0267 | ruoyi-fastapi-frontend/src/components/Crontab/hour.vue / L126-L133 style-1 完整内容 | react-front/src/components/Crontab/hour.tsx |
| I0268 | ruoyi-fastapi-frontend/src/components/Crontab/hour.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/Crontab/hour.tsx |
| I0269 | ruoyi-fastapi-frontend/src/components/Crontab/index.vue / L127-L252 script-setup 完整内容 | react-front/src/components/Crontab/index.tsx |
| I0270 | ruoyi-fastapi-frontend/src/components/Crontab/index.vue / L1-L125 template 完整内容 | react-front/src/components/Crontab/index.tsx |
| I0271 | ruoyi-fastapi-frontend/src/components/Crontab/index.vue / L254-L317 style-1 完整内容 | react-front/src/components/Crontab/index.tsx |
| I0272 | ruoyi-fastapi-frontend/src/components/Crontab/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/Crontab/index.tsx |
| I0273 | ruoyi-fastapi-frontend/src/components/Crontab/min.vue / L35-L117 script-setup 完整内容 | react-front/src/components/Crontab/min.tsx |
| I0274 | ruoyi-fastapi-frontend/src/components/Crontab/min.vue / L1-L34 template 完整内容 | react-front/src/components/Crontab/min.tsx |
| I0275 | ruoyi-fastapi-frontend/src/components/Crontab/min.vue / L119-L126 style-1 完整内容 | react-front/src/components/Crontab/min.tsx |
| I0276 | ruoyi-fastapi-frontend/src/components/Crontab/min.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/Crontab/min.tsx |
| I0277 | ruoyi-fastapi-frontend/src/components/Crontab/month.vue / L36-L132 script-setup 完整内容 | react-front/src/components/Crontab/month.tsx |
| I0278 | ruoyi-fastapi-frontend/src/components/Crontab/month.vue / L1-L34 template 完整内容 | react-front/src/components/Crontab/month.tsx |
| I0279 | ruoyi-fastapi-frontend/src/components/Crontab/month.vue / L134-L141 style-1 完整内容 | react-front/src/components/Crontab/month.tsx |
| I0280 | ruoyi-fastapi-frontend/src/components/Crontab/month.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/Crontab/month.tsx |
| I0281 | ruoyi-fastapi-frontend/src/components/Crontab/result.vue / L15-L70 script-setup 完整内容 | react-front/src/components/Crontab/result.tsx |
| I0282 | ruoyi-fastapi-frontend/src/components/Crontab/result.vue / L1-L13 template 完整内容 | react-front/src/components/Crontab/result.tsx |
| I0283 | ruoyi-fastapi-frontend/src/components/Crontab/result.vue / L72-L76 style-1 完整内容 | react-front/src/components/Crontab/result.tsx |
| I0284 | ruoyi-fastapi-frontend/src/components/Crontab/result.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/Crontab/result.tsx |
| I0285 | ruoyi-fastapi-frontend/src/components/Crontab/second.vue / L36-L119 script-setup 完整内容 | react-front/src/components/Crontab/second.tsx |
| I0286 | ruoyi-fastapi-frontend/src/components/Crontab/second.vue / L1-L34 template 完整内容 | react-front/src/components/Crontab/second.tsx |
| I0287 | ruoyi-fastapi-frontend/src/components/Crontab/second.vue / L121-L128 style-1 完整内容 | react-front/src/components/Crontab/second.tsx |
| I0288 | ruoyi-fastapi-frontend/src/components/Crontab/second.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/Crontab/second.tsx |
| I0289 | ruoyi-fastapi-frontend/src/components/Crontab/week.vue / L71-L185 script-setup 完整内容 | react-front/src/components/Crontab/week.tsx |
| I0290 | ruoyi-fastapi-frontend/src/components/Crontab/week.vue / L1-L69 template 完整内容 | react-front/src/components/Crontab/week.tsx |
| I0291 | ruoyi-fastapi-frontend/src/components/Crontab/week.vue / L187-L197 style-1 完整内容 | react-front/src/components/Crontab/week.tsx |
| I0292 | ruoyi-fastapi-frontend/src/components/Crontab/week.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/Crontab/week.tsx |
| I0293 | ruoyi-fastapi-frontend/src/components/Crontab/year.vue / L43-L134 script-setup 完整内容 | react-front/src/components/Crontab/year.tsx |
| I0294 | ruoyi-fastapi-frontend/src/components/Crontab/year.vue / L1-L41 template 完整内容 | react-front/src/components/Crontab/year.tsx |
| I0295 | ruoyi-fastapi-frontend/src/components/Crontab/year.vue / L136-L143 style-1 完整内容 | react-front/src/components/Crontab/year.tsx |
| I0296 | ruoyi-fastapi-frontend/src/components/Crontab/year.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/Crontab/year.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/monitor/job.js

逻辑定位：previewJob@L4–13.
- URL/请求对象 L5: `'post' '/monitor/job/preview'`; params=`None`, data=`data`

### ruoyi-fastapi-frontend/src/components/Crontab/day.vue

逻辑定位：default@L71–72, changeRadioValue@L102–127, onRadioChange@L129–164.
全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/components/Crontab/hour.vue

逻辑定位：default@L53–54, changeRadioValue@L79–102, onRadioChange@L103–123.
全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/components/Crontab/index.vue

逻辑定位：default@L141–141, shouldHide@L181–183, resolveExp@L184–207, tabCheck@L209–211, updateCrontabValue@L213–215, checkNumber@L217–226, hidePopup@L228–230, submitFill@L232–235, clearCron@L236–247.
全部模板事件/权限：update=updateCrontabValue@L6; update=updateCrontabValue@L15; update=updateCrontabValue@L24; update=updateCrontabValue@L33; update=updateCrontabValue@L42; update=updateCrontabValue@L51; update=updateCrontabValue@L60; click=submitFill@L119; click=clearCron@L120; click=hidePopup@L121.

### ruoyi-fastapi-frontend/src/components/Crontab/min.vue

逻辑定位：default@L52–53, changeRadioValue@L78–95, onRadioChange@L96–116.
全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/components/Crontab/month.vue

逻辑定位：default@L53–54, changeRadioValue@L93–110, onRadioChange@L111–131.
全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/components/Crontab/result.vue

全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/components/Crontab/second.vue

逻辑定位：default@L53–54, changeRadioValue@L79–96, onRadioChange@L98–118.
全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/components/Crontab/week.vue

逻辑定位：default@L88–89, changeRadioValue@L128–151, onRadioChange@L152–184.
全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/components/Crontab/year.vue

逻辑定位：default@L60–61, changeRadioValue@L90–109, onRadioChange@L110–133.
全部模板事件/权限：.
