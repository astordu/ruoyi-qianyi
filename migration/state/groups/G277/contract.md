# G277 src/views/register.vue：完整能力

依赖：G000, G025, G187, G222, G245

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I04307 `ruoyi-fastapi-frontend/src/views/register.vue` lines 79-79 ImportDeclaration: 
  - 基线：源语句 sha256=95a861e76707a7d078dda0720dbe6f73f55c8a12785223fb9606535795ce573a；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/register.tsx
- I04308 `ruoyi-fastapi-frontend/src/views/register.vue` lines 80-80 ImportDeclaration: 
  - 基线：源语句 sha256=9e6117299f5e18b1ad26852dd53089c63ff99bc1e887e67ca50cd7d07ccc1751；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/register.tsx
- I04309 `ruoyi-fastapi-frontend/src/views/register.vue` lines 81-81 ImportDeclaration: 
  - 基线：源语句 sha256=c9c128b54ab88c97d92ae51e2a1065c1ade8d91f9c9c2e9070a7b4c15774f713；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/register.tsx
- I04310 `ruoyi-fastapi-frontend/src/views/register.vue` lines 82-82 ImportDeclaration: 
  - 基线：源语句 sha256=9e7caad4ddde694df2576991b895ec8efd58a3b552f365319292392a1e88f0e8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/register.tsx
- I04311 `ruoyi-fastapi-frontend/src/views/register.vue` lines 84-84 VariableDeclaration: title
  - 基线：源语句 sha256=02222f0009b239b60ede837919ce88126a7b40cb72e40af1c600484384a02e71；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/register.tsx
- I04312 `ruoyi-fastapi-frontend/src/views/register.vue` lines 85-85 VariableDeclaration: footerContent
  - 基线：源语句 sha256=3e88c7e4c67413b1ab6b4c1dd3367608df8cc696b0ce3bc9999ad8f073e00f01；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/register.tsx
- I04313 `ruoyi-fastapi-frontend/src/views/register.vue` lines 86-86 VariableDeclaration: router
  - 基线：源语句 sha256=5921d8bbcfc7da27a18289d8a47cc51136866f8fdbebe22e9d1d1135aa55e0e6；保留返回、异常及 0 个分支，调用=useRouter。
  - 去向：react-front/src/views/register.tsx
- I04314 `ruoyi-fastapi-frontend/src/views/register.vue` lines 87-87 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/views/register.tsx
- I04315 `ruoyi-fastapi-frontend/src/views/register.vue` lines 88-88 VariableDeclaration: 
  - 基线：源语句 sha256=aa200969019e1d7095d80d33f098179cc0f14de204952d1783febb5e6d9d5560；保留返回、异常及 0 个分支，调用=usePasswordRule。
  - 去向：react-front/src/views/register.tsx
- I04316 `ruoyi-fastapi-frontend/src/views/register.vue` lines 90-96 VariableDeclaration: registerForm
  - 基线：源语句 sha256=f7460eef9567f5c5b51cc95498cda543ce237cecaad1106390b4656212271bdf；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/register.tsx
- I04317 `ruoyi-fastapi-frontend/src/views/register.vue` lines 98-104 VariableDeclaration: equalToPassword
  - 基线：源语句 sha256=64d643406fe7247055dc5b8f15f00708cbb187176a4edaff983e61d9e5aa946b；保留返回、异常及 1 个分支，调用=callback。
  - 去向：react-front/src/views/register.tsx
- I04318 `ruoyi-fastapi-frontend/src/views/register.vue` lines 106-116 VariableDeclaration: registerRules
  - 基线：源语句 sha256=f3739f6f06869766def24f4dd5dc65412456e2f696561401b11bcba9f2a475dd；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/register.tsx
- I04319 `ruoyi-fastapi-frontend/src/views/register.vue` lines 118-118 VariableDeclaration: codeUrl
  - 基线：源语句 sha256=c816eb23f867d8a69a5cbbae3767a4c0bf60d598c65c31da0e27e8ea8b949947；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/register.tsx
- I04320 `ruoyi-fastapi-frontend/src/views/register.vue` lines 119-119 VariableDeclaration: loading
  - 基线：源语句 sha256=0f2d86fe0699597a69087a478d5543264e008a02dbd9826dd2138c7409858393；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/register.tsx
- I04321 `ruoyi-fastapi-frontend/src/views/register.vue` lines 120-120 VariableDeclaration: captchaEnabled
  - 基线：源语句 sha256=1f09801e6be8934723cafc392a162dbda559383f0eb1f725973527e77e03269b；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/register.tsx
