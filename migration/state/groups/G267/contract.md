# G267 src/views/monitor/job/index.vue：状态、输入与依赖接口

依赖：G000, G028, G162, G179, G230, G232, G243, G246, G250, G266, G269

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I03360 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 311-311 ImportDeclaration: 
  - 基线：源语句 sha256=183eda20473d05ad89f987e31d1c2fe3555edc724db02e113f69d08ec5a01ec4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03361 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 312-312 ImportDeclaration: 
  - 基线：源语句 sha256=bc9badff35f5f48e4bf982c9fd8dad330f971871307c0a26c2f87406df34b1a5；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03362 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 313-313 ImportDeclaration: 
  - 基线：源语句 sha256=29461ff5fd35dc5c22f1ec35c0b7ff77be0ddb46fec5cfecfa36472fbe9749e5；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03363 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 314-314 ImportDeclaration: 
  - 基线：源语句 sha256=33d87f443487d246811f35cc8911ac7f07b772f3631610de0cbd0321fbf10fed；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03364 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 315-315 ImportDeclaration: 
  - 基线：源语句 sha256=ee2d9f8dee8eddbf43a452b8931d3d6f270b4f2d5ad0574a6a9598e2c3963989；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03365 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 316-316 ImportDeclaration: 
  - 基线：源语句 sha256=152ff74004dfe6cb3e92c3962da6e35977b61b6ac75a851a42e723078f547eab；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03366 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 317-317 ImportDeclaration: 
  - 基线：源语句 sha256=0d60c3a020c001f8bea6b247fa331badaafb626ed9be2b63394d8c4aa81f83b5；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03367 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 318-318 ImportDeclaration: 
  - 基线：源语句 sha256=c351978f324903ca33541ef37b2b07118aae76a82edaab040cb71996f923341f；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03368 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 320-320 VariableDeclaration: router
  - 基线：源语句 sha256=5921d8bbcfc7da27a18289d8a47cc51136866f8fdbebe22e9d1d1135aa55e0e6；保留返回、异常及 0 个分支，调用=useRouter。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03369 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 321-321 VariableDeclaration: userStore
  - 基线：源语句 sha256=21eb42d5aa135e6ffd33998f9b7f8924e85e1259d2572f4a34415ca53d396344；保留返回、异常及 0 个分支，调用=useUserStore。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03370 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 322-322 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03371 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 323-323 VariableDeclaration: 
  - 基线：源语句 sha256=a52c55e482f7d740576aa1bb0a0153fd14c7ee416c3a1e6c603939c49f9f8287；保留返回、异常及 0 个分支，调用=proxy.useDict。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03372 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 325-325 VariableDeclaration: jobList
  - 基线：源语句 sha256=c2182acb35899eb4c8827757dbc2cb6e73fe7ec91f2bc04ee469f7e0c6ce4d23；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03373 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 326-326 VariableDeclaration: open
  - 基线：源语句 sha256=a542e4df0517d4fd7db7dda3114abbaf21c848158a19f33261b636975b69e307；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03374 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 327-327 VariableDeclaration: loading
  - 基线：源语句 sha256=c6d283c2f3ea7c9a46a2b20e0ef90bfcf6ffbde99656d9a424ad43f7d28f2aba；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03375 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 328-328 VariableDeclaration: showSearch
  - 基线：源语句 sha256=484353ab3c6f747541b20072d8cc3a9816d7c60d7a687326a0ab4d6700d69e17；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03376 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 329-329 VariableDeclaration: ids
  - 基线：源语句 sha256=470784de1db68be78831742511d0069dcbb9f19878d3ca4a6d5a2ad0370b79f0；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03377 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 330-330 VariableDeclaration: single
  - 基线：源语句 sha256=d8b92433028a1ee7912903c3a8cf52435102e8d5f5c98809c169ecda5a0c1d2a；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03378 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 331-331 VariableDeclaration: multiple
  - 基线：源语句 sha256=1e95758ba50bec4821d45483dad55ab07195518d0ab2626c714ec7b128480ffc；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03379 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 332-332 VariableDeclaration: total
  - 基线：源语句 sha256=3ea22b280c119d04a2e23fb7967b98534357cc6c46eb2621b3817c605f822958；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03380 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 333-333 VariableDeclaration: title
  - 基线：源语句 sha256=6452e9e4e944a2ca0aaab11c2229fadd77c42d71c76662caecb1fe68378567dd；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03381 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 334-334 VariableDeclaration: openView
  - 基线：源语句 sha256=74ecfb2ee72d98c88b2a47143ae1177aeb9a9736f277d07f55f19f93d848c93b；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03382 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 335-335 VariableDeclaration: openCron
  - 基线：源语句 sha256=8f228f864ceddb89a262fcea4a785e694069b22be7b0194a81ebb999330196ee；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03383 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 336-336 VariableDeclaration: expression
  - 基线：源语句 sha256=94b2bc2f79960df1117b7a65e81923b06e2eaac15f77686710971bea0c2ff2ad；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03384 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 337-337 VariableDeclaration: submitting
  - 基线：源语句 sha256=a34593ddd3f7624e09cce0d11047ff1f08df09e7c8286c2ed9433e777da0f101；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03385 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 338-338 VariableDeclaration: changingIds
  - 基线：源语句 sha256=749bd388ea8c5ea3cc40ede0340d9d68aa564bf7f8a3e91b3823b30c4864a2b7；保留返回、异常及 0 个分支，调用=reactive。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03386 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 339-339 VariableDeclaration: runningIds
  - 基线：源语句 sha256=ad44dc69540b40a42f8ce87fd2b47ace289113acc228b8107d28712b89396da9；保留返回、异常及 0 个分支，调用=reactive。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03387 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 340-340 VariableDeclaration: runtimeOpen
  - 基线：源语句 sha256=dc84c2600a222320cda09e882f6df5c007718bb4690636f101be2909abe4f26c；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03388 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 341-341 VariableDeclaration: runtimeContext
  - 基线：源语句 sha256=338629faca201b8ef54c7ef404d4c45db307bc9fba433b57661366a1459a6ef6；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03390 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 343-343 VariableDeclaration: syncRefreshTimer
  - 基线：源语句 sha256=7434993a08d8c6b6205e0ebf93b9181da88373d8118940b044db0bd810e18ac8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03391 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 344-344 VariableDeclaration: listController
  - 基线：源语句 sha256=860573d30123a60ac94a97082bbd4c6f0d949ef9b641181df6e50ebd64f7259e；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03392 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 345-345 VariableDeclaration: listVersion
  - 基线：源语句 sha256=132304c2ab86d65d84ce665600c4597f57ce94c0f6c6b137877be6d023ddcc47；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03393 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 346-346 VariableDeclaration: pageActive
  - 基线：源语句 sha256=487ed9c8661e3ed0ffbb1a1bde9fcea15dd39d153fb47ba6aef5727dfd8abdf6；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03394 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 347-349 VariableDeclaration: timeZoneOptions
  - 基线：源语句 sha256=80aa99af4f06c323ac4b95f65510792238c7bda535e1aaf5613cd291092d08e0；保留返回、异常及 1 个分支，调用=Intl.supportedValuesOf。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03397 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 367-388 VariableDeclaration: data
  - 基线：源语句 sha256=bce101a474a54815c6e640894ba511d6b8ad7b86f75e910283a2f11d5b0edb25；保留返回、异常及 0 个分支，调用=reactive。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03398 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 390-390 VariableDeclaration: 
  - 基线：源语句 sha256=1302c7f6c9f01c8414a694cd88e708a5a66cf40450bbd6957204a754bd0d4050；保留返回、异常及 0 个分支，调用=toRefs。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03399 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 391-396 VariableDeclaration: unlimitedDelay
  - 基线：源语句 sha256=2380d4375c48f7057e436effed01b312d7e736e35a33c2fdb2a5b9a45a01637c；保留返回、异常及 1 个分支，调用=computed。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03421 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 600-600 ExpressionStatement: 
  - 基线：源语句 sha256=792c39b2734765318409256a63d6f119847649d42fd5b3a04652bf708c379f56；保留返回、异常及 0 个分支，调用=onMounted, document.addEventListener。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03422 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 601-606 ExpressionStatement: 
  - 基线：源语句 sha256=77b153ba8dbebb64aac9b68075c73300824cfe9287fbe45fff462b666d61cf3d；保留返回、异常及 1 个分支，调用=onActivated, getList。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03423 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 607-610 ExpressionStatement: 
  - 基线：源语句 sha256=9d0fdc43dc4403ba894fbe28013221e1de7d26a349a588f2cf46892b0b62f8e3；保留返回、异常及 0 个分支，调用=onDeactivated, stopListRefresh。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03424 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 611-615 ExpressionStatement: 
  - 基线：源语句 sha256=62eeddd978a2de01b0349d7d1fd72e00676bbffcd796dca800d06ca8565ba8ea；保留返回、异常及 0 个分支，调用=onBeforeUnmount, stopListRefresh, document.removeEventListener。
  - 去向：react-front/src/views/monitor/job/index.context.ts
- I03425 `ruoyi-fastapi-frontend/src/views/monitor/job/index.vue` lines 616-616 ExpressionStatement: 
  - 基线：源语句 sha256=e966d3b08f869f7c7962cc988172bf8bc4840aa64d83fa58b0a15b31a76e4d3d；保留返回、异常及 0 个分支，调用=getList。
  - 去向：react-front/src/views/monitor/job/index.context.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
