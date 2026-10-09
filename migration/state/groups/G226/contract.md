# G226 src/store/modules/lock.js：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02576 `ruoyi-fastapi-frontend/src/store/modules/lock.js` lines 1-1 VariableDeclaration: LOCK_KEY
  - 基线：源语句 sha256=9303d40344c58c9b4802d7daf972f6c601182ce481344ff15035fb9d5b23d049；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/lock.ts
- I02577 `ruoyi-fastapi-frontend/src/store/modules/lock.js` lines 2-2 VariableDeclaration: LOCK_PATH_KEY
  - 基线：源语句 sha256=8d788ff1a45af92b9c3b82d87baf9a707f4b8b8873a57bb4b013dc78e56f2611；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/lock.ts
- I02578 `ruoyi-fastapi-frontend/src/store/modules/lock.js` lines 4-25 ExportNamedDeclaration: useLockStore
  - 基线：源语句 sha256=81a43420634affdcb03093ca78740d14a7208767ef55c0c3a26ff83b682cc539；保留返回、异常及 3 个分支，调用=defineStore, JSON.parse, localStorage.getItem, localStorage.setItem。
  - 去向：react-front/src/store/modules/lock.ts
- I02579 `ruoyi-fastapi-frontend/src/store/modules/lock.js` lines 27-27 ExportDefaultDeclaration: 
  - 基线：源语句 sha256=2641d052740faf00aa1ad1c557c6f6465a9ac2ca83dadb645a735221aa3b59e5；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/lock.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
