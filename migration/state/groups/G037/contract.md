# G037 src/api/system/dict/data.js：完整能力

依赖：G000, G249

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00514 `ruoyi-fastapi-frontend/src/api/system/dict/data.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=cd462474cb30a9a5954fbd44474b2f4e19f6d48d3c7dff5aebf452db4c8517f8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/api/system/dict/data.ts
- I00515 `ruoyi-fastapi-frontend/src/api/system/dict/data.js` lines 4-10 ExportNamedDeclaration: listData
  - 基线：源语句 sha256=6b4c120f113793cb2dade69ec41cb00fa5e647f79aa943873bc58ea7748a9b27；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/dict/data.ts
- I00516 `ruoyi-fastapi-frontend/src/api/system/dict/data.js` lines 13-18 ExportNamedDeclaration: getData
  - 基线：源语句 sha256=d4b8c8ca20687a24aedac8023ac85af92e0625fbfad9ef2654d54843e3069b8d；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/dict/data.ts
- I00517 `ruoyi-fastapi-frontend/src/api/system/dict/data.js` lines 21-26 ExportNamedDeclaration: getDicts
  - 基线：源语句 sha256=883e6674c17b10744ff3204ac5597b1409e0d15f5579f7edf65c13dd0c4c928d；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/dict/data.ts
- I00518 `ruoyi-fastapi-frontend/src/api/system/dict/data.js` lines 29-35 ExportNamedDeclaration: addData
  - 基线：源语句 sha256=38e0ae77d6b5bb6a466399243aa1aad716122e64c4cd4ab06b01746b770622a9；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/dict/data.ts
- I00519 `ruoyi-fastapi-frontend/src/api/system/dict/data.js` lines 38-44 ExportNamedDeclaration: updateData
  - 基线：源语句 sha256=27bf53b4dca2a701ad27fe64e6584bb218762a0e8e60d9e08e8e53a4938a62c2；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/dict/data.ts
- I00520 `ruoyi-fastapi-frontend/src/api/system/dict/data.js` lines 47-52 ExportNamedDeclaration: delData
  - 基线：源语句 sha256=90d2b9b2e5b91a957e951fd3b3a19e0309346b425f5c89741b8aa62f814463f2；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/dict/data.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
