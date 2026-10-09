# G229 src/store/modules/tagsView.js：完整能力

依赖：G000, G216, G228

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02606 `ruoyi-fastapi-frontend/src/store/modules/tagsView.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=819249c9809a1e47bb12de03da21c4c25f60b908825d07094d219578c4c835ec；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/tagsView.ts
- I02607 `ruoyi-fastapi-frontend/src/store/modules/tagsView.js` lines 2-2 ImportDeclaration: 
  - 基线：源语句 sha256=88996687f5ac2ffe958aa6952515839565c6f908d46ea4106fe92135e3f788d7；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/tagsView.ts
- I02608 `ruoyi-fastapi-frontend/src/store/modules/tagsView.js` lines 4-4 VariableDeclaration: PERSIST_KEY
  - 基线：源语句 sha256=9bc4a9bbdaf72a0ead129e8b47f5b58b90976b501ff294b90ba4f40aecc6189d；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/tagsView.ts
- I02609 `ruoyi-fastapi-frontend/src/store/modules/tagsView.js` lines 6-8 FunctionDeclaration: isPersistEnabled
  - 基线：源语句 sha256=01dea49eaf6cbd7e6448cd9441215ab0029019e4b6d974ae6b3f9cae6c8e9c9d；保留返回、异常及 1 个分支，调用=useSettingsStore。
  - 去向：react-front/src/store/modules/tagsView.ts
- I02610 `ruoyi-fastapi-frontend/src/store/modules/tagsView.js` lines 10-14 FunctionDeclaration: saveVisitedViews
  - 基线：源语句 sha256=1533bb425dd0066e2f0858273748de689fb2cbd19208b3e622a83f60a45dcee4；保留返回、异常及 3 个分支，调用=isPersistEnabled, CallExpression.map, views.filter, cache.local.setJSON。
  - 去向：react-front/src/store/modules/tagsView.ts
- I02611 `ruoyi-fastapi-frontend/src/store/modules/tagsView.js` lines 16-18 FunctionDeclaration: loadVisitedViews
  - 基线：源语句 sha256=e06200d3f8e886bc23df745252c4e15f02200323c0ddcab6c3313884a347b2d8；保留返回、异常及 2 个分支，调用=cache.local.getJSON。
  - 去向：react-front/src/store/modules/tagsView.ts
- I02612 `ruoyi-fastapi-frontend/src/store/modules/tagsView.js` lines 20-22 FunctionDeclaration: clearVisitedViews
  - 基线：源语句 sha256=099c5db0d034d7aa6d6113ba195137fec4cc06e2129e1ec6e16b0aa20b7bdccb；保留返回、异常及 0 个分支，调用=cache.local.remove。
  - 去向：react-front/src/store/modules/tagsView.ts
- I02613 `ruoyi-fastapi-frontend/src/store/modules/tagsView.js` lines 24-224 VariableDeclaration: useTagsViewStore
  - 基线：源语句 sha256=2d30d3c5775cf9d191786ea3f21322693229da2f25b205cb1dfdca62ef0c3c81；保留返回、异常及 48 个分支，调用=defineStore, ThisExpression.addVisitedView, ThisExpression.addCachedView, ThisExpression.iframeViews.some, ThisExpression.iframeViews.push, Object.assign, ThisExpression.visitedViews.some, ThisExpression.visitedViews.push, saveVisitedViews, ThisExpression.visitedViews.unshift, ThisExpression.cachedViews.includes, ThisExpression.cachedViews.push, ThisExpression.delVisitedView, ThisExpression.delCachedView, resolve, ThisExpression.visitedViews.entries, ThisExpression.visitedViews.splice, ThisExpression.iframeViews.filter, ThisExpression.cachedViews.indexOf, ThisExpression.cachedViews.splice, ThisExpression.delOthersVisitedViews, ThisExpression.delOthersCachedViews, ThisExpression.visitedViews.filter, ThisExpression.cachedViews.slice, ThisExpression.delAllVisitedViews, ThisExpression.delAllCachedViews, clearVisitedViews, ThisExpression.visitedViews.findIndex, ThisExpression.iframeViews.findIndex, ThisExpression.iframeViews.splice, loadVisitedViews, views.forEach。
  - 去向：react-front/src/store/modules/tagsView.ts
- I02614 `ruoyi-fastapi-frontend/src/store/modules/tagsView.js` lines 226-226 ExportDefaultDeclaration: 
  - 基线：源语句 sha256=c865d345122f087361594fa0b82261b42a8b3c037168a82d28f075875f988763；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/tagsView.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
