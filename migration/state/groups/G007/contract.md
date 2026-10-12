# G007 字典获取、缓存与标签展示

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

字典获取、缓存与标签展示可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G005 HTTP 请求、会话提示与导出

## 正常、异常与边界检查条件

1. 首次 dictType 返回空列表后异步填充 label/value/listClass/cssClass；已有缓存不重复请求；移除/清空缓存后页面重新获取。
2. 数值、字符串、数组、按 separator 分割的值按旧宽松值匹配；未匹配项和 showValue、默认 span/彩色 tag 与间距对应旧展示。
3. 空值、空 options、多个字典类型、接口失败均登记实际行为；Vue 模板过滤器写法适配为 React 明确渲染，比较 Vue 当前渲染结果以区分旧缺陷与迁移差异。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0068 | ruoyi-fastapi-frontend/src/api/system/dict/data.js / L21-L26 完整导出 getDicts | react-front/src/api/system/dict/data-dict.ts |
| I0297 | ruoyi-fastapi-frontend/src/components/DictTag/index.vue / L27-L81 script-setup 完整内容 | react-front/src/components/DictTag/index.tsx |
| I0298 | ruoyi-fastapi-frontend/src/components/DictTag/index.vue / L1-L25 template 完整内容 | react-front/src/components/DictTag/index.tsx |
| I0299 | ruoyi-fastapi-frontend/src/components/DictTag/index.vue / L83-L87 style-1 完整内容 | react-front/src/components/DictTag/index.tsx |
| I0300 | ruoyi-fastapi-frontend/src/components/DictTag/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/DictTag/index.tsx |
| I0457 | ruoyi-fastapi-frontend/src/store/modules/dict.js / L1-L58 module 完整内容 | react-front/src/store/modules/dict.ts |
| I0464 | ruoyi-fastapi-frontend/src/utils/dict.js / L1-L24 module 完整内容 | react-front/src/utils/dict.ts |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/system/dict/data.js

逻辑定位：getDicts@L21–26.
- URL/请求对象 L22: `'get' '/system/dict/data/type/' + dictType`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/components/DictTag/index.vue

逻辑定位：handleArray@L71–76, isValueMatch@L78–80.
全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/store/modules/dict.js

逻辑定位：state@L4–6, getDict@L9–22, setDict@L24–31, removeDict@L33–46, cleanDict@L48–50, initDict@L52–53.

### ruoyi-fastapi-frontend/src/utils/dict.js

逻辑定位：useDict@L7–24.
