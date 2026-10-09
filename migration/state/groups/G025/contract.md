# G025 src/api/login.js：完整能力

依赖：G000, G249

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00448 `ruoyi-fastapi-frontend/src/api/login.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=cd462474cb30a9a5954fbd44474b2f4e19f6d48d3c7dff5aebf452db4c8517f8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/api/login.ts
- I00449 `ruoyi-fastapi-frontend/src/api/login.js` lines 4-21 ExportNamedDeclaration: login
  - 基线：源语句 sha256=8de2a7457ccc0ce03a954eb87472144627ff8dbc2c45eace44e36f223b74176a；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/login.ts
- I00450 `ruoyi-fastapi-frontend/src/api/login.js` lines 24-33 ExportNamedDeclaration: register
  - 基线：源语句 sha256=87584e5b330cc6041a30b62afd5a6456f15741a7e51396dc7c0d0e284ec62cc8；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/login.ts
- I00451 `ruoyi-fastapi-frontend/src/api/login.js` lines 36-41 ExportNamedDeclaration: getInfo
  - 基线：源语句 sha256=275039e2a6b2517a67cc4479e282762c90fca4bd87604e436a8f209d41b84e9d；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/login.ts
- I00452 `ruoyi-fastapi-frontend/src/api/login.js` lines 44-50 ExportNamedDeclaration: unlockScreen
  - 基线：源语句 sha256=d5b25eeb870b92a7f4aef94914c38d8e2a5f01996cee65b9e2e071a444e2b7c6；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/login.ts
- I00453 `ruoyi-fastapi-frontend/src/api/login.js` lines 53-58 ExportNamedDeclaration: logout
  - 基线：源语句 sha256=56dac18a4ec275900a1172642c9eeb5b6cf42816997f664f90cd3f839b340131；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/login.ts
- I00454 `ruoyi-fastapi-frontend/src/api/login.js` lines 61-70 ExportNamedDeclaration: getCodeImg
  - 基线：源语句 sha256=35a5e35683d0343634b232f9c67df226ab39d360b0d5f4e9f72e98715eef8b8c；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/login.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
