# G251 src/utils/scroll-to.js：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02780 `ruoyi-fastapi-frontend/src/utils/scroll-to.js` lines 1-8 ExpressionStatement: 
  - 基线：源语句 sha256=9d46d7813fd06a6ae96e94023232344eade1bba865d7d2a36c9519edbfcc0288；保留返回、异常及 3 个分支，调用=。
  - 去向：react-front/src/utils/scroll-to.ts
- I02781 `ruoyi-fastapi-frontend/src/utils/scroll-to.js` lines 11-13 VariableDeclaration: requestAnimFrame
  - 基线：源语句 sha256=3bba13a29816b69b0f2af799ae7c65d6673dfb9e20df8e05f45b1ec534ecdb0e；保留返回、异常及 4 个分支，调用=FunctionExpression, window.setTimeout。
  - 去向：react-front/src/utils/scroll-to.ts
- I02782 `ruoyi-fastapi-frontend/src/utils/scroll-to.js` lines 19-23 FunctionDeclaration: move
  - 基线：源语句 sha256=c668649861a9b038f3cfcc81c65332b5669e72b5df90ba545396a9702d2a79e0；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/scroll-to.ts
- I02783 `ruoyi-fastapi-frontend/src/utils/scroll-to.js` lines 25-27 FunctionDeclaration: position
  - 基线：源语句 sha256=57c92f903a72c8123a4e1f344cbf88f5f9cf024722c282daefb643ee627b4e23；保留返回、异常及 3 个分支，调用=。
  - 去向：react-front/src/utils/scroll-to.ts
- I02784 `ruoyi-fastapi-frontend/src/utils/scroll-to.js` lines 34-58 ExportNamedDeclaration: scrollTo
  - 基线：源语句 sha256=00f0f4b3e1a08fb69e3f93e19416c1e213301321a7067204309561bab9840e05；保留返回、异常及 4 个分支，调用=position, Math.easeInOutQuad, move, requestAnimFrame, callback, animateScroll。
  - 去向：react-front/src/utils/scroll-to.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
