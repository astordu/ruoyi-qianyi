# G271 src/views/monitor/online/index.vue：完整能力

依赖：G000, G031, G180, G250

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I03852 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` lines 61-61 ImportDeclaration: 
  - 基线：源语句 sha256=cdc21d0623021c480a33e222f50fc43e96805dd5997ba84b4cd248ccb2ab0dc9；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03853 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` lines 63-63 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03854 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` lines 65-65 VariableDeclaration: onlineList
  - 基线：源语句 sha256=c13bd419ae103e9df50286925413dca5459e649b2be2097988dbe755e61e773f；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03855 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` lines 66-66 VariableDeclaration: loading
  - 基线：源语句 sha256=c6d283c2f3ea7c9a46a2b20e0ef90bfcf6ffbde99656d9a424ad43f7d28f2aba；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03856 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` lines 67-67 VariableDeclaration: total
  - 基线：源语句 sha256=3ea22b280c119d04a2e23fb7967b98534357cc6c46eb2621b3817c605f822958；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03857 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` lines 68-68 VariableDeclaration: pageNum
  - 基线：源语句 sha256=f70607a841a32586286ce8e239d4b9bbd47d02fb5c7abad6a6ff895ec63fb10c；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03858 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` lines 69-69 VariableDeclaration: pageSize
  - 基线：源语句 sha256=9e3646a51135f666ce346e41f9d1aa81ce94f9164840bafb1975f01c83840288；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03859 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` lines 71-74 VariableDeclaration: queryParams
  - 基线：源语句 sha256=3460ab505a4d4c107439a99383530dab095286fa909c1bb08d2c74e3bafe2b5f；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03860 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` lines 77-84 FunctionDeclaration: getList
  - 基线：源语句 sha256=4f394d8404f1a4b38d6bb8132d4fc49b55dee3dd0951f2abfd2757fe1a4b1498；保留返回、异常及 0 个分支，调用=CallExpression.then, initData。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03861 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` lines 86-89 FunctionDeclaration: handleQuery
  - 基线：源语句 sha256=e8d9075b9b97d11d309b9dc432b606d3f18ff38a3ccd88a2d1ed865013e8f876；保留返回、异常及 0 个分支，调用=getList。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03862 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` lines 91-94 FunctionDeclaration: resetQuery
  - 基线：源语句 sha256=92181fa4359ab7a75cdb4811fb23d7927c816d7cf603e5534064a28e122424e0；保留返回、异常及 0 个分支，调用=proxy.resetForm, handleQuery。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03863 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` lines 96-103 FunctionDeclaration: handleForceLogout
  - 基线：源语句 sha256=9e42e8f1375b03d349aed0a074f4452cbc3ff33e8bf6078c47f2d103444dc058；保留返回、异常及 1 个分支，调用=CallExpression.catch, CallExpression.then, proxy.$modal.confirm, forceLogout, getList, proxy.$modal.msgSuccess。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03864 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` lines 105-105 ExpressionStatement: 
  - 基线：源语句 sha256=e966d3b08f869f7c7962cc988172bf8bc4840aa64d83fa58b0a15b31a76e4d3d；保留返回、异常及 0 个分支，调用=getList。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03865 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template lines 1-58（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03866 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 3: v-bind:model
  - 基线：原表达式：queryParams；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03867 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 3: v-bind:inline
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03868 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 6: v-model:
  - 基线：原表达式：queryParams.ipaddr；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03869 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 10: v-on:keyup
  - 基线：原表达式：handleQuery；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03870 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 15: v-model:
  - 基线：原表达式：queryParams.userName；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03871 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 19: v-on:keyup
  - 基线：原表达式：handleQuery；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03872 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 23: v-on:click
  - 基线：原表达式：handleQuery；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03873 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 24: v-on:click
  - 基线：原表达式：resetQuery；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03874 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 28: v-loading:
  - 基线：原表达式：loading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03875 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 29: v-bind:data
  - 基线：原表达式：onlineList.slice((pageNum - 1) * pageSize, pageNum * pageSize)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03876 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 33: v-slot:default
  - 基线：原表达式：scope；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03877 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 37: v-bind:show-overflow-tooltip
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03878 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 38: v-bind:show-overflow-tooltip
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03879 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 39: v-bind:show-overflow-tooltip
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03880 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 40: v-bind:show-overflow-tooltip
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03881 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 41: v-bind:show-overflow-tooltip
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03882 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 42: v-bind:show-overflow-tooltip
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03883 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 43: v-bind:show-overflow-tooltip
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03884 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 45: v-slot:default
  - 基线：原表达式：scope；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03885 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 50: v-slot:default
  - 基线：原表达式：scope；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03886 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 51: v-on:click
  - 基线：原表达式：handleForceLogout(scope.row)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03887 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 51: v-hasPermi:
  - 基线：原表达式：['monitor:online:forceLogout']；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03888 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 56: v-show:
  - 基线：原表达式：total > 0；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03889 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 56: v-bind:total
  - 基线：原表达式：total；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03890 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 56: v-model:page
  - 基线：原表达式：pageNum；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03891 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template line 56: v-model:limit
  - 基线：原表达式：pageSize；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03892 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template interpolation line 34
  - 基线：原显示表达式：(pageNum - 1) * pageSize + scope.$index + 1
  - 去向：react-front/src/views/monitor/online/index.tsx
- I03893 `ruoyi-fastapi-frontend/src/views/monitor/online/index.vue` template interpolation line 46
  - 基线：原显示表达式：parseTime(scope.row.loginTime)
  - 去向：react-front/src/views/monitor/online/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
