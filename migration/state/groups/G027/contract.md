# G027 src/api/monitor/cache.js：完整能力

依赖：G000, G249

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00457 `ruoyi-fastapi-frontend/src/api/monitor/cache.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=cd462474cb30a9a5954fbd44474b2f4e19f6d48d3c7dff5aebf452db4c8517f8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/api/monitor/cache.ts
- I00458 `ruoyi-fastapi-frontend/src/api/monitor/cache.js` lines 4-9 ExportNamedDeclaration: getCache
  - 基线：源语句 sha256=f324db11ce7601f45e26e1bb41777891f6943cd536f0c226a84041467e560c5f；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/cache.ts
- I00459 `ruoyi-fastapi-frontend/src/api/monitor/cache.js` lines 12-17 ExportNamedDeclaration: listCacheName
  - 基线：源语句 sha256=1a62a4b64147bd37266808bcc4d36e4393a423d7950940bab019296489670309；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/cache.ts
- I00460 `ruoyi-fastapi-frontend/src/api/monitor/cache.js` lines 20-25 ExportNamedDeclaration: listCacheKey
  - 基线：源语句 sha256=77240b5a0b37be76fe8ed64f66cbbcae081cd37e61c5365f06dd2d3c614c5b81；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/cache.ts
- I00461 `ruoyi-fastapi-frontend/src/api/monitor/cache.js` lines 28-33 ExportNamedDeclaration: getCacheValue
  - 基线：源语句 sha256=87d6f1b94789448759713d2d5d4eed8c22dd69e8825521d50151d9c3b4c31aff；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/cache.ts
- I00462 `ruoyi-fastapi-frontend/src/api/monitor/cache.js` lines 36-41 ExportNamedDeclaration: clearCacheName
  - 基线：源语句 sha256=1f0afac1d1cf097a7c68c9428f41b6eab314a67c6eb6884e4d145067b026ac43；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/cache.ts
- I00463 `ruoyi-fastapi-frontend/src/api/monitor/cache.js` lines 44-49 ExportNamedDeclaration: clearCacheKey
  - 基线：源语句 sha256=a962f846fefa1c81bfc267f4136aeaaecb9f16a2d49669eb66715920cd03d9c4；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/cache.ts
- I00464 `ruoyi-fastapi-frontend/src/api/monitor/cache.js` lines 52-57 ExportNamedDeclaration: clearCacheAll
  - 基线：源语句 sha256=d6c60e3c27cd1dfb9a94d5c8566b90b00dfaa64a2e1646efb51e585de0565fd8；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/cache.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
