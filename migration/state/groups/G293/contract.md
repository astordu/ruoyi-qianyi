# G293 src/views/system/file/components/FileTransferDialog.vue：完整能力

依赖：G000, G039

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I05506 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` lines 81-85 ImportDeclaration: 
  - 基线：源语句 sha256=7ebb53cf7faae9910a230e23743ecec68b163f4f98fe0168e415fe504ccf7574；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05507 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` lines 87-87 VariableDeclaration: emit
  - 基线：源语句 sha256=000f8803e150d60c6d770de50ab5bdb69c7c7599de94c475abb3a63c89abf22c；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05508 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` lines 88-88 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05509 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` lines 89-89 VariableDeclaration: visible
  - 基线：源语句 sha256=1e5831fe2e56f6cc177d5ecfd848b4a6a30d10008c0fed3fc9f2ab7bcf3c3453；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05510 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` lines 90-90 VariableDeclaration: saving
  - 基线：源语句 sha256=0ed4610a63d84622d45fa05fda6df512f5264acc5b946a32df9ca21ed419ed5a；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05511 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` lines 91-91 VariableDeclaration: userLoading
  - 基线：源语句 sha256=b956decd065276ce77ca8701a2a0a9fa6e87d67438c07f446bc1722d1ef47252；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05512 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` lines 92-92 VariableDeclaration: fileIds
  - 基线：源语句 sha256=d0da7d5b148a01f41c8681538e7a0f2bf222e00843e8432e4e39e5a161bc1f43；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05513 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` lines 93-93 VariableDeclaration: fileName
  - 基线：源语句 sha256=002d68d0f126e088bacfdbc8f608f68deeccca37344c0fcc0fa31a91662553f3；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05514 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` lines 94-94 VariableDeclaration: userOptions
  - 基线：源语句 sha256=e628c948b410b4514bdb42f2a71383f3c854295fa1c026a8d2a40d30cb2eac5e；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05515 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` lines 95-95 VariableDeclaration: deptOptions
  - 基线：源语句 sha256=236d0e7c904cd13eca18f821c6ce9044c96c113c5ffc8c000b9d24335913858e；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05516 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` lines 96-96 VariableDeclaration: formRef
  - 基线：源语句 sha256=675818d38d5ba9d23f55c06aae6e2ca2f35bc0b963de79460f91f8c6ec4da123；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05517 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` lines 97-102 VariableDeclaration: form
  - 基线：源语句 sha256=e030c462da87525f57daf90d85c54f20b8add0e89d507ccbcfd83f4c63beef55；保留返回、异常及 0 个分支，调用=reactive。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05518 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` lines 103-109 VariableDeclaration: rules
  - 基线：源语句 sha256=a8e0152bfd76bc013b6edc6a3615917a32148dea570e4cb1312d091b4cf992f2；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05519 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` lines 111-128 FunctionDeclaration: open
  - 基线：源语句 sha256=9e3f4a5ead8c96aa2bd0796683244ce0f5115293e2906d02d319f0ac8566aacb；保留返回、异常及 2 个分支，调用=selectedIds.join, Object.assign, nextTick, formRef.value.clearValidate, CallExpression.then, getFileAclDeptTree, searchUsers。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05520 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` lines 130-139 FunctionDeclaration: searchUsers
  - 基线：源语句 sha256=98660c129509814d7d17c9ea00d58569b2b09ee7d1c83079dc78cb9ecca0743d；保留返回、异常及 0 个分支，调用=CallExpression.finally, CallExpression.then, searchFileAclSubjects。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05521 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` lines 141-146 FunctionDeclaration: handleUserChange
  - 基线：源语句 sha256=d8113f5a0521dc0a463522dc117de4878538f3ccc23eed7a9f69c7fa09a6823a；保留返回、异常及 1 个分支，调用=userOptions.value.find。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05522 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` lines 148-162 FunctionDeclaration: submit
  - 基线：源语句 sha256=0576153a18e05878fb3f190a43e31a7604eb18f4c77422474ad4770528316f8f；保留返回、异常及 2 个分支，调用=formRef.value.validate, CallExpression.finally, CallExpression.then, transferFile, emit, proxy.$modal.msgSuccess。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05523 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` lines 164-164 ExpressionStatement: 
  - 基线：源语句 sha256=2e56640d2586072b42b8ea1f2cbd05f1d669da4f3e9e5617eb50a334cf1e3d67；保留返回、异常及 0 个分支，调用=defineExpose。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05524 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template lines 1-78（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05525 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 3: v-bind:title
  - 基线：原表达式：`转移文件 - ${fileName}`；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05526 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 4: v-model:
  - 基线：原表达式：visible；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05527 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 8: v-bind:model
  - 基线：原表达式：form；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05528 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 8: v-bind:rules
  - 基线：原表达式：rules；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05529 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 11: v-model:
  - 基线：原表达式：form.ownerUserId；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05530 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 15: v-bind:loading
  - 基线：原表达式：userLoading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05531 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 16: v-bind:remote-method
  - 基线：原表达式：searchUsers；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05532 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 17: v-on:visible-change
  - 基线：原表达式：visible => visible && searchUsers('')；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05533 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 18: v-on:change
  - 基线：原表达式：handleUserChange；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05534 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 23: v-for:
  - 基线：原表达式：item in userOptions；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05535 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 24: v-bind:key
  - 基线：原表达式：item.subjectId；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05536 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 25: v-bind:label
  - 基线：原表达式：item.subjectName；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05537 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 26: v-bind:value
  - 基线：原表达式：item.subjectId；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05538 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 32: v-model:
  - 基线：原表达式：form.deptId；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05539 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 33: v-bind:data
  - 基线：原表达式：deptOptions；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05540 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 34: v-bind:props
  - 基线：原表达式：{ value: 'id', label: 'label', children: 'children' }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05541 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 40: v-bind:render-after-expand
  - 基线：原表达式：false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05542 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 46: v-model:
  - 基线：原表达式：form.retainUploaderAccess；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05543 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 60: v-model:
  - 基线：原表达式：form.reason；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05544 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 62: v-bind:rows
  - 基线：原表达式：3；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05545 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 69: v-slot:footer
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05546 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 71: v-bind:loading
  - 基线：原表达式：saving；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05547 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 71: v-on:click
  - 基线：原表达式：submit；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05548 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template line 74: v-on:click
  - 基线：原表达式：visible = false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05549 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` template interpolation line 51
  - 基线：原显示表达式：form.retainUploaderAccess
              ? "原上传人继续拥有内置下载权限，匹配的显式拒绝仍可覆盖。"
              : "原上传人不再因上传身份获得下载权限，上传记录仍会保留。"
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx
- I05550 `ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue` style[0] lines 167-175
  - 基线：保留全部选择器、声明和 url；lang=css, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/views/system/file/components/FileTransferDialog.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
