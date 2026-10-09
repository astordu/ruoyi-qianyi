# G208 src/layout/components/TagsView/index.vue：状态、输入与依赖接口

依赖：G000, G207, G227, G228, G229, G250

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02247 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 69-69 ImportDeclaration: 
  - 基线：源语句 sha256=fab2d85968778d88deefb97af0aaba869edad8849f5efcdbce5947b3f1786a50；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02248 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 70-70 ImportDeclaration: 
  - 基线：源语句 sha256=8a7cf6589682c7c62a14023574b67d2639dd45e581c104ac2ed99db272c6d63e；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02249 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 71-71 ImportDeclaration: 
  - 基线：源语句 sha256=0e55dbc3aac4ad1d960b0ed9d1afe4a12b6fdebafcf121b5a290f88823abb0c4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02250 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 72-72 ImportDeclaration: 
  - 基线：源语句 sha256=88996687f5ac2ffe958aa6952515839565c6f908d46ea4106fe92135e3f788d7；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02251 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 73-73 ImportDeclaration: 
  - 基线：源语句 sha256=efbb342d84aefbc6dc4b206f290d81fe87a23b34796df1ad0da69cd6a90b7ea3；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02252 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 75-75 VariableDeclaration: visible
  - 基线：源语句 sha256=1e5831fe2e56f6cc177d5ecfd848b4a6a30d10008c0fed3fc9f2ab7bcf3c3453；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02253 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 76-76 VariableDeclaration: top
  - 基线：源语句 sha256=6b471557280fb61c357187ff94d5bc3f5a164c6a8d244faa25683c01c9c87acb；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02254 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 77-77 VariableDeclaration: left
  - 基线：源语句 sha256=a9c82d4a8333f8660e064ae21000307a31dfd43b7ac49a3f785d56bbc6ebdeba；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02255 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 78-78 VariableDeclaration: selectedTag
  - 基线：源语句 sha256=47c7fbb3a197d5146ebe8383cae4b300805893d574f637118afff9cb65effef9；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02256 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 79-79 VariableDeclaration: affixTags
  - 基线：源语句 sha256=05ffffb0c246d6555a2fa7c03a093522b06a2312c6936784b913c78a3dcc9e6e；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02257 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 80-80 VariableDeclaration: scrollPaneRef
  - 基线：源语句 sha256=672a323cbac5fb4a20448bdf42c3f7c210499dd24ba9f8c3772b8c24e2cc27aa；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02258 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 81-81 VariableDeclaration: canScrollLeft
  - 基线：源语句 sha256=ea24ae8a4e6a62bc00c9171a55410700bfe9a3a6dcca589a7adda5b746a49eba；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02259 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 82-82 VariableDeclaration: canScrollRight
  - 基线：源语句 sha256=71d895b9e6ab405c4db860041bfe122bca2c4fbee545acae69424166a3852b5a；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02260 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 83-83 VariableDeclaration: isFullscreen
  - 基线：源语句 sha256=a25c8f0f4bb97b2211ab309df60bc4fdadd14b5bee6cfad1d18c407859a29ee5；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02261 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 85-85 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02262 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 86-86 VariableDeclaration: route
  - 基线：源语句 sha256=19ffaf888604ba2654aa25f29ba0210e96226ea7089e9e15dc5c05cf276b3a9f；保留返回、异常及 0 个分支，调用=useRoute。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02263 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 87-87 VariableDeclaration: router
  - 基线：源语句 sha256=5921d8bbcfc7da27a18289d8a47cc51136866f8fdbebe22e9d1d1135aa55e0e6；保留返回、异常及 0 个分支，调用=useRouter。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02264 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 88-88 VariableDeclaration: settingsStore
  - 基线：源语句 sha256=53647c4c620ff8d612232f46d116eb0d1e39a2943e0b2af620b068ca8e6d3ba3；保留返回、异常及 0 个分支，调用=useSettingsStore。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02272 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 100-103 ExpressionStatement: 
  - 基线：源语句 sha256=0ea91d1b544d6ba364881d57e80d6e27c3e635a3bd7e6186b5dd8dc74be8a076；保留返回、异常及 0 个分支，调用=watch, addTags, moveToCurrentTag。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02273 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 104-110 ExpressionStatement: 
  - 基线：源语句 sha256=dacaa46df2d60f2a1ff21e8348a1cb88f786cfeda54f24f4548a0d8633344821；保留返回、异常及 1 个分支，调用=watch, document.body.addEventListener, document.body.removeEventListener。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02274 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 111-113 ExpressionStatement: 
  - 基线：源语句 sha256=a555098f97298676812df1679e5b5ff2fbf011dbb96b28f3adb792d237909087；保留返回、异常及 0 个分支，调用=watch, nextTick, updateArrowState。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02275 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 114-119 ExpressionStatement: 
  - 基线：源语句 sha256=d4c1c5ad2a19067d93fc118af484130fba3cf390e46d2ceea3e677dbb90e5fd9；保留返回、异常及 0 个分支，调用=onMounted, initTags, addTags, window.addEventListener, document.addEventListener。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts
- I02276 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` lines 120-123 ExpressionStatement: 
  - 基线：源语句 sha256=c4d67d44423062dd31077e152bffecb9c3291e0d7cc4816959a2d19f2710d789；保留返回、异常及 0 个分支，调用=onBeforeUnmount, window.removeEventListener, document.removeEventListener。
  - 去向：react-front/src/layout/components/TagsView/index.context.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
