# G025 账号注册页面

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

账号注册页面可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G006 密码规则与记住密码适配, G008 SVG 图标与图标选择器, G009 系统主题与布局偏好, G010 会话、权限与路由策略, G024 登录页面完整流程

## 正常、异常与边界检查条件

1. 用户名2–20字符、密码6–20和字符规则、确认密码一致与条件验证码校验保持；不合法输入不提交。
2. 成功弹出旧注册成功反馈再跳登录；失败解除 loading，验证码分支按照实际条件重放；接口关闭注册时不伪造成功。
3. 注册页背景和登录链接、图标、浅深主题与原版对照；验证码获取共用 getCodeImg。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0561 | ruoyi-fastapi-frontend/src/views/register.vue / L78-L155 script-setup 完整内容 | react-front/src/views/register.tsx |
| I0562 | ruoyi-fastapi-frontend/src/views/register.vue / L1-L76 template 完整内容 | react-front/src/views/register.tsx |
| I0563 | ruoyi-fastapi-frontend/src/views/register.vue / L157-L219 style-1 完整内容 | react-front/src/views/register.tsx |
| I0564 | ruoyi-fastapi-frontend/src/views/register.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/register.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/views/register.vue

逻辑定位：equalToPassword@L98–104, handleRegister@L122–142, getCode@L144–152.
全部模板事件/权限：keyup=handleRegister@L23; keyup=handleRegister@L35; keyup=handleRegister@L47; click=getCode@L52; click=handleRegister@L61.
