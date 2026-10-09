# G021 plugins/ai/views/chat/index.vue：状态、输入与依赖接口

依赖：G000, G018, G019, G020, G231

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00126 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 414-414 ImportDeclaration: 
  - 基线：源语句 sha256=a5b384feb5660fd7b1dcb475bf4012af11c1420d5b133d61ea3bb25759c94ff5；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00127 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 415-422 ImportDeclaration: 
  - 基线：源语句 sha256=a585e36c1ce2059e920a1c7307353373fe833797fb47961b9f08924472212816；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00128 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 423-423 ImportDeclaration: 
  - 基线：源语句 sha256=7e557e7755cde2bc76ecec008e45301b1ef2a9b9385fd232bf80b291853fe1eb；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00129 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 424-424 ImportDeclaration: 
  - 基线：源语句 sha256=c2c77f62057b3106067427803bcfe1be395281c78aa84cf5376cf31490c6c24d；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00130 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 425-425 ImportDeclaration: 
  - 基线：源语句 sha256=5da3db75d2343c8616120220cbb52b81c90a30c307680a1559d325b8ba4d19c8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00131 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 426-426 ImportDeclaration: 
  - 基线：源语句 sha256=d990b534141f37b30970fd7dd9d20561b1aca617adffc08b2c6f81ba7c9d2e8d；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00132 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 427-427 ImportDeclaration: 
  - 基线：源语句 sha256=d7d70690dba542f38d6706ed44b133c2004c27a01a1bdf8a9dd20677e0bf7f87；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00133 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 428-428 ImportDeclaration: 
  - 基线：源语句 sha256=300ebd7bf9d5171da359c950dd86b1ddd72b727798c0fc528995d7167e50ae61；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00134 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 430-430 ExpressionStatement: 
  - 基线：源语句 sha256=7ac269382d69de9ebf9f318b21d598949c83da4e13c255e03f8acef60e274129；保留返回、异常及 0 个分支，调用=getUseMonaco。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00135 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 432-432 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00136 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 434-434 VariableDeclaration: modelOptions
  - 基线：源语句 sha256=2394f3dd942abef4bc1cda2a76d4b725846832d5e2e9d3fa0b912192f7165ce1；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00137 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 435-435 VariableDeclaration: currentModelId
  - 基线：源语句 sha256=927aa2245bda162aa610a92ea289156a3a97e8018a22b4a64c910341898bd0d4；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00138 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 436-436 VariableDeclaration: messageList
  - 基线：源语句 sha256=4054ced1998d5fca47381c6248184406cf9a126c9ad35c27945949d142f8906d；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00139 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 437-437 VariableDeclaration: inputMessage
  - 基线：源语句 sha256=780ad48d0b73b0c58247d7c0c2ba0f48090aa1e5771bb570e92dbb24fdeebf3e；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00140 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 438-438 VariableDeclaration: inputImages
  - 基线：源语句 sha256=227d5fba6cbb6ea14aa6090cf985f1b3c8aed5570626af9d6555a2a3c61f51b4；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00141 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 439-439 VariableDeclaration: loading
  - 基线：源语句 sha256=0f2d86fe0699597a69087a478d5543264e008a02dbd9826dd2138c7409858393；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00142 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 440-440 VariableDeclaration: chatHistoryRef
  - 基线：源语句 sha256=1c452b847560dca02003868a5bc457d7fa63654593b52c9c818d79bff5847f1e；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00143 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 441-441 VariableDeclaration: chatContentRef
  - 基线：源语句 sha256=4218d037521cb03c75a8e94e535acc10f5b0bb7634f61cc68d414d42852351bb；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00144 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 442-442 VariableDeclaration: currentSessionId
  - 基线：源语句 sha256=5744b35d90d894bde480f5e1a03d93d7fa9f198402d0711dc13d5fc8c7876d0e；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00145 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 443-443 VariableDeclaration: showConfigDialog
  - 基线：源语句 sha256=ac72535b2ab18999239aaaff6c8ec7382b427060223d2755222327d0d04076e5；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00146 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 444-444 VariableDeclaration: imageInputRef
  - 基线：源语句 sha256=5b97642d633a3de912aa68e0b24a61c94e86b25b39d0c09d1304ee58d9e6e0b9；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00147 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 445-445 VariableDeclaration: sessionList
  - 基线：源语句 sha256=9dda3c7194d9beaa2fdd480e72562f2d0ed7603cddd98dfa7f1cfbd385b569e7；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00148 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 446-446 VariableDeclaration: sessionLoading
  - 基线：源语句 sha256=59ec5f2bbfe121e961e0fab4ceeb452642d05d414ec6a104ac77f15562713f29；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00149 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 447-447 VariableDeclaration: abortController
  - 基线：源语句 sha256=19f67f346b48a612ce78b1643972ee1bf860bc157346c9c6323e01f31806b9fb；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00150 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 448-448 VariableDeclaration: currentRunId
  - 基线：源语句 sha256=6c6aa65f5bad667769fa77bf1e8f61e1c17d0d6691fedb9165d6b14110e19bf1；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00151 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 449-449 VariableDeclaration: isAutoScroll
  - 基线：源语句 sha256=f115ece2af4c901ce3061a39e0cba88e70f9a2a7eb9ec3bcda8d33cb727105c4；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00152 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 450-450 VariableDeclaration: currentSessionAgentData
  - 基线：源语句 sha256=173acc6c8333442f6343cd4b94e8357e73aa8e8f61849aa18d37aa7da55c0dd6；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00153 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 451-451 VariableDeclaration: isProgrammaticScroll
  - 基线：源语句 sha256=08cb86a6bd377f2d455dcf3d38864be609c6deba547a04a8123966b9d3e22309；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00154 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 452-452 VariableDeclaration: scrollTimeout
  - 基线：源语句 sha256=17fbd912172bf50b6d6232f8aef770d9e22b53deae28da7a4a66653f8551cfcb；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00156 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 458-461 VariableDeclaration: chatConfig
  - 基线：源语句 sha256=451358b3e24b37f51ebd5109bf4dcb83551ff0c678b060373ad10fcb5bfb557b；保留返回、异常及 0 个分支，调用=reactive。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00157 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 463-475 VariableDeclaration: userConfig
  - 基线：源语句 sha256=bd6082df06c6d6566b2d50538fe4d0058f2ad78d432fa6b5dfbbdd2014b16e6b；保留返回、异常及 0 个分支，调用=reactive。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00158 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 477-489 VariableDeclaration: editingUserConfig
  - 基线：源语句 sha256=fa872a6a89e8a121cd3d5894636242ccf2466bfa45a0e8384315a396ed8afe0b；保留返回、异常及 0 个分支，调用=reactive。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00167 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 566-571 ExpressionStatement: 
  - 基线：源语句 sha256=eb8cd46f99236b0b99c8d4c1f04a9120b83bd9c8ac77fdb04f12df5841861ef2；保留返回、异常及 1 个分支，调用=watch, modelOptions.value.find。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00181 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 889-893 ExpressionStatement: 
  - 基线：源语句 sha256=3b0ffd3e8976f8653a4bd36d5211c5a5aec55c636c75ffd80556b7d3fcf4e831；保留返回、异常及 1 个分支，调用=useResizeObserver, scrollToBottom。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts
- I00182 `ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue` lines 895-899 ExpressionStatement: 
  - 基线：源语句 sha256=9de716cd357fd4a5fe1d3fcde775878535e2a8873c11f180965dae718e4fa014；保留返回、异常及 0 个分支，调用=onMounted, getModels, getSessions, loadUserConfig。
  - 去向：react-front/plugins/ai/views/chat/index.context.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
