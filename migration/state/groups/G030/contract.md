# G030 src/api/monitor/logininfor.js：完整能力

依赖：G000, G249

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00482 `ruoyi-fastapi-frontend/src/api/monitor/logininfor.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=cd462474cb30a9a5954fbd44474b2f4e19f6d48d3c7dff5aebf452db4c8517f8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/api/monitor/logininfor.ts
- I00483 `ruoyi-fastapi-frontend/src/api/monitor/logininfor.js` lines 4-10 ExportNamedDeclaration: list
  - 基线：源语句 sha256=abfe9db077dd180196f74895dfd19510913f258cc76425e257250b60688bb38d；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/logininfor.ts
- I00484 `ruoyi-fastapi-frontend/src/api/monitor/logininfor.js` lines 13-18 ExportNamedDeclaration: delLogininfor
  - 基线：源语句 sha256=f69fa388ac6ecc54bd92c6ab4afc776607ce9a92d8fe29c0f6d11e1d701674dd；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/logininfor.ts
- I00485 `ruoyi-fastapi-frontend/src/api/monitor/logininfor.js` lines 21-26 ExportNamedDeclaration: unlockLogininfor
  - 基线：源语句 sha256=c1a624005508fede44e39fe0a1131692b883ec7b55713e497bf42aa1c0f05ee0；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/logininfor.ts
- I00486 `ruoyi-fastapi-frontend/src/api/monitor/logininfor.js` lines 29-34 ExportNamedDeclaration: cleanLogininfor
  - 基线：源语句 sha256=78bddab3ae5cad1474e28f41fc7ad8b9673ef842db7b483888ade2f2d27df2cc；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/monitor/logininfor.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
