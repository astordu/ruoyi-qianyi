# G297 src/views/system/notice/ReadUsers.vue：完整能力

依赖：G000, G041, G180, G250

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I05848 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` lines 49-49 ImportDeclaration: 
  - 基线：源语句 sha256=e02d65ff577ac9026cd0cf6f3723c9bb4547c7cb653f89b90bed187e13b68aa9；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05849 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` lines 50-50 ImportDeclaration: 
  - 基线：源语句 sha256=f51ee4e2bf68dbe9f6b1e333000e93c8d08c59fa3a2c602c434b440fba41e4ca；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05850 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` lines 52-52 VariableDeclaration: 
  - 基线：源语句 sha256=d3917068104e0f2158733e5e758c09ff6781b09fc4b90611c9a30e2625c695d6；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05851 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` lines 54-54 VariableDeclaration: visible
  - 基线：源语句 sha256=131588e506b10f4b16485c9067fceb50053d9acd0559369303f97aa3a383855a；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05852 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` lines 55-55 VariableDeclaration: loading
  - 基线：源语句 sha256=360133162609dea18ceb29cc60a4fd9166a9ed26b0d8544941212d26502f30ef；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05853 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` lines 56-56 VariableDeclaration: noticeTitle
  - 基线：源语句 sha256=bedd5be34fb9a0b5fb5cc6110bc9bc8093d897e580e9faf18ae843acf31747ba；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05854 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` lines 57-57 VariableDeclaration: total
  - 基线：源语句 sha256=36c446a21d367c0f494c66800724a3ae39f74ae700177cac10f20a7dc41191e0；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05855 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` lines 58-58 VariableDeclaration: userList
  - 基线：源语句 sha256=af803aaf308120af92fc98ad5974f9e46ff096de5735c0e293b4a64e2e6980ed；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05856 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` lines 60-65 VariableDeclaration: queryParams
  - 基线：源语句 sha256=30d1e3d5c4b8c662fad9550a9a9c0a2f19f317d2dd19a0f82f56f901e750e3cb；保留返回、异常及 0 个分支，调用=reactive。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05857 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` lines 67-74 FunctionDeclaration: open
  - 基线：源语句 sha256=8730d88aeeee4b5243e020fb2f02e28e906b904c15b83f19e440507985b47bab；保留返回、异常及 0 个分支，调用=getList。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05858 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` lines 76-84 FunctionDeclaration: getList
  - 基线：源语句 sha256=8ae8e3a5d2fbef0076c855c1c5061cb8770e0888b9d72941a98a2bca8bc16311；保留返回、异常及 0 个分支，调用=CallExpression.finally, CallExpression.then, listNoticeReadUsers。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05859 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` lines 86-89 FunctionDeclaration: handleQuery
  - 基线：源语句 sha256=9c96c5a1719f709178a9408a0e7b3b5dc305a30bcad5a85b8705e82e15b9888f；保留返回、异常及 0 个分支，调用=getList。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05860 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` lines 91-94 FunctionDeclaration: resetQuery
  - 基线：源语句 sha256=3f89b3b7618db423a3284447eb4c7468fddd9114fb8247c2462a1d854b69a60a；保留返回、异常及 0 个分支，调用=proxy.resetForm, handleQuery。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05861 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` lines 96-100 FunctionDeclaration: handleClose
  - 基线：源语句 sha256=06448244dbf97d73b26b25517a550712a230e780eff04868dc4ff7c43ed620f7；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05862 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` lines 102-104 ExpressionStatement: 
  - 基线：源语句 sha256=64705ef294d9f2ca1192d1c35cd3874553f37329b77d7c9615d5c7fbc3aae3a4；保留返回、异常及 0 个分支，调用=defineExpose。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05863 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template lines 1-46（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05864 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 2: v-model:
  - 基线：原表达式：visible；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05865 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 2: v-bind:title
  - 基线：原表达式：`「${noticeTitle}」已读用户`；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05866 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 2: v-on:close
  - 基线：原表达式：handleClose；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05867 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 3: v-bind:model
  - 基线：原表达式：queryParams；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05868 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 3: v-bind:inline
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05869 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 6: v-model:
  - 基线：原表达式：queryParams.searchValue；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05870 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 9: v-bind:prefix-icon
  - 基线：原表达式：Search；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05871 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 11: v-on:keyup
  - 基线：原表达式：handleQuery；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05872 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 12: v-on:clear
  - 基线：原表达式：handleQuery；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05873 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 16: v-on:click
  - 基线：原表达式：handleQuery；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05874 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 17: v-on:click
  - 基线：原表达式：resetQuery；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05875 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 25: v-loading:
  - 基线：原表达式：loading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05876 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 25: v-bind:data
  - 基线：原表达式：userList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05877 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 27: v-bind:show-overflow-tooltip
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05878 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 28: v-bind:show-overflow-tooltip
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05879 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 29: v-bind:show-overflow-tooltip
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05880 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 32: v-slot:default
  - 基线：原表达式：scope；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05881 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 38: v-show:
  - 基线：原表达式：total > 0；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05882 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 39: v-bind:total
  - 基线：原表达式：total；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05883 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 40: v-model:page
  - 基线：原表达式：queryParams.pageNum；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05884 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 41: v-model:limit
  - 基线：原表达式：queryParams.pageSize；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05885 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template line 42: v-on:pagination
  - 基线：原表达式：getList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05886 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template interpolation line 21
  - 基线：原显示表达式：total
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05887 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` template interpolation line 33
  - 基线：原显示表达式：parseTime(scope.row.readTime)
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx
- I05888 `ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue` style[0] lines 107-118
  - 基线：保留全部选择器、声明和 url；lang=css, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/views/system/notice/ReadUsers.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
