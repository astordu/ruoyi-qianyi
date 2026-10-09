# G294 src/views/system/file/components/fileFormatters.js：完整能力

依赖：G000, G250

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I05551 `ruoyi-fastapi-frontend/src/views/system/file/components/fileFormatters.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=fe54fe8d0bc37a6edd34d5955113fdff6e14cfed8bb0025a58369785c850be00；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/fileFormatters.ts
- I05552 `ruoyi-fastapi-frontend/src/views/system/file/components/fileFormatters.js` lines 3-9 ExportNamedDeclaration: formatFileSize
  - 基线：源语句 sha256=9f28ce57557e3d256a81757cd79c76fc9bf3e81d4dcb380df6bcd128f5e06357；保留返回、异常及 8 个分支，调用=Number, BinaryExpression.toFixed。
  - 去向：react-front/src/views/system/file/components/fileFormatters.ts
- I05553 `ruoyi-fastapi-frontend/src/views/system/file/components/fileFormatters.js` lines 11-13 ExportNamedDeclaration: accessTypeLabel
  - 基线：源语句 sha256=746f5c58e52339cd3bdd63d505b78dccf5bda25f7365589bff357de6c9e4c4c3；保留返回、异常及 2 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/fileFormatters.ts
- I05554 `ruoyi-fastapi-frontend/src/views/system/file/components/fileFormatters.js` lines 15-21 ExportNamedDeclaration: statusLabel
  - 基线：源语句 sha256=428875cd2e7b1adb77d1986a6a314a52047664a40677c3ac053bc905cd716041；保留返回、异常及 2 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/fileFormatters.ts
- I05555 `ruoyi-fastapi-frontend/src/views/system/file/components/fileFormatters.js` lines 23-29 ExportNamedDeclaration: expirationLabel
  - 基线：源语句 sha256=3bad70625407771e78a026ee2cf04e8f469d92956f569a10e43e1a62617f2802；保留返回、异常及 7 个分支，调用=NewExpression.getTime, Date.now, parseTime。
  - 去向：react-front/src/views/system/file/components/fileFormatters.ts
- I05556 `ruoyi-fastapi-frontend/src/views/system/file/components/fileFormatters.js` lines 31-36 ExportNamedDeclaration: expirationTagType
  - 基线：源语句 sha256=b5447783386ba4d68fd80216cb4218f405d0d4c32d127601b64a16c91268c2a7；保留返回、异常及 6 个分支，调用=NewExpression.getTime, Date.now。
  - 去向：react-front/src/views/system/file/components/fileFormatters.ts
- I05557 `ruoyi-fastapi-frontend/src/views/system/file/components/fileFormatters.js` lines 38-42 ExportNamedDeclaration: isAclExpiring
  - 基线：源语句 sha256=a9da71f4855765f8fa43feb651468e58bf3124ea7ff596ab48add9bc0836e865；保留返回、异常及 4 个分支，调用=NewExpression.getTime, Date.now。
  - 去向：react-front/src/views/system/file/components/fileFormatters.ts
- I05558 `ruoyi-fastapi-frontend/src/views/system/file/components/fileFormatters.js` lines 44-51 ExportNamedDeclaration: storageStatusLabel
  - 基线：源语句 sha256=12963ab8c8f4fcad3bd893948a346db4385c743265e23a711219420ad645ecba；保留返回、异常及 2 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/fileFormatters.ts
- I05559 `ruoyi-fastapi-frontend/src/views/system/file/components/fileFormatters.js` lines 53-60 ExportNamedDeclaration: storageStatusTagType
  - 基线：源语句 sha256=ceb88ccc696f3b1beade2a92be94736876fc66a9816f15aef4ea43036018f1a5；保留返回、异常及 2 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/fileFormatters.ts
- I05560 `ruoyi-fastapi-frontend/src/views/system/file/components/fileFormatters.js` lines 62-75 ExportNamedDeclaration: actionLabel
  - 基线：源语句 sha256=285e855478dada258b7437615c95a3e58e453c12b3aa2fb99ad20d089133c7d4；保留返回、异常及 2 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/fileFormatters.ts
- I05561 `ruoyi-fastapi-frontend/src/views/system/file/components/fileFormatters.js` lines 77-84 ExportNamedDeclaration: resultLabel
  - 基线：源语句 sha256=e39370abee7f1ac6ab05ab084de0cd7e5df7a65a9aa0cd2fa84129ef7319c104；保留返回、异常及 2 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/fileFormatters.ts
- I05562 `ruoyi-fastapi-frontend/src/views/system/file/components/fileFormatters.js` lines 86-93 ExportNamedDeclaration: resultTagType
  - 基线：源语句 sha256=5eaa45c611ad05f76d34ccf2e5fe10282215a3f1d1246e63a58269e761c1e983；保留返回、异常及 2 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/fileFormatters.ts
- I05563 `ruoyi-fastapi-frontend/src/views/system/file/components/fileFormatters.js` lines 95-106 ExportNamedDeclaration: parseOperationDetail
  - 基线：源语句 sha256=d14b5de182df5fd8a7107fbc57ef9f8e55cb406da0d65578198987336df6e271；保留返回、异常及 7 个分支，调用=JSON.parse, CallExpression.map, Object.entries, auditDetailKeyLabel, JSON.stringify, String。
  - 去向：react-front/src/views/system/file/components/fileFormatters.ts
- I05564 `ruoyi-fastapi-frontend/src/views/system/file/components/fileFormatters.js` lines 108-146 FunctionDeclaration: auditDetailKeyLabel
  - 基线：源语句 sha256=21fdf756fc51d5ea885adc5f7ca8b268254b0fc3dc67f215b61eb304ec99817f；保留返回、异常及 2 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/fileFormatters.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
