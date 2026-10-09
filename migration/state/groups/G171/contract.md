# G171 src/components/ExcelImportDialog/index.vue：完整能力

依赖：G000, G231

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01399 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 26-26 ImportDeclaration: 
  - 基线：源语句 sha256=2ec8863f7e5e99b6e9f4898b63d49c0737c19ccb341a54be6cd435a7da40e781；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01400 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 28-28 VariableDeclaration: 
  - 基线：源语句 sha256=d3917068104e0f2158733e5e758c09ff6781b09fc4b90611c9a30e2625c695d6；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01401 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 30-61 VariableDeclaration: props
  - 基线：源语句 sha256=2f86f2a9538ec861fd82aa0caa1a99db5fe8038d2431def23caf62b05b3dd363；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01402 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 63-63 VariableDeclaration: emit
  - 基线：源语句 sha256=43ea2b7714c815d4c58505be1aebfa8c442578d653859ba09e88a83ee43affe2；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01403 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 65-65 VariableDeclaration: uploadRef
  - 基线：源语句 sha256=9fa13610dcf70b5c07138341ae19d7d02c20266ea4fabc1f28918b060ee8fdd2；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01404 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 66-66 VariableDeclaration: visible
  - 基线：源语句 sha256=131588e506b10f4b16485c9067fceb50053d9acd0559369303f97aa3a383855a；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01405 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 67-67 VariableDeclaration: selectedFile
  - 基线：源语句 sha256=0fa2b29eefea1a8648e69fe8ec60e14fe52febe308c394ca78a0b3a4442b76d1；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01406 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 68-68 VariableDeclaration: isUploading
  - 基线：源语句 sha256=0d0ea6053aceb202770e85d39519f49ee41dafb92b38795f21733d4d08882069；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01407 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 69-69 VariableDeclaration: updateSupport
  - 基线：源语句 sha256=b5c0670e67c708df6a424d3cdf7fcef36a25fcf0ba2169e49976146b19ac8a65；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01408 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 70-70 VariableDeclaration: headers
  - 基线：源语句 sha256=d5fc8e8784536649f8e2693d85c52d9f3d14a76110202ffe891e6757b9572840；保留返回、异常及 0 个分支，调用=getToken。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01409 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 72-74 VariableDeclaration: uploadUrl
  - 基线：源语句 sha256=0728adc4eb55156dd20f9b6baf71cda5887091c868eb476c66a741c86bf61c65；保留返回、异常及 2 个分支，调用=computed。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01410 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 76-76 VariableDeclaration: templateUrl
  - 基线：源语句 sha256=ab199d26117e960c7d319f6e60febe35ea320daa28d40dd03c2c908053375682；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01411 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 79-87 FunctionDeclaration: open
  - 基线：源语句 sha256=6f6b36067e1a7301209367732f7ec914589b185edaf2f9e020f236ae0699e2e8；保留返回、异常及 0 个分支，调用=nextTick, uploadRef.value.clearFiles。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01412 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 90-94 FunctionDeclaration: handleClose
  - 基线：源语句 sha256=a2f16b8e6ecd391a3a87805a6243e200715fe810fc5a47573810de8b7aee38ff；保留返回、异常及 0 个分支，调用=uploadRef.value.clearFiles。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01413 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 97-99 FunctionDeclaration: handleDownloadTemplate
  - 基线：源语句 sha256=3e5d7de4d7e8623c00bc4c49008056be8ba61b81d39c09d453aa211fb03cb955；保留返回、异常及 0 个分支，调用=proxy.download, NewExpression.getTime。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01414 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 102-104 FunctionDeclaration: handleProgress
  - 基线：源语句 sha256=4c6ac880263eca55827bb611acd8dad7aeb4239c7e80370ff5cd3587382e29c6；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01415 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 107-109 VariableDeclaration: handleFileChange
  - 基线：源语句 sha256=1447b28d4ac3906a24bb8eadb3caf58c86256484017950b133cf1fb2871a9084；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01416 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 112-114 VariableDeclaration: handleFileRemove
  - 基线：源语句 sha256=74076febdfa4390ebe68c341562e9444bbbbba12528b599d6c0e71e9440a04b1；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01417 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 117-124 FunctionDeclaration: handleSuccess
  - 基线：源语句 sha256=f3410d1c5b6fb69f9643f965520b3f124880c4786723d1587831b864394f26b6；保留返回、异常及 0 个分支，调用=uploadRef.value.clearFiles, proxy.$alert, emit。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01418 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 127-134 FunctionDeclaration: handleSubmit
  - 基线：源语句 sha256=990dfe52071e02da286e15cc87645152846bd0370a7797e61e7b64623f427570；保留返回、异常及 5 个分支，调用=CallExpression.endsWith, file.name.toLowerCase, proxy.$modal.msgError, uploadRef.value.submit。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01419 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` lines 136-136 ExpressionStatement: 
  - 基线：源语句 sha256=8b3d7a5640c4038061f5cc79be7cbb3b242d25adefb4490169f3613c91c55945；保留返回、异常及 0 个分支，调用=defineExpose。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01420 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template lines 1-23（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01421 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template line 2: v-bind:title
  - 基线：原表达式：title；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01422 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template line 2: v-model:
  - 基线：原表达式：visible；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01423 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template line 2: v-bind:width
  - 基线：原表达式：width；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01424 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template line 2: v-on:close
  - 基线：原表达式：handleClose；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01425 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template line 3: v-bind:limit
  - 基线：原表达式：1；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01426 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template line 3: v-bind:headers
  - 基线：原表达式：headers；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01427 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template line 3: v-bind:action
  - 基线：原表达式：uploadUrl；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01428 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template line 3: v-bind:disabled
  - 基线：原表达式：isUploading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01429 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template line 3: v-bind:on-progress
  - 基线：原表达式：handleProgress；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01430 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template line 3: v-bind:on-change
  - 基线：原表达式：handleFileChange；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01431 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template line 3: v-bind:on-remove
  - 基线：原表达式：handleFileRemove；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01432 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template line 3: v-bind:on-success
  - 基线：原表达式：handleSuccess；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01433 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template line 3: v-bind:auto-upload
  - 基线：原表达式：false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01434 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template line 6: v-slot:tip
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01435 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template line 9: v-model:
  - 基线：原表达式：updateSupport；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01436 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template line 12: v-if:
  - 基线：原表达式：templateUrl；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01437 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template line 12: v-on:click
  - 基线：原表达式：handleDownloadTemplate；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01438 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template line 16: v-slot:footer
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01439 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template line 18: v-on:click
  - 基线：原表达式：handleSubmit；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01440 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template line 19: v-on:click
  - 基线：原表达式：visible = false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx
- I01441 `ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue` template interpolation line 9
  - 基线：原显示表达式：updateSupportLabel
  - 去向：react-front/src/components/ExcelImportDialog/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
