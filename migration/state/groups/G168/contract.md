# G168 src/components/Crontab/year.vue：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01295 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` lines 44-44 VariableDeclaration: emit
  - 基线：源语句 sha256=f52c487d27bf44d349196d1da2411f18a851ffd07aa7988aba1c29134849f094；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01296 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` lines 45-63 VariableDeclaration: props
  - 基线：源语句 sha256=36da941f3b71ce09238ff930b72ae508548937e1d248797e4646f7a343cc87de；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01297 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` lines 65-65 VariableDeclaration: fullYear
  - 基线：源语句 sha256=04705f78ecb876db09bf8e1116986b5d332588d8fe1e30768bd5f2b12c80d41b；保留返回、异常及 0 个分支，调用=Number, NewExpression.getFullYear。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01298 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` lines 66-66 VariableDeclaration: maxFullYear
  - 基线：源语句 sha256=289fe27be11c726e0c24abb32d23b699201eeaa93a7bca4de0d08f6a5e4206b1；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01299 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` lines 67-67 VariableDeclaration: radioValue
  - 基线：源语句 sha256=d6dac5dbdbe52a8dfa14bbca498211e3e3cfbc7933b01429dae5abf2f3d92fe3；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01300 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` lines 68-68 VariableDeclaration: cycle01
  - 基线：源语句 sha256=67729df249aa43eeaa4a49502398fe34b6de7a244f60f471090133a0f13c5537；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01301 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` lines 69-69 VariableDeclaration: cycle02
  - 基线：源语句 sha256=92717c388a7fcf4e60f015eb56e773e139d363790b778e045fdc006306bdeb3d；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01302 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` lines 70-70 VariableDeclaration: average01
  - 基线：源语句 sha256=2ed0c309f2bcea675a7fe698f309da06a3f83b8903365364a5d368f67c1bad08；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01303 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` lines 71-71 VariableDeclaration: average02
  - 基线：源语句 sha256=d581ad2816eda85ea005d7665ac179d9a93e253259c7f1915b405a07c38fea2e；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01304 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` lines 72-72 VariableDeclaration: checkboxList
  - 基线：源语句 sha256=ee3b33beba175fcd3d908e44f74569f944c4962386599cbf458bb60ee9361945；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01305 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` lines 73-73 VariableDeclaration: checkCopy
  - 基线：源语句 sha256=8bcf713bc73637a0d1323f4194afa6b05cc9e5450714687cd5254c31c0036968；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01306 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` lines 75-79 VariableDeclaration: cycleTotal
  - 基线：源语句 sha256=3ae76dfffd6bf07942d5e07186d9ec28b1d14c2dc4d14caaab2a4df5e5cda36f；保留返回、异常及 1 个分支，调用=computed, props.check。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01307 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` lines 80-84 VariableDeclaration: averageTotal
  - 基线：源语句 sha256=23d1c33d88ef43f50f454584e6009a7ad30963faec7f069407225f315d1d5b6d；保留返回、异常及 1 个分支，调用=computed, props.check。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01308 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` lines 85-87 VariableDeclaration: checkboxString
  - 基线：源语句 sha256=b2ff8a92eb8c9d806982bb74302990c19f032df3d9f67b81b253f9cf7884714a；保留返回、异常及 1 个分支，调用=computed, checkboxList.value.join。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01309 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` lines 88-88 ExpressionStatement: 
  - 基线：源语句 sha256=53eba31e1c9f5391501f8f2e94a358c220a9ca894f558a358fdcf69c1b79cdc6；保留返回、异常及 0 个分支，调用=watch, changeRadioValue。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01310 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` lines 89-89 ExpressionStatement: 
  - 基线：源语句 sha256=05cddea7c63a39b112a532bf264f90b38c4d3cd25e7b8d76466d5234281aa6cb；保留返回、异常及 0 个分支，调用=watch, onRadioChange。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01311 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` lines 90-109 FunctionDeclaration: changeRadioValue
  - 基线：源语句 sha256=eb143e771effceba278b164c5b26971f0f15985a3011ea980d8b67424f817ce5；保留返回、异常及 4 个分支，调用=value.indexOf, value.split, Number, CallExpression.map。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01312 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` lines 110-133 FunctionDeclaration: onRadioChange
  - 基线：源语句 sha256=c2167096ab9a850cda88edc8e9e6a0f270ea0f6e823e954aef5e5ca0956877bf；保留返回、异常及 6 个分支，调用=emit, checkboxList.value.push。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01313 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template lines 1-41（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01314 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 4: v-bind:value
  - 基线：原表达式：1；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01315 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 4: v-model:
  - 基线：原表达式：radioValue；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01316 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 10: v-bind:value
  - 基线：原表达式：2；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01317 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 10: v-model:
  - 基线：原表达式：radioValue；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01318 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 16: v-bind:value
  - 基线：原表达式：3；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01319 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 16: v-model:
  - 基线：原表达式：radioValue；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01320 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 18: v-model:
  - 基线：原表达式：cycle01；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01321 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 18: v-bind:min
  - 基线：原表达式：fullYear；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01322 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 18: v-bind:max
  - 基线：原表达式：2098；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01323 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 19: v-model:
  - 基线：原表达式：cycle02；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01324 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 19: v-bind:min
  - 基线：原表达式：cycle01 ? cycle01 + 1 : fullYear + 1；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01325 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 19: v-bind:max
  - 基线：原表达式：2099；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01326 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 24: v-bind:value
  - 基线：原表达式：4；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01327 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 24: v-model:
  - 基线：原表达式：radioValue；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01328 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 26: v-model:
  - 基线：原表达式：average01；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01329 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 26: v-bind:min
  - 基线：原表达式：fullYear；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01330 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 26: v-bind:max
  - 基线：原表达式：2098；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01331 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 27: v-model:
  - 基线：原表达式：average02；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01332 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 27: v-bind:min
  - 基线：原表达式：1；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01333 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 27: v-bind:max
  - 基线：原表达式：2099 - average01 || fullYear；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01334 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 33: v-bind:value
  - 基线：原表达式：5；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01335 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 33: v-model:
  - 基线：原表达式：radioValue；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01336 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 35: v-model:
  - 基线：原表达式：checkboxList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01337 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 35: v-bind:multiple-limit
  - 基线：原表达式：8；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01338 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 36: v-for:
  - 基线：原表达式：item in 9；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01339 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 36: v-bind:key
  - 基线：原表达式：item；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01340 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 36: v-bind:value
  - 基线：原表达式：item - 1 + fullYear；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01341 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` template line 36: v-bind:label
  - 基线：原表达式：item -1 + fullYear；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/year.tsx
- I01342 `ruoyi-fastapi-frontend/src/components/Crontab/year.vue` style[0] lines 136-143
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/components/Crontab/year.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
