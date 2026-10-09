# G028 src/api/monitor/job.js：完整能力

依赖：G000, G249

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00465 `ruoyi-fastapi-frontend/src/api/monitor/job.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=cd462474cb30a9a5954fbd44474b2f4e19f6d48d3c7dff5aebf452db4c8517f8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/api/monitor/job.ts
- I00466 `ruoyi-fastapi-frontend/src/api/monitor/job.js` lines 4-13 ExportNamedDeclaration: previewJob
  - 基线：源语句 sha256=9306122eff02a15f6038eca127bd669b6d676290a6fe59bbd4cee800ef2b163a；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/job.ts
- I00467 `ruoyi-fastapi-frontend/src/api/monitor/job.js` lines 16-23 ExportNamedDeclaration: listJob
  - 基线：源语句 sha256=e03182bcd1aa67d3f7431bc26fe8bbe1a48491b5a773d6c8975547dd8debc4fc；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/job.ts
- I00468 `ruoyi-fastapi-frontend/src/api/monitor/job.js` lines 26-31 ExportNamedDeclaration: getJob
  - 基线：源语句 sha256=f179e7e419bff4bcd9eb189adabf8b65165683085c4d5cc06e1038594a701335；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/job.ts
- I00469 `ruoyi-fastapi-frontend/src/api/monitor/job.js` lines 34-40 ExportNamedDeclaration: addJob
  - 基线：源语句 sha256=31d74107ccf09f0762c70538c6dd64aff91971b97dbe1a1b88bb9ffdb03b2ae6；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/job.ts
- I00470 `ruoyi-fastapi-frontend/src/api/monitor/job.js` lines 43-49 ExportNamedDeclaration: updateJob
  - 基线：源语句 sha256=51370bce768367513eb778f8bc24f24ed09a8c35ba453ba0a1a61921cc34aa85；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/job.ts
- I00471 `ruoyi-fastapi-frontend/src/api/monitor/job.js` lines 52-57 ExportNamedDeclaration: delJob
  - 基线：源语句 sha256=46b9161ed63ceafc572d2006741ffad76419414e34fdf15efeaa0a31ccc3b9be；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/job.ts
- I00472 `ruoyi-fastapi-frontend/src/api/monitor/job.js` lines 60-70 ExportNamedDeclaration: changeJobStatus
  - 基线：源语句 sha256=462e686faeb3cf597afbddb2eea6373cdb178cbd678cfa4ee1b533278622e10a；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/job.ts
- I00473 `ruoyi-fastapi-frontend/src/api/monitor/job.js` lines 74-83 ExportNamedDeclaration: runJob
  - 基线：源语句 sha256=5bdc1f4b5d459d05ec80d7f42dacdfaf85a8009558a20d0d66554362bea62a73；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/job.ts
- I00474 `ruoyi-fastapi-frontend/src/api/monitor/job.js` lines 86-93 ExportNamedDeclaration: listJobExecutions
  - 基线：源语句 sha256=2a7fa56d3b24be15bcad3b680cff1f32087f5aae697b7fe871bba8b69b54ef94；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/job.ts
- I00475 `ruoyi-fastapi-frontend/src/api/monitor/job.js` lines 96-102 ExportNamedDeclaration: getJobExecution
  - 基线：源语句 sha256=a56629787baccdf903b3a27e04eabdf4ca423068abf94caf2c5ebacd4243e4aa；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/job.ts
- I00476 `ruoyi-fastapi-frontend/src/api/monitor/job.js` lines 105-112 ExportNamedDeclaration: listJobSync
  - 基线：源语句 sha256=b3c1751853f01ff8697f40b46f0ec12c5527d21b928b55ad019f8fb22371f844；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/job.ts
- I00477 `ruoyi-fastapi-frontend/src/api/monitor/job.js` lines 115-120 ExportNamedDeclaration: retryJobSync
  - 基线：源语句 sha256=6248f868ff85ef8277a9a8243d9790d7a99f91041f23aa5564ecb5efaf90bdf8；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/job.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
