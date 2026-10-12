# G005 HTTP 请求、会话提示与导出

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

HTTP 请求、会话提示与导出可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G003 时区、日期输入与提交序列化, G004 传输加密策略与请求响应协议

## 正常、异常与边界检查条件

1. 请求默认 10 秒超时，携带 Bearer Token 与 X-Timezone；isToken=false、repeatSubmit=false、interval 覆盖保留。POST/PUT 同 URL/数据/时区在默认 1000ms 内拒绝重复；5MB 以上按原分支处理。
2. 参数拼接前完成传输加密；GET 查询编码后清空 params；blob/arraybuffer 直接返回二进制，普通 code 缺省按 200，500/601/其他错误提示类型与拒绝结果对应旧版。
3. 401 只弹一个重新登录确认，取消可继续停留；确认调用会话注销再跳转 /index。通过注入 session-expired handler 消除 request 对 userStore 的反向依赖。
4. 422 将 loc 去掉首段映射 fieldErrors，skipErrorMessage 阻止统一弹出；429 是 warning，网络/超时/HTTP 错误文本按源码区分；Axios 取消不弹错误。
5. 旧密钥错误只重试一次，用原始明文快照重新加密，防重复提交豁免生效。通用 POST 导出使用 form-urlencoded、二进制和 encrypt=false，成功保存，JSON 错误展示后关闭 loading。
6. 共享 getConfigKey 单独落在 config-read.ts，供密码规则和其他页面使用；不要求先完成参数管理页面。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0059 | ruoyi-fastapi-frontend/src/api/system/config.js / L21-L26 完整导出 getConfigKey | react-front/src/api/system/config-http.ts |
| I0451 | ruoyi-fastapi-frontend/src/plugins/modal.js / L1-L83 module 完整内容 | react-front/src/plugins/modal.ts |
| I0463 | ruoyi-fastapi-frontend/src/utils/auth.js / L1-L16 module 完整内容 | react-front/src/utils/auth.ts |
| I0466 | ruoyi-fastapi-frontend/src/utils/errorCode.js / L1-L7 module 完整内容 | react-front/src/utils/errorCode.ts |
| I0481 | ruoyi-fastapi-frontend/src/utils/request.js / L1-L219 module 完整内容 | react-front/src/utils/request.ts |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/system/config.js

逻辑定位：getConfigKey@L21–26.
- URL/请求对象 L22: `'get' '/system/config/configKey/' + configKey`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/plugins/modal.js

逻辑定位：msg@L7–9, msgError@L11–13, msgSuccess@L15–17, msgWarning@L19–21, alert@L23–25, alertError@L27–29, alertSuccess@L31–33, alertWarning@L35–37, notify@L39–41, notifyError@L43–45, notifySuccess@L47–49, notifyWarning@L51–53, confirm@L55–61, prompt@L63–69, loading@L71–77, closeLoading@L79–81.

### ruoyi-fastapi-frontend/src/utils/auth.js

逻辑定位：getToken@L5–7, setToken@L9–11, removeToken@L13–15.

### ruoyi-fastapi-frontend/src/utils/errorCode.js


### ruoyi-fastapi-frontend/src/utils/request.js

逻辑定位：download@L192–216.
- URL/请求对象 L51: `(非请求URL对象) config.url`; params=`None`, data=`typeof config.data === 'object' ? JSON.stringify(config.data) : config.data`

## 源循环/延后装配的明确接口

- `ruoyi-fastapi-frontend/src/utils/request.js` → `ruoyi-fastapi-frontend/src/store/modules/user.js` (G010): HTTP 接收 session-expired handler；会话组注册真实注销/跳转，J001/J002验收。

这些源关系保留在 dependency-review.json；只是将运行依赖改为显式接口注入，未删除功能。最终必须以真实页面/服务接线验收。
