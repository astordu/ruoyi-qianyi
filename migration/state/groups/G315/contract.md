# G315 src/views/system/user/profile/userInfo.vue：完整能力

依赖：G000, G045

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I07740 `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` lines 26-26 ImportDeclaration: 
  - 基线：源语句 sha256=77b8fa3b95b8b96bd5141c117de9b50e2a88f9478918d6e249c02af2f06fa67c；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/profile/userInfo.tsx
- I07741 `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` lines 28-32 VariableDeclaration: props
  - 基线：源语句 sha256=b8d1c1cc34abebd61c72e4975af1a01cd322490940e9082ef3a5e224e6e42125；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/views/system/user/profile/userInfo.tsx
- I07742 `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` lines 34-34 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/views/system/user/profile/userInfo.tsx
- I07743 `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` lines 36-36 VariableDeclaration: form
  - 基线：源语句 sha256=51c1b4cff3a752a571645a777c81e184f8608a1aba2a688e088e7e0b059ee3e5；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/profile/userInfo.tsx
- I07744 `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` lines 37-41 VariableDeclaration: rules
  - 基线：源语句 sha256=550edaf924b8f602306cf674ce225ea69e47f9de3653c0f1f607acacde4295cf；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/profile/userInfo.tsx
- I07745 `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` lines 44-54 FunctionDeclaration: submit
  - 基线：源语句 sha256=2fa97de50302806904bbd83474aff0043fdb847d78bd8922c82ab09fa05fe934；保留返回、异常及 1 个分支，调用=proxy.$refs.userRef.validate, CallExpression.then, updateUserProfile, proxy.$modal.msgSuccess。
  - 去向：react-front/src/views/system/user/profile/userInfo.tsx
- I07746 `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` lines 54-54 EmptyStatement: 
  - 基线：源语句 sha256=41b805ea7ac014e23556e98bb374702a08344268f92489a02f0880849394a1e4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/profile/userInfo.tsx
- I07747 `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` lines 57-59 FunctionDeclaration: close
  - 基线：源语句 sha256=0820ce7fb0ee428426bc0c0722cf5d7093569826bc53547d32f25d374d85ddb7；保留返回、异常及 0 个分支，调用=proxy.$tab.closePage。
  - 去向：react-front/src/views/system/user/profile/userInfo.tsx
- I07748 `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` lines 59-59 EmptyStatement: 
  - 基线：源语句 sha256=41b805ea7ac014e23556e98bb374702a08344268f92489a02f0880849394a1e4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/profile/userInfo.tsx
- I07749 `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` lines 62-66 ExpressionStatement: 
  - 基线：源语句 sha256=09bef42ba987091984916421d7fe72901888886bfe96a62d8e60a2728a24cdac；保留返回、异常及 1 个分支，调用=watch。
  - 去向：react-front/src/views/system/user/profile/userInfo.tsx
- I07750 `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` template lines 1-23（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/system/user/profile/userInfo.tsx
- I07751 `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` template line 2: v-bind:model
  - 基线：原表达式：form；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/userInfo.tsx
- I07752 `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` template line 2: v-bind:rules
  - 基线：原表达式：rules；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/userInfo.tsx
- I07753 `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` template line 4: v-model:
  - 基线：原表达式：form.nickName；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/userInfo.tsx
- I07754 `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` template line 7: v-model:
  - 基线：原表达式：form.phonenumber；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/userInfo.tsx
- I07755 `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` template line 10: v-model:
  - 基线：原表达式：form.email；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/userInfo.tsx
- I07756 `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` template line 13: v-model:
  - 基线：原表达式：form.sex；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/userInfo.tsx
- I07757 `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` template line 19: v-on:click
  - 基线：原表达式：submit；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/userInfo.tsx
- I07758 `ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue` template line 20: v-on:click
  - 基线：原表达式：close；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/userInfo.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
