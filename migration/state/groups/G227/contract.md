# G227 src/store/modules/permission.js：完整能力

依赖：G000, G026, G181, G200, G215, G248

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02580 `ruoyi-fastapi-frontend/src/store/modules/permission.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=b034e86ec457e3cb94cbcaea70797b51134dc7fe0eb6ac621961f8ad73fbdec4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/permission.ts
- I02581 `ruoyi-fastapi-frontend/src/store/modules/permission.js` lines 2-2 ImportDeclaration: 
  - 基线：源语句 sha256=54ec76b443416cfc9885e2eb415b279f1ab08aa5a9eea245532b9d7105f8a4b3；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/permission.ts
- I02582 `ruoyi-fastapi-frontend/src/store/modules/permission.js` lines 3-3 ImportDeclaration: 
  - 基线：源语句 sha256=3ad04fb820903830492a31f462261921d032c8f75f1ed2fc1f040a25b689aaeb；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/permission.ts
- I02583 `ruoyi-fastapi-frontend/src/store/modules/permission.js` lines 4-4 ImportDeclaration: 
  - 基线：源语句 sha256=e0e2beae58543b5079d990f7a02daa5d625febd3d2e17452477d329afe6439cb；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/permission.ts
- I02584 `ruoyi-fastapi-frontend/src/store/modules/permission.js` lines 5-5 ImportDeclaration: 
  - 基线：源语句 sha256=9e9fbda2846f3daf38b4b2ad1ae09f29829813b583b9b88303739173ea1c1f02；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/permission.ts
- I02585 `ruoyi-fastapi-frontend/src/store/modules/permission.js` lines 6-6 ImportDeclaration: 
  - 基线：源语句 sha256=5c0407b2d8c2cd3ba67a1f52a559a38d14127ca003c894ab5dc6d02b8b2feef9；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/permission.ts
- I02586 `ruoyi-fastapi-frontend/src/store/modules/permission.js` lines 7-7 ImportDeclaration: 
  - 基线：源语句 sha256=e550e31215727cd34d03f6247aca270a9c19f57f03e25f7ef11f3dbf66fbe06c；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/permission.ts
- I02587 `ruoyi-fastapi-frontend/src/store/modules/permission.js` lines 10-10 VariableDeclaration: builtinModules
  - 基线：源语句 sha256=ca5784ba089a09dd541170f11c6122f905dc26d9524865e932de18c1b5a5dd14；保留返回、异常及 0 个分支，调用=MetaProperty.glob。
  - 去向：react-front/src/store/modules/permission.ts
- I02588 `ruoyi-fastapi-frontend/src/store/modules/permission.js` lines 11-11 VariableDeclaration: pluginModules
  - 基线：源语句 sha256=81c53ea99a0c955e052f9e32700dfec16a074a0b219fb920afc90c9065984c3b；保留返回、异常及 0 个分支，调用=MetaProperty.glob。
  - 去向：react-front/src/store/modules/permission.ts
- I02589 `ruoyi-fastapi-frontend/src/store/modules/permission.js` lines 12-12 VariableDeclaration: missingView
  - 基线：源语句 sha256=325c4e9e6a961f0b5f3ab157450862232f0c640506434d6fc02104c6f2e18aab；保留返回、异常及 0 个分支，调用=Import。
  - 去向：react-front/src/store/modules/permission.ts
- I02590 `ruoyi-fastapi-frontend/src/store/modules/permission.js` lines 14-59 VariableDeclaration: usePermissionStore
  - 基线：源语句 sha256=fc3538e210c027a745ebddac92e8c23ecea0222cc935b6b0cf0abce585a3355a；保留返回、异常及 1 个分支，调用=defineStore, constantRoutes.concat, CallExpression.then, getRouters, JSON.parse, JSON.stringify, filterAsyncRouter, filterDynamicRoutes, asyncRoutes.forEach, router.addRoute, ThisExpression.setRoutes, ThisExpression.setSidebarRouters, ThisExpression.setDefaultRoutes, ThisExpression.setTopbarRoutes, resolve。
  - 去向：react-front/src/store/modules/permission.ts
- I02591 `ruoyi-fastapi-frontend/src/store/modules/permission.js` lines 62-87 FunctionDeclaration: filterAsyncRouter
  - 基线：源语句 sha256=0ca86dbff7ca142ffd06e0c95de3e6c91793b2da5c578708f358a9073aa82317；保留返回、异常及 11 个分支，调用=asyncRouterMap.filter, filterChildren, loadView, filterAsyncRouter。
  - 去向：react-front/src/store/modules/permission.ts
- I02592 `ruoyi-fastapi-frontend/src/store/modules/permission.js` lines 89-100 FunctionDeclaration: filterChildren
  - 基线：源语句 sha256=977a7c2db78175accc74c477b31f8f95424c71f726e9906d82fdedc0a1a41ec3；保留返回、异常及 5 个分支，调用=childrenMap.forEach, children.concat, filterChildren, children.push。
  - 去向：react-front/src/store/modules/permission.ts
- I02593 `ruoyi-fastapi-frontend/src/store/modules/permission.js` lines 103-117 ExportNamedDeclaration: filterDynamicRoutes
  - 基线：源语句 sha256=a615d77c5966514f9b4c8f715e050f27f1229e22274b26bffac5afbaebf837cf；保留返回、异常及 5 个分支，调用=routes.forEach, auth.hasPermiOr, res.push, auth.hasRoleOr。
  - 去向：react-front/src/store/modules/permission.ts
- I02594 `ruoyi-fastapi-frontend/src/store/modules/permission.js` lines 124-142 ExportNamedDeclaration: loadView
  - 基线：源语句 sha256=a853a1789edcf54cdbb1d1bca8d5bc4ab63b19269872fb875e8ed8fa0e0a6887；保留返回、异常及 7 个分支，调用=view.startsWith, resolvePluginViewPath, pluginModules.pluginViewPath, console.warn, CallExpression.NumericLiteral.split, path.split, builtinModules.path。
  - 去向：react-front/src/store/modules/permission.ts
- I02595 `ruoyi-fastapi-frontend/src/store/modules/permission.js` lines 144-144 ExportDefaultDeclaration: 
  - 基线：源语句 sha256=515b6e91683504ed9d92d7972bfa5aa6dfd487da0e528bd649e3bd126d414404；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/permission.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
