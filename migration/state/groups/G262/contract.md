# G262 src/views/login.vue：完整能力

依赖：G000, G025, G187, G222, G230, G244

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I03091 `ruoyi-fastapi-frontend/src/views/login.vue` lines 68-68 ImportDeclaration: 
  - 基线：源语句 sha256=5f4b4bca4c504f63c6cfc86f1e4b7ba8a1681464ce31f6dbc69dcde95c760923；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/login.tsx
- I03092 `ruoyi-fastapi-frontend/src/views/login.vue` lines 69-69 ImportDeclaration: 
  - 基线：源语句 sha256=4ac01d15c2c924737aefcd342c6e314024c73effe70259e27ce7204f182229c3；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/login.tsx
- I03093 `ruoyi-fastapi-frontend/src/views/login.vue` lines 70-70 ImportDeclaration: 
  - 基线：源语句 sha256=5be0e000904982acbb93bf8ba86e000d108a97950027c912883b2b6d7dbe3928；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/login.tsx
- I03094 `ruoyi-fastapi-frontend/src/views/login.vue` lines 71-71 ImportDeclaration: 
  - 基线：源语句 sha256=c351978f324903ca33541ef37b2b07118aae76a82edaab040cb71996f923341f；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/login.tsx
- I03095 `ruoyi-fastapi-frontend/src/views/login.vue` lines 72-72 ImportDeclaration: 
  - 基线：源语句 sha256=c9c128b54ab88c97d92ae51e2a1065c1ade8d91f9c9c2e9070a7b4c15774f713；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/login.tsx
- I03096 `ruoyi-fastapi-frontend/src/views/login.vue` lines 74-74 VariableDeclaration: title
  - 基线：源语句 sha256=02222f0009b239b60ede837919ce88126a7b40cb72e40af1c600484384a02e71；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/login.tsx
- I03097 `ruoyi-fastapi-frontend/src/views/login.vue` lines 75-75 VariableDeclaration: footerContent
  - 基线：源语句 sha256=3e88c7e4c67413b1ab6b4c1dd3367608df8cc696b0ce3bc9999ad8f073e00f01；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/login.tsx
- I03098 `ruoyi-fastapi-frontend/src/views/login.vue` lines 76-76 VariableDeclaration: userStore
  - 基线：源语句 sha256=21eb42d5aa135e6ffd33998f9b7f8924e85e1259d2572f4a34415ca53d396344；保留返回、异常及 0 个分支，调用=useUserStore。
  - 去向：react-front/src/views/login.tsx
- I03099 `ruoyi-fastapi-frontend/src/views/login.vue` lines 77-77 VariableDeclaration: route
  - 基线：源语句 sha256=19ffaf888604ba2654aa25f29ba0210e96226ea7089e9e15dc5c05cf276b3a9f；保留返回、异常及 0 个分支，调用=useRoute。
  - 去向：react-front/src/views/login.tsx
- I03100 `ruoyi-fastapi-frontend/src/views/login.vue` lines 78-78 VariableDeclaration: router
  - 基线：源语句 sha256=5921d8bbcfc7da27a18289d8a47cc51136866f8fdbebe22e9d1d1135aa55e0e6；保留返回、异常及 0 个分支，调用=useRouter。
  - 去向：react-front/src/views/login.tsx
- I03101 `ruoyi-fastapi-frontend/src/views/login.vue` lines 79-79 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/views/login.tsx
- I03102 `ruoyi-fastapi-frontend/src/views/login.vue` lines 81-87 VariableDeclaration: loginForm
  - 基线：源语句 sha256=7c8848f42f9bcc80b9430dd26b8dfc3728281f6c8b9ddef0df663f763e61d3d7；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/login.tsx
- I03103 `ruoyi-fastapi-frontend/src/views/login.vue` lines 89-93 VariableDeclaration: loginRules
  - 基线：源语句 sha256=3facdedcc1ad88e0ee4bc82646f23f0364b058e54fcb38eba9ae1b9dc42410ee；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/login.tsx
