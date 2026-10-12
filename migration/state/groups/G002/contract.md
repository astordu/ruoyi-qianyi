# G002 共用数据与表单适配

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

共用数据与表单适配可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G001 React 工程、环境与部署, G003 时区、日期输入与提交序列化

## 正常、异常与边界检查条件

1. tansParams 对数组、嵌套对象、空字符串/null/undefined 使用旧键名与编码规则；param/param2Obj/getQueryObject 保留各自区别，不合并成改变业务的单一算法。
2. handleTree 在根父节点缺失、子节点先于父节点时仍按旧 id/parentId 规则组树；字典单值/多值的未匹配值和分隔符规则保留。
3. 深拷贝、对象合并、去重、数字/URL/外链判断、字符串转换、日期范围 begin/end 参数按全部导出覆盖；Date 格式化使用时间能力。
4. cache 的 JSON 与普通值存取保持 session/local 隔离；copyText 的成功/失败提示、剪贴板回退和事件解绑可验证。
5. resetForm 适配 React 表单引用；debounce 的 immediate/尾调用与滚动动画结束回调保持旧行为。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0373 | ruoyi-fastapi-frontend/src/directive/common/copyText.js / L1-L66 module 完整内容 | react-front/src/directive/common/copyText.ts |
| I0448 | ruoyi-fastapi-frontend/src/plugins/cache.js / L1-L80 module 完整内容 | react-front/src/plugins/cache.ts |
| I0474 | ruoyi-fastapi-frontend/src/utils/index.js / L1-L366 module 完整内容 | react-front/src/utils/index.ts |
| I0482 | ruoyi-fastapi-frontend/src/utils/ruoyi.js / L1-L219 module 完整内容 | react-front/src/utils/ruoyi.ts |
| I0483 | ruoyi-fastapi-frontend/src/utils/scroll-to.js / L1-L59 module 完整内容 | react-front/src/utils/scroll-to.ts |
| I0488 | ruoyi-fastapi-frontend/src/utils/validate.js / L1-L120 module 完整内容 | react-front/src/utils/validate.ts |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/directive/common/copyText.js

逻辑定位：beforeMount@L6–20, handler@L11–16, copyTextToClipboard@L23–65.

### ruoyi-fastapi-frontend/src/plugins/cache.js

逻辑定位：set@L2–9, get@L10–18, setJSON@L19–23, getJSON@L24–30, remove@L31–33, set@L36–43, get@L44–52, setJSON@L53–57, getJSON@L58–64, remove@L65–67.

### ruoyi-fastapi-frontend/src/utils/index.js

逻辑定位：formatDate@L6–8, formatTime@L15–34, getQueryObject@L40–53, byteLength@L59–69, cleanArray@L75–83, param@L89–97, param2Obj@L103–119, html2Text@L125–129, objectMerge@L137–153, toggleClass@L159–173, getTime@L179–185, debounce@L193–226, later@L196–211, deepClone@L235–248, uniqueArr@L254–256, createUniqueString@L261–265, hasClass@L273–275, addClass@L282–284, removeClass@L291–296, makeMap@L298–307, titleCase@L353–355, camelCase@L358–360, isNumberStr@L362–364.

### ruoyi-fastapi-frontend/src/utils/ruoyi.js

逻辑定位：parseTime@L11–13, resetForm@L16–20, addDateRange@L23–34, selectDictLabel@L37–52, selectDictLabels@L55–78, sprintf@L81–93, parseStrEmpty@L96–101, mergeRecursive@L104–117, handleTree@L126–168, adaptToChildrenList@L157–166, tansParams@L174–200, getNormalPath@L204–213, blobValidate@L216–218.

### ruoyi-fastapi-frontend/src/utils/scroll-to.js

逻辑定位：move@L19–23, position@L25–27, scrollTo@L34–58, animateScroll@L40–56.

### ruoyi-fastapi-frontend/src/utils/validate.js

逻辑定位：isPathMatch@L7–16, isEmpty@L23–28, isHttp@L35–37, isExternal@L44–46, validUsername@L52–55, validURL@L61–64, validLowerCase@L70–73, validUpperCase@L79–82, validAlphabets@L88–91, validEmail@L97–100, isString@L106–108, isArray@L114–119.
