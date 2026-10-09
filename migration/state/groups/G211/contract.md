# G211 src/layout/components/index.js：完整能力

依赖：G000, G195, G201, G202, G208

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02423 `ruoyi-fastapi-frontend/src/layout/components/index.js` lines 1-1 ExportNamedDeclaration: 
  - 基线：源语句 sha256=0823dc36d1dda0d61542d9de08163231b20c13e6640db543887ab9efaa59a7b8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/index.ts
- I02424 `ruoyi-fastapi-frontend/src/layout/components/index.js` lines 2-2 ExportNamedDeclaration: 
  - 基线：源语句 sha256=8d560ac20d13f6f97ad3cce4f73ab52f2b5a3d7de6662b8c91d7fe46cc990d96；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/index.ts
- I02425 `ruoyi-fastapi-frontend/src/layout/components/index.js` lines 3-3 ExportNamedDeclaration: 
  - 基线：源语句 sha256=53c06dd92879ba5961ee5588475ee46e748ef7dea113beb9cb466f845311bf28；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/index.ts
- I02426 `ruoyi-fastapi-frontend/src/layout/components/index.js` lines 4-4 ExportNamedDeclaration: 
  - 基线：源语句 sha256=2785c39d09af75996865b4ef6c53e65c0cc290a66cd83be10bbc0e5cb2220846；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/index.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
