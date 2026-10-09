# G158 src/components/BusinessDateTimePicker/index.vue：完整能力

依赖：G000, G253F025, G253F033, G253F036

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00782 `ruoyi-fastapi-frontend/src/components/BusinessDateTimePicker/index.vue` lines 21-21 ImportDeclaration: 
  - 基线：源语句 sha256=60f4eefa37851a2ba9fde1f298f7ce10a7f222720e76008960a141d1c9e2c3ba；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/BusinessDateTimePicker/index.tsx
- I00783 `ruoyi-fastapi-frontend/src/components/BusinessDateTimePicker/index.vue` lines 24-98 ExportDefaultDeclaration: wallValue, timezoneName, get, set
  - 基线：源语句 sha256=9473ffeec07b1e80ca20468273e76214fb2cbab9798da4294d0a7b74e60bcb9e；保留返回、异常及 18 个分支，调用=getDisplayTimezone, ThisExpression.wallValue.slice, ThisExpression.updateValue, formatBusinessTime, getWallTimeCandidates, ThisExpression.$emit。
  - 去向：react-front/src/components/BusinessDateTimePicker/index.tsx
- I00784 `ruoyi-fastapi-frontend/src/components/BusinessDateTimePicker/index.vue` template lines 1-18（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/components/BusinessDateTimePicker/index.tsx
- I00785 `ruoyi-fastapi-frontend/src/components/BusinessDateTimePicker/index.vue` template line 5: v-model:
  - 基线：原表达式：dateInput；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessDateTimePicker/index.tsx
- I00786 `ruoyi-fastapi-frontend/src/components/BusinessDateTimePicker/index.vue` template line 7: v-bind:aria-label
  - 基线：原表达式：label + '日期'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessDateTimePicker/index.tsx
- I00787 `ruoyi-fastapi-frontend/src/components/BusinessDateTimePicker/index.vue` template line 8: v-bind:disabled
  - 基线：原表达式：disabled；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessDateTimePicker/index.tsx
- I00788 `ruoyi-fastapi-frontend/src/components/BusinessDateTimePicker/index.vue` template line 9: v-bind:clearable
  - 基线：原表达式：clearable；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessDateTimePicker/index.tsx
- I00789 `ruoyi-fastapi-frontend/src/components/BusinessDateTimePicker/index.vue` template line 11: v-model:
  - 基线：原表达式：timeInput；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessDateTimePicker/index.tsx
- I00790 `ruoyi-fastapi-frontend/src/components/BusinessDateTimePicker/index.vue` template line 11: v-bind:aria-label
  - 基线：原表达式：label + '时间'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessDateTimePicker/index.tsx
- I00791 `ruoyi-fastapi-frontend/src/components/BusinessDateTimePicker/index.vue` template line 11: v-bind:disabled
  - 基线：原表达式：disabled；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessDateTimePicker/index.tsx
- I00792 `ruoyi-fastapi-frontend/src/components/BusinessDateTimePicker/index.vue` template line 14: v-if:
  - 基线：原表达式：validationMessage；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessDateTimePicker/index.tsx
- I00793 `ruoyi-fastapi-frontend/src/components/BusinessDateTimePicker/index.vue` template interpolation line 13
  - 基线：原显示表达式：timezoneName
  - 去向：react-front/src/components/BusinessDateTimePicker/index.tsx
- I00794 `ruoyi-fastapi-frontend/src/components/BusinessDateTimePicker/index.vue` template interpolation line 15
  - 基线：原显示表达式：validationMessage
  - 去向：react-front/src/components/BusinessDateTimePicker/index.tsx
- I00795 `ruoyi-fastapi-frontend/src/components/BusinessDateTimePicker/index.vue` style[0] lines 101-123
  - 基线：保留全部选择器、声明和 url；lang=css, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/components/BusinessDateTimePicker/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
