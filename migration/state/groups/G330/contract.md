# G330 tests/job/job-form.test.js：完整能力

依赖：G000, G243

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I08709 `ruoyi-fastapi-frontend/tests/job/job-form.test.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=a4635e5c72089cbfa239a6a50420de223fe688748a52da7028ae0a399c6e3152；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/tests/job/job-form.test.ts
- I08710 `ruoyi-fastapi-frontend/tests/job/job-form.test.js` lines 2-2 ImportDeclaration: 
  - 基线：源语句 sha256=a1c39937508c4a8bd3abaa0f193fa262439fdf7908a3aa46b5712e63d7bcc574；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/tests/job/job-form.test.ts
- I08711 `ruoyi-fastapi-frontend/tests/job/job-form.test.js` lines 3-3 ImportDeclaration: 
  - 基线：源语句 sha256=993e295561babfaa2c79b6b3b161d7f5dc519a897db7e83a4bbaa56da9012ce2；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/tests/job/job-form.test.ts
- I08712 `ruoyi-fastapi-frontend/tests/job/job-form.test.js` lines 5-22 ExpressionStatement: 
  - 基线：源语句 sha256=eb41545e0533c4f734ffeadd17a66bcd36f9531503fa3345dfff8e22b513d90c；保留返回、异常及 0 个分支，调用=test, buildJobPayload, assert.deepEqual, assert.equal。
  - 去向：react-front/tests/job/job-form.test.ts
- I08713 `ruoyi-fastapi-frontend/tests/job/job-form.test.js` lines 24-26 ExpressionStatement: 
  - 基线：源语句 sha256=f611a448ac0791c0ac153c594f554c11c2972fa0267876f871ee747758f9e678；保留返回、异常及 0 个分支，调用=test, assert.deepEqual, buildJobPayload。
  - 去向：react-front/tests/job/job-form.test.ts
- I08714 `ruoyi-fastapi-frontend/tests/job/job-form.test.js` lines 28-36 ExpressionStatement: 
  - 基线：源语句 sha256=0fdcf41aa2fb0f0c47056ee67c5d13ac22b298a63c2056f75aaa4ade13c2e569；保留返回、异常及 0 个分支，调用=test, assert.throws, parseJobParameter。
  - 去向：react-front/tests/job/job-form.test.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
