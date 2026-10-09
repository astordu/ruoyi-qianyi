# G035 src/api/system/config.js：完整能力

依赖：G000, G249

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00498 `ruoyi-fastapi-frontend/src/api/system/config.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=cd462474cb30a9a5954fbd44474b2f4e19f6d48d3c7dff5aebf452db4c8517f8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/api/system/config.ts
- I00499 `ruoyi-fastapi-frontend/src/api/system/config.js` lines 4-10 ExportNamedDeclaration: listConfig
  - 基线：源语句 sha256=b954ade13712d63263a25b5e7bd162208dcb8cb02176460bf5b54eb2369c260a；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/config.ts
- I00500 `ruoyi-fastapi-frontend/src/api/system/config.js` lines 13-18 ExportNamedDeclaration: getConfig
  - 基线：源语句 sha256=62fbe6835704ecaf34d108c6adb314dade88c3862f7b24324174f3f5bf1a6748；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/config.ts
- I00501 `ruoyi-fastapi-frontend/src/api/system/config.js` lines 21-26 ExportNamedDeclaration: getConfigKey
  - 基线：源语句 sha256=b745ddf850ad194b873521ff805e3f650e3d1d17006a1ed43c41b97dc8ed7a22；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/config.ts
- I00502 `ruoyi-fastapi-frontend/src/api/system/config.js` lines 29-35 ExportNamedDeclaration: addConfig
  - 基线：源语句 sha256=ad8279ff9eacb52c5833f0f2e0523a7ecd8c9f2b820e3c6f9b6c132fc10fe705；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/config.ts
- I00503 `ruoyi-fastapi-frontend/src/api/system/config.js` lines 38-44 ExportNamedDeclaration: updateConfig
  - 基线：源语句 sha256=171c440313353e12d8b54d548cb9b4086fc2fcceea4fd78203ea5bddd393357b；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/config.ts
- I00504 `ruoyi-fastapi-frontend/src/api/system/config.js` lines 47-52 ExportNamedDeclaration: delConfig
  - 基线：源语句 sha256=ebf4ad3461351a21b46c1e6731b6c2c8b622c4cc224e38afa196a8c0f315a755；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/config.ts
- I00505 `ruoyi-fastapi-frontend/src/api/system/config.js` lines 55-60 ExportNamedDeclaration: refreshCache
  - 基线：源语句 sha256=dc6edd88273e10db4d0e90c167a566aa9daf48c344f81e83afa461f39e5198c7；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/config.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
