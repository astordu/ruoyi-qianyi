# G170 src/components/Editor/index.vue：完整能力

依赖：G000, G231

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01367 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` lines 30-30 ImportDeclaration: 
  - 基线：源语句 sha256=7eb2575d00cee03750b17c50c904a112ee75425bbe3f8a225c0c5da4bafef706；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/Editor/index.tsx
- I01368 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` lines 31-31 ImportDeclaration: 
  - 基线：源语句 sha256=513e95f6d302abd14a359e3ce6ffadda7ea3e618a8300a244b0c3e72d3d214ab；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/Editor/index.tsx
- I01369 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` lines 32-32 ImportDeclaration: 
  - 基线：源语句 sha256=a0ecc257ae23ded95bc9380460f81f0ff8364a01fbe91caadc31aa17c9a0167b；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/Editor/index.tsx
- I01370 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` lines 33-33 ImportDeclaration: 
  - 基线：源语句 sha256=7e557e7755cde2bc76ecec008e45301b1ef2a9b9385fd232bf80b291853fe1eb；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/Editor/index.tsx
- I01371 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` lines 35-35 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/components/Editor/index.tsx
- I01372 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` lines 37-37 VariableDeclaration: quillEditorRef
  - 基线：源语句 sha256=bebc25a1245729569d21c333f1e9e0fbf19b724ed729d4b26531fa8684f22199；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Editor/index.tsx
- I01373 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` lines 38-38 VariableDeclaration: uploadUrl
  - 基线：源语句 sha256=5fff422757295437bacbbcb166455fc374cea5de333a0f3f0800746610ce928f；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Editor/index.tsx
- I01374 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` lines 39-41 VariableDeclaration: headers
  - 基线：源语句 sha256=28893311c95d02ed54b228f5a2175dfb97f9df4252c6ef32a5e4587e112e894b；保留返回、异常及 0 个分支，调用=ref, getToken。
  - 去向：react-front/src/components/Editor/index.tsx
- I01375 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` lines 43-73 VariableDeclaration: props
  - 基线：源语句 sha256=d9f87d09f2cc9601daea26605f9da78618a9e04e7f0441886ccf2085e2ae575b；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/components/Editor/index.tsx
- I01376 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` lines 75-96 VariableDeclaration: options
  - 基线：源语句 sha256=4f004de85fe9406b04b5a1a0aea4e17b0ffa2ea2d52b346d4b12182989148a9f；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Editor/index.tsx
- I01377 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` lines 98-107 VariableDeclaration: styles
  - 基线：源语句 sha256=8df62021ce207a9a5b29f3cf75a28831dfab979de5ab6d9b7bc8ae0203b238aa；保留返回、异常及 3 个分支，调用=computed。
  - 去向：react-front/src/components/Editor/index.tsx
- I01378 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` lines 109-109 VariableDeclaration: content
  - 基线：源语句 sha256=f173552f1cfcedab38a989c2d1e6d3f8fa3bd16c13a5fca00dc4bda0bbb73e0e；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Editor/index.tsx
- I01379 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` lines 110-114 ExpressionStatement: 
  - 基线：源语句 sha256=cd55adf06661c90e7bd5d0324ef15df00255832ce9e856024317bf6e6241ce0f；保留返回、异常及 2 个分支，调用=watch。
  - 去向：react-front/src/components/Editor/index.tsx
- I01380 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` lines 117-130 ExpressionStatement: 
  - 基线：源语句 sha256=8023cfc8d8936f622e513b3f5c571a601dfe9280c1e97d751073dd9ec8cfffc8；保留返回、异常及 2 个分支，调用=onMounted, quillEditorRef.value.getQuill, quill.getModule, toolbar.addHandler, proxy.$refs.uploadRef.click, quill.format, quill.root.addEventListener。
  - 去向：react-front/src/components/Editor/index.tsx
- I01381 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` lines 133-150 FunctionDeclaration: handleBeforeUpload
  - 基线：源语句 sha256=907e4464025f8807851801adefdb8ab77801e978b92b473bda37445f87651f85；保留返回、异常及 6 个分支，调用=type.includes, proxy.$modal.msgError。
  - 去向：react-front/src/components/Editor/index.tsx
- I01382 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` lines 153-167 FunctionDeclaration: handleUploadSuccess
  - 基线：源语句 sha256=e0410bf075e7a64951db4a8f83b162d971ac882bee45bcead7d5446e896cb89a；保留返回、异常及 1 个分支，调用=CallExpression.getQuill, toRaw, quill.insertEmbed, quill.setSelection, proxy.$modal.msgError。
  - 去向：react-front/src/components/Editor/index.tsx
- I01383 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` lines 170-172 FunctionDeclaration: handleUploadError
  - 基线：源语句 sha256=9b32425e19ed56c9048a563d6d2c7429ed044e56896fe90295279c8de9b673b4；保留返回、异常及 0 个分支，调用=proxy.$modal.msgError。
  - 去向：react-front/src/components/Editor/index.tsx
- I01384 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` lines 175-187 FunctionDeclaration: handlePasteCapture
  - 基线：源语句 sha256=aa9fe0be2d801454e11a2e3a30830039c456a3eeba2581895cdbb78ad0eedc85；保留返回、异常及 4 个分支，调用=item.type.indexOf, e.preventDefault, item.getAsFile, insertImage。
  - 去向：react-front/src/components/Editor/index.tsx
- I01385 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` lines 189-195 FunctionDeclaration: insertImage
  - 基线：源语句 sha256=75849a86a414c966aa97e9dd9b904b1db5eb230147cf71d6f53bc8b4de605412；保留返回、异常及 0 个分支，调用=formData.append, CallExpression.then, axios.post, handleUploadSuccess。
  - 去向：react-front/src/components/Editor/index.tsx
- I01386 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` template lines 1-27（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/components/Editor/index.tsx
- I01387 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` template line 4: v-bind:action
  - 基线：原表达式：uploadUrl；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Editor/index.tsx
- I01388 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` template line 5: v-bind:before-upload
  - 基线：原表达式：handleBeforeUpload；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Editor/index.tsx
- I01389 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` template line 6: v-bind:on-success
  - 基线：原表达式：handleUploadSuccess；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Editor/index.tsx
- I01390 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` template line 7: v-bind:on-error
  - 基线：原表达式：handleUploadError；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Editor/index.tsx
- I01391 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` template line 9: v-bind:show-file-list
  - 基线：原表达式：false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Editor/index.tsx
- I01392 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` template line 10: v-bind:headers
  - 基线：原表达式：headers；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Editor/index.tsx
- I01393 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` template line 12: v-if:
  - 基线：原表达式：type == 'url'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Editor/index.tsx
- I01394 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` template line 20: v-model:content
  - 基线：原表达式：content；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Editor/index.tsx
- I01395 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` template line 22: v-on:textChange
  - 基线：原表达式：(e) => $emit('update:modelValue', content)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Editor/index.tsx
- I01396 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` template line 23: v-bind:options
  - 基线：原表达式：options；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Editor/index.tsx
- I01397 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` template line 24: v-bind:style
  - 基线：原表达式：styles；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Editor/index.tsx
- I01398 `ruoyi-fastapi-frontend/src/components/Editor/index.vue` style[0] lines 198-276
  - 基线：保留全部选择器、声明和 url；lang=css, scoped=False；原样式选择器在 source-audit.json。
  - 去向：react-front/src/components/Editor/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
