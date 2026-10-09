# G230 src/store/modules/user.js：完整能力

依赖：G000, G025, G147, G216, G226, G231, G253F019, G253F021, G256

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02615 `ruoyi-fastapi-frontend/src/store/modules/user.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=16fd4543dc8d478f7f7767c5aefc83e58b60720d5c73f34a7b2193673018cc0c；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/user.ts
- I02616 `ruoyi-fastapi-frontend/src/store/modules/user.js` lines 2-2 ImportDeclaration: 
  - 基线：源语句 sha256=819249c9809a1e47bb12de03da21c4c25f60b908825d07094d219578c4c835ec；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/user.ts
- I02617 `ruoyi-fastapi-frontend/src/store/modules/user.js` lines 3-3 ImportDeclaration: 
  - 基线：源语句 sha256=cae13d9c95f4e9c4ecf6ac6633b9c69880eb3576f755cc814323609f99a97877；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/user.ts
- I02618 `ruoyi-fastapi-frontend/src/store/modules/user.js` lines 4-4 ImportDeclaration: 
  - 基线：源语句 sha256=60cbc6e5687d10f3fa3488730fd44f7dca243fdba3d5cf31b74ccec0f98194ce；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/user.ts
- I02619 `ruoyi-fastapi-frontend/src/store/modules/user.js` lines 5-5 ImportDeclaration: 
  - 基线：源语句 sha256=a3acbf6c5298fe27edab013290e7b538711a3929ccd0c21c3752a0739e2260c9；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/user.ts
- I02620 `ruoyi-fastapi-frontend/src/store/modules/user.js` lines 6-6 ImportDeclaration: 
  - 基线：源语句 sha256=b0efd487be96875bddd743d16f135bdf670cc640f109de0c095ce48881f78bdc；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/user.ts
- I02621 `ruoyi-fastapi-frontend/src/store/modules/user.js` lines 7-7 ImportDeclaration: 
  - 基线：源语句 sha256=2d0f39dc9174848d559b2af4eb3fd1c3ee52f1afe8aadda5517104e6899a5e31；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/user.ts
- I02622 `ruoyi-fastapi-frontend/src/store/modules/user.js` lines 8-8 ImportDeclaration: 
  - 基线：源语句 sha256=56bc4c9061f8b753cafaec1815dba7fb04ce0a7503190381a9e1126f5fb1cfd0；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/user.ts
- I02623 `ruoyi-fastapi-frontend/src/store/modules/user.js` lines 9-9 ImportDeclaration: 
  - 基线：源语句 sha256=0cee6614fb11d313969b4a24630b3fadded7f957271e8a0d37792b9e63edf564；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/user.ts
- I02624 `ruoyi-fastapi-frontend/src/store/modules/user.js` lines 11-105 VariableDeclaration: useUserStore
  - 基线：源语句 sha256=6a61bbf565e372b129be2cd2034a762754882d21a0513b69ab378c1621479102；保留返回、异常及 11 个分支，调用=defineStore, getToken, setUserTimezone, userInfo.username.trim, CallExpression.catch, CallExpression.then, login, setToken, CallExpression.unlockScreen, useLockStore, resolve, reject, getInfo, setBusinessTimezone, ThisExpression.applyTimezone, isHttp, isEmpty, cache.session.set, ElMessageBox.confirm, router.push, logout, removeToken。
  - 去向：react-front/src/store/modules/user.ts
- I02625 `ruoyi-fastapi-frontend/src/store/modules/user.js` lines 107-107 ExportDefaultDeclaration: 
  - 基线：源语句 sha256=a3e064cbee93a627f88d9743b181fc03b519b4365bec8ae18ae82bdd39e8749b；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/user.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
