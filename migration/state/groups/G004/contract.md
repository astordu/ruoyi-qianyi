# G004 传输加密策略与请求响应协议

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

传输加密策略与请求响应协议可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G001 React 工程、环境与部署, G002 共用数据与表单适配

## 正常、异常与边界检查条件

1. 策略并发加载去重、有效期缓存、强制失效与 60 秒失败重试保持旧行为；无历史策略加载失败时回退 off，有历史策略沿用历史策略并重试。
2. excludePaths 优先，enabledPaths 非空时限制范围；encrypt/encryptResponse/encryptQuery=false、multipart/binary、固定下载路径按源码豁免。
3. RSA-OAEP 包装 AES-256-GCM 会话密钥；请求/响应 AAD 的 method/path/direction、kid/version/alg、nonce、base64url、表单和查询信封与后端契约逐字段核对。
4. 无 WebCrypto、无效公钥/信封/过期版本/认证失败不能当作正常 JSON；加密查询 URL 超过 maxEncryptedGetUrlLength 按源码错误路径处理，不泄露明文。
5. 密钥缓存刷新和并发复用、原始请求快照/reset、错误响应解密、旧密钥一次重试与防重复提交豁免联动在 HTTP 集成重放。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0486 | ruoyi-fastapi-frontend/src/utils/transportCrypto.js / L1-L749 module 完整内容 | react-front/src/utils/transportCrypto.ts |
| I0487 | ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js / L1-L371 module 完整内容 | react-front/src/utils/transportCryptoPolicy.ts |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/utils/transportCrypto.js

逻辑定位：getBrowserCrypto@L35–41, getHeaderValue@L50–58, setHeaderValue@L68–77, toBase64Url@L85–91, fromBase64Url@L99–104, pemToArrayBuffer@L112–116, encodeQueryEnvelope@L124–127, buildQueryUrlLength@L136–144, getBaseApiPath@L151–160, getRequestPath@L168–184, buildRequestAad@L192–197, buildResponseAad@L205–211, normalizePlainPayload@L219–224, stringifyPayload@L232–235, cloneRequestValue@L243–254, stringifyEnvelopeField@L262–267, encodeFormEnvelope@L275–281, parseJsonObject@L290–296, validateTransportPublicKeyResponse@L304–308, validateTransportPublicKeyPayload@L317–327, validateResponseEnvelope@L338–364, rememberOriginalRequestSnapshot@L372–382, getNowTimestamp@L389–391, buildKeyRefreshAt@L400–412, isUsableKeyMeta@L421–427, getTransportKeyMeta@L435–507, buildTransportContext@L514–529, encryptPayloadText@L539–560, decryptEnvelope@L569–581, getOrCreateTransportContext@L589–595, encryptTransportRequest@L603–644, invalidateTransportKeyMeta@L651–655, resetTransportRequestConfig@L663–679, shouldRetryTransportWithFreshKey@L687–691, decryptTransportResponse@L699–717, decryptTransportErrorResponse@L725–748.
- URL/请求对象 L376: `(非请求URL对象) config.url`; params=`cloneRequestValue(config.params)`, data=`cloneRequestValue(config.data)`

### ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js

逻辑定位：getNowTimestamp@L35–37, matchExcludedUrl@L45–47, matchPathPrefix@L56–58, getHeaderValue@L67–75, getBaseApiPath@L82–91, getRequestPath@L99–115, normalizePaths@L123–128, normalizeTransportPolicy@L136–152, buildFallbackTransportPolicy@L159–176, buildRetryableTransportPolicy@L184–191, isUsableTransportPolicy@L199–210, loadPersistedTransportPolicy@L217–223, getTransportCryptoPolicy@L230–232, invalidateTransportCryptoPolicy@L239–243, ensureTransportCryptoPolicyLoaded@L251–289, shouldEncryptRequest@L298–323, shouldEncryptResponse@L332–356, shouldEncryptQuery@L365–370.
