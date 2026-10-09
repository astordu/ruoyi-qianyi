# G236 src/utils/generator/css.js：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02643 `ruoyi-fastapi-frontend/src/utils/generator/css.js` lines 1-4 VariableDeclaration: styles
  - 基线：源语句 sha256=f39b9eb0bd32b0d3afe65e2993322a29713f814fade5075538675e4b5c158e24；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/generator/css.ts
- I02644 `ruoyi-fastapi-frontend/src/utils/generator/css.js` lines 6-12 FunctionDeclaration: addCss
  - 基线：源语句 sha256=bd09091ea7ee13bd8085ffc3ec69db01abcf03026f4ef6424bcd4ecfa4d9e162；保留返回、异常及 3 个分支，调用=cssList.indexOf, cssList.push, el.children.forEach, addCss。
  - 去向：react-front/src/utils/generator/css.ts
- I02645 `ruoyi-fastapi-frontend/src/utils/generator/css.js` lines 14-18 ExportNamedDeclaration: makeUpCss
  - 基线：源语句 sha256=abad857e40fb7406791c857509b4e3cb7c659e7e9b7e93c385d3589c31876ca7；保留返回、异常及 1 个分支，调用=conf.fields.forEach, addCss, cssList.join。
  - 去向：react-front/src/utils/generator/css.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
