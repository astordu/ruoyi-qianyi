# G241 src/utils/generator/render.js：完整能力

依赖：G000, G242

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02683 `ruoyi-fastapi-frontend/src/utils/generator/render.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=66f3b84f4fb823cb874eaad8b6125b73b8c00d665d6314a9dbf690b78c87982e；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/generator/render.ts
- I02684 `ruoyi-fastapi-frontend/src/utils/generator/render.js` lines 2-2 ImportDeclaration: 
  - 基线：源语句 sha256=839c8e4be6471ccc97b79dad0be0236e5a6dc30c49db774f00ee11be025dfe3a；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/generator/render.ts
- I02685 `ruoyi-fastapi-frontend/src/utils/generator/render.js` lines 4-18 VariableDeclaration: isAttr
  - 基线：源语句 sha256=24fc0848df0e9a4bd2edaa3e67246e9b3a16d4df672e4d36a4f6df91d6fd9539；保留返回、异常及 0 个分支，调用=makeMap。
  - 去向：react-front/src/utils/generator/render.ts
- I02686 `ruoyi-fastapi-frontend/src/utils/generator/render.js` lines 19-21 VariableDeclaration: isNotProps
  - 基线：源语句 sha256=e1266d86a1a554ea7b792a80dbaacf02d1f8b10b17a59334ac4e34e6c63e6735；保留返回、异常及 0 个分支，调用=makeMap。
  - 去向：react-front/src/utils/generator/render.ts
- I02687 `ruoyi-fastapi-frontend/src/utils/generator/render.js` lines 23-28 FunctionDeclaration: useVModel
  - 基线：源语句 sha256=d1cc0879d32ca824c7ee25306916726dddbcb98f57d547408e7b6faf39494506；保留返回、异常及 1 个分支，调用=emit。
  - 去向：react-front/src/utils/generator/render.ts
- I02688 `ruoyi-fastapi-frontend/src/utils/generator/render.js` lines 29-82 VariableDeclaration: componentChild
  - 基线：源语句 sha256=4990ea56bd5515eb40a978d6a05b618278beb8c82e4634eff19a0db8ada30176；保留返回、异常及 9 个分支，调用=conf.options.map, h, resolveComponent。
  - 去向：react-front/src/utils/generator/render.ts
- I02689 `ruoyi-fastapi-frontend/src/utils/generator/render.js` lines 83-93 VariableDeclaration: componentSlot
  - 基线：源语句 sha256=807294e5c548718371c8742e293de1d42b221b2016ad88e91d80e9cb4734632b；保留返回、异常及 2 个分支，调用=h。
  - 去向：react-front/src/utils/generator/render.ts
- I02690 `ruoyi-fastapi-frontend/src/utils/generator/render.js` lines 94-156 ExportDefaultDeclaration: render
  - 基线：源语句 sha256=3a1466998b96c1c39d3f93fb99a866403a78d3c6785ac80acbc54a1ae9657f55；保留返回、异常及 10 个分支，调用=defineComponent, JSON.parse, JSON.stringify, CallExpression.forEach, Object.keys, children.push, childFunc, isAttr, isNotProps, h, resolveComponent。
  - 去向：react-front/src/utils/generator/render.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
