# G312 src/views/system/user/profile/resetPwd.vue：完整能力

依赖：G000, G045, G245

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I07606 `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` lines 20-20 ImportDeclaration: 
  - 基线：源语句 sha256=5bd645450abdc3cf121741837838eeca960201472f0941de1cc2eb30ad4b2975；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/profile/resetPwd.tsx
- I07607 `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` lines 21-21 ImportDeclaration: 
  - 基线：源语句 sha256=54debe3ce674c107e6758e09765946e3128dae9b7016047acb60c2678f604665；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/profile/resetPwd.tsx
- I07608 `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` lines 23-23 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/views/system/user/profile/resetPwd.tsx
- I07609 `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` lines 24-24 VariableDeclaration: 
  - 基线：源语句 sha256=55d7777b1f4724244ba5303ac014cd0b7111b4faee4057231d0587d779fbe8b0；保留返回、异常及 0 个分支，调用=usePasswordRule。
  - 去向：react-front/src/views/system/user/profile/resetPwd.tsx
- I07610 `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` lines 26-30 VariableDeclaration: user
  - 基线：源语句 sha256=0ad435bf2c7dbb9b56478971193b29594258fa355f14f6c238ba2c8887570a5c；保留返回、异常及 0 个分支，调用=reactive。
  - 去向：react-front/src/views/system/user/profile/resetPwd.tsx
- I07611 `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` lines 32-38 VariableDeclaration: equalToPassword
  - 基线：源语句 sha256=ec3904aba36cdc011ba7ff3d0b63120ce820cfda3e776dd7bf87c3f0d92b94af；保留返回、异常及 1 个分支，调用=callback。
  - 去向：react-front/src/views/system/user/profile/resetPwd.tsx
- I07612 `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` lines 39-42 VariableDeclaration: rules
  - 基线：源语句 sha256=37cdd53c1228ccac3f110b5600fe418c382e4cae83941a9f6697436b07ef18e8；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/profile/resetPwd.tsx
- I07613 `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` lines 45-53 FunctionDeclaration: submit
  - 基线：源语句 sha256=f337369e4b2c0affd707c8e2d565bb949894755d6509d8198da987f302c54db4；保留返回、异常及 1 个分支，调用=proxy.$refs.pwdRef.validate, CallExpression.then, updateUserPwd, proxy.$modal.msgSuccess。
  - 去向：react-front/src/views/system/user/profile/resetPwd.tsx
- I07614 `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` lines 53-53 EmptyStatement: 
  - 基线：源语句 sha256=41b805ea7ac014e23556e98bb374702a08344268f92489a02f0880849394a1e4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/profile/resetPwd.tsx
- I07615 `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` lines 55-57 FunctionDeclaration: close
  - 基线：源语句 sha256=0820ce7fb0ee428426bc0c0722cf5d7093569826bc53547d32f25d374d85ddb7；保留返回、异常及 0 个分支，调用=proxy.$tab.closePage。
  - 去向：react-front/src/views/system/user/profile/resetPwd.tsx
- I07616 `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` lines 57-57 EmptyStatement: 
  - 基线：源语句 sha256=41b805ea7ac014e23556e98bb374702a08344268f92489a02f0880849394a1e4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/profile/resetPwd.tsx
- I07617 `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` template lines 1-17（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/system/user/profile/resetPwd.tsx
- I07618 `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` template line 2: v-bind:model
  - 基线：原表达式：user；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/resetPwd.tsx
- I07619 `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` template line 2: v-bind:rules
  - 基线：原表达式：rules；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/resetPwd.tsx
- I07620 `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` template line 4: v-model:
  - 基线：原表达式：user.oldPassword；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/resetPwd.tsx
- I07621 `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` template line 6: v-bind:rules
  - 基线：原表达式：infoPwdValidator；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/resetPwd.tsx
- I07622 `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` template line 7: v-model:
  - 基线：原表达式：user.newPassword；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/resetPwd.tsx
- I07623 `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` template line 10: v-model:
  - 基线：原表达式：user.confirmPassword；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/resetPwd.tsx
- I07624 `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` template line 13: v-on:click
  - 基线：原表达式：submit；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/resetPwd.tsx
- I07625 `ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue` template line 14: v-on:click
  - 基线：原表达式：close；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/resetPwd.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