- I03104 `ruoyi-fastapi-frontend/src/views/login.vue` lines 95-95 VariableDeclaration: codeUrl
  - 基线：源语句 sha256=c816eb23f867d8a69a5cbbae3767a4c0bf60d598c65c31da0e27e8ea8b949947；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/login.tsx
- I03105 `ruoyi-fastapi-frontend/src/views/login.vue` lines 96-96 VariableDeclaration: loading
  - 基线：源语句 sha256=0f2d86fe0699597a69087a478d5543264e008a02dbd9826dd2138c7409858393；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/login.tsx
- I03106 `ruoyi-fastapi-frontend/src/views/login.vue` lines 98-98 VariableDeclaration: captchaEnabled
  - 基线：源语句 sha256=1f09801e6be8934723cafc392a162dbda559383f0eb1f725973527e77e03269b；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/login.tsx
- I03107 `ruoyi-fastapi-frontend/src/views/login.vue` lines 100-100 VariableDeclaration: register
  - 基线：源语句 sha256=109f1a06cdcabfa54f40479fde9bb77f234d5aaa80ff69a3b4ae36a571e6e1f3；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/login.tsx
- I03108 `ruoyi-fastapi-frontend/src/views/login.vue` lines 101-101 VariableDeclaration: redirect
  - 基线：源语句 sha256=58891d982dba9d94b1b9a4cc8902df10c9803e38a3ca2afa713661de267457f1；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/login.tsx
- I03109 `ruoyi-fastapi-frontend/src/views/login.vue` lines 103-105 ExpressionStatement: 
  - 基线：源语句 sha256=119a4533a2f359c1eaf1920e074471844eadc999f2a10e1f74beb54c459344b1；保留返回、异常及 1 个分支，调用=watch。
  - 去向：react-front/src/views/login.tsx
- I03110 `ruoyi-fastapi-frontend/src/views/login.vue` lines 107-141 FunctionDeclaration: handleLogin
  - 基线：源语句 sha256=699afcfb9f2188ec02fc791914b510c171775b1bb91b20a8adfd01ebad095e1a；保留返回、异常及 6 个分支，调用=proxy.$refs.loginRef.validate, Cookies.set, encrypt, Cookies.remove, CallExpression.catch, CallExpression.then, userStore.login, CallExpression.reduce, Object.keys, router.push, getCode。
  - 去向：react-front/src/views/login.tsx
- I03111 `ruoyi-fastapi-frontend/src/views/login.vue` lines 143-152 FunctionDeclaration: getCode
  - 基线：源语句 sha256=20941fa8fe074f3f68ade809b6b9d5121b787333b2a1035115a6e74930257dcc；保留返回、异常及 3 个分支，调用=CallExpression.then, getCodeImg。
  - 去向：react-front/src/views/login.tsx
- I03112 `ruoyi-fastapi-frontend/src/views/login.vue` lines 154-163 FunctionDeclaration: getCookie
  - 基线：源语句 sha256=b29ac6590d81ec1b3ad607e58d64e540f500fc68b1a24140a8731551701e268e；保留返回、异常及 3 个分支，调用=Cookies.get, decrypt, Boolean。
  - 去向：react-front/src/views/login.tsx
- I03113 `ruoyi-fastapi-frontend/src/views/login.vue` lines 165-165 ExpressionStatement: 
  - 基线：源语句 sha256=d959f4e7d064ea3e535de52d7d75e0eb2d9b09f1b828453cc370820286f49ec7；保留返回、异常及 0 个分支，调用=getCode。
  - 去向：react-front/src/views/login.tsx
- I03114 `ruoyi-fastapi-frontend/src/views/login.vue` lines 166-166 ExpressionStatement: 
  - 基线：源语句 sha256=04b9ef129c4aa9740f112d10aa6308dd0d59be14bc2ada9459c8aad4cff88cc5；保留返回、异常及 0 个分支，调用=getCookie。
  - 去向：react-front/src/views/login.tsx
