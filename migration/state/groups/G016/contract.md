# G016 JSON 编辑器校验与主题

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

JSON 编辑器校验与主题可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G001 React 工程、环境与部署, G009 系统主题与布局偏好

## 正常、异常与边界检查条件

1. 异步 Monaco 加载期间展示 loading；modelValue 更新触发表单值/校验状态，非法 JSON 显示错误位置，revealError 可定位。
2. 仅有效 JSON 可格式化；外部值变更不形成循环，编辑器高度、禁用和暴露方法与调用方相容。
3. 深浅主题随 DOM 主题改变，卸载销毁 editor/model/listeners，Monaco worker 构建后可加载。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0333 | ruoyi-fastapi-frontend/src/components/JsonEditor/index.vue / L29-L155 script-setup 完整内容 | react-front/src/components/JsonEditor/index.tsx |
| I0334 | ruoyi-fastapi-frontend/src/components/JsonEditor/index.vue / L1-L27 template 完整内容 | react-front/src/components/JsonEditor/index.tsx |
| I0335 | ruoyi-fastapi-frontend/src/components/JsonEditor/index.vue / L157-L238 style-1 完整内容 | react-front/src/components/JsonEditor/index.tsx |
| I0336 | ruoyi-fastapi-frontend/src/components/JsonEditor/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/JsonEditor/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/components/JsonEditor/index.vue

逻辑定位：default@L36–36, updateValue@L64–69, validateForm@L72–74, formatDocument@L77–81, revealError@L84–90, updateTheme@L93–95.
全部模板事件/权限：click=formatDocument@L7; click=expanded = !expanded@L9; update:model-value=updateValue@L16; blur=validateForm@L16; click=revealError@L20.
