# G308 src/views/system/role/selectUser.vue：完整能力

依赖：G000, G044, G169, G180, G232, G250

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I07294 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` lines 64-64 ImportDeclaration: 
  - 基线：源语句 sha256=6c49e5cc2d35c063173f00b6d3dc884a2726b70c5a6d422157496c15507a87d7；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07295 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` lines 66-70 VariableDeclaration: props
  - 基线：源语句 sha256=0628d3d8f234feb1595103a2034846c3cbd88c2d294796d754f7818b1174797c；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07296 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` lines 72-72 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07297 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` lines 73-73 VariableDeclaration: 
  - 基线：源语句 sha256=e39eef28f5bbe01b170f2bfb21463bd64109f87928694efa0dd8eb360768e609；保留返回、异常及 0 个分支，调用=proxy.useDict。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07298 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` lines 75-75 VariableDeclaration: userList
  - 基线：源语句 sha256=27329f009483a63c964b05b2e6dcbf3a61052d302dbb204b9efcc11efd5d485b；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07299 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` lines 76-76 VariableDeclaration: visible
  - 基线：源语句 sha256=1e5831fe2e56f6cc177d5ecfd848b4a6a30d10008c0fed3fc9f2ab7bcf3c3453；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07300 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` lines 77-77 VariableDeclaration: total
  - 基线：源语句 sha256=3ea22b280c119d04a2e23fb7967b98534357cc6c46eb2621b3817c605f822958；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07301 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` lines 78-78 VariableDeclaration: userIds
  - 基线：源语句 sha256=d6782c35c2dc1256465c3b6c6c769b20577bd543f6596e059b536680c1c5a75d；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07302 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` lines 80-86 VariableDeclaration: queryParams
  - 基线：源语句 sha256=cf70d3ed194ef8484a1af6c716ca5771cb1838ab89636e89050e0bde299587ed；保留返回、异常及 0 个分支，调用=reactive。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07303 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` lines 89-93 FunctionDeclaration: show
  - 基线：源语句 sha256=f11ee3ec1a75769af91565af679fc3297820c56ec41900367f94825149920629；保留返回、异常及 0 个分支，调用=getList。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07304 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` lines 95-97 FunctionDeclaration: clickRow
  - 基线：源语句 sha256=23e4e66f46b94aab92ade4d1ed2d000368c37ae681e23820cde6163055f56d98；保留返回、异常及 0 个分支，调用=proxy.$refs.refTable.toggleRowSelection。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07305 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` lines 99-101 FunctionDeclaration: handleSelectionChange
  - 基线：源语句 sha256=77efb72fbe8bdace0dcb6bfdb1d701e8ab7fefd0a7e2bbe8945d09fb3bdb2aa6；保留返回、异常及 0 个分支，调用=selection.map。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07306 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` lines 103-108 FunctionDeclaration: getList
  - 基线：源语句 sha256=712fb8902ee9460d7dc817a3b534050d3f72f78f854d6eacfd7992085de4f010；保留返回、异常及 0 个分支，调用=CallExpression.then, unallocatedUserList。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07307 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` lines 110-113 FunctionDeclaration: handleQuery
  - 基线：源语句 sha256=edd514b444273e1673cb3a87378aacdb6449d6d09764ffd0dde80e216d9ef27e；保留返回、异常及 0 个分支，调用=getList。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07308 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` lines 115-118 FunctionDeclaration: resetQuery
  - 基线：源语句 sha256=92181fa4359ab7a75cdb4811fb23d7927c816d7cf603e5534064a28e122424e0；保留返回、异常及 0 个分支，调用=proxy.resetForm, handleQuery。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07309 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` lines 119-119 VariableDeclaration: emit
  - 基线：源语句 sha256=3b2578c18adfa0d7b599ed5745a291660f65e7e01f131193cd40ddbd2e95a55e；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07310 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` lines 121-133 FunctionDeclaration: handleSelectUser
  - 基线：源语句 sha256=1a60f3a36ea0da676dfb73a7d121c043df7846c106d1be5f81250380ee438c54；保留返回、异常及 2 个分支，调用=userIds.value.join, proxy.$modal.msgError, CallExpression.then, authUserSelectAll, proxy.$modal.msgSuccess, emit。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07311 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` lines 135-137 ExpressionStatement: 
  - 基线：源语句 sha256=c2460c623311437fe7df2af44a678c1b077e77ea0d0b348c475836da9dba739d；保留返回、异常及 0 个分支，调用=defineExpose。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07312 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template lines 1-61（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07313 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 3: v-model:
  - 基线：原表达式：visible；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07314 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 4: v-bind:model
  - 基线：原表达式：queryParams；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07315 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 4: v-bind:inline
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07316 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 7: v-model:
  - 基线：原表达式：queryParams.userName；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07317 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 11: v-on:keyup
  - 基线：原表达式：handleQuery；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07318 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 16: v-model:
  - 基线：原表达式：queryParams.phonenumber；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07319 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 20: v-on:keyup
  - 基线：原表达式：handleQuery；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07320 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 24: v-on:click
  - 基线：原表达式：handleQuery；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07321 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 25: v-on:click
  - 基线：原表达式：resetQuery；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07322 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 29: v-on:row-click
  - 基线：原表达式：clickRow；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07323 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 29: v-bind:data
  - 基线：原表达式：userList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07324 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 29: v-on:selection-change
  - 基线：原表达式：handleSelectionChange；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07325 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 31: v-bind:show-overflow-tooltip
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07326 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 32: v-bind:show-overflow-tooltip
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07327 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 33: v-bind:show-overflow-tooltip
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07328 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 34: v-bind:show-overflow-tooltip
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07329 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 36: v-slot:default
  - 基线：原表达式：scope；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07330 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 37: v-bind:options
  - 基线：原表达式：sys_normal_disable；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07331 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 37: v-bind:value
  - 基线：原表达式：scope.row.status；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07332 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 41: v-slot:default
  - 基线：原表达式：scope；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07333 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 47: v-show:
  - 基线：原表达式：total > 0；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07334 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 48: v-bind:total
  - 基线：原表达式：total；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07335 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 49: v-model:page
  - 基线：原表达式：queryParams.pageNum；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07336 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 50: v-model:limit
  - 基线：原表达式：queryParams.pageSize；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07337 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 51: v-on:pagination
  - 基线：原表达式：getList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07338 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 54: v-slot:footer
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07339 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 56: v-on:click
  - 基线：原表达式：handleSelectUser；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07340 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template line 57: v-on:click
  - 基线：原表达式：visible = false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/role/selectUser.tsx
- I07341 `ruoyi-fastapi-frontend/src/views/system/role/selectUser.vue` template interpolation line 42
  - 基线：原显示表达式：parseTime(scope.row.createTime)
  - 去向：react-front/src/views/system/role/selectUser.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
