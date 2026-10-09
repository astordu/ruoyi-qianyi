# G286 src/views/system/file/components/FileReconcileDrawer.vue：状态、输入与依赖接口

依赖：G000, G039, G294

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I05044 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 361-367 ImportDeclaration: 
  - 基线：源语句 sha256=577dac727ca424cf29a764c92eaf6f1467cbbe9a4fe4411c820b4f93367eb29c；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05045 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 368-368 ImportDeclaration: 
  - 基线：源语句 sha256=87fb0cfcdb7f5235aec4af3e73d3d63d1c863744216f1de5bb59af890dd52fdb；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05046 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 370-370 VariableDeclaration: emit
  - 基线：源语句 sha256=000f8803e150d60c6d770de50ab5bdb69c7c7599de94c475abb3a63c89abf22c；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05047 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 371-371 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05048 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 372-372 VariableDeclaration: visible
  - 基线：源语句 sha256=1e5831fe2e56f6cc177d5ecfd848b4a6a30d10008c0fed3fc9f2ab7bcf3c3453；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05049 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 373-373 VariableDeclaration: activeTab
  - 基线：源语句 sha256=1fdbffab6997d97fc3443be387b17e48dc071d372b49e67c52fd839fa73370cc；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05050 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 374-374 VariableDeclaration: issueLoading
  - 基线：源语句 sha256=0ffafc6679f7f873f5e6f45615a123019bcdb689f3ae4b2c674e43eedaafdc60；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05051 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 375-375 VariableDeclaration: runLoading
  - 基线：源语句 sha256=da6ebdc46f0bd56a163edefe8933b7890baaaadad1567eac82fc1c8851443379；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05052 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 376-376 VariableDeclaration: scanning
  - 基线：源语句 sha256=8a64ceb75636e741a8e179a8c651785c58944136b787225218b40eea49c9a284；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05053 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 377-377 VariableDeclaration: handling
  - 基线：源语句 sha256=24012e657b81b7060ac46a5f63a95595d4e912aed6230b840d30b6d4e959d63d；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05054 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 378-378 VariableDeclaration: checkHash
  - 基线：源语句 sha256=31597c1269b3be690e8676043729edebab98d9804c8d682d0158ebd35974e9b0；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05055 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 379-379 VariableDeclaration: issueList
  - 基线：源语句 sha256=2d58c5d27566e0dd9d958b093959c11d5b8b4a2cca3c7b0aed18b13dda5fe6f8；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05056 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 380-380 VariableDeclaration: runList
  - 基线：源语句 sha256=6abf37ec6695e4cd7acd50604ef764ce17b26f31cd9240d9d5a156aec7fa828f；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05057 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 381-381 VariableDeclaration: issueTotal
  - 基线：源语句 sha256=6ee73143cd8b2b80480d86cb793f0a3ee215fbb5bf04339926e5db969ac24a66；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05058 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 382-382 VariableDeclaration: runTotal
  - 基线：源语句 sha256=54469ee7b3df890595afdeb349a02cb6f622d3cd3626ea3b97f3dbf8bcf8aee7；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05059 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 383-383 VariableDeclaration: issueQueryRef
  - 基线：源语句 sha256=1a55a2e8f44015b84bec0d82f5160905813808b6f4abf775222e735109c11fac；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05060 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 384-384 VariableDeclaration: handleFormRef
  - 基线：源语句 sha256=bff2fd4111bfb7632434dcbc6bd0360b63287d939de89f0b9d844d131ba1d45f；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05061 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 385-385 VariableDeclaration: handleOpen
  - 基线：源语句 sha256=99e85851638ad253d4a0af9dec8faccdb0dc7728fdb5f77cfd622f228ea95ea0；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05062 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 386-386 VariableDeclaration: currentIssueId
  - 基线：源语句 sha256=9208756c022803db0b4916f94b147a05e0b9d12984d9a21ff9bd790a14f8a3dc；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05063 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 387-387 VariableDeclaration: pollTimer
  - 基线：源语句 sha256=6db807ea2b9aa453d66cdc312bc8f5b58d9b5d0a260d782a823e33d3b6af269a；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05064 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 389-396 VariableDeclaration: stats
  - 基线：源语句 sha256=65a13575be499ddf083d89c6e6b3d96bb0dcc3a22df70008bb1e5e6c6a281fb2；保留返回、异常及 0 个分支，调用=reactive。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05065 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 397-404 VariableDeclaration: issueQuery
  - 基线：源语句 sha256=4dfab4d0c2e95572dec55c5039d5058b4536022a985d4edb51107b989531a9fa；保留返回、异常及 0 个分支，调用=reactive。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05066 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 405-408 VariableDeclaration: runQuery
  - 基线：源语句 sha256=ad2c1fc177cd277d71c8539e1a1325337bdd6ccd7c63fcc48986973c3f0a78ec；保留返回、异常及 0 个分支，调用=reactive。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05067 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 409-413 VariableDeclaration: handleForm
  - 基线：源语句 sha256=7aa67e162070efa69f8f54eed550540b2459713b71c15b50ea00390861c8a512；保留返回、异常及 0 个分支，调用=reactive。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05068 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 414-428 VariableDeclaration: handleRules
  - 基线：源语句 sha256=7a88a6eaf0ad8e59b71816b4530b7115ad06f396c57e4c4a6e5cc0bb8cdd9c4a；保留返回、异常及 3 个分支，调用=callback。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05069 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 429-440 VariableDeclaration: issueTypeOptions
  - 基线：源语句 sha256=87e064033a52c6003a3b574168086b0b29f24ef6894c4d01bba16c0cb6ae66f3；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05070 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 441-445 VariableDeclaration: dangerousActions
  - 基线：源语句 sha256=97f729c3c7ad2abaf570eaae314d01363a44339034eceeabb1e9be9cfd45bacd；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05071 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 446-457 VariableDeclaration: actionDescriptions
  - 基线：源语句 sha256=c80e523e0560bb58669021502ddd8c2c4b420875c5c5ff8f95505a3c4fc25008；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05095 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 650-650 ExpressionStatement: 
  - 基线：源语句 sha256=c03d14766f679596998c0c6b1214917183872df8684efca8372fb8353b155a0d；保留返回、异常及 0 个分支，调用=onBeforeUnmount, clearInterval。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts
- I05096 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue` lines 652-652 ExpressionStatement: 
  - 基线：源语句 sha256=2e56640d2586072b42b8ea1f2cbd05f1d669da4f3e9e5617eb50a334cf1e3d67；保留返回、异常及 0 个分支，调用=defineExpose。
  - 去向：react-front/src/views/system/file/components/FileReconcileDrawer.context.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