- I04322 `ruoyi-fastapi-frontend/src/views/register.vue` lines 122-142 FunctionDeclaration: handleRegister
  - 基线：源语句 sha256=aa09c39bc06915c3ff60610ad22381bbbb8a564b6348647fd55e687bdddffd56；保留返回、异常及 2 个分支，调用=proxy.$refs.registerRef.validate, CallExpression.catch, CallExpression.then, register, ElMessageBox.alert, router.push, getCode。
  - 去向：react-front/src/views/register.tsx
- I04323 `ruoyi-fastapi-frontend/src/views/register.vue` lines 144-152 FunctionDeclaration: getCode
  - 基线：源语句 sha256=14203628578651f42c1a77839505b6474b8737f0f3f5373b4e71410b8952111f；保留返回、异常及 2 个分支，调用=CallExpression.then, getCodeImg。
  - 去向：react-front/src/views/register.tsx
- I04324 `ruoyi-fastapi-frontend/src/views/register.vue` lines 154-154 ExpressionStatement: 
  - 基线：源语句 sha256=d959f4e7d064ea3e535de52d7d75e0eb2d9b09f1b828453cc370820286f49ec7；保留返回、异常及 0 个分支，调用=getCode。
  - 去向：react-front/src/views/register.tsx
- I04325 `ruoyi-fastapi-frontend/src/views/register.vue` template lines 1-76（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/register.tsx
- I04326 `ruoyi-fastapi-frontend/src/views/register.vue` template line 3: v-bind:model
  - 基线：原表达式：registerForm；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04327 `ruoyi-fastapi-frontend/src/views/register.vue` template line 3: v-bind:rules
  - 基线：原表达式：registerRules；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04328 `ruoyi-fastapi-frontend/src/views/register.vue` template line 7: v-model:
  - 基线：原表达式：registerForm.username；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04329 `ruoyi-fastapi-frontend/src/views/register.vue` template line 13: v-slot:prefix
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04330 `ruoyi-fastapi-frontend/src/views/register.vue` template line 16: v-bind:rules
  - 基线：原表达式：registerPwdValidator；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04331 `ruoyi-fastapi-frontend/src/views/register.vue` template line 18: v-model:
  - 基线：原表达式：registerForm.password；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04332 `ruoyi-fastapi-frontend/src/views/register.vue` template line 23: v-on:keyup
  - 基线：原表达式：handleRegister；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04333 `ruoyi-fastapi-frontend/src/views/register.vue` template line 25: v-slot:prefix
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04334 `ruoyi-fastapi-frontend/src/views/register.vue` template line 30: v-model:
  - 基线：原表达式：registerForm.confirmPassword；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04335 `ruoyi-fastapi-frontend/src/views/register.vue` template line 35: v-on:keyup
  - 基线：原表达式：handleRegister；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04336 `ruoyi-fastapi-frontend/src/views/register.vue` template line 37: v-slot:prefix
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04337 `ruoyi-fastapi-frontend/src/views/register.vue` template line 40: v-if:
  - 基线：原表达式：captchaEnabled；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04338 `ruoyi-fastapi-frontend/src/views/register.vue` template line 43: v-model:
  - 基线：原表达式：registerForm.code；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04339 `ruoyi-fastapi-frontend/src/views/register.vue` template line 47: v-on:keyup
  - 基线：原表达式：handleRegister；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04340 `ruoyi-fastapi-frontend/src/views/register.vue` template line 49: v-slot:prefix
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04341 `ruoyi-fastapi-frontend/src/views/register.vue` template line 52: v-bind:src
  - 基线：原表达式：codeUrl；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04342 `ruoyi-fastapi-frontend/src/views/register.vue` template line 52: v-on:click
  - 基线：原表达式：getCode；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04343 `ruoyi-fastapi-frontend/src/views/register.vue` template line 57: v-bind:loading
  - 基线：原表达式：loading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04344 `ruoyi-fastapi-frontend/src/views/register.vue` template line 61: v-on:click
  - 基线：原表达式：handleRegister；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04345 `ruoyi-fastapi-frontend/src/views/register.vue` template line 63: v-if:
  - 基线：原表达式：!loading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04346 `ruoyi-fastapi-frontend/src/views/register.vue` template line 64: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04347 `ruoyi-fastapi-frontend/src/views/register.vue` template line 67: v-bind:to
  - 基线：原表达式：'/login'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/register.tsx
- I04348 `ruoyi-fastapi-frontend/src/views/register.vue` template interpolation line 4
  - 基线：原显示表达式：title
  - 去向：react-front/src/views/register.tsx
- I04349 `ruoyi-fastapi-frontend/src/views/register.vue` template interpolation line 73
  - 基线：原显示表达式：footerContent
  - 去向：react-front/src/views/register.tsx
- I04350 `ruoyi-fastapi-frontend/src/views/register.vue` style[0] lines 157-219
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/views/register.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
