# G006 密码规则与记住密码适配

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

密码规则与记住密码适配可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G005 HTTP 请求、会话提示与导出

## 正常、异常与边界检查条件

1. 按服务端 pwrChrtype 选择全部密码字符规则，长度 6–20；普通表单 validator 和 prompt validator 的错误结果保持对应。
2. 登录记住密码使用原 JSEncrypt 格式加解密；已有 cookie 可读取，失败结果按原版记录，不把密码或源码密钥写入计划/日志。
3. 修改配置后再读取规则，不把规则静态固定；注册、重置密码、个人中心分别验证真实表单接线。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0476 | ruoyi-fastapi-frontend/src/utils/jsencrypt.js / L1-L31 module 完整内容 | react-front/src/utils/jsencrypt.ts |
| I0477 | ruoyi-fastapi-frontend/src/utils/passwordRule.js / L1-L74 module 完整内容 | react-front/src/utils/passwordRule.ts |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/utils/jsencrypt.js

逻辑定位：encrypt@L18–22, decrypt@L25–29.

### ruoyi-fastapi-frontend/src/utils/passwordRule.js

逻辑定位：usePasswordRule@L27–73, pwdPromptValidator@L38–46.
