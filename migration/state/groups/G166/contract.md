# G166 src/components/Crontab/second.vue：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01185 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` lines 37-37 VariableDeclaration: emit
  - 基线：源语句 sha256=f52c487d27bf44d349196d1da2411f18a851ffd07aa7988aba1c29134849f094；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01186 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` lines 38-56 VariableDeclaration: props
  - 基线：源语句 sha256=c34b05fe0912e6ee5683e70ec7664935ec1c5ae82d36f790c29de6e5f03fdb43；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01187 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` lines 57-57 VariableDeclaration: radioValue
  - 基线：源语句 sha256=d6dac5dbdbe52a8dfa14bbca498211e3e3cfbc7933b01429dae5abf2f3d92fe3；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01188 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` lines 58-58 VariableDeclaration: cycle01
  - 基线：源语句 sha256=24b3dcb90bbf2c2c580461e7acb5a36ccc9c5a653bd5c78b2bdd1942a57fe670；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01189 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` lines 59-59 VariableDeclaration: cycle02
  - 基线：源语句 sha256=05c791453be267c62af6439c230fb44c7b5f0cbe14a17d344b9dd6da949ccb0f；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01190 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` lines 60-60 VariableDeclaration: average01
  - 基线：源语句 sha256=f93fd678fd5afc2b08c6c34655bdfe38163e282dd3dec10763b9bd48acdb1b6e；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01191 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` lines 61-61 VariableDeclaration: average02
  - 基线：源语句 sha256=d581ad2816eda85ea005d7665ac179d9a93e253259c7f1915b405a07c38fea2e；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01192 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` lines 62-62 VariableDeclaration: checkboxList
  - 基线：源语句 sha256=ee3b33beba175fcd3d908e44f74569f944c4962386599cbf458bb60ee9361945；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01193 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` lines 63-63 VariableDeclaration: checkCopy
  - 基线：源语句 sha256=5eb50752380c484d7fa77e721c8536244a501a1aae79260a885da84fabb8de4c；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01194 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` lines 64-68 VariableDeclaration: cycleTotal
  - 基线：源语句 sha256=26c58ac5facce45c4089a36caa244d631e6cdc071079dd36cb7e3f07e9737ce2；保留返回、异常及 1 个分支，调用=computed, props.check。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01195 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` lines 69-73 VariableDeclaration: averageTotal
  - 基线：源语句 sha256=5019ac4c27b83cd86fa9bcdbe3b388f06448a7816d36627ef5f003d4111108b2；保留返回、异常及 1 个分支，调用=computed, props.check。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01196 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` lines 74-76 VariableDeclaration: checkboxString
  - 基线：源语句 sha256=b2ff8a92eb8c9d806982bb74302990c19f032df3d9f67b81b253f9cf7884714a；保留返回、异常及 1 个分支，调用=computed, checkboxList.value.join。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01197 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` lines 77-77 ExpressionStatement: 
  - 基线：源语句 sha256=5f3620d048d4b49860a6b7bbe1ff128439e09b828854d675bac68cf500094a6a；保留返回、异常及 0 个分支，调用=watch, changeRadioValue。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01198 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` lines 78-78 ExpressionStatement: 
  - 基线：源语句 sha256=05cddea7c63a39b112a532bf264f90b38c4d3cd25e7b8d76466d5234281aa6cb；保留返回、异常及 0 个分支，调用=watch, onRadioChange。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01199 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` lines 79-96 FunctionDeclaration: changeRadioValue
  - 基线：源语句 sha256=bcb4aa2fdfd88120e97faf620f27289aa762d6a704cdfb4546cb6456ada8e16d；保留返回、异常及 3 个分支，调用=value.indexOf, value.split, Number, CallExpression.map。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01200 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` lines 98-118 FunctionDeclaration: onRadioChange
  - 基线：源语句 sha256=9c6f49aa2a166b72a40a9b17ded0dedfe79e3f5692e74f7e4df569c51609d055；保留返回、异常及 5 个分支，调用=emit, checkboxList.value.push。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01201 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template lines 1-34（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01202 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 4: v-model:
  - 基线：原表达式：radioValue；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01203 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 4: v-bind:value
  - 基线：原表达式：1；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01204 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 10: v-model:
  - 基线：原表达式：radioValue；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01205 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 10: v-bind:value
  - 基线：原表达式：2；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01206 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 12: v-model:
  - 基线：原表达式：cycle01；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01207 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 12: v-bind:min
  - 基线：原表达式：0；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01208 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 12: v-bind:max
  - 基线：原表达式：58；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01209 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 13: v-model:
  - 基线：原表达式：cycle02；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01210 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 13: v-bind:min
  - 基线：原表达式：cycle01 + 1；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01211 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 13: v-bind:max
  - 基线：原表达式：59；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01212 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 18: v-model:
  - 基线：原表达式：radioValue；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01213 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 18: v-bind:value
  - 基线：原表达式：3；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01214 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 20: v-model:
  - 基线：原表达式：average01；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01215 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 20: v-bind:min
  - 基线：原表达式：0；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01216 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 20: v-bind:max
  - 基线：原表达式：58；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01217 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 21: v-model:
  - 基线：原表达式：average02；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01218 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 21: v-bind:min
  - 基线：原表达式：1；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01219 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 21: v-bind:max
  - 基线：原表达式：59 - average01；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01220 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 26: v-model:
  - 基线：原表达式：radioValue；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01221 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 26: v-bind:value
  - 基线：原表达式：4；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01222 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 28: v-model:
  - 基线：原表达式：checkboxList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01223 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 28: v-bind:multiple-limit
  - 基线：原表达式：10；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01224 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 29: v-for:
  - 基线：原表达式：item in 60；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01225 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 29: v-bind:key
  - 基线：原表达式：item；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01226 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 29: v-bind:label
  - 基线：原表达式：item - 1；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01227 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` template line 29: v-bind:value
  - 基线：原表达式：item - 1；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/second.tsx
- I01228 `ruoyi-fastapi-frontend/src/components/Crontab/second.vue` style[0] lines 121-128
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/components/Crontab/second.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
