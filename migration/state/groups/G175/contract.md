# G175 src/components/IconSelect/index.vue：完整能力

依赖：G000, G176, G187

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01555 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` lines 27-27 ImportDeclaration: 
  - 基线：源语句 sha256=443c95f212cf5ea4b867b152f619bca32bf6334d629f74901a674f89618a5b8d；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/IconSelect/index.tsx
- I01556 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` lines 29-33 VariableDeclaration: props
  - 基线：源语句 sha256=8efdf4f3c859743f60edbce3c473bdeb92dd0f971684723869c16c42ed45b138；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/components/IconSelect/index.tsx
- I01557 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` lines 35-35 VariableDeclaration: iconName
  - 基线：源语句 sha256=880a9341f7b7bf3f51f291e28bf835a0a2ead87ee720188839785d3807259832；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/IconSelect/index.tsx
- I01558 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` lines 36-36 VariableDeclaration: iconList
  - 基线：源语句 sha256=245cd4f7a153c923a2d04ab91c55feb080b6b5fe26255f5a90efe8aa42862882；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/IconSelect/index.tsx
- I01559 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` lines 37-37 VariableDeclaration: emit
  - 基线：源语句 sha256=7bf1164e0bce34dd191deaf21af5eaca642222f428b5cae839ce7135e359b387；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/components/IconSelect/index.tsx
- I01560 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` lines 39-44 FunctionDeclaration: filterIcons
  - 基线：源语句 sha256=0c731b7638d18f674eb0c601c262324ac6f390d45d0012d52b5167a2bcb8500b；保留返回、异常及 1 个分支，调用=icons.filter, item.indexOf。
  - 去向：react-front/src/components/IconSelect/index.tsx
- I01561 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` lines 46-49 FunctionDeclaration: selectedIcon
  - 基线：源语句 sha256=8e0b248d25576bcde265df1f2a8e4322e2cce99d5c311f8d119eb00e08bd8b8c；保留返回、异常及 0 个分支，调用=emit, document.body.click。
  - 去向：react-front/src/components/IconSelect/index.tsx
- I01562 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` lines 51-54 FunctionDeclaration: reset
  - 基线：源语句 sha256=9218b8c025aefb99d5262cc092899d2c02c04b0da93c2a423f989c339d22a6fe；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/IconSelect/index.tsx
- I01563 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` lines 56-58 ExpressionStatement: 
  - 基线：源语句 sha256=8c1e40460a71e38b5cf778806b065a71891a80587082a61b547b124e7f115080；保留返回、异常及 0 个分支，调用=defineExpose。
  - 去向：react-front/src/components/IconSelect/index.tsx
- I01564 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` template lines 1-24（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/components/IconSelect/index.tsx
- I01565 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` template line 4: v-model:
  - 基线：原表达式：iconName；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/IconSelect/index.tsx
- I01566 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` template line 8: v-on:clear
  - 基线：原表达式：filterIcons；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/IconSelect/index.tsx
- I01567 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` template line 9: v-on:input
  - 基线：原表达式：filterIcons；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/IconSelect/index.tsx
- I01568 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` template line 11: v-slot:suffix
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/IconSelect/index.tsx
- I01569 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` template line 15: v-for:
  - 基线：原表达式：(item, index) in iconList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/IconSelect/index.tsx
- I01570 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` template line 15: v-bind:key
  - 基线：原表达式：index；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/IconSelect/index.tsx
- I01571 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` template line 15: v-on:click
  - 基线：原表达式：selectedIcon(item)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/IconSelect/index.tsx
- I01572 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` template line 16: v-bind:class
  - 基线：原表达式：['icon-item', { active: activeIcon === item }]；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/IconSelect/index.tsx
- I01573 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` template line 17: v-bind:icon-class
  - 基线：原表达式：item；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/IconSelect/index.tsx
- I01574 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` template interpolation line 18
  - 基线：原显示表达式：item
  - 去向：react-front/src/components/IconSelect/index.tsx
- I01575 `ruoyi-fastapi-frontend/src/components/IconSelect/index.vue` style[0] lines 61-111
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/components/IconSelect/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
