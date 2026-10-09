# G337 vite/plugins/index.js：完整能力

依赖：G000, G335, G336, G338, G339

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I08744 `ruoyi-fastapi-frontend/vite/plugins/index.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=97a1f583733341b279083adbc95ba16d5d26f991ecb0162e1e405cd41a3694aa；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/vite/plugins/index.ts
- I08745 `ruoyi-fastapi-frontend/vite/plugins/index.js` lines 2-2 ImportDeclaration: 
  - 基线：源语句 sha256=040d77c436fd8f5e325cbdd1144bea6723675161ecdba4008aa50d61b72f033e；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/vite/plugins/index.ts
- I08746 `ruoyi-fastapi-frontend/vite/plugins/index.js` lines 4-4 ImportDeclaration: 
  - 基线：源语句 sha256=1e567b832ae1e9967b9e17e078de79896281aa7768a2a4abd1a0f83f770d88a9；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/vite/plugins/index.ts
- I08747 `ruoyi-fastapi-frontend/vite/plugins/index.js` lines 5-5 ImportDeclaration: 
  - 基线：源语句 sha256=198c07d40366de486d72df6584a38a8a3286a2ae5add8a67ad434f4a11e81b53；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/vite/plugins/index.ts
- I08748 `ruoyi-fastapi-frontend/vite/plugins/index.js` lines 6-6 ImportDeclaration: 
  - 基线：源语句 sha256=be97ee8589a97c2cc9833ee10649a51d20b76a7ed91d1c5ea26fd1be25965052；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/vite/plugins/index.ts
- I08749 `ruoyi-fastapi-frontend/vite/plugins/index.js` lines 7-7 ImportDeclaration: 
  - 基线：源语句 sha256=4d8904bbd08041705f2da108fdbbba51f1fee281d3d87cbdbea121f34bbdde6e；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/vite/plugins/index.ts
- I08750 `ruoyi-fastapi-frontend/vite/plugins/index.js` lines 9-30 VariableDeclaration: monacoWorkers
  - 基线：源语句 sha256=f5ecab7adeeed981e0357244e1fcf46766feaabfce30509963f3ba26d04d5607；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/vite/plugins/index.ts
- I08751 `ruoyi-fastapi-frontend/vite/plugins/index.js` lines 32-43 ExportDefaultDeclaration: createVitePlugins
  - 基线：源语句 sha256=25bc688502379dcf100ecc0985cd5c203715f975f056e796b25b9413dc0077c5；保留返回、异常及 2 个分支，调用=vue, vitePlugins.push, createAutoImport, createSetupExtend, monacoEditorEsmPlugin, createSvgIcon, createCompression。
  - 去向：react-front/vite/plugins/index.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
