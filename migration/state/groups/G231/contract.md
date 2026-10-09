# G231 src/utils/auth.js：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02626 `ruoyi-fastapi-frontend/src/utils/auth.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=ef343712ba6fc056099408d79793d007ac951f930da62d2f498ad7578f93f27f；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/auth.ts
- I02627 `ruoyi-fastapi-frontend/src/utils/auth.js` lines 3-3 VariableDeclaration: TokenKey
  - 基线：源语句 sha256=659c7ade0da706198f1dcf923fc7bc149d148a82fb187d49b8b733d28824c583；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/auth.ts
- I02628 `ruoyi-fastapi-frontend/src/utils/auth.js` lines 5-7 ExportNamedDeclaration: getToken
  - 基线：源语句 sha256=ac4e9d8a0dbcccebafbc019b06db334be9e8d29b92c2a8a81e56da185e1ad60f；保留返回、异常及 1 个分支，调用=Cookies.get。
  - 去向：react-front/src/utils/auth.ts
- I02629 `ruoyi-fastapi-frontend/src/utils/auth.js` lines 9-11 ExportNamedDeclaration: setToken
  - 基线：源语句 sha256=e03aa2a37574b696ea3cb88d9fba567b5e568a6f09dd5fca1cc371ea3fbf5a44；保留返回、异常及 1 个分支，调用=Cookies.set。
  - 去向：react-front/src/utils/auth.ts
- I02630 `ruoyi-fastapi-frontend/src/utils/auth.js` lines 13-15 ExportNamedDeclaration: removeToken
  - 基线：源语句 sha256=3535abddcf5186f31d38eda8cbc60de22c45b1150560d171f2bff2dc4c981028；保留返回、异常及 1 个分支，调用=Cookies.remove。
  - 去向：react-front/src/utils/auth.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
