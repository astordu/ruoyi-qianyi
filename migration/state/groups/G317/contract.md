# G317 src/views/tool/build/CodeTypeDialog.vue：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I07819 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` lines 24-24 VariableDeclaration: open
  - 基线：源语句 sha256=f2e582a9560e7ef247d50b4d39dd91b249fcb6f316d6b8a2830457494ec5d668；保留返回、异常及 0 个分支，调用=defineModel。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07820 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` lines 25-27 VariableDeclaration: props
  - 基线：源语句 sha256=b9e7605f0054a166c02fce6beb1ab95e89f06957f486617bea2ee13d0e988bdb；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07821 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` lines 28-28 VariableDeclaration: emit
  - 基线：源语句 sha256=1a21846cdb0f59358443949a0dd87f7acdbc258c02d89bb6d7c7297c67f507f8；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07822 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` lines 29-32 VariableDeclaration: formData
  - 基线：源语句 sha256=ea05812b7bd18a531ac49997b575b8beb2f47a668c72682da3b3331f48f637ab；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07823 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` lines 33-33 VariableDeclaration: codeTypeForm
  - 基线：源语句 sha256=417b99c09d638216a42a7ced384b7b97bae9478d2daede769cd9b3e1a0cce9e5；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07824 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` lines 34-45 VariableDeclaration: rules
  - 基线：源语句 sha256=54330ac9ca3352c094a1fd8443a24d7bd3a92f47c23d7fcf77a29aeb66e9b333；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07825 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` lines 46-55 VariableDeclaration: typeOptions
  - 基线：源语句 sha256=3db365366e06e4fc3b1dc4aed6c088fa7c58064d168f31c69608c23f31c929a7；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07826 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` lines 56-60 FunctionDeclaration: onOpen
  - 基线：源语句 sha256=bd9c4b5802a964ba725bef4a3f75be16996a7ec1213f365b44c9f62fe8157339；保留返回、异常及 1 个分支，调用=。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07827 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` lines 61-63 FunctionDeclaration: onClose
  - 基线：源语句 sha256=7297c788cc30bc363a5bdc60db29cbfeacc76f8ef3605d0e995559fc8d19c27c；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07828 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` lines 64-70 FunctionDeclaration: handelConfirm
  - 基线：源语句 sha256=a832502923169b246d761e72b0998b0d0ae68604d97bb78d409d417465ff954c；保留返回、异常及 2 个分支，调用=codeTypeForm.value.validate, emit, onClose。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07829 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` template lines 1-21（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07830 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` template line 2: v-model:
  - 基线：原表达式：open；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07831 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` template line 2: v-on:open
  - 基线：原表达式：onOpen；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07832 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` template line 2: v-on:close
  - 基线：原表达式：onClose；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07833 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` template line 3: v-bind:model
  - 基线：原表达式：formData；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07834 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` template line 3: v-bind:rules
  - 基线：原表达式：rules；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07835 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` template line 5: v-model:
  - 基线：原表达式：formData.type；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07836 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` template line 6: v-for:
  - 基线：原表达式：(item, index) in typeOptions；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07837 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` template line 6: v-bind:key
  - 基线：原表达式：index；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07838 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` template line 6: v-bind:label
  - 基线：原表达式：item.value；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07839 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` template line 11: v-if:
  - 基线：原表达式：showFileName；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07840 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` template line 12: v-model:
  - 基线：原表达式：formData.fileName；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07841 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` template line 16: v-slot:footer
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07842 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` template line 17: v-on:click
  - 基线：原表达式：onClose；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07843 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` template line 18: v-on:click
  - 基线：原表达式：handelConfirm；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx
- I07844 `ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue` template interpolation line 7
  - 基线：原显示表达式：item.label
  - 去向：react-front/src/views/tool/build/CodeTypeDialog.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
