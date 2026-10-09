# G216 src/plugins/cache.js：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02531 `ruoyi-fastapi-frontend/src/plugins/cache.js` lines 1-34 VariableDeclaration: sessionCache
  - 基线：源语句 sha256=470f98af22219caaf8e60a663d8d55b41e56e42a93316122a24f2f6584c7cd3e；保留返回、异常及 13 个分支，调用=sessionStorage.setItem, sessionStorage.getItem, ThisExpression.set, JSON.stringify, ThisExpression.get, JSON.parse, sessionStorage.removeItem。
  - 去向：react-front/src/plugins/cache.ts
- I02532 `ruoyi-fastapi-frontend/src/plugins/cache.js` lines 35-68 VariableDeclaration: localCache
  - 基线：源语句 sha256=e1cea8e957db953a873fe2cea9db5dbe9d9c438e74ecd53db3bdfee30b0b802d；保留返回、异常及 13 个分支，调用=localStorage.setItem, localStorage.getItem, ThisExpression.set, JSON.stringify, ThisExpression.get, JSON.parse, localStorage.removeItem。
  - 去向：react-front/src/plugins/cache.ts
- I02533 `ruoyi-fastapi-frontend/src/plugins/cache.js` lines 70-79 ExportDefaultDeclaration: 
  - 基线：源语句 sha256=30da4d8c8fc5057480e26466e78b445e1bd6b9628ae2aeb35f0b408fbf36bee1；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/plugins/cache.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