- I03115 `ruoyi-fastapi-frontend/src/views/login.vue` template lines 1-65（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/login.tsx
- I03116 `ruoyi-fastapi-frontend/src/views/login.vue` template line 3: v-bind:model
  - 基线：原表达式：loginForm；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/login.tsx
- I03117 `ruoyi-fastapi-frontend/src/views/login.vue` template line 3: v-bind:rules
  - 基线：原表达式：loginRules；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/login.tsx
- I03118 `ruoyi-fastapi-frontend/src/views/login.vue` template line 7: v-model:
  - 基线：原表达式：loginForm.username；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/login.tsx
- I03119 `ruoyi-fastapi-frontend/src/views/login.vue` template line 13: v-slot:prefix
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/login.tsx
- I03120 `ruoyi-fastapi-frontend/src/views/login.vue` template line 18: v-model:
  - 基线：原表达式：loginForm.password；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/login.tsx
- I03121 `ruoyi-fastapi-frontend/src/views/login.vue` template line 23: v-on:keyup
  - 基线：原表达式：handleLogin；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/login.tsx
- I03122 `ruoyi-fastapi-frontend/src/views/login.vue` template line 25: v-slot:prefix
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/login.tsx
- I03123 `ruoyi-fastapi-frontend/src/views/login.vue` template line 28: v-if:
  - 基线：原表达式：captchaEnabled；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/login.tsx
- I03124 `ruoyi-fastapi-frontend/src/views/login.vue` template line 30: v-model:
  - 基线：原表达式：loginForm.code；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/login.tsx
- I03125 `ruoyi-fastapi-frontend/src/views/login.vue` template line 35: v-on:keyup
  - 基线：原表达式：handleLogin；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/login.tsx
- I03126 `ruoyi-fastapi-frontend/src/views/login.vue` template line 37: v-slot:prefix
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/login.tsx
- I03127 `ruoyi-fastapi-frontend/src/views/login.vue` template line 40: v-bind:src
  - 基线：原表达式：codeUrl；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/login.tsx
- I03128 `ruoyi-fastapi-frontend/src/views/login.vue` template line 40: v-on:click
  - 基线：原表达式：getCode；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/login.tsx
- I03129 `ruoyi-fastapi-frontend/src/views/login.vue` template line 43: v-model:
  - 基线：原表达式：loginForm.rememberMe；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/login.tsx
- I03130 `ruoyi-fastapi-frontend/src/views/login.vue` template line 46: v-bind:loading
  - 基线：原表达式：loading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/login.tsx
- I03131 `ruoyi-fastapi-frontend/src/views/login.vue` template line 50: v-on:click
  - 基线：原表达式：handleLogin；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/login.tsx
- I03132 `ruoyi-fastapi-frontend/src/views/login.vue` template line 52: v-if:
  - 基线：原表达式：!loading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/login.tsx
- I03133 `ruoyi-fastapi-frontend/src/views/login.vue` template line 53: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/login.tsx
- I03134 `ruoyi-fastapi-frontend/src/views/login.vue` template line 55: v-if:
  - 基线：原表达式：register；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/login.tsx
- I03135 `ruoyi-fastapi-frontend/src/views/login.vue` template line 56: v-bind:to
  - 基线：原表达式：'/register'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/login.tsx
- I03136 `ruoyi-fastapi-frontend/src/views/login.vue` template interpolation line 4
  - 基线：原显示表达式：title
  - 去向：react-front/src/views/login.tsx
- I03137 `ruoyi-fastapi-frontend/src/views/login.vue` template interpolation line 62
  - 基线：原显示表达式：footerContent
  - 去向：react-front/src/views/login.tsx
- I03138 `ruoyi-fastapi-frontend/src/views/login.vue` style[0] lines 169-243
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/views/login.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
