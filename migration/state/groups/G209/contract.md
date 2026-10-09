# G209 src/layout/components/TopBar/index.vue：完整能力

依赖：G000, G205, G224, G227, G228

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02342 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` lines 15-15 ImportDeclaration: 
  - 基线：源语句 sha256=72fbadf261d17dd8128dd0ef0db2ff87f8e0d9b66fedb2022c4eb1f1bae36108；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02343 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` lines 16-16 ImportDeclaration: 
  - 基线：源语句 sha256=b6ad1bf6c41f923901306683414efcc226cc2299d4a2d3ca4208a8af934a00cf；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02344 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` lines 17-17 ImportDeclaration: 
  - 基线：源语句 sha256=88996687f5ac2ffe958aa6952515839565c6f908d46ea4106fe92135e3f788d7；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02345 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` lines 18-18 ImportDeclaration: 
  - 基线：源语句 sha256=efbb342d84aefbc6dc4b206f290d81fe87a23b34796df1ad0da69cd6a90b7ea3；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02346 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` lines 20-20 VariableDeclaration: route
  - 基线：源语句 sha256=4d0e93888827dba310f5cf48815c617b23da1a2eb2ff3690209994f3b8c71ff7；保留返回、异常及 0 个分支，调用=useRoute。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02347 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` lines 21-21 VariableDeclaration: appStore
  - 基线：源语句 sha256=060bc36594e85646e5cc27ede11c88fb8230b9d84a9ac50cfd6e4bbef468bdf4；保留返回、异常及 0 个分支，调用=useAppStore。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02348 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` lines 22-22 VariableDeclaration: settingsStore
  - 基线：源语句 sha256=53647c4c620ff8d612232f46d116eb0d1e39a2943e0b2af620b068ca8e6d3ba3；保留返回、异常及 0 个分支，调用=useSettingsStore。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02349 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` lines 23-23 VariableDeclaration: permissionStore
  - 基线：源语句 sha256=8aea4ee78c3bc335fb25695e39a02e09a8551a4b638040cc30c3a575ef5ec2ed；保留返回、异常及 0 个分支，调用=usePermissionStore。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02350 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` lines 25-25 VariableDeclaration: sidebarRouters
  - 基线：源语句 sha256=24d77cdfbc48ab559cb99a36e97837ea0fd9f2f5dcc1d02228998593001cf175；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02351 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` lines 26-26 VariableDeclaration: theme
  - 基线：源语句 sha256=576f9e83791f266ad7c3a6a7bc2c3897c331f5e14043131b95e08fb5e6d5ef7a；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02352 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` lines 27-27 VariableDeclaration: device
  - 基线：源语句 sha256=d8adce4edffffb0fd8e9f363ca1fe21ff638f3387bda57f570ae11a5e3fa24d6；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02353 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` lines 28-34 VariableDeclaration: activeMenu
  - 基线：源语句 sha256=fcdf7284c20e5d8c4fcd66a5ff0178e005a11c95f44686514d0af38bc7e5f22b；保留返回、异常及 3 个分支，调用=computed。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02354 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` lines 36-36 VariableDeclaration: visibleNumber
  - 基线：源语句 sha256=07b31f5733be8e3f53b7dfa3585a39cb0c4726f4b3be87a3fbd13c42c748bcb2；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02355 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` lines 37-39 VariableDeclaration: topMenus
  - 基线：源语句 sha256=b46dccbf67a58780303fb6ca009e261d7b65b40cd03c8f9589bb2ff641b3e075；保留返回、异常及 1 个分支，调用=computed, CallExpression.slice, permissionStore.sidebarRouters.filter。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02356 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` lines 40-42 VariableDeclaration: moreRoutes
  - 基线：源语句 sha256=423cba2970c2f5eaaef195b14ce85dfff297d9f6de037b4a4849c9d14a9a44b3；保留返回、异常及 1 个分支，调用=computed, CallExpression.slice, permissionStore.sidebarRouters.filter。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02357 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` lines 43-46 FunctionDeclaration: setVisibleNumber
  - 基线：源语句 sha256=921caff3ad839f8fa8ec2ee5e1b86c811a42853f1bd30c6ba92afd090a45f7ac；保留返回、异常及 0 个分支，调用=document.body.getBoundingClientRect, Math.max, parseInt。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02358 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` lines 48-50 ExpressionStatement: 
  - 基线：源语句 sha256=208dd854e6505deec512999551f1d177c4fe3b1a63732813465dade0fdfa9749；保留返回、异常及 0 个分支，调用=onMounted, window.addEventListener。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02359 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` lines 51-53 ExpressionStatement: 
  - 基线：源语句 sha256=86f655b704f66dc5c7468ff7d1ecfd0ebc26f6082e6a0e51710c66b862e5977b；保留返回、异常及 0 个分支，调用=onBeforeUnmount, window.removeEventListener。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02360 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` lines 55-57 ExpressionStatement: 
  - 基线：源语句 sha256=1d86283e9aee0cdb71bd19f4c119ed85de74e7a23dd669ad4513a2661533e413；保留返回、异常及 0 个分支，调用=onMounted, setVisibleNumber。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02361 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` template lines 1-12（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02362 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` template line 2: v-bind:ellipsis
  - 基线：原表达式：false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02363 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` template line 2: v-bind:default-active
  - 基线：原表达式：activeMenu；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02364 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` template line 2: v-bind:active-text-color
  - 基线：原表达式：theme；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02365 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` template line 3: v-bind:key
  - 基线：原表达式：route.path + index；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02366 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` template line 3: v-for:
  - 基线：原表达式：(route, index) in topMenus；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02367 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` template line 3: v-bind:item
  - 基线：原表达式：route；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02368 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` template line 3: v-bind:base-path
  - 基线：原表达式：route.path；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02369 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` template line 5: v-if:
  - 基线：原表达式：moreRoutes.length > 0；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02370 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` template line 6: v-slot:title
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02371 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` template line 9: v-bind:key
  - 基线：原表达式：route.path + index；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02372 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` template line 9: v-for:
  - 基线：原表达式：(route, index) in moreRoutes；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02373 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` template line 9: v-bind:item
  - 基线：原表达式：route；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02374 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` template line 9: v-bind:base-path
  - 基线：原表达式：route.path；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TopBar/index.tsx
- I02375 `ruoyi-fastapi-frontend/src/layout/components/TopBar/index.vue` style[0] lines 60-99
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=False；原样式选择器在 source-audit.json。
  - 去向：react-front/src/layout/components/TopBar/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
