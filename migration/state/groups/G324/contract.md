# G324 src/views/tool/gen/createTable.vue：完整能力

依赖：G000, G046

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I08365 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` lines 33-33 ImportDeclaration: 
  - 基线：源语句 sha256=8f97ff51b53aa5573fba38d8a0e62af28508f9b1b228a1d43405de4e4a7c8c10；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08366 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` lines 35-35 VariableDeclaration: visible
  - 基线：源语句 sha256=1e5831fe2e56f6cc177d5ecfd848b4a6a30d10008c0fed3fc9f2ab7bcf3c3453；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08367 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` lines 36-36 VariableDeclaration: content
  - 基线：源语句 sha256=f173552f1cfcedab38a989c2d1e6d3f8fa3bd16c13a5fca00dc4bda0bbb73e0e；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08368 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` lines 37-37 VariableDeclaration: dataSourceName
  - 基线：源语句 sha256=ce1c5fe411d61c6d06c4a348d63a7fdb77f6ee863168d05674adf38982cf8eb0；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08369 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` lines 38-38 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08370 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` lines 39-44 VariableDeclaration: props
  - 基线：源语句 sha256=857145bf70982c0182a9fcce22fbc82b7bfe5533a0c6e18326131b1ed790b388；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08371 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` lines 45-45 VariableDeclaration: emit
  - 基线：源语句 sha256=3b2578c18adfa0d7b599ed5745a291660f65e7e01f131193cd40ddbd2e95a55e；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08372 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` lines 48-52 FunctionDeclaration: show
  - 基线：源语句 sha256=4c9918b544ff0eb28e43d94564afe7b68dfdba8b867cc4309d6323e961eb7b7c；保留返回、异常及 2 个分支，调用=props.dataSources.find。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08373 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` lines 55-71 FunctionDeclaration: handleImportTable
  - 基线：源语句 sha256=36657d4ecc2e6262cb66c63ed43b06bd017462ff95384bd58540c025d8e32594；保留返回、异常及 5 个分支，调用=proxy.$modal.msgError, CallExpression.then, createTable, proxy.$modal.msgSuccess, emit。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08374 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` lines 73-75 ExpressionStatement: 
  - 基线：源语句 sha256=c2460c623311437fe7df2af44a678c1b077e77ea0d0b348c475836da9dba739d；保留返回、异常及 0 个分支，调用=defineExpose。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08375 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` template lines 1-30（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08376 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` template line 3: v-model:
  - 基线：原表达式：visible；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08377 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` template line 7: v-model:
  - 基线：原表达式：dataSourceName；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08378 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` template line 13: v-for:
  - 基线：原表达式：source in props.dataSources；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08379 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` template line 14: v-bind:key
  - 基线：原表达式：source.name；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08380 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` template line 15: v-bind:label
  - 基线：原表达式：source.name + '（' + source.dbType + '）'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08381 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` template line 16: v-bind:value
  - 基线：原表达式：source.name；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08382 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` template line 22: v-bind:rows
  - 基线：原表达式：10；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08383 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` template line 22: v-model:
  - 基线：原表达式：content；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08384 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` template line 23: v-slot:footer
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08385 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` template line 25: v-on:click
  - 基线：原表达式：handleImportTable；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/gen/createTable.tsx
- I08386 `ruoyi-fastapi-frontend/src/views/tool/gen/createTable.vue` template line 26: v-on:click
  - 基线：原表达式：visible = false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/gen/createTable.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
