# G221 src/router/index.js：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02562 `ruoyi-fastapi-frontend/src/router/index.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=2cfe64116fcb14fe25a6e2478d252e3efaeea93e457a990852974ad8dd02e576；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/router/index.ts
- I02563 `ruoyi-fastapi-frontend/src/router/index.js` lines 3-3 ImportDeclaration: 
  - 基线：源语句 sha256=8bb019c7c467ab328e0e38638ab52c297c18974105b3b31542d214cfa86264d8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/router/index.ts
- I02564 `ruoyi-fastapi-frontend/src/router/index.js` lines 28-93 ExportNamedDeclaration: constantRoutes
  - 基线：源语句 sha256=c693cd8bdb2c458f03d42e4e40de8312244b3d80d445edc26b3da02b8416c5ef；保留返回、异常及 0 个分支，调用=Import。
  - 去向：react-front/src/router/index.ts
- I02565 `ruoyi-fastapi-frontend/src/router/index.js` lines 96-167 ExportNamedDeclaration: dynamicRoutes
  - 基线：源语句 sha256=88b40054d44a3f14d29730aa5179ad19da30c93b57535b63b312d6198fff4f75；保留返回、异常及 0 个分支，调用=Import。
  - 去向：react-front/src/router/index.ts
- I02566 `ruoyi-fastapi-frontend/src/router/index.js` lines 169-178 VariableDeclaration: router
  - 基线：源语句 sha256=da83beaee594691f2b0b37fd96ed2e174cb269f18edfb1a8df5732e6eb9c7d29；保留返回、异常及 3 个分支，调用=createRouter, createWebHistory。
  - 去向：react-front/src/router/index.ts
- I02567 `ruoyi-fastapi-frontend/src/router/index.js` lines 180-180 ExportDefaultDeclaration: 
  - 基线：源语句 sha256=446aaf4abedbce1d9a77dfc444a1fc6662bdf2667332132445e7019251f9bcd8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/router/index.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
