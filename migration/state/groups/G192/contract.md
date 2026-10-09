# G192 src/directive/index.js：完整能力

依赖：G000, G191, G193, G194

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01905 `ruoyi-fastapi-frontend/src/directive/index.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=e15db6fe27cd0e35c968a98335d93547f906a89496ee10ad051f772753029b71；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/directive/index.ts
- I01906 `ruoyi-fastapi-frontend/src/directive/index.js` lines 2-2 ImportDeclaration: 
  - 基线：源语句 sha256=1216115c81c23fffa7e85331178f3b722a8326711e76a29131f917defa2f452f；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/directive/index.ts
- I01907 `ruoyi-fastapi-frontend/src/directive/index.js` lines 3-3 ImportDeclaration: 
  - 基线：源语句 sha256=494b16ed7468a94ac3f68c13cc3c29c59b7a251b7353e4da9ccfcf227014bb61；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/directive/index.ts
- I01908 `ruoyi-fastapi-frontend/src/directive/index.js` lines 5-9 ExportDefaultDeclaration: directive
  - 基线：源语句 sha256=027b7f0ebeb5abd2a51f650accb2cf77b56ff707311e07e3f08a021ad16a9c84；保留返回、异常及 0 个分支，调用=app.directive。
  - 去向：react-front/src/directive/index.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
