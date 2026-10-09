# G309 src/views/system/user/authRole.vue：完整能力

依赖：G000, G045, G180

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I07342 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 49-49 ImportDeclaration: 
  - 基线：源语句 sha256=7e1da58c82507018efda3ce8b82e252f61fdb91fcf5b633ae0fed43b2c4ae382；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07343 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 51-51 VariableDeclaration: route
  - 基线：源语句 sha256=19ffaf888604ba2654aa25f29ba0210e96226ea7089e9e15dc5c05cf276b3a9f；保留返回、异常及 0 个分支，调用=useRoute。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07344 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 52-52 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07345 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 54-54 VariableDeclaration: loading
  - 基线：源语句 sha256=c6d283c2f3ea7c9a46a2b20e0ef90bfcf6ffbde99656d9a424ad43f7d28f2aba；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07346 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 55-55 VariableDeclaration: total
  - 基线：源语句 sha256=3ea22b280c119d04a2e23fb7967b98534357cc6c46eb2621b3817c605f822958；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07347 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 56-56 VariableDeclaration: pageNum
  - 基线：源语句 sha256=f70607a841a32586286ce8e239d4b9bbd47d02fb5c7abad6a6ff895ec63fb10c；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07348 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 57-57 VariableDeclaration: pageSize
  - 基线：源语句 sha256=9e3646a51135f666ce346e41f9d1aa81ce94f9164840bafb1975f01c83840288；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07349 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 58-58 VariableDeclaration: roleIds
  - 基线：源语句 sha256=88cd0a46862a100884ea7df14f414238460a2f89a6dd1295158f6d9cd594cec2；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07350 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 59-59 VariableDeclaration: roles
  - 基线：源语句 sha256=a6cb200648cd72097cee99385e6a81c0ca8c1661f5f5ab23fec8e4e86ef3e8b2；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07351 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 60-64 VariableDeclaration: form
  - 基线：源语句 sha256=263a08002cb8bc9ed1dba78be9b1a3818918ca394cee64fb67cb4668564b493d；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07352 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 67-71 FunctionDeclaration: clickRow
  - 基线：源语句 sha256=4a17bd3b88b222e052eeecde389ceda0fa40046babdb2c838c9c36d3c9695325；保留返回、异常及 1 个分支，调用=checkSelectable, proxy.$refs.roleRef.toggleRowSelection。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07353 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 71-71 EmptyStatement: 
  - 基线：源语句 sha256=41b805ea7ac014e23556e98bb374702a08344268f92489a02f0880849394a1e4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07354 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 74-76 FunctionDeclaration: handleSelectionChange
  - 基线：源语句 sha256=ad43ca5099084ed97ae16c9ec67cb6ff4304ed8c1370dc91edd28a87271f93ae；保留返回、异常及 0 个分支，调用=selection.map。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07355 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 76-76 EmptyStatement: 
  - 基线：源语句 sha256=41b805ea7ac014e23556e98bb374702a08344268f92489a02f0880849394a1e4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07356 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 79-81 FunctionDeclaration: getRowKey
  - 基线：源语句 sha256=b9b76f96106e3c1e2ad589ef16b6b01d3e91b7b3b36df43a8576df0de95e7a8f；保留返回、异常及 1 个分支，调用=。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07357 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 81-81 EmptyStatement: 
  - 基线：源语句 sha256=41b805ea7ac014e23556e98bb374702a08344268f92489a02f0880849394a1e4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07358 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 84-86 FunctionDeclaration: checkSelectable
  - 基线：源语句 sha256=8e712ba804f778080acb774e64288f42d169e7f5c4627fa496af9ae5d1d76b3c；保留返回、异常及 2 个分支，调用=。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07359 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 86-86 EmptyStatement: 
  - 基线：源语句 sha256=41b805ea7ac014e23556e98bb374702a08344268f92489a02f0880849394a1e4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07360 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 89-92 FunctionDeclaration: close
  - 基线：源语句 sha256=8acc952da58d8d5cd630aa2008046847a1aed2b7a47d7b98c1970bdf33ade71c；保留返回、异常及 0 个分支，调用=proxy.$tab.closeOpenPage。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07361 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 92-92 EmptyStatement: 
  - 基线：源语句 sha256=41b805ea7ac014e23556e98bb374702a08344268f92489a02f0880849394a1e4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07362 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 95-102 FunctionDeclaration: submitForm
  - 基线：源语句 sha256=84e785a630ce539fcd046f834f6d33f8e047e77a03a41b69ef00c9e20510290f；保留返回、异常及 0 个分支，调用=roleIds.value.join, CallExpression.then, updateAuthRole, proxy.$modal.msgSuccess, close。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07363 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 102-102 EmptyStatement: 
  - 基线：源语句 sha256=41b805ea7ac014e23556e98bb374702a08344268f92489a02f0880849394a1e4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07364 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` lines 104-122 ExpressionStatement: 
  - 基线：源语句 sha256=8d1ec1935e76be9053e4a6098c668baff79f115b51f474cb3d6555500a2f0ce0；保留返回、异常及 3 个分支，调用=ArrowFunctionExpression, CallExpression.then, getAuthRole, nextTick, roles.value.forEach, proxy.$refs.roleRef.toggleRowSelection。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07365 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template lines 1-46（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07366 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 4: v-bind:model
  - 基线：原表达式：form；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07367 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 6: v-bind:span
  - 基线：原表达式：8；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07368 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 6: v-bind:offset
  - 基线：原表达式：2；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07369 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 8: v-model:
  - 基线：原表达式：form.nickName；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07370 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 11: v-bind:span
  - 基线：原表达式：8；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07371 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 11: v-bind:offset
  - 基线：原表达式：2；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07372 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 13: v-model:
  - 基线：原表达式：form.userName；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07373 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 20: v-loading:
  - 基线：原表达式：loading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07374 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 20: v-bind:row-key
  - 基线：原表达式：getRowKey；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07375 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 20: v-on:row-click
  - 基线：原表达式：clickRow；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07376 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 20: v-on:selection-change
  - 基线：原表达式：handleSelectionChange；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07377 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 20: v-bind:data
  - 基线：原表达式：roles.slice((pageNum - 1) * pageSize, pageNum * pageSize)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07378 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 22: v-slot:default
  - 基线：原表达式：scope；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07379 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 26: v-bind:reserve-selection
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07380 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 26: v-bind:selectable
  - 基线：原表达式：checkSelectable；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07381 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 31: v-slot:default
  - 基线：原表达式：scope；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07382 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 37: v-show:
  - 基线：原表达式：total > 0；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07383 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 37: v-bind:total
  - 基线：原表达式：total；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07384 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 37: v-model:page
  - 基线：原表达式：pageNum；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07385 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 37: v-model:limit
  - 基线：原表达式：pageSize；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07386 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 41: v-on:click
  - 基线：原表达式：submitForm()；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07387 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template line 42: v-on:click
  - 基线：原表达式：close()；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07388 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template interpolation line 23
  - 基线：原显示表达式：(pageNum - 1) * pageSize + scope.$index + 1
  - 去向：react-front/src/views/system/user/authRole.tsx
- I07389 `ruoyi-fastapi-frontend/src/views/system/user/authRole.vue` template interpolation line 32
  - 基线：原显示表达式：parseTime(scope.row.createTime)
  - 去向：react-front/src/views/system/user/authRole.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
