# G028 401 与 404 错误页面

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

401 与 404 错误页面可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G009 系统主题与布局偏好, G010 会话、权限与路由策略

## 正常、异常与边界检查条件

1. 401 返回在 noGoBack 条件下回首页，否则浏览器后退；404 返回首页链接与错误插图/动画完整。
2. 无权限入口与不存在 URL 实际到正确错误页面，直接刷新仍可访问；GIF/云图片逐文件复用。
3. 浅深主题、图片布局、文案和浏览器返回边界按原页面对照。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0139 | ruoyi-fastapi-frontend/src/assets/401_images/401.gif / L1-L1 asset 完整内容 | react-front/src/assets/401_images/401.gif |
| I0140 | ruoyi-fastapi-frontend/src/assets/404_images/404.png / L1-L1 asset 完整内容 | react-front/src/assets/404_images/404.png |
| I0141 | ruoyi-fastapi-frontend/src/assets/404_images/404_cloud.png / L1-L1 asset 完整内容 | react-front/src/assets/404_images/404_cloud.png |
| I0499 | ruoyi-fastapi-frontend/src/views/error/401.vue / L28-L42 script-setup 完整内容 | react-front/src/views/error/401.tsx |
| I0500 | ruoyi-fastapi-frontend/src/views/error/401.vue / L1-L26 template 完整内容 | react-front/src/views/error/401.tsx |
| I0501 | ruoyi-fastapi-frontend/src/views/error/401.vue / L44-L82 style-1 完整内容 | react-front/src/views/error/401.tsx |
| I0502 | ruoyi-fastapi-frontend/src/views/error/401.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/error/401.tsx |
| I0503 | ruoyi-fastapi-frontend/src/views/error/404.vue / L28-L32 script-setup 完整内容 | react-front/src/views/error/404.tsx |
| I0504 | ruoyi-fastapi-frontend/src/views/error/404.vue / L1-L26 template 完整内容 | react-front/src/views/error/404.tsx |
| I0505 | ruoyi-fastapi-frontend/src/views/error/404.vue / L34-L227 style-1 完整内容 | react-front/src/views/error/404.tsx |
| I0506 | ruoyi-fastapi-frontend/src/views/error/404.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/error/404.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/assets/401_images/401.gif


### ruoyi-fastapi-frontend/src/assets/404_images/404.png


### ruoyi-fastapi-frontend/src/assets/404_images/404_cloud.png


### ruoyi-fastapi-frontend/src/views/error/401.vue

逻辑定位：back@L35–41.
全部模板事件/权限：click=back@L3.

### ruoyi-fastapi-frontend/src/views/error/404.vue

全部模板事件/权限：.
