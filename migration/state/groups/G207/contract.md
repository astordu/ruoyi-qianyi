# G207 src/layout/components/TagsView/ScrollPane.vue：完整能力

依赖：G000, G229

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02226 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` lines 13-13 ImportDeclaration: 
  - 基线：源语句 sha256=0e55dbc3aac4ad1d960b0ed9d1afe4a12b6fdebafcf121b5a290f88823abb0c4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx
- I02227 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` lines 15-15 VariableDeclaration: tagAndTagSpacing
  - 基线：源语句 sha256=085137831b8c7592374d4952d5fa5923d8ff7091876ae0e080f62914183b6bf7；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx
- I02228 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` lines 16-16 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx
- I02229 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` lines 18-18 VariableDeclaration: scrollWrapper
  - 基线：源语句 sha256=0dd74df6d9d2fa93ab2d5643c5c41774d9920eadb75481c0ce06132c87339d51；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx
- I02230 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` lines 19-19 VariableDeclaration: emits
  - 基线：源语句 sha256=55ef585d6f908ee44acfbd4dd03dc187566f8109764b5c60f321b3b5a59b9395；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx
- I02231 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` lines 21-23 ExpressionStatement: 
  - 基线：源语句 sha256=78247d2c3c542c9c4a16ccc3447a051f2c3a71ed9f02bee0fbd59c9c14c25f23；保留返回、异常及 0 个分支，调用=onMounted, scrollWrapper.value.addEventListener。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx
- I02232 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` lines 24-26 ExpressionStatement: 
  - 基线：源语句 sha256=38dc8d6d6baebce585b43015d5e69120e788a09af740f2dcf69928dd33ef6bc6；保留返回、异常及 0 个分支，调用=onBeforeUnmount, scrollWrapper.value.removeEventListener。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx
- I02233 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` lines 28-31 VariableDeclaration: emitScroll
  - 基线：源语句 sha256=9b5f330ada03b59acf7525bed5f2df58a972b4adee3bd56a8cc6ae13da7e7fdd；保留返回、异常及 0 个分支，调用=emits。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx
- I02234 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` lines 33-60 FunctionDeclaration: smoothScrollTo
  - 基线：源语句 sha256=6e5295c56d277315a61cd91f746c7b1624fabeea89efafb681eef0aaa03660c5；保留返回、异常及 5 个分支，调用=ease, requestAnimationFrame, emits。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx
- I02235 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` lines 62-67 FunctionDeclaration: handleScroll
  - 基线：源语句 sha256=da200bc621f1baad14531f92fa4cfaead8b394bf5c8728d2b59e7f770457e65c；保留返回、异常及 1 个分支，调用=emits。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx
- I02236 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` lines 69-69 VariableDeclaration: tagsViewStore
  - 基线：源语句 sha256=dbfbc56aa9364e962a8e720e9f9ee583383fec56ec33ea0e1c1bf1795a06ff75；保留返回、异常及 0 个分支，调用=useTagsViewStore。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx
- I02237 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` lines 70-70 VariableDeclaration: visitedViews
  - 基线：源语句 sha256=68cb4ba55c17cee8ecf00d5e551b8733119f710422383d3db6dc35d8b058e733；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx
- I02238 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` lines 72-114 FunctionDeclaration: moveToTarget
  - 基线：源语句 sha256=5c7924b85909012581223bdf05f68d8c1bcb39c77266655b4b9937bc6064da90；保留返回、异常及 9 个分支，调用=smoothScrollTo, document.getElementsByClassName, visitedViews.value.findIndex, Object.hasOwnProperty.call。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx
- I02239 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` lines 116-118 FunctionDeclaration: scrollToStart
  - 基线：源语句 sha256=0a70a5b6f5fadbeb046781c0fea43f352c5667af3bc04cf6907eaea47f04c5c9；保留返回、异常及 0 个分支，调用=smoothScrollTo。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx
- I02240 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` lines 120-123 FunctionDeclaration: scrollToEnd
  - 基线：源语句 sha256=2e472c17f7f4eb3fa33e42353c99dd45d3824d76d6e982cd6e7ef9932fc3bc23；保留返回、异常及 0 个分支，调用=smoothScrollTo。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx
- I02241 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` lines 125-131 FunctionDeclaration: getScrollState
  - 基线：源语句 sha256=265a222242a751f61774f5ea12eb555c14b4d22920344beb4e7b43a65c2db6a2；保留返回、异常及 1 个分支，调用=。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx
- I02242 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` lines 133-138 ExpressionStatement: 
  - 基线：源语句 sha256=badbf9b9e03e765d8e87f19126aceae957c71f2f7d8656b2d0cba54d783e9fe9；保留返回、异常及 0 个分支，调用=defineExpose。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx
- I02243 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` template lines 1-10（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx
- I02244 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` template line 4: v-bind:vertical
  - 基线：原表达式：false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx
- I02245 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` template line 6: v-on:wheel
  - 基线：原表达式：handleScroll；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx
- I02246 `ruoyi-fastapi-frontend/src/layout/components/TagsView/ScrollPane.vue` style[0] lines 141-156
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/layout/components/TagsView/ScrollPane.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
