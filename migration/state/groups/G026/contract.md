# G026 锁屏页面与解锁

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

锁屏页面与解锁可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G003 时区、日期输入与提交序列化, G009 系统主题与布局偏好, G010 会话、权限与路由策略

## 正常、异常与边界检查条件

1. 锁定显示真实账号头像/姓名与按显示时区更新的时钟；空密码不调用 unlockscreen，失败清空/聚焦/错误状态按源执行。
2. 解锁成功恢复原 lockPath 后清除锁记录；退出账号解除锁并注销后跳登录；刷新仍按锁记录拦截。
3. 粒子背景 resize/RAF 与时钟 interval 在卸载清理；头像失败回退和移动屏幕布局有原版截图依据。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0507 | ruoyi-fastapi-frontend/src/views/lock.vue / L36-L171 script-setup 完整内容 | react-front/src/views/lock.tsx |
| I0508 | ruoyi-fastapi-frontend/src/views/lock.vue / L1-L34 template 完整内容 | react-front/src/views/lock.tsx |
| I0509 | ruoyi-fastapi-frontend/src/views/lock.vue / L173-L373 style-1 完整内容 | react-front/src/views/lock.tsx |
| I0510 | ruoyi-fastapi-frontend/src/views/lock.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/lock.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/views/lock.vue

逻辑定位：onAvatarError@L61–63, startClock@L65–73, update@L66–70, handleUnlock@L75–95, showError@L97–101, goLogin@L103–108, initParticles@L110–159, resize@L114–117, draw@L130–157.
全部模板事件/权限：error=onAvatarError@L13; keydown=handleUnlock@L20; click=handleUnlock@L21; click=goLogin@L30.
