# G024 登录页面完整流程

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

登录页面完整流程可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G006 密码规则与记住密码适配, G008 SVG 图标与图标选择器, G009 系统主题与布局偏好, G010 会话、权限与路由策略

## 正常、异常与边界检查条件

1. captchaEnabled 缺省 true、registerEnabled 缺省 false；验证码图/uuid 加载、点击刷新、启停校验与注册链接匹配原版。
2. 表单验证失败不请求；成功 Token 入会话后返回 redirect 并保留其余 query，缺省首页；失败解除 loading 并在验证码启用时重取。
3. 勾选记住密码设置 username/加密 password/rememberMe 30 天 cookie，取消删除；初始 Cookie 回填与 source 默认值保持。
4. 浅/深色背景、400px 登录卡、验证码与 footer 在参考尺寸截图对比；已有的重定向边界问题记录事实再处理。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0238 | ruoyi-fastapi-frontend/src/assets/images/login-background.jpg / L1-L1 asset 完整内容 | react-front/src/assets/images/login-background.jpg |
| I0511 | ruoyi-fastapi-frontend/src/views/login.vue / L67-L167 script-setup 完整内容 | react-front/src/views/login.tsx |
| I0512 | ruoyi-fastapi-frontend/src/views/login.vue / L1-L65 template 完整内容 | react-front/src/views/login.tsx |
| I0513 | ruoyi-fastapi-frontend/src/views/login.vue / L169-L243 style-1 完整内容 | react-front/src/views/login.tsx |
| I0514 | ruoyi-fastapi-frontend/src/views/login.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/login.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/assets/images/login-background.jpg


### ruoyi-fastapi-frontend/src/views/login.vue

逻辑定位：handleLogin@L107–141, getCode@L143–152, getCookie@L154–163.
全部模板事件/权限：keyup=handleLogin@L23; keyup=handleLogin@L35; click=getCode@L40; click=handleLogin@L50.
