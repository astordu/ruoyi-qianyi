# G218 src/plugins/index.js：完整能力

依赖：G000, G215, G216, G217, G219, G220

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02550 `ruoyi-fastapi-frontend/src/plugins/index.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=f62a5cb70b61684d2c08400bfa124c632811669231d34daab90d1fd8eec77890；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/plugins/index.ts
- I02551 `ruoyi-fastapi-frontend/src/plugins/index.js` lines 2-2 ImportDeclaration: 
  - 基线：源语句 sha256=4b566375045bf192b7e6c8e473375c9820a2b8da07933f00802bab30e0b17550；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/plugins/index.ts
- I02552 `ruoyi-fastapi-frontend/src/plugins/index.js` lines 3-3 ImportDeclaration: 
  - 基线：源语句 sha256=fbc288ef5312c1da2869bacb10359d1d365e9240726c7046e61c555702531e40；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/plugins/index.ts
- I02553 `ruoyi-fastapi-frontend/src/plugins/index.js` lines 4-4 ImportDeclaration: 
  - 基线：源语句 sha256=3c99d0412fb208283b2ec9e73d1901fbfbd566b39f18b94c10b41103121b0e74；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/plugins/index.ts
- I02554 `ruoyi-fastapi-frontend/src/plugins/index.js` lines 5-5 ImportDeclaration: 
  - 基线：源语句 sha256=4c249f2834e521fe6e866d0a9fa3c9adeac3212b01ceb288b7ff162d39d2fe84；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/plugins/index.ts
- I02555 `ruoyi-fastapi-frontend/src/plugins/index.js` lines 7-18 ExportDefaultDeclaration: installPlugins
  - 基线：源语句 sha256=ae6788b378ced089e8e20e4eb270ce78b5058b8bcf647649c67200d4469691bd；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/plugins/index.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
