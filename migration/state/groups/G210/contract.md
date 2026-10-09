# G210 src/layout/components/TopNav/index.vue：完整能力

依赖：G000, G187, G221, G224, G227, G228, G256

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02376 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 36-36 ImportDeclaration: 
  - 基线：源语句 sha256=3581ae5104050e3766caaf146add24c86f891d0274c9b17a861325b454bcb401；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02377 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 37-37 ImportDeclaration: 
  - 基线：源语句 sha256=453c099bdd3e4e4183e7854482e7cbba5941d26dee45c4e0ad469e4d3df55f02；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02378 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 38-38 ImportDeclaration: 
  - 基线：源语句 sha256=b6ad1bf6c41f923901306683414efcc226cc2299d4a2d3ca4208a8af934a00cf；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02379 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 39-39 ImportDeclaration: 
  - 基线：源语句 sha256=88996687f5ac2ffe958aa6952515839565c6f908d46ea4106fe92135e3f788d7；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02380 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 40-40 ImportDeclaration: 
  - 基线：源语句 sha256=efbb342d84aefbc6dc4b206f290d81fe87a23b34796df1ad0da69cd6a90b7ea3；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02381 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 43-43 VariableDeclaration: visibleNumber
  - 基线：源语句 sha256=c99e51c3fb4ed0b9a0c425eb36d7f5cb77c58fdcb145e5638b5775342fa4ecb4；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02382 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 45-45 VariableDeclaration: currentIndex
  - 基线：源语句 sha256=ca80cc3194e8f3ab425d2f41ad660b7f54e1138c2509c124b84d163181d2ff19；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02383 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 47-47 VariableDeclaration: hideList
  - 基线：源语句 sha256=7b985fdca44581cca8f8f8d09e08848078364dce8b0f4040a6adfd2ea8a37f82；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02384 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 49-49 VariableDeclaration: appStore
  - 基线：源语句 sha256=060bc36594e85646e5cc27ede11c88fb8230b9d84a9ac50cfd6e4bbef468bdf4；保留返回、异常及 0 个分支，调用=useAppStore。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02385 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 50-50 VariableDeclaration: settingsStore
  - 基线：源语句 sha256=53647c4c620ff8d612232f46d116eb0d1e39a2943e0b2af620b068ca8e6d3ba3；保留返回、异常及 0 个分支，调用=useSettingsStore。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02386 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 51-51 VariableDeclaration: permissionStore
  - 基线：源语句 sha256=8aea4ee78c3bc335fb25695e39a02e09a8551a4b638040cc30c3a575ef5ec2ed；保留返回、异常及 0 个分支，调用=usePermissionStore。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02387 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 52-52 VariableDeclaration: route
  - 基线：源语句 sha256=19ffaf888604ba2654aa25f29ba0210e96226ea7089e9e15dc5c05cf276b3a9f；保留返回、异常及 0 个分支，调用=useRoute。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02388 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 53-53 VariableDeclaration: router
  - 基线：源语句 sha256=5921d8bbcfc7da27a18289d8a47cc51136866f8fdbebe22e9d1d1135aa55e0e6；保留返回、异常及 0 个分支，调用=useRouter。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02389 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 56-56 VariableDeclaration: theme
  - 基线：源语句 sha256=4151e7b9b3773f9a424ce1f499b146b014780f6c8359f951b275d448f3633def；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02390 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 58-58 VariableDeclaration: routers
  - 基线：源语句 sha256=1675830cb6cd3bfbc19cc6491cf831d32dfff532764939da196d40f0a49a23b6；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02391 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 61-74 VariableDeclaration: topMenus
  - 基线：源语句 sha256=c859a02318e8df7503ac631b275dd0d532ec987e54436510dbb9a0cc41e6e48a；保留返回、异常及 4 个分支，调用=computed, routers.value.map, topMenus.push。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02392 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 77-95 VariableDeclaration: childrenMenus
  - 基线：源语句 sha256=5d9e35e72881d0ccfb8e8dc55450bc3185da01a6572f58fbec1c8f6cee5d29e9；保留返回、异常及 4 个分支，调用=computed, routers.value.map, isHttp, childrenMenus.push, constantRoutes.concat。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02393 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 98-113 VariableDeclaration: activeMenu
  - 基线：源语句 sha256=040ad63feda1245a64054ab089ddcb5227f557b31a92403e78b3edc10b1ccb9b；保留返回、异常及 6 个分支，调用=computed, path.lastIndexOf, hideList.indexOf, path.substring, tmpPath.substring, tmpPath.indexOf, appStore.toggleSideBarHide, activeRoutes。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02394 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 115-118 FunctionDeclaration: setVisibleNumber
  - 基线：源语句 sha256=cb85f0b8964155471cb86bf62714ec176dbbe3951f887ea9ed86269a4af1ff15；保留返回、异常及 0 个分支，调用=document.body.getBoundingClientRect, Math.max, parseInt。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02395 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 120-141 FunctionDeclaration: handleSelect
  - 基线：源语句 sha256=0ed2903cc11e027653f5bf40e9ecd415925710709b8a48632bdc0f5a0ab3f41a；保留返回、异常及 5 个分支，调用=routers.value.find, isHttp, window.open, childrenMenus.value.find, JSON.parse, router.push, appStore.toggleSideBarHide, activeRoutes。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02396 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 143-158 FunctionDeclaration: activeRoutes
  - 基线：源语句 sha256=9d933e4286b148f34ce0c13c65fc4576714c48f9b729a6e38fbbfa657c449bff；保留返回、异常及 7 个分支，调用=childrenMenus.value.map, routes.push, permissionStore.setSidebarRouters, appStore.toggleSideBarHide。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02397 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 160-162 ExpressionStatement: 
  - 基线：源语句 sha256=208dd854e6505deec512999551f1d177c4fe3b1a63732813465dade0fdfa9749；保留返回、异常及 0 个分支，调用=onMounted, window.addEventListener。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02398 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 164-166 ExpressionStatement: 
  - 基线：源语句 sha256=86f655b704f66dc5c7468ff7d1ecfd0ebc26f6082e6a0e51710c66b862e5977b；保留返回、异常及 0 个分支，调用=onBeforeUnmount, window.removeEventListener。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02399 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` lines 168-170 ExpressionStatement: 
  - 基线：源语句 sha256=1d86283e9aee0cdb71bd19f4c119ed85de74e7a23dd669ad4513a2661533e413；保留返回、异常及 0 个分支，调用=onMounted, setVisibleNumber。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02400 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template lines 1-33（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02401 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template line 3: v-bind:default-active
  - 基线：原表达式：activeMenu；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02402 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template line 5: v-on:select
  - 基线：原表达式：handleSelect；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02403 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template line 6: v-bind:ellipsis
  - 基线：原表达式：false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02404 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template line 8: v-for:
  - 基线：原表达式：(item, index) in topMenus；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02405 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template line 9: v-bind:style
  - 基线：原表达式：{'--theme': theme}；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02406 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template line 9: v-bind:index
  - 基线：原表达式：item.path；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02407 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template line 9: v-bind:key
  - 基线：原表达式：index；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02408 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template line 9: v-if:
  - 基线：原表达式：index < visibleNumber；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02409 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template line 11: v-if:
  - 基线：原表达式：item.meta && item.meta.icon && item.meta.icon !== '#'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02410 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template line 12: v-bind:icon-class
  - 基线：原表达式：item.meta.icon；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02411 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template line 18: v-bind:style
  - 基线：原表达式：{'--theme': theme}；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02412 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template line 18: v-if:
  - 基线：原表达式：topMenus.length > visibleNumber；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02413 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template line 19: v-slot:title
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02414 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template line 20: v-for:
  - 基线：原表达式：(item, index) in topMenus；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02415 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template line 22: v-bind:index
  - 基线：原表达式：item.path；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02416 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template line 23: v-bind:key
  - 基线：原表达式：index；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02417 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template line 24: v-if:
  - 基线：原表达式：index >= visibleNumber；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02418 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template line 26: v-if:
  - 基线：原表达式：item.meta && item.meta.icon && item.meta.icon !== '#'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02419 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template line 27: v-bind:icon-class
  - 基线：原表达式：item.meta.icon；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02420 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template interpolation line 13
  - 基线：原显示表达式：item.meta.title
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02421 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` template interpolation line 28
  - 基线：原显示表达式：item.meta.title
  - 去向：react-front/src/layout/components/TopNav/index.tsx
- I02422 `ruoyi-fastapi-frontend/src/layout/components/TopNav/index.vue` style[0] lines 173-220
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=False；原样式选择器在 source-audit.json。
  - 去向：react-front/src/layout/components/TopNav/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
