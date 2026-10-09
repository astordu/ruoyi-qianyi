# G178 src/components/ImageUpload/index.vue：完整能力

依赖：G000, G231, G256

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01592 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 51-51 ImportDeclaration: 
  - 基线：源语句 sha256=7e557e7755cde2bc76ecec008e45301b1ef2a9b9385fd232bf80b291853fe1eb；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01593 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 52-52 ImportDeclaration: 
  - 基线：源语句 sha256=9ba7d673f7e7d40d378be5cb01aa397488015eb4f529f69c55058d6e9117ef53；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01594 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 53-53 ImportDeclaration: 
  - 基线：源语句 sha256=eb3320dea953a5a6b2e7f9de85b27606a1cd7f7092a26edc607dbd7d32032f8c；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01595 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 55-96 VariableDeclaration: props
  - 基线：源语句 sha256=1aa77810b53726d004b53cac33a112f92d2b7b26e60339fe777befdcb4029f8b；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01596 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 98-98 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01597 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 99-99 VariableDeclaration: emit
  - 基线：源语句 sha256=1b382f8bdab7123c262d55c109efe48a53f3d65160e8c9048a82e13bc6954fe1；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01598 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 100-100 VariableDeclaration: number
  - 基线：源语句 sha256=7b1a8ceb3bd2b844886f5d11eeb6f17fd000dfcba2c0faf531942f0b5ca7e340；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01599 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 101-101 VariableDeclaration: uploadList
  - 基线：源语句 sha256=b0f5ec9c76d360cfc3e1d096f47ac659c6b0a5957c1b79ff7e54fd8845df5a72；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01600 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 102-102 VariableDeclaration: dialogImageUrl
  - 基线：源语句 sha256=e93bfc95b17645da2ae96d11f884f532acbcae8c86de3da53efe99544bcda716；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01601 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 103-103 VariableDeclaration: dialogVisible
  - 基线：源语句 sha256=d11b50d01941cceb6ddac111d5e589c7d6918f0a0ff33b6c062904da130fda74；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01602 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 104-104 VariableDeclaration: baseUrl
  - 基线：源语句 sha256=e83eb4d6cf9019dd0673e8cb79ae3f451419d6424077b06b8f0c5444a65220f3；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01603 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 105-105 VariableDeclaration: uploadImgUrl
  - 基线：源语句 sha256=20e8a3bcbbd7f72cf448af5349b33b1956308c43683be3267ea2b886622aa55a；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01604 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 106-106 VariableDeclaration: headers
  - 基线：源语句 sha256=10b7b2c7980a3e4073da57bd176be21d1701c45e4b752620306991e12272c906；保留返回、异常及 0 个分支，调用=ref, getToken。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01605 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 107-107 VariableDeclaration: fileList
  - 基线：源语句 sha256=ddad872b2ccb910eaf948cd720efd3d35c69ef319d802a8d495fa66220f7064c；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01606 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 108-110 VariableDeclaration: showTip
  - 基线：源语句 sha256=d4767c8bfb3846caae82eff73e5c462ffbc1c21ae0228eb1652c5185287bfa54；保留返回、异常及 2 个分支，调用=computed。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01607 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 112-131 ExpressionStatement: 
  - 基线：源语句 sha256=c94d11118891224b05011672245360f92509b274a077e030587ea7bf23dcfd00；保留返回、异常及 7 个分支，调用=watch, Array.isArray, props.modelValue.split, list.map, item.indexOf, isExternal。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01608 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 134-166 FunctionDeclaration: handleBeforeUpload
  - 基线：源语句 sha256=70c18bbe5a20917cfbaef6d647bf0f0a0f107a85a96995e13ccf5fbd035b44a1；保留返回、异常及 15 个分支，调用=file.name.lastIndexOf, file.name.slice, props.fileType.some, file.type.indexOf, fileExtension.indexOf, proxy.$modal.msgError, props.fileType.join, file.name.includes, proxy.$modal.loading。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01609 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 169-171 FunctionDeclaration: handleExceed
  - 基线：源语句 sha256=b03de6955d615f11da532fcc3679fe8f2288fb75844504311b5e224b8a38401e；保留返回、异常及 0 个分支，调用=proxy.$modal.msgError。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01610 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 174-185 FunctionDeclaration: handleUploadSuccess
  - 基线：源语句 sha256=064e2a8ba386cf4e0007550235d6950d174b065c9af3f2ad5c126899ece3765d；保留返回、异常及 1 个分支，调用=uploadList.value.push, uploadedSuccessfully, proxy.$modal.closeLoading, proxy.$modal.msgError, proxy.$refs.imageUpload.handleRemove。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01611 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 188-195 FunctionDeclaration: handleDelete
  - 基线：源语句 sha256=942aa778bf579e8b4c8aae58d22c8544faa7aa19c80dff77580032613d6f1570；保留返回、异常及 3 个分支，调用=CallExpression.indexOf, fileList.value.map, fileList.value.splice, emit, listToString。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01612 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 198-206 FunctionDeclaration: uploadedSuccessfully
  - 基线：源语句 sha256=1fc7634460adfd2497090493cfb91ecbad24ee5e02865eefff823ab2225588ce；保留返回、异常及 2 个分支，调用=CallExpression.concat, fileList.value.filter, emit, listToString, proxy.$modal.closeLoading。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01613 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 209-212 FunctionDeclaration: handleUploadError
  - 基线：源语句 sha256=f8f73197f14da9f52491b29628fe81a75765129e3d1137435f03d18187781723；保留返回、异常及 0 个分支，调用=proxy.$modal.msgError, proxy.$modal.closeLoading。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01614 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 215-218 FunctionDeclaration: handlePictureCardPreview
  - 基线：源语句 sha256=3b269e0346276ae806005e4bccd3066ec3885d84ce7af538ebe5321ed0397cb0；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01615 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 221-230 FunctionDeclaration: listToString
  - 基线：源语句 sha256=a1743970408ff893c5a3da31ab82ebb1fd1fc0a89e3b948c524e534ed30bbe27；保留返回、异常及 5 个分支，调用=list.i.url.indexOf, list.i.url.replace, strs.substr。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01616 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` lines 233-246 ExpressionStatement: 
  - 基线：源语句 sha256=200643b5b2588faeb160ef1ae89e67cdf0ab562918496fb2e3e86357064cd857；保留返回、异常及 2 个分支，调用=onMounted, nextTick, proxy.$refs.imageUpload.$el.querySelector, Sortable.create, fileList.value.splice, emit, listToString。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01617 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template lines 1-48（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01618 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template line 5: v-bind:disabled
  - 基线：原表达式：disabled；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01619 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template line 6: v-bind:action
  - 基线：原表达式：uploadImgUrl；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01620 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template line 8: v-bind:on-success
  - 基线：原表达式：handleUploadSuccess；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01621 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template line 9: v-bind:before-upload
  - 基线：原表达式：handleBeforeUpload；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01622 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template line 10: v-bind:data
  - 基线：原表达式：data；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01623 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template line 11: v-bind:limit
  - 基线：原表达式：limit；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01624 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template line 12: v-bind:on-error
  - 基线：原表达式：handleUploadError；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01625 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template line 13: v-bind:on-exceed
  - 基线：原表达式：handleExceed；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01626 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template line 15: v-bind:before-remove
  - 基线：原表达式：handleDelete；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01627 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template line 16: v-bind:show-file-list
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01628 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template line 17: v-bind:headers
  - 基线：原表达式：headers；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01629 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template line 18: v-bind:file-list
  - 基线：原表达式：fileList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01630 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template line 19: v-bind:on-preview
  - 基线：原表达式：handlePictureCardPreview；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01631 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template line 20: v-bind:class
  - 基线：原表达式：{ hide: fileList.length >= limit }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01632 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template line 25: v-if:
  - 基线：原表达式：showTip && !disabled；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01633 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template line 27: v-if:
  - 基线：原表达式：fileSize；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01634 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template line 30: v-if:
  - 基线：原表达式：fileType；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01635 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template line 37: v-model:
  - 基线：原表达式：dialogVisible；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01636 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template line 43: v-bind:src
  - 基线：原表达式：dialogImageUrl；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01637 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template interpolation line 28
  - 基线：原显示表达式：fileSize
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01638 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` template interpolation line 31
  - 基线：原显示表达式：fileType.join("/")
  - 去向：react-front/src/components/ImageUpload/index.tsx
- I01639 `ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue` style[0] lines 249-258
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/components/ImageUpload/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
