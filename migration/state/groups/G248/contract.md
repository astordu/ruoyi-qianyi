# G248 src/utils/pluginViewResolver.js：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02745 `ruoyi-fastapi-frontend/src/utils/pluginViewResolver.js` lines 1-1 VariableDeclaration: PLUGIN_ID_PATTERN
  - 基线：源语句 sha256=0317a91f4007e2703612beaa95c333c800f3d20c474865415be3a6a015e17c34；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/pluginViewResolver.ts
- I02746 `ruoyi-fastapi-frontend/src/utils/pluginViewResolver.js` lines 2-2 VariableDeclaration: VIEW_SEGMENT_PATTERN
  - 基线：源语句 sha256=b384cb89e1345d358830e5c1c3008ddba3fc0e7dbdce1b9bb3c7bec3a666ae08；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/pluginViewResolver.ts
- I02747 `ruoyi-fastapi-frontend/src/utils/pluginViewResolver.js` lines 9-26 ExportNamedDeclaration: resolvePluginViewPath
  - 基线：源语句 sha256=c966258b56d4b3e766f47bb21139a5fd11bc1159d6cb23fda2e2db7beeb1cd0d；保留返回、异常及 9 个分支，调用=CallExpression.split, view.replace, parts.slice, PLUGIN_ID_PATTERN.test, viewSegments.every, VIEW_SEGMENT_PATTERN.test, viewSegments.join。
  - 去向：react-front/src/utils/pluginViewResolver.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
