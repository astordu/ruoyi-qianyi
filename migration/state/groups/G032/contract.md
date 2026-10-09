# G032 src/api/monitor/operlog.js：完整能力

依赖：G000, G249

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00490 `ruoyi-fastapi-frontend/src/api/monitor/operlog.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=cd462474cb30a9a5954fbd44474b2f4e19f6d48d3c7dff5aebf452db4c8517f8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/api/monitor/operlog.ts
- I00491 `ruoyi-fastapi-frontend/src/api/monitor/operlog.js` lines 4-10 ExportNamedDeclaration: list
  - 基线：源语句 sha256=4ecae399f70f98c970d71c603190fc54453690cf4252d8963b2706ad4eb9045f；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/operlog.ts
- I00492 `ruoyi-fastapi-frontend/src/api/monitor/operlog.js` lines 13-18 ExportNamedDeclaration: delOperlog
  - 基线：源语句 sha256=2dd3cc928e0f9e1bd3d6acf8d76d25b064a310bb112835d6e1153d27b1aed601；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/operlog.ts
- I00493 `ruoyi-fastapi-frontend/src/api/monitor/operlog.js` lines 21-26 ExportNamedDeclaration: cleanOperlog
  - 基线：源语句 sha256=ac98d7aad0bfc4f7d032b90abfb8e83b00edf8ed1256881dfc5cc06d67f83c76；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/operlog.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
