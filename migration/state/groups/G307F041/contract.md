# G307F041 src/views/system/role/index.vue：handleUpdate

依赖：G000, G040, G044, G232, G250, G253F025, G307, G307F039, G307F042

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I07164 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 417-437 FunctionDeclaration: handleUpdate
  - 基线：源语句 sha256=e451fe439e206602f39556c85350951eac3ee62f165e3597dc9130bb836fb99b；保留返回、异常及 1 个分支，调用=reset, getRoleMenuTreeselect, CallExpression.then, getRole, Number, nextTick, roleMenu.then, checkedKeys.forEach, menuRef.value.setChecked。
  - 去向：react-front/src/views/system/role/index.parts/handleUpdate.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
