# G260 src/views/error/404.vue：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I03042 `ruoyi-fastapi-frontend/src/views/error/404.vue` lines 29-31 VariableDeclaration: message
  - 基线：源语句 sha256=70cdca0b5d151beb53b9d83f21341ebb9b65e93768a971b1cc6ce736ded1feb5；保留返回、异常及 1 个分支，调用=computed。
  - 去向：react-front/src/views/error/404.tsx
- I03043 `ruoyi-fastapi-frontend/src/views/error/404.vue` template lines 1-26（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/error/404.tsx
- I03044 `ruoyi-fastapi-frontend/src/views/error/404.vue` template interpolation line 15
  - 基线：原显示表达式：message
  - 去向：react-front/src/views/error/404.tsx
- I03045 `ruoyi-fastapi-frontend/src/views/error/404.vue` style[0] lines 34-227
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/views/error/404.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
