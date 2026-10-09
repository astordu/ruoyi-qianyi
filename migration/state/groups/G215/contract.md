# G215 src/plugins/auth.js：完整能力

依赖：G000, G230

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02527 `ruoyi-fastapi-frontend/src/plugins/auth.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=c351978f324903ca33541ef37b2b07118aae76a82edaab040cb71996f923341f；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/plugins/auth.ts
- I02528 `ruoyi-fastapi-frontend/src/plugins/auth.js` lines 3-13 FunctionDeclaration: authPermission
  - 基线：源语句 sha256=102fbef2f1deb73220c6db0128e4db9165d664565393dbe8734e8fc8702d342b；保留返回、异常及 6 个分支，调用=useUserStore, permissions.some。
  - 去向：react-front/src/plugins/auth.ts
- I02529 `ruoyi-fastapi-frontend/src/plugins/auth.js` lines 15-25 FunctionDeclaration: authRole
  - 基线：源语句 sha256=c1cfb7b09be88bb2416163ecb06f41bacc5ca0b9c18afa7d52939afce8996310；保留返回、异常及 6 个分支，调用=useUserStore, roles.some。
  - 去向：react-front/src/plugins/auth.ts
- I02530 `ruoyi-fastapi-frontend/src/plugins/auth.js` lines 27-60 ExportDefaultDeclaration: hasPermi, hasPermiOr, hasPermiAnd, hasRole
  - 基线：源语句 sha256=4a4ff9e537c48ad9b548a4db33d73ca8271bc0b18509f0feb7b451f5154d401a；保留返回、异常及 10 个分支，调用=authPermission, permissions.some, permissions.every, authRole, roles.some, roles.every。
  - 去向：react-front/src/plugins/auth.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
