# G195 src/layout/components/AppMain.vue：完整能力

依赖：G000, G196, G199, G229

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01913 `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue` lines 16-16 ImportDeclaration: 
  - 基线：源语句 sha256=537d1b5e7e265262e31aa373cca5caa487ba71f905c46fdc4f2ffd03def4e73e；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/AppMain.tsx
- I01914 `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue` lines 17-17 ImportDeclaration: 
  - 基线：源语句 sha256=7b52a6618e2edbc2ee1001b82af64089331a21f8695e98e3ac775b3e78163eda；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/AppMain.tsx
- I01915 `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue` lines 18-18 ImportDeclaration: 
  - 基线：源语句 sha256=0e55dbc3aac4ad1d960b0ed9d1afe4a12b6fdebafcf121b5a290f88823abb0c4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/AppMain.tsx
- I01916 `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue` lines 20-20 VariableDeclaration: route
  - 基线：源语句 sha256=4d0e93888827dba310f5cf48815c617b23da1a2eb2ff3690209994f3b8c71ff7；保留返回、异常及 0 个分支，调用=useRoute。
  - 去向：react-front/src/layout/components/AppMain.tsx
- I01917 `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue` lines 21-21 VariableDeclaration: tagsViewStore
  - 基线：源语句 sha256=dbfbc56aa9364e962a8e720e9f9ee583383fec56ec33ea0e1c1bf1795a06ff75；保留返回、异常及 0 个分支，调用=useTagsViewStore。
  - 去向：react-front/src/layout/components/AppMain.tsx
- I01918 `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue` lines 23-25 ExpressionStatement: 
  - 基线：源语句 sha256=d7dc87030ed2ebdefce6f94a673a71a64d188660fcf681cbb2fe30623ad965c1；保留返回、异常及 0 个分支，调用=onMounted, addIframe。
  - 去向：react-front/src/layout/components/AppMain.tsx
- I01919 `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue` lines 27-29 ExpressionStatement: 
  - 基线：源语句 sha256=0452210e701589b5aa09eefe15f91fd4ad03783e8c6319ebd3301c1daf596821；保留返回、异常及 0 个分支，调用=watchEffect, addIframe。
  - 去向：react-front/src/layout/components/AppMain.tsx
- I01920 `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue` lines 31-35 FunctionDeclaration: addIframe
  - 基线：源语句 sha256=147bd3f3288f2f15d346d48f761e0bc19944a85f0b1701fac82bf6ffac10f39a；保留返回、异常及 1 个分支，调用=CallExpression.addIframeView, useTagsViewStore。
  - 去向：react-front/src/layout/components/AppMain.tsx
- I01921 `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue` template lines 1-13（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/layout/components/AppMain.tsx
- I01922 `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue` template line 3: v-slot:
  - 基线：原表达式：{ Component, route }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/AppMain.tsx
- I01923 `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue` template line 5: v-bind:include
  - 基线：原表达式：tagsViewStore.cachedViews；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/AppMain.tsx
- I01924 `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue` template line 6: v-if:
  - 基线：原表达式：!route.meta.link；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/AppMain.tsx
- I01925 `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue` template line 6: v-bind:is
  - 基线：原表达式：Component；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/AppMain.tsx
- I01926 `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue` template line 6: v-bind:key
  - 基线：原表达式：route.path；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/AppMain.tsx
- I01927 `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue` style[0] lines 38-107
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/layout/components/AppMain.tsx
- I01928 `ruoyi-fastapi-frontend/src/layout/components/AppMain.vue` style[1] lines 109-123
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=False；原样式选择器在 source-audit.json。
  - 去向：react-front/src/layout/components/AppMain.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
