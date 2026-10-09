# G212 src/layout/index.vue：完整能力

依赖：G000, G206, G211, G224, G228

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02427 `ruoyi-fastapi-frontend/src/layout/index.vue` lines 17-17 ImportDeclaration: 
  - 基线：源语句 sha256=8144aca8d44d1e808db28163823bf7d1b407e7a9db59fde14ba53fe0d8621a91；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/index.tsx
- I02428 `ruoyi-fastapi-frontend/src/layout/index.vue` lines 18-18 ImportDeclaration: 
  - 基线：源语句 sha256=4820524430a1350eb3a42f11c7e063ad7ba12ae164b753a3ff7666ca0ef6a27a；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/index.tsx
- I02429 `ruoyi-fastapi-frontend/src/layout/index.vue` lines 19-19 ImportDeclaration: 
  - 基线：源语句 sha256=5b56bcd6d03c44bb9653e89f7c7f206faf7fd8dd1b09612545019db0fced4bd5；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/index.tsx
- I02430 `ruoyi-fastapi-frontend/src/layout/index.vue` lines 20-20 ImportDeclaration: 
  - 基线：源语句 sha256=b6ad1bf6c41f923901306683414efcc226cc2299d4a2d3ca4208a8af934a00cf；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/index.tsx
- I02431 `ruoyi-fastapi-frontend/src/layout/index.vue` lines 21-21 ImportDeclaration: 
  - 基线：源语句 sha256=88996687f5ac2ffe958aa6952515839565c6f908d46ea4106fe92135e3f788d7；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/index.tsx
- I02432 `ruoyi-fastapi-frontend/src/layout/index.vue` lines 23-23 VariableDeclaration: settingsStore
  - 基线：源语句 sha256=53647c4c620ff8d612232f46d116eb0d1e39a2943e0b2af620b068ca8e6d3ba3；保留返回、异常及 0 个分支，调用=useSettingsStore。
  - 去向：react-front/src/layout/index.tsx
- I02433 `ruoyi-fastapi-frontend/src/layout/index.vue` lines 24-24 VariableDeclaration: theme
  - 基线：源语句 sha256=4151e7b9b3773f9a424ce1f499b146b014780f6c8359f951b275d448f3633def；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/layout/index.tsx
- I02434 `ruoyi-fastapi-frontend/src/layout/index.vue` lines 25-25 VariableDeclaration: sidebar
  - 基线：源语句 sha256=7c33c26983e077bbb86d4d063d417a93b9aaeb93ad0d9360c3de8b0955570a93；保留返回、异常及 0 个分支，调用=computed, useAppStore。
  - 去向：react-front/src/layout/index.tsx
- I02435 `ruoyi-fastapi-frontend/src/layout/index.vue` lines 26-26 VariableDeclaration: device
  - 基线：源语句 sha256=44edfe0c696eea2d6f37e4127f6f4e82b8043665197b0970ca25218626304f6c；保留返回、异常及 0 个分支，调用=computed, useAppStore。
  - 去向：react-front/src/layout/index.tsx
- I02436 `ruoyi-fastapi-frontend/src/layout/index.vue` lines 27-27 VariableDeclaration: needTagsView
  - 基线：源语句 sha256=36bfedc5faa98397727f6016fad74ea42fad1102374de58f6f354ce12c5a9f74；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/layout/index.tsx
- I02437 `ruoyi-fastapi-frontend/src/layout/index.vue` lines 28-28 VariableDeclaration: fixedHeader
  - 基线：源语句 sha256=b72485ac1b311795b8810ef6191794bed2d0252745cd675f2610c279e2ab606b；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/layout/index.tsx
- I02438 `ruoyi-fastapi-frontend/src/layout/index.vue` lines 30-35 VariableDeclaration: classObj
  - 基线：源语句 sha256=9454bba94f8c49624338e11eb6cea4fb376a708249444a1c28c282b68e6a3251；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/layout/index.tsx
- I02439 `ruoyi-fastapi-frontend/src/layout/index.vue` lines 37-37 VariableDeclaration: 
  - 基线：源语句 sha256=f463d65cee9cb7d34bf0938bd9c84e85fe7835c576672b3c1d2f5a56583d2069；保留返回、异常及 0 个分支，调用=useWindowSize。
  - 去向：react-front/src/layout/index.tsx
