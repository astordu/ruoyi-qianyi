# G261 src/views/lock.vue：完整能力

依赖：G000, G025, G147, G226, G230, G253F033

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I03046 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 37-37 ImportDeclaration: 
  - 基线：源语句 sha256=a6a65e625626f94a2a642dcd55861a80c6cc9fe9dd70db2abc961e81710b82c4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/lock.tsx
- I03047 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 38-38 ImportDeclaration: 
  - 基线：源语句 sha256=c351978f324903ca33541ef37b2b07118aae76a82edaab040cb71996f923341f；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/lock.tsx
- I03048 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 39-39 ImportDeclaration: 
  - 基线：源语句 sha256=56bc4c9061f8b753cafaec1815dba7fb04ce0a7503190381a9e1126f5fb1cfd0；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/lock.tsx
- I03049 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 40-40 ImportDeclaration: 
  - 基线：源语句 sha256=30a7b100d5d3786c074aa7c977d2cb540f3053e80973f2ca1250a232585606b3；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/lock.tsx
- I03050 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 41-41 ImportDeclaration: 
  - 基线：源语句 sha256=f2c3ea9218322e89dc8d9ea031dbdffda0e5289f328a390fd5ecd276f36e7d84；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/lock.tsx
- I03051 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 42-42 ImportDeclaration: 
  - 基线：源语句 sha256=0cee6614fb11d313969b4a24630b3fadded7f957271e8a0d37792b9e63edf564；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/lock.tsx
- I03052 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 44-44 VariableDeclaration: router
  - 基线：源语句 sha256=4493bc84540aad888c32c80251d8de79e93d311f4a9a11bb353ecaee4838a473；保留返回、异常及 0 个分支，调用=useRouter。
  - 去向：react-front/src/views/lock.tsx
- I03053 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 45-45 VariableDeclaration: userStore
  - 基线：源语句 sha256=1251336d9bdee09ff9fca3bb6abee75e79e3848e2049264fdca9e1b18043734d；保留返回、异常及 0 个分支，调用=useUserStore。
  - 去向：react-front/src/views/lock.tsx
- I03054 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 46-46 VariableDeclaration: lockStore
  - 基线：源语句 sha256=bc93fde5ad65cf9ac53e9d9aad86631c54c3aef810ab598737acaf3a42babb90；保留返回、异常及 0 个分支，调用=useLockStore。
  - 去向：react-front/src/views/lock.tsx
- I03055 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 48-48 VariableDeclaration: password
  - 基线：源语句 sha256=8ded76aaad6a765ca0dc3e3cd6931d9b525bf3d7d42bef03b989fe60ea8ac498；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/lock.tsx
- I03056 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 49-49 VariableDeclaration: loading
  - 基线：源语句 sha256=360133162609dea18ceb29cc60a4fd9166a9ed26b0d8544941212d26502f30ef；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/lock.tsx
- I03057 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 50-50 VariableDeclaration: errorMsg
  - 基线：源语句 sha256=38ade668d1fa1ccb6214b15498f8f4bfcd8bfcfcb60d297ed7399004e7fc22c7；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/lock.tsx
- I03058 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 51-51 VariableDeclaration: isShaking
  - 基线：源语句 sha256=4239f93a4cbf0a0641c034636f687f642d834a64a3802eb456dbb293e7f81af4；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/lock.tsx
- I03059 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 52-52 VariableDeclaration: currentTime
  - 基线：源语句 sha256=9858ab454399853fb2b311931abfc1a9251ac47222fb95360e0ec2017a82eb28；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/lock.tsx
- I03060 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 53-53 VariableDeclaration: currentDate
  - 基线：源语句 sha256=e34654aeb86f5359a74ac67e13c17e116753e773717b74959d9f16a6218787c5；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/lock.tsx
- I03061 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 54-54 VariableDeclaration: passwordInput
  - 基线：源语句 sha256=594ace9847cc648796496279578527b5be56da562a52dacf62a683046460c5c6；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/lock.tsx
- I03062 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 55-55 VariableDeclaration: particleCanvas
  - 基线：源语句 sha256=3b1635889d59b176c13c71f394a3cdd45f8745370f181153152696622e83cb1d；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/lock.tsx
- I03063 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 57-57 VariableDeclaration: timer
  - 基线：源语句 sha256=0ec34b38f5d15b2c7bc1b357de2851fe86ae67dae01a711541b2a03d31f6c9fb；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/lock.tsx
- I03064 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 58-58 VariableDeclaration: animationId
  - 基线：源语句 sha256=27b8eca7a1497a9b9204d63a38cd8bb6e4fd2e539535733ea45f86706cd89bce；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/lock.tsx
- I03065 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 59-59 VariableDeclaration: particles
  - 基线：源语句 sha256=4389111af1c9fe5f48e09a5486e5e7a822a9abb68753b060d6ccd588d0c1ee63；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/lock.tsx
- I03066 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 61-63 VariableDeclaration: onAvatarError
  - 基线：源语句 sha256=7a3d228eca191cbeaadd7f9593489cc9d048a1473e1a6bd4109495a35d9cb82c；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/lock.tsx
- I03067 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 65-73 VariableDeclaration: startClock
  - 基线：源语句 sha256=4f138d9c81a69ff8467c7a5618c420e3beb155fbac5f2033a0edd462a0070005；保留返回、异常及 0 个分支，调用=formatBusinessTime, update, setInterval。
  - 去向：react-front/src/views/lock.tsx
