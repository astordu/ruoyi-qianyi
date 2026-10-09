# G249 src/utils/request.js：完整能力

依赖：G000, G216, G231, G234, G250, G253F025, G254F045, G254F046, G254F047, G254F048, G254F049, G254F050

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02748 `ruoyi-fastapi-frontend/src/utils/request.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=b922f0193d652b2c0de36098fb1aa440be1a522c617f1ee9035355a86f788986；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/request.ts
- I02749 `ruoyi-fastapi-frontend/src/utils/request.js` lines 2-2 ImportDeclaration: 
  - 基线：源语句 sha256=61e2f0784b912f7284650c15dcbb09143d1599654eb435424722c6c0e993041b；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/request.ts
- I02750 `ruoyi-fastapi-frontend/src/utils/request.js` lines 3-3 ImportDeclaration: 
  - 基线：源语句 sha256=2ec8863f7e5e99b6e9f4898b63d49c0737c19ccb341a54be6cd435a7da40e781；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/request.ts
- I02751 `ruoyi-fastapi-frontend/src/utils/request.js` lines 4-4 ImportDeclaration: 
  - 基线：源语句 sha256=5ded6eea1b8b6b5a422c9929d852248cb6a5f6bab74a1bf6350e8bf942cda7ae；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/request.ts
- I02752 `ruoyi-fastapi-frontend/src/utils/request.js` lines 5-5 ImportDeclaration: 
  - 基线：源语句 sha256=0460519625276597ebbc47c63a83fa0e7bc263f33807a3b88d3b9e952a376716；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/request.ts
- I02753 `ruoyi-fastapi-frontend/src/utils/request.js` lines 6-6 ImportDeclaration: 
  - 基线：源语句 sha256=e5170e3ed5615afa3a37e27015c639b48cd13b7195645b9214a295589ea16128；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/request.ts
- I02754 `ruoyi-fastapi-frontend/src/utils/request.js` lines 7-7 ImportDeclaration: 
  - 基线：源语句 sha256=819249c9809a1e47bb12de03da21c4c25f60b908825d07094d219578c4c835ec；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/request.ts
- I02755 `ruoyi-fastapi-frontend/src/utils/request.js` lines 8-8 ImportDeclaration: 
  - 基线：源语句 sha256=7389186de11cafd7624f8a0e5caccc3af1f087d5a425425c73df6c8827b071b0；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/request.ts
- I02756 `ruoyi-fastapi-frontend/src/utils/request.js` lines 9-9 ImportDeclaration: 
  - 基线：源语句 sha256=c351978f324903ca33541ef37b2b07118aae76a82edaab040cb71996f923341f；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/request.ts
- I02757 `ruoyi-fastapi-frontend/src/utils/request.js` lines 10-17 ImportDeclaration: 
  - 基线：源语句 sha256=9ed913e132b55810df414f688f0c3058d886b94454944ae45e86b10d8eec6ecf；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/request.ts
- I02758 `ruoyi-fastapi-frontend/src/utils/request.js` lines 19-19 VariableDeclaration: downloadLoadingInstance
  - 基线：源语句 sha256=bbe0de991a7dbaef70b16ff03fbe01850ca4c95539d8487bb3ddbef07780afde；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/request.ts
- I02759 `ruoyi-fastapi-frontend/src/utils/request.js` lines 21-21 ExportNamedDeclaration: isRelogin
  - 基线：源语句 sha256=7af6fe6d9d41922e45b144ad56b5c49abad9abb7cb900be44b7ca1f2d0328e80；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/request.ts
- I02760 `ruoyi-fastapi-frontend/src/utils/request.js` lines 23-23 ExpressionStatement: 
  - 基线：源语句 sha256=48002408d50c8d0cf3298007d73f0126d993c47b5e9accf62ffdbf488b38ad6c；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/request.ts
- I02761 `ruoyi-fastapi-frontend/src/utils/request.js` lines 25-30 VariableDeclaration: service
  - 基线：源语句 sha256=6fa2dc6fc56451d2d33bf4c46ad84463435d02e28b03394d93790239d044531b；保留返回、异常及 0 个分支，调用=axios.create。
  - 去向：react-front/src/utils/request.ts
- I02762 `ruoyi-fastapi-frontend/src/utils/request.js` lines 39-92 ExpressionStatement: 
  - 基线：源语句 sha256=d9f369dcbb80da538c54f428f3e27bc5ca77371526a8a91e103501f2868e74e9；保留返回、异常及 25 个分支，调用=service.interceptors.request.use, getDisplayTimezone, getToken, JSON.stringify, NewExpression.getTime, Object.keys, console.warn, cache.session.getJSON, cache.session.setJSON, Promise.reject, encryptTransportRequest, tansParams, url.slice, console.log。
  - 去向：react-front/src/utils/request.ts
- I02763 `ruoyi-fastapi-frontend/src/utils/request.js` lines 101-180 ExpressionStatement: 
  - 基线：源语句 sha256=acf2e8fe070f707332fdd36f602f54fb25e8f72421786d05e8dcbe4615a1e778；保留返回、异常及 41 个分支，调用=service.interceptors.response.use, decryptTransportResponse, CallExpression.catch, CallExpression.then, ElMessageBox.confirm, CallExpression.logOut, useUserStore, Promise.reject, ElMessage, ElNotification.error, Promise.resolve, axios.isCancel, decryptTransportErrorResponse, shouldRetryTransportWithFreshKey, invalidateTransportKeyMeta, resetTransportRequestConfig, service.request, console.log, Array.isArray, Object.fromEntries, details.map, OptionalCallExpression.join, item.loc.slice, CallExpression.join, message.includes, message.slice。
  - 去向：react-front/src/utils/request.ts
- I02764 `ruoyi-fastapi-frontend/src/utils/request.js` lines 192-216 ExportNamedDeclaration: download
  - 基线：源语句 sha256=50b89cad401fac463537f643495657067d83b3f3b5c659262d00b9756dd71dde；保留返回、异常及 5 个分支，调用=ElLoading.service, CallExpression.catch, CallExpression.then, service.post, tansParams, blobValidate, saveAs, data.text, JSON.parse, ElMessage.error, downloadLoadingInstance.close, console.error。
  - 去向：react-front/src/utils/request.ts
- I02765 `ruoyi-fastapi-frontend/src/utils/request.js` lines 218-218 ExportDefaultDeclaration: 
  - 基线：源语句 sha256=2489b70b34279ed6bb9479ea2cd40fe30ff8e4f864ebec9956dff0a9b295df2b；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/request.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
