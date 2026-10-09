# G290 src/views/system/file/components/FileSearchForm.vue：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I05391 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` lines 105-114 ExpressionStatement: 
  - 基线：源语句 sha256=6d8f7e41b3f4fc7a90d70ce74a2e513e22c825289aca48931d66a22bc486a151；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05392 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` lines 116-116 VariableDeclaration: emit
  - 基线：源语句 sha256=a94ea3610cf972934f3505ceba09dce54bddc070a8edf587449f24b84d2d84b2；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05393 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` lines 117-120 VariableDeclaration: queryParams
  - 基线：源语句 sha256=b3578de44dd119e137d2d615774491f2f5e26a2cc6c0e28a9d34da06ad20e593；保留返回、异常及 0 个分支，调用=defineModel。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05394 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` lines 121-124 VariableDeclaration: dateRange
  - 基线：源语句 sha256=c6f351f80497a2563666a40050ea359e6868ca8018ad89655ee8a64b19818a48；保留返回、异常及 0 个分支，调用=defineModel。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05395 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` lines 125-125 VariableDeclaration: queryRef
  - 基线：源语句 sha256=b52ca337d7c86a04eaef302f27d98b1831ddd5d7dd99f23be1ffd9df6a470f89；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05396 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` lines 127-131 FunctionDeclaration: handleReset
  - 基线：源语句 sha256=0fce106b569afbe04b0b1d5e749a862f057e915586170015e3595173bd893893；保留返回、异常及 0 个分支，调用=queryRef.value.resetFields, emit。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05397 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` template lines 1-102（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05398 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` template line 4: v-show:
  - 基线：原表达式：show；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05399 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` template line 5: v-bind:model
  - 基线：原表达式：queryParams；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05400 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` template line 6: v-bind:inline
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05401 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` template line 11: v-model:
  - 基线：原表达式：queryParams.originalName；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05402 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` template line 15: v-on:keyup
  - 基线：原表达式：emit('query')；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05403 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` template line 20: v-model:
  - 基线：原表达式：queryParams.accessType；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05404 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` template line 31: v-model:
  - 基线：原表达式：queryParams.status；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05405 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` template line 43: v-model:
  - 基线：原表达式：queryParams.createBy；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05406 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` template line 47: v-on:keyup
  - 基线：原表达式：emit('query')；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05407 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` template line 52: v-model:
  - 基线：原表达式：queryParams.ownerName；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05408 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` template line 56: v-on:keyup
  - 基线：原表达式：emit('query')；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05409 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` template line 61: v-model:
  - 基线：原表达式：queryParams.deptId；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05410 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` template line 62: v-bind:data
  - 基线：原表达式：deptOptions；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05411 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` template line 63: v-bind:props
  - 基线：原表达式：{ value: 'id', label: 'label', children: 'children' }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05412 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` template line 69: v-bind:render-after-expand
  - 基线：原表达式：false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05413 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` template line 75: v-model:
  - 基线：原表达式：queryParams.expirationStatus；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05414 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` template line 88: v-model:
  - 基线：原表达式：dateRange；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05415 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` template line 98: v-on:click
  - 基线：原表达式：emit('query')；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx
- I05416 `ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue` template line 99: v-on:click
  - 基线：原表达式：handleReset；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileSearchForm.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