- I03068 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 75-95 VariableDeclaration: handleUnlock
  - 基线：源语句 sha256=762702a19bc81b9ae7f02e0ee0359b930a873999f5080e4648afd23a2b1dbdf5；保留返回、异常及 4 个分支，调用=showError, unlockScreen, lockStore.unlockScreen, router.replace, err.toString, nextTick, passwordInput.value.focus。
  - 去向：react-front/src/views/lock.tsx
- I03069 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 97-101 VariableDeclaration: showError
  - 基线：源语句 sha256=32aa4e190a28ee620b6c9452249c1aebef7615096ff8d190df9dcea0011d5bdf；保留返回、异常及 0 个分支，调用=setTimeout。
  - 去向：react-front/src/views/lock.tsx
- I03070 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 103-108 VariableDeclaration: goLogin
  - 基线：源语句 sha256=ca1c95800cdc4cca5ef3975dac7de8f6f43f3bc4ae0c92d54181b7851b62b8ea；保留返回、异常及 0 个分支，调用=lockStore.unlockScreen, CallExpression.then, userStore.logOut, router.push。
  - 去向：react-front/src/views/lock.tsx
- I03071 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 110-159 VariableDeclaration: initParticles
  - 基线：源语句 sha256=c21247420f3d3e61938e194e1350569dd727d5a98707df2fc2b5e54996db66c7；保留返回、异常及 7 个分支，调用=canvas.getContext, resize, window.addEventListener, Array.from, Math.random, ctx.clearRect, particles.forEach, ctx.beginPath, ctx.arc, ctx.fill, Math.hypot, ctx.moveTo, ctx.lineTo, ctx.stroke, requestAnimationFrame, draw。
  - 去向：react-front/src/views/lock.tsx
- I03072 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 161-165 ExpressionStatement: 
  - 基线：源语句 sha256=78a4405a3cedcad184905a6182f038d6375e29962e541c9148756b33baac8d78；保留返回、异常及 0 个分支，调用=onMounted, startClock, initParticles, nextTick, passwordInput.value.focus。
  - 去向：react-front/src/views/lock.tsx
- I03073 `ruoyi-fastapi-frontend/src/views/lock.vue` lines 167-170 ExpressionStatement: 
  - 基线：源语句 sha256=df1c14b83460e1ed26f3a7e42edf65e30f5fabd1e385fd5edf1b569992446067；保留返回、异常及 0 个分支，调用=onBeforeUnmount, clearInterval, cancelAnimationFrame。
  - 去向：react-front/src/views/lock.tsx
- I03074 `ruoyi-fastapi-frontend/src/views/lock.vue` template lines 1-34（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/lock.tsx
- I03075 `ruoyi-fastapi-frontend/src/views/lock.vue` template line 13: v-bind:src
  - 基线：原表达式：userStore.avatar；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/lock.tsx
- I03076 `ruoyi-fastapi-frontend/src/views/lock.vue` template line 13: v-on:error
  - 基线：原表达式：onAvatarError；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/lock.tsx
- I03077 `ruoyi-fastapi-frontend/src/views/lock.vue` template line 19: v-bind:class
  - 基线：原表达式：{ shake: isShaking }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/lock.tsx
- I03078 `ruoyi-fastapi-frontend/src/views/lock.vue` template line 20: v-model:
  - 基线：原表达式：password；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/lock.tsx
- I03079 `ruoyi-fastapi-frontend/src/views/lock.vue` template line 20: v-on:keydown
  - 基线：原表达式：handleUnlock；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/lock.tsx
- I03080 `ruoyi-fastapi-frontend/src/views/lock.vue` template line 21: v-on:click
  - 基线：原表达式：handleUnlock；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/lock.tsx
- I03081 `ruoyi-fastapi-frontend/src/views/lock.vue` template line 21: v-bind:disabled
  - 基线：原表达式：loading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/lock.tsx
- I03082 `ruoyi-fastapi-frontend/src/views/lock.vue` template line 22: v-if:
  - 基线：原表达式：!loading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/lock.tsx
- I03083 `ruoyi-fastapi-frontend/src/views/lock.vue` template line 23: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/lock.tsx
- I03084 `ruoyi-fastapi-frontend/src/views/lock.vue` template line 27: v-if:
  - 基线：原表达式：errorMsg；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/lock.tsx
- I03085 `ruoyi-fastapi-frontend/src/views/lock.vue` template line 30: v-on:click
  - 基线：原表达式：goLogin；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/lock.tsx
- I03086 `ruoyi-fastapi-frontend/src/views/lock.vue` template interpolation line 7
  - 基线：原显示表达式：currentTime
  - 去向：react-front/src/views/lock.tsx
- I03087 `ruoyi-fastapi-frontend/src/views/lock.vue` template interpolation line 8
  - 基线：原显示表达式：currentDate
  - 去向：react-front/src/views/lock.tsx
- I03088 `ruoyi-fastapi-frontend/src/views/lock.vue` template interpolation line 16
  - 基线：原显示表达式：userStore.nickName
  - 去向：react-front/src/views/lock.tsx
- I03089 `ruoyi-fastapi-frontend/src/views/lock.vue` template interpolation line 27
  - 基线：原显示表达式：errorMsg
  - 去向：react-front/src/views/lock.tsx
- I03090 `ruoyi-fastapi-frontend/src/views/lock.vue` style[0] lines 173-373
  - 基线：保留全部选择器、声明和 url；lang=css, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/views/lock.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
