# G321 src/views/tool/build/TreeNodeDialog.vue：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I08202 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` lines 35-35 VariableDeclaration: open
  - 基线：源语句 sha256=f2e582a9560e7ef247d50b4d39dd91b249fcb6f316d6b8a2830457494ec5d668；保留返回、异常及 0 个分支，调用=defineModel。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08203 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` lines 36-36 VariableDeclaration: emit
  - 基线：源语句 sha256=1a21846cdb0f59358443949a0dd87f7acdbc258c02d89bb6d7c7297c67f507f8；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08204 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` lines 37-40 VariableDeclaration: formData
  - 基线：源语句 sha256=f3d25633c0124c5b4815683b5e30e6c02ccee4a836d35e3e20b3d6c1bc8eccab；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08205 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` lines 41-56 VariableDeclaration: rules
  - 基线：源语句 sha256=c0664d7126b814125a52adb701656a1919d6a2af48a29391895580e65f610ed3；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08206 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` lines 57-57 VariableDeclaration: dataType
  - 基线：源语句 sha256=158fe65a09deab9f7f530d7c927a245b59c07d8bb7af643ca46236c282aac898；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08207 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` lines 58-67 VariableDeclaration: dataTypeOptions
  - 基线：源语句 sha256=9c0cfde01c6795a64eafb2e18a4147ad6e18b2d7fc9a55091a64c625462d6d07；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08208 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` lines 68-68 VariableDeclaration: id
  - 基线：源语句 sha256=e7cea0c66edde5668fccee010d7a68f0441da1bb2661f555d1861dbb40adc743；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08209 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` lines 69-69 VariableDeclaration: treeNodeForm
  - 基线：源语句 sha256=89196976a1438d9f024fc6b253c9fe2b687ed9e9f5cd0a658b7bea4028c1d614；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08210 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` lines 71-76 FunctionDeclaration: onOpen
  - 基线：源语句 sha256=4d4cff7be6bf43c2021751b7d1a944813b19ca4458d15ea23b93195948db930e；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08211 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` lines 78-80 FunctionDeclaration: onClose
  - 基线：源语句 sha256=7297c788cc30bc363a5bdc60db29cbfeacc76f8ef3605d0e995559fc8d19c27c；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08212 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` lines 82-92 FunctionDeclaration: handelConfirm
  - 基线：源语句 sha256=06baacb9126fe2a94325bf34ea6860555411c15367fc93e1c961e85db3b6e7d4；保留返回、异常及 3 个分支，调用=treeNodeForm.value.validate, parseFloat, emit, onClose。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08213 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template lines 1-33（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08214 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 3: v-model:
  - 基线：原表达式：open；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08215 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 3: v-bind:close-on-click-modal
  - 基线：原表达式：false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08216 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 3: v-bind:modal-append-to-body
  - 基线：原表达式：false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08217 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 4: v-on:open
  - 基线：原表达式：onOpen；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08218 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 4: v-on:close
  - 基线：原表达式：onClose；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08219 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 5: v-bind:model
  - 基线：原表达式：formData；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08220 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 5: v-bind:rules
  - 基线：原表达式：rules；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08221 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 6: v-bind:span
  - 基线：原表达式：24；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08222 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 8: v-model:
  - 基线：原表达式：formData.label；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08223 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 11: v-bind:span
  - 基线：原表达式：24；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08224 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 13: v-model:
  - 基线：原表达式：formData.value；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08225 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 14: v-slot:append
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08226 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 15: v-model:
  - 基线：原表达式：dataType；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08227 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 15: v-bind:style
  - 基线：原表达式：{ width: '100px' }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08228 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 16: v-for:
  - 基线：原表达式：(item, index) in dataTypeOptions；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08229 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 16: v-bind:key
  - 基线：原表达式：index；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08230 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 16: v-bind:label
  - 基线：原表达式：item.label；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08231 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 16: v-bind:value
  - 基线：原表达式：item.value；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08232 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 17: v-bind:disabled
  - 基线：原表达式：item.disabled；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08233 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 25: v-slot:footer
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08234 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 27: v-on:click
  - 基线：原表达式：handelConfirm；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx
- I08235 `ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue` template line 28: v-on:click
  - 基线：原表达式：onClose；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/TreeNodeDialog.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
