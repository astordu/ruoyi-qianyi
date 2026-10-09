# G180 src/components/Pagination/index.vue：完整能力

依赖：G000, G251

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01691 `ruoyi-fastapi-frontend/src/components/Pagination/index.vue` lines 18-18 ImportDeclaration: 
  - 基线：源语句 sha256=556c278f2525a7a844bb8ad779b5302a558418b6cb8e39e5374a8a39650a2664；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/Pagination/index.tsx
- I01692 `ruoyi-fastapi-frontend/src/components/Pagination/index.vue` lines 20-60 VariableDeclaration: props
  - 基线：源语句 sha256=8275f95bf02bd27d8405591db47e541b7ba6eeade111df30b2ff6f550fe90762；保留返回、异常及 2 个分支，调用=defineProps。
  - 去向：react-front/src/components/Pagination/index.tsx
- I01693 `ruoyi-fastapi-frontend/src/components/Pagination/index.vue` lines 62-62 VariableDeclaration: emit
  - 基线：源语句 sha256=1b382f8bdab7123c262d55c109efe48a53f3d65160e8c9048a82e13bc6954fe1；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/components/Pagination/index.tsx
- I01694 `ruoyi-fastapi-frontend/src/components/Pagination/index.vue` lines 63-70 VariableDeclaration: currentPage
  - 基线：源语句 sha256=50a0b118b46c7cf4014be1078a67baeced6205d1340677a503fc8c3e3c73c0a0；保留返回、异常及 1 个分支，调用=computed, emit。
  - 去向：react-front/src/components/Pagination/index.tsx
- I01695 `ruoyi-fastapi-frontend/src/components/Pagination/index.vue` lines 71-78 VariableDeclaration: pageSize
  - 基线：源语句 sha256=6c3140b01d19eae0e8608845e28bc7ef7fe19fb0ea5630b7ae9e62dcce1a82b8；保留返回、异常及 1 个分支，调用=computed, emit。
  - 去向：react-front/src/components/Pagination/index.tsx
- I01696 `ruoyi-fastapi-frontend/src/components/Pagination/index.vue` lines 79-87 FunctionDeclaration: handleSizeChange
  - 基线：源语句 sha256=4c5d89011054ff3e359a8664b21a6580b4ddee629b77b0f587f3fff530257292；保留返回、异常及 2 个分支，调用=emit, scrollTo。
  - 去向：react-front/src/components/Pagination/index.tsx
- I01697 `ruoyi-fastapi-frontend/src/components/Pagination/index.vue` lines 88-93 FunctionDeclaration: handleCurrentChange
  - 基线：源语句 sha256=540b60594709ade29386a100256237e6d866cf29a82869d5933b5e0f10b730de；保留返回、异常及 1 个分支，调用=emit, scrollTo。
  - 去向：react-front/src/components/Pagination/index.tsx
- I01698 `ruoyi-fastapi-frontend/src/components/Pagination/index.vue` template lines 1-15（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/components/Pagination/index.tsx
- I01699 `ruoyi-fastapi-frontend/src/components/Pagination/index.vue` template line 2: v-bind:class
  - 基线：原表达式：{ 'hidden': hidden }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Pagination/index.tsx
- I01700 `ruoyi-fastapi-frontend/src/components/Pagination/index.vue` template line 4: v-bind:background
  - 基线：原表达式：background；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Pagination/index.tsx
- I01701 `ruoyi-fastapi-frontend/src/components/Pagination/index.vue` template line 5: v-model:current-page
  - 基线：原表达式：currentPage；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Pagination/index.tsx
- I01702 `ruoyi-fastapi-frontend/src/components/Pagination/index.vue` template line 6: v-model:page-size
  - 基线：原表达式：pageSize；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Pagination/index.tsx
- I01703 `ruoyi-fastapi-frontend/src/components/Pagination/index.vue` template line 7: v-bind:layout
  - 基线：原表达式：layout；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Pagination/index.tsx
- I01704 `ruoyi-fastapi-frontend/src/components/Pagination/index.vue` template line 8: v-bind:page-sizes
  - 基线：原表达式：pageSizes；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Pagination/index.tsx
- I01705 `ruoyi-fastapi-frontend/src/components/Pagination/index.vue` template line 9: v-bind:pager-count
  - 基线：原表达式：pagerCount；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Pagination/index.tsx
- I01706 `ruoyi-fastapi-frontend/src/components/Pagination/index.vue` template line 10: v-bind:total
  - 基线：原表达式：total；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Pagination/index.tsx
- I01707 `ruoyi-fastapi-frontend/src/components/Pagination/index.vue` template line 11: v-on:size-change
  - 基线：原表达式：handleSizeChange；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Pagination/index.tsx
- I01708 `ruoyi-fastapi-frontend/src/components/Pagination/index.vue` template line 12: v-on:current-change
  - 基线：原表达式：handleCurrentChange；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Pagination/index.tsx
- I01709 `ruoyi-fastapi-frontend/src/components/Pagination/index.vue` style[0] lines 97-104
  - 基线：保留全部选择器、声明和 url；lang=css, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/components/Pagination/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
