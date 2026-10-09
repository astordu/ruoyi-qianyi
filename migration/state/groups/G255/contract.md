# G255 src/utils/transportCryptoPolicy.js：完整能力

依赖：G000, G216

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02892 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=b922f0193d652b2c0de36098fb1aa440be1a522c617f1ee9035355a86f788986；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02893 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 3-3 ImportDeclaration: 
  - 基线：源语句 sha256=819249c9809a1e47bb12de03da21c4c25f60b908825d07094d219578c4c835ec；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02894 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 5-5 VariableDeclaration: TRANSPORT_BASE_URL
  - 基线：源语句 sha256=dbd4119f25a0f520194b7708c1f58c7507a9bfd6d464578b05a1c78676cbaec3；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02895 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 6-13 VariableDeclaration: EXCLUDED_URL_PATTERNS
  - 基线：源语句 sha256=61eb0b0ddef366394049dd9f76f4cb88ef815da1692bfc0c8e820761451e5210；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02896 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 14-14 VariableDeclaration: TRANSPORT_FRONTEND_CONFIG_CACHE_KEY
  - 基线：源语句 sha256=a9c9120a9deffe496ac52f7a19a5c3e8369b897e26638f4e1961f9eeb2a37dca；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02897 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 15-15 VariableDeclaration: TRANSPORT_FRONTEND_CONFIG_URL
  - 基线：源语句 sha256=e7fed1a68330baee9fdc432203de230e908842d142ee27f45f470c9813c53e97；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02898 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 16-16 VariableDeclaration: TRANSPORT_FRONTEND_CONFIG_FALLBACK_TTL_SECONDS
  - 基线：源语句 sha256=a0f013929f7d2fd17c1367e2e4353fc328f42267e4114b1f723c6616015f8559；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02899 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 17-17 VariableDeclaration: DEFAULT_TRANSPORT_ENVELOPE_VERSION
  - 基线：源语句 sha256=001ff3aa33730c3790fbe890e784f4743ac610fc661f3f5af0b4a95f80a15502；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02900 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 18-18 VariableDeclaration: DEFAULT_REQUEST_ENVELOPE_ALGORITHM
  - 基线：源语句 sha256=1bb22a7e732dd3c50c0447c64818f4adc2323364d7724c3289cb8cf9257c9d13；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02901 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 19-19 VariableDeclaration: DEFAULT_RESPONSE_ENVELOPE_ALGORITHM
  - 基线：源语句 sha256=bcf55dc4042063df0992dda530633c5a549dd802b24c3dc81ba27d27abfee67f；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02902 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 20-20 VariableDeclaration: DEFAULT_TRANSPORT_MAX_GET_URL_LENGTH
  - 基线：源语句 sha256=40b02c18e9f99ee194828ae82350f3a670aabef5c6b391044aae9bb3d9e4d2c1；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02903 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 22-25 VariableDeclaration: transportPolicyClient
  - 基线：源语句 sha256=bcd2cbf56aeaa1f9b784a588e3af1edf24bd421d582ef630058e8ffed7c733df；保留返回、异常及 0 个分支，调用=axios.create。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02904 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 27-27 VariableDeclaration: cachedTransportPolicy
  - 基线：源语句 sha256=626fcd80c116573ae5ff8cf96103e245a87155b018c5985615b3d8a8d2f99e68；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02905 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 28-28 VariableDeclaration: inflightTransportPolicyPromise
  - 基线：源语句 sha256=b495b035af6ecedc4092fc211e815148584bca9da9b77020f49cf1da8e6df2bf；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02906 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 35-37 FunctionDeclaration: getNowTimestamp
  - 基线：源语句 sha256=ece719ad56066eabb8c0662ffd8eba3b306d046f215668602d94485e26759bdf；保留返回、异常及 1 个分支，调用=Math.floor, Date.now。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02907 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 45-47 FunctionDeclaration: matchExcludedUrl
  - 基线：源语句 sha256=7ed9eb8680485c422aa6cfd62249ed3e747be432e2227a666dd7b49875517642；保留返回、异常及 1 个分支，调用=EXCLUDED_URL_PATTERNS.some, url.includes。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02908 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 56-58 FunctionDeclaration: matchPathPrefix
  - 基线：源语句 sha256=3c324e554a8f8d31c4499b7e569d7910d3c3fa2c1df6b078174bd7e3f6b17205；保留返回、异常及 2 个分支，调用=pathPatterns.some, path.startsWith。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02909 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 67-75 FunctionDeclaration: getHeaderValue
  - 基线：源语句 sha256=105eb666c5018e825f4dade73a8b0228a24913ead2b4fc3150ed51093db541f2；保留返回、异常及 6 个分支，调用=headers.get, name.toLowerCase。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02910 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 82-91 FunctionDeclaration: getBaseApiPath
  - 基线：源语句 sha256=7029377c55a503361c402e9c0a8eea0458439f8a9d04c3a2c9665cef136f63f7；保留返回、异常及 7 个分支，调用=TRANSPORT_BASE_URL.startsWith。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02911 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 99-115 FunctionDeclaration: getRequestPath
  - 基线：源语句 sha256=ae3ddc75dfe2b5350304034184d9824899f53e148915a0180867d3342e0bb63c；保留返回、异常及 10 个分支，调用=getBaseApiPath, String, normalizedUrl.startsWith, normalizedUrl.split, pathname.startsWith, pathname.slice。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02912 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 123-128 FunctionDeclaration: normalizePaths
  - 基线：源语句 sha256=f23f6691ee2cb9dfbf17030fd9a2f8da60123530e842449ac484495ae6d8d368；保留返回、异常及 4 个分支，调用=Array.isArray, CallExpression.filter, paths.map, CallExpression.trim, String。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02913 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 136-152 FunctionDeclaration: normalizeTransportPolicy
  - 基线：源语句 sha256=d07e0ea063da3ca713b3dce38f90105f563d54189b3d5f69893b184eff41a865；保留返回、异常及 10 个分支，调用=Boolean, String, normalizePaths, Number。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02914 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 159-176 FunctionDeclaration: buildFallbackTransportPolicy
  - 基线：源语句 sha256=e7ba02a9fe7b1eec01f1768307c463e29adf89b0057b5f562fe7d98c05905455；保留返回、异常及 1 个分支，调用=getNowTimestamp。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02915 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 184-191 FunctionDeclaration: buildRetryableTransportPolicy
  - 基线：源语句 sha256=160bb4980c7268c05d99621ee86bea3244268d42620739cdc3989f3d0e42145a；保留返回、异常及 1 个分支，调用=normalizeTransportPolicy, getNowTimestamp。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02916 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 199-210 FunctionDeclaration: isUsableTransportPolicy
  - 基线：源语句 sha256=f020dbd5858cbfc3e16580c1ebf8e56615ef121f8d59e2bea3d073df925fb278；保留返回、异常及 7 个分支，调用=getNowTimestamp。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02917 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 217-223 FunctionDeclaration: loadPersistedTransportPolicy
  - 基线：源语句 sha256=dd12b63f1b53e124dd642c7f3ebed1e53f4b7d7c828ff0462d86ce0b19b7e315；保留返回、异常及 3 个分支，调用=cache.session.getJSON, normalizeTransportPolicy。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02918 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 230-232 ExportNamedDeclaration: getTransportCryptoPolicy
  - 基线：源语句 sha256=1e58696d7815b2810ac23d31b72f7860da47dcb6c090b2adeacc35c9d112141e；保留返回、异常及 2 个分支，调用=buildFallbackTransportPolicy。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02919 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 239-243 ExportNamedDeclaration: invalidateTransportCryptoPolicy
  - 基线：源语句 sha256=a84c73789633a0d3ace6a7aedf340a7687e7e540ca3b96e3844274ab9488cdb3；保留返回、异常及 0 个分支，调用=cache.session.remove。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02920 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 251-289 ExportNamedDeclaration: ensureTransportCryptoPolicyLoaded
  - 基线：源语句 sha256=4ccf1fa047e2ec0351e6cfb0a175c222af9a83798e43c8eef455828e8c24b372；保留返回、异常及 15 个分支，调用=loadPersistedTransportPolicy, isUsableTransportPolicy, CallExpression.catch, CallExpression.then, transportPolicyClient.get, normalizeTransportPolicy, cache.session.setJSON, buildRetryableTransportPolicy, buildFallbackTransportPolicy, console.warn。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02921 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 298-323 ExportNamedDeclaration: shouldEncryptRequest
  - 基线：源语句 sha256=5a7a62779d800d71f41fbea952b550eede24eaafc702c692c44018463015b730；保留返回、异常及 22 个分支，调用=getTransportCryptoPolicy, getRequestPath, matchPathPrefix, matchExcludedUrl, getHeaderValue, contentType.includes。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02922 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 332-356 ExportNamedDeclaration: shouldEncryptResponse
  - 基线：源语句 sha256=479da4e12882cca50970d30d039ffe78ad6507246254048d74ca7aca65b1a5e1；保留返回、异常及 21 个分支，调用=getTransportCryptoPolicy, getRequestPath, matchPathPrefix, matchExcludedUrl。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts
- I02923 `ruoyi-fastapi-frontend/src/utils/transportCryptoPolicy.js` lines 365-370 ExportNamedDeclaration: shouldEncryptQuery
  - 基线：源语句 sha256=e5fcf5fba2bc2cb3542314edeed423287717eaab404b4e8ea7913a9124dbc6de；保留返回、异常及 4 个分支，调用=getTransportCryptoPolicy, shouldEncryptRequest。
  - 去向：react-front/src/utils/transportCryptoPolicy.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
