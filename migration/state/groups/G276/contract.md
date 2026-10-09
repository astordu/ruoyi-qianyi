# G276 src/views/redirect/index.vue：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I04300 `ruoyi-fastapi-frontend/src/views/redirect/index.vue` lines 6-6 ImportDeclaration: 
  - 基线：源语句 sha256=85c981671a850ee14f961f425e420222fc93ac1922b681949655949c21824f6b；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/redirect/index.tsx
- I04301 `ruoyi-fastapi-frontend/src/views/redirect/index.vue` lines 8-8 VariableDeclaration: route
  - 基线：源语句 sha256=19ffaf888604ba2654aa25f29ba0210e96226ea7089e9e15dc5c05cf276b3a9f；保留返回、异常及 0 个分支，调用=useRoute。
  - 去向：react-front/src/views/redirect/index.tsx
- I04302 `ruoyi-fastapi-frontend/src/views/redirect/index.vue` lines 9-9 VariableDeclaration: router
  - 基线：源语句 sha256=5921d8bbcfc7da27a18289d8a47cc51136866f8fdbebe22e9d1d1135aa55e0e6；保留返回、异常及 0 个分支，调用=useRouter。
  - 去向：react-front/src/views/redirect/index.tsx
- I04303 `ruoyi-fastapi-frontend/src/views/redirect/index.vue` lines 10-10 VariableDeclaration: 
  - 基线：源语句 sha256=be3e6b3923bc380d6380c5c78dcddb1200cbfeda0fa91691baa2766daa9c064d；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/redirect/index.tsx
- I04304 `ruoyi-fastapi-frontend/src/views/redirect/index.vue` lines 11-11 VariableDeclaration: 
  - 基线：源语句 sha256=2aa0cdc2bc8726342638c3637e89abe270c8e623edaa7853c687d10534142723；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/redirect/index.tsx
- I04305 `ruoyi-fastapi-frontend/src/views/redirect/index.vue` lines 13-13 ExpressionStatement: 
  - 基线：源语句 sha256=7c4e7ba392019f335c0156ac34dde627c23ebd670812aaf9a3cde9b6a8f98d0e；保留返回、异常及 0 个分支，调用=router.replace。
  - 去向：react-front/src/views/redirect/index.tsx
- I04306 `ruoyi-fastapi-frontend/src/views/redirect/index.vue` template lines 1-3（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/redirect/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
