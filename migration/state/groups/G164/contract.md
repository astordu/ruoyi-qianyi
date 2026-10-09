# G164 src/components/Crontab/month.vue：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01118 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` lines 37-37 VariableDeclaration: emit
  - 基线：源语句 sha256=f52c487d27bf44d349196d1da2411f18a851ffd07aa7988aba1c29134849f094；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01119 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` lines 38-56 VariableDeclaration: props
  - 基线：源语句 sha256=c34b05fe0912e6ee5683e70ec7664935ec1c5ae82d36f790c29de6e5f03fdb43；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01120 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` lines 57-57 VariableDeclaration: radioValue
  - 基线：源语句 sha256=d6dac5dbdbe52a8dfa14bbca498211e3e3cfbc7933b01429dae5abf2f3d92fe3；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01121 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` lines 58-58 VariableDeclaration: cycle01
  - 基线：源语句 sha256=473d76b74b4d44ef5d37f7068e83c9e1559cc1d926deef0148c144d747bfdf13；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01122 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` lines 59-59 VariableDeclaration: cycle02
  - 基线：源语句 sha256=cd70582fd433db01468630a2d12bc97452e6e12debbc0d0883b4daad05b9e9e8；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01123 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` lines 60-60 VariableDeclaration: average01
  - 基线：源语句 sha256=943ac7abea6f0424ef0ef828aec950e41170731fd483df6407c9cd1ccd92c24a；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01124 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` lines 61-61 VariableDeclaration: average02
  - 基线：源语句 sha256=d581ad2816eda85ea005d7665ac179d9a93e253259c7f1915b405a07c38fea2e；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01125 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` lines 62-62 VariableDeclaration: checkboxList
  - 基线：源语句 sha256=ee3b33beba175fcd3d908e44f74569f944c4962386599cbf458bb60ee9361945；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01126 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` lines 63-63 VariableDeclaration: checkCopy
  - 基线：源语句 sha256=5b5e4b078b56574839f2edb81d688ad399381cdd3144269b3f2998985aad7d8e；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01127 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` lines 64-77 VariableDeclaration: monthList
  - 基线：源语句 sha256=c771131279640357a35ce964bca817f6865c8699967b4c19e1c65530531476ac；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01128 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` lines 78-82 VariableDeclaration: cycleTotal
  - 基线：源语句 sha256=bdafe41a0476c7c88b3f43433b61b1b7811a476bfd99208a17e2ea63ad188009；保留返回、异常及 1 个分支，调用=computed, props.check。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01129 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` lines 83-87 VariableDeclaration: averageTotal
  - 基线：源语句 sha256=20a60a90a2b04a49b9104e4c94fd0cb99659e8e1e7604f6f64bfb132ef9d17fc；保留返回、异常及 1 个分支，调用=computed, props.check。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01130 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` lines 88-90 VariableDeclaration: checkboxString
  - 基线：源语句 sha256=b2ff8a92eb8c9d806982bb74302990c19f032df3d9f67b81b253f9cf7884714a；保留返回、异常及 1 个分支，调用=computed, checkboxList.value.join。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01131 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` lines 91-91 ExpressionStatement: 
  - 基线：源语句 sha256=743e642316a532c7082e5c9bf407dfe5570e8692658eb224588744fb8c6563ac；保留返回、异常及 0 个分支，调用=watch, changeRadioValue。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01132 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` lines 92-92 ExpressionStatement: 
  - 基线：源语句 sha256=05cddea7c63a39b112a532bf264f90b38c4d3cd25e7b8d76466d5234281aa6cb；保留返回、异常及 0 个分支，调用=watch, onRadioChange。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01133 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` lines 93-110 FunctionDeclaration: changeRadioValue
  - 基线：源语句 sha256=bcb4aa2fdfd88120e97faf620f27289aa762d6a704cdfb4546cb6456ada8e16d；保留返回、异常及 3 个分支，调用=value.indexOf, value.split, Number, CallExpression.map。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01134 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` lines 111-131 FunctionDeclaration: onRadioChange
  - 基线：源语句 sha256=b1aeb20a3fa0455e3d3acad36f28743b1cf88ed7de0865b0982921bb30cc5fd7；保留返回、异常及 5 个分支，调用=emit, checkboxList.value.push。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01135 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template lines 1-34（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01136 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 4: v-model:
  - 基线：原表达式：radioValue；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01137 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 4: v-bind:value
  - 基线：原表达式：1；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01138 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 10: v-model:
  - 基线：原表达式：radioValue；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01139 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 10: v-bind:value
  - 基线：原表达式：2；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01140 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 12: v-model:
  - 基线：原表达式：cycle01；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01141 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 12: v-bind:min
  - 基线：原表达式：1；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01142 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 12: v-bind:max
  - 基线：原表达式：11；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01143 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 13: v-model:
  - 基线：原表达式：cycle02；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01144 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 13: v-bind:min
  - 基线：原表达式：cycle01 + 1；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01145 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 13: v-bind:max
  - 基线：原表达式：12；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01146 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 18: v-model:
  - 基线：原表达式：radioValue；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01147 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 18: v-bind:value
  - 基线：原表达式：3；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01148 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 20: v-model:
  - 基线：原表达式：average01；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01149 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 20: v-bind:min
  - 基线：原表达式：1；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01150 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 20: v-bind:max
  - 基线：原表达式：11；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01151 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 21: v-model:
  - 基线：原表达式：average02；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01152 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 21: v-bind:min
  - 基线：原表达式：1；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01153 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 21: v-bind:max
  - 基线：原表达式：12 - average01；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01154 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 26: v-model:
  - 基线：原表达式：radioValue；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01155 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 26: v-bind:value
  - 基线：原表达式：4；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01156 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 28: v-model:
  - 基线：原表达式：checkboxList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01157 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 28: v-bind:multiple-limit
  - 基线：原表达式：8；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01158 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 29: v-for:
  - 基线：原表达式：item in monthList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01159 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 29: v-bind:key
  - 基线：原表达式：item.key；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01160 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 29: v-bind:label
  - 基线：原表达式：item.value；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01161 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` template line 29: v-bind:value
  - 基线：原表达式：item.key；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/month.tsx
- I01162 `ruoyi-fastapi-frontend/src/components/Crontab/month.vue` style[0] lines 134-141
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/components/Crontab/month.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