- I02440 `ruoyi-fastapi-frontend/src/layout/index.vue` lines 38-38 VariableDeclaration: WIDTH
  - 基线：源语句 sha256=c88345d5123bfe4f37230e83e9e17f3ab1831c2c4e741ae1d72f7262a3c24cf7；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/index.tsx
- I02441 `ruoyi-fastapi-frontend/src/layout/index.vue` lines 40-44 ExpressionStatement: 
  - 基线：源语句 sha256=d755e1a3c1e5b90188acecc7017d8e3898935474da7b2877fce94ff7d315a425；保留返回、异常及 2 个分支，调用=watch, CallExpression.closeSideBar, useAppStore。
  - 去向：react-front/src/layout/index.tsx
- I02442 `ruoyi-fastapi-frontend/src/layout/index.vue` lines 46-53 ExpressionStatement: 
  - 基线：源语句 sha256=969253c3bbd6650bffaec88e6f41ac5b0d5bf5af5031d3c3f9dff585e4ff24c1；保留返回、异常及 1 个分支，调用=watchEffect, CallExpression.toggleDevice, useAppStore, CallExpression.closeSideBar。
  - 去向：react-front/src/layout/index.tsx
- I02443 `ruoyi-fastapi-frontend/src/layout/index.vue` lines 55-57 FunctionDeclaration: handleClickOutside
  - 基线：源语句 sha256=10b6776bbf7bc1e489aad2ed6c0bd7793aeb19631c8492f6a6ec0338d3ad3658；保留返回、异常及 0 个分支，调用=CallExpression.closeSideBar, useAppStore。
  - 去向：react-front/src/layout/index.tsx
- I02444 `ruoyi-fastapi-frontend/src/layout/index.vue` lines 59-59 VariableDeclaration: settingRef
  - 基线：源语句 sha256=200463647a872e0755a55f6dd28fc51fdd8443388c43259530a5c50f70e88d26；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/index.tsx
- I02445 `ruoyi-fastapi-frontend/src/layout/index.vue` lines 60-62 FunctionDeclaration: setLayout
  - 基线：源语句 sha256=473569a007f4d135c7a59a5ac22656277b9fe273fd671de389a69d288b90a6c6；保留返回、异常及 0 个分支，调用=settingRef.value.openSetting。
  - 去向：react-front/src/layout/index.tsx
- I02446 `ruoyi-fastapi-frontend/src/layout/index.vue` template lines 1-14（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/layout/index.tsx
- I02447 `ruoyi-fastapi-frontend/src/layout/index.vue` template line 2: v-bind:class
  - 基线：原表达式：classObj；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/index.tsx
- I02448 `ruoyi-fastapi-frontend/src/layout/index.vue` template line 2: v-bind:style
  - 基线：原表达式：{ '--current-color': theme, '--current-color-light': theme + '1a', '--current-color-dark-bg': theme + '33' }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/index.tsx
- I02449 `ruoyi-fastapi-frontend/src/layout/index.vue` template line 3: v-if:
  - 基线：原表达式：device === 'mobile' && sidebar.opened；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/index.tsx
- I02450 `ruoyi-fastapi-frontend/src/layout/index.vue` template line 3: v-on:click
  - 基线：原表达式：handleClickOutside；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/index.tsx
- I02451 `ruoyi-fastapi-frontend/src/layout/index.vue` template line 4: v-if:
  - 基线：原表达式：!sidebar.hide；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/index.tsx
- I02452 `ruoyi-fastapi-frontend/src/layout/index.vue` template line 5: v-bind:class
  - 基线：原表达式：{ hasTagsView: needTagsView, sidebarHide: sidebar.hide }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/index.tsx
- I02453 `ruoyi-fastapi-frontend/src/layout/index.vue` template line 6: v-bind:class
  - 基线：原表达式：{ 'fixed-header': fixedHeader }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/index.tsx
- I02454 `ruoyi-fastapi-frontend/src/layout/index.vue` template line 7: v-on:setLayout
  - 基线：原表达式：setLayout；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/index.tsx
- I02455 `ruoyi-fastapi-frontend/src/layout/index.vue` template line 8: v-if:
  - 基线：原表达式：needTagsView；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/index.tsx
- I02456 `ruoyi-fastapi-frontend/src/layout/index.vue` style[0] lines 65-116
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/layout/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
