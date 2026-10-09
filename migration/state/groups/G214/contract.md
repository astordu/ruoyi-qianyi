# G214 src/permission.js：完整能力

依赖：G000, G221, G226, G227, G228, G230, G231, G249, G256

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02511 `ruoyi-fastapi-frontend/src/permission.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=35e52e99ce2a4703317a6fcc82d1c84b53f91d3ba38e87dca518d3a5eafd45e4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/permission.ts
- I02512 `ruoyi-fastapi-frontend/src/permission.js` lines 2-2 ImportDeclaration: 
  - 基线：源语句 sha256=4457e12145c39e48c136ec810328be51e9cd6003b57510fe47103e0ef2175a10；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/permission.ts
- I02513 `ruoyi-fastapi-frontend/src/permission.js` lines 3-3 ImportDeclaration: 
  - 基线：源语句 sha256=371d05523704f2343afaba0564cac136e3366f977b706c5c9cd134ed8280a46a；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/permission.ts
- I02514 `ruoyi-fastapi-frontend/src/permission.js` lines 4-4 ImportDeclaration: 
  - 基线：源语句 sha256=82ba0f6b64c2b1ceb00ed4f483a98e84a30d033ac1e30b6ca1d0257710f514ef；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/permission.ts
- I02515 `ruoyi-fastapi-frontend/src/permission.js` lines 5-5 ImportDeclaration: 
  - 基线：源语句 sha256=2ec8863f7e5e99b6e9f4898b63d49c0737c19ccb341a54be6cd435a7da40e781；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/permission.ts
- I02516 `ruoyi-fastapi-frontend/src/permission.js` lines 6-6 ImportDeclaration: 
  - 基线：源语句 sha256=2d2b6200e8964b4a7909f2b46d003eb729f9f19f70ebd81203bed2965a1638c7；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/permission.ts
- I02517 `ruoyi-fastapi-frontend/src/permission.js` lines 7-7 ImportDeclaration: 
  - 基线：源语句 sha256=b3b0b0c86cd2bea2ca59abb79a83004be3b1769dd1b261657df72d3a253254d6；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/permission.ts
- I02518 `ruoyi-fastapi-frontend/src/permission.js` lines 8-8 ImportDeclaration: 
  - 基线：源语句 sha256=c351978f324903ca33541ef37b2b07118aae76a82edaab040cb71996f923341f；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/permission.ts
- I02519 `ruoyi-fastapi-frontend/src/permission.js` lines 9-9 ImportDeclaration: 
  - 基线：源语句 sha256=56bc4c9061f8b753cafaec1815dba7fb04ce0a7503190381a9e1126f5fb1cfd0；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/permission.ts
- I02520 `ruoyi-fastapi-frontend/src/permission.js` lines 10-10 ImportDeclaration: 
  - 基线：源语句 sha256=88996687f5ac2ffe958aa6952515839565c6f908d46ea4106fe92135e3f788d7；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/permission.ts
- I02521 `ruoyi-fastapi-frontend/src/permission.js` lines 11-11 ImportDeclaration: 
  - 基线：源语句 sha256=efbb342d84aefbc6dc4b206f290d81fe87a23b34796df1ad0da69cd6a90b7ea3；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/permission.ts
- I02522 `ruoyi-fastapi-frontend/src/permission.js` lines 13-13 ExpressionStatement: 
  - 基线：源语句 sha256=bf0a370104c087a6f123b3dd5f402813d2736aa5a91bcc8005de79251dda91a4；保留返回、异常及 0 个分支，调用=NProgress.configure。
  - 去向：react-front/src/permission.ts
- I02523 `ruoyi-fastapi-frontend/src/permission.js` lines 15-15 VariableDeclaration: whiteList
  - 基线：源语句 sha256=500989233a69192b44bc3d266500844ab3ba76a61cdf0ead3eb91283ade9bb76；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/permission.ts
- I02524 `ruoyi-fastapi-frontend/src/permission.js` lines 17-19 VariableDeclaration: isWhiteList
  - 基线：源语句 sha256=134421235e1cba93b547cbb8c04daae576db7bb25dcbe4c93c45a5f2e2172258；保留返回、异常及 1 个分支，调用=whiteList.some, isPathMatch。
  - 去向：react-front/src/permission.ts
- I02525 `ruoyi-fastapi-frontend/src/permission.js` lines 21-72 ExpressionStatement: 
  - 基线：源语句 sha256=63830ac7c1d47ca48eea93ff8c853eb3b437f7cff0008a207febf9e38063cdb8；保留返回、异常及 21 个分支，调用=router.beforeEach, NProgress.start, getToken, CallExpression.setTitle, useSettingsStore, useLockStore, NProgress.done, isWhiteList, useUserStore, CallExpression.getInfo, CallExpression.generateRoutes, usePermissionStore, accessRoutes.forEach, isHttp, router.addRoute, CallExpression.logOut, ElMessage.error。
  - 去向：react-front/src/permission.ts
- I02526 `ruoyi-fastapi-frontend/src/permission.js` lines 74-76 ExpressionStatement: 
  - 基线：源语句 sha256=c73bc6f326b1823a07977457ece84de542af38609e214dbb63602b31c75c2b1b；保留返回、异常及 0 个分支，调用=router.afterEach, NProgress.done。
  - 去向：react-front/src/permission.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
