# G203 src/layout/components/Sidebar/Link.vue：完整能力

依赖：G000, G256

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02130 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Link.vue` lines 8-8 ImportDeclaration: 
  - 基线：源语句 sha256=f66a8e181b51bf3ddb875b67d0b529175756e08ffaf5d1611f25438e9344d850；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/Sidebar/Link.tsx
- I02131 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Link.vue` lines 10-15 VariableDeclaration: props
  - 基线：源语句 sha256=02320980d16c1e39bd41ea3f2e820c4b3e0fb8a315d0dc49ed11b04f41b2fbf0；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/layout/components/Sidebar/Link.tsx
- I02132 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Link.vue` lines 17-19 VariableDeclaration: isExt
  - 基线：源语句 sha256=980f16e9965a1366781f1af88aac09ca24a039cd6525212e5d6da50f6af8f0ba；保留返回、异常及 1 个分支，调用=computed, isExternal。
  - 去向：react-front/src/layout/components/Sidebar/Link.tsx
- I02133 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Link.vue` lines 21-26 VariableDeclaration: type
  - 基线：源语句 sha256=684d711aea76874cb1d26a38bfdcd2152d6eeedbb35bbd17383b4ed9b52b447b；保留返回、异常及 3 个分支，调用=computed。
  - 去向：react-front/src/layout/components/Sidebar/Link.tsx
- I02134 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Link.vue` lines 28-39 FunctionDeclaration: linkProps
  - 基线：源语句 sha256=57b412c73754cfe1dba79a11eaa07b791188b4e4dfa580a8ea6cc7e35d00597b；保留返回、异常及 3 个分支，调用=。
  - 去向：react-front/src/layout/components/Sidebar/Link.tsx
- I02135 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Link.vue` template lines 1-5（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/layout/components/Sidebar/Link.tsx
- I02136 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Link.vue` template line 2: v-bind:is
  - 基线：原表达式：type；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/Link.tsx
- I02137 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Link.vue` template line 2: v-bind:
  - 基线：原表达式：linkProps()；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/Link.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
