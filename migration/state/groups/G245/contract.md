# G245 src/utils/passwordRule.js：完整能力

依赖：G000, G216

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02726 `ruoyi-fastapi-frontend/src/utils/passwordRule.js` lines 13-13 ImportDeclaration: 
  - 基线：源语句 sha256=819249c9809a1e47bb12de03da21c4c25f60b908825d07094d219578c4c835ec；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/passwordRule.ts
- I02727 `ruoyi-fastapi-frontend/src/utils/passwordRule.js` lines 16-16 VariableDeclaration: pwdChrType
  - 基线：源语句 sha256=10c3e430b0bc1aabe5cdb52cf97cfff7de180e1d1238a37e70720639617b8f26；保留返回、异常及 1 个分支，调用=ref, cache.session.get。
  - 去向：react-front/src/utils/passwordRule.ts
- I02728 `ruoyi-fastapi-frontend/src/utils/passwordRule.js` lines 19-25 VariableDeclaration: PWD_RULES
  - 基线：源语句 sha256=bf67d3ae55fdaa6a46fdb2a0971fad327e43b6035d58361e5c831166e6b90aec；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/passwordRule.ts
- I02729 `ruoyi-fastapi-frontend/src/utils/passwordRule.js` lines 27-73 ExportNamedDeclaration: usePasswordRule
  - 基线：源语句 sha256=8b42ab4b33bfda30f8ecf418e530d80f01947b9ab909b36eb406818e6cb9b4d3；保留返回、异常及 12 个分支，调用=computed, rule.pattern.test。
  - 去向：react-front/src/utils/passwordRule.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
