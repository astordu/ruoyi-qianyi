# G018 plugins/ai/api/chat.js：完整能力

依赖：G000, G249

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00085 `ruoyi-fastapi-frontend/plugins/ai/api/chat.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=61e91c1ede8a9285d8357e07bda32e48170c71df8aa8a5c4a0dfd9830d2be5e2；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/plugins/ai/api/chat.ts
- I00086 `ruoyi-fastapi-frontend/plugins/ai/api/chat.js` lines 4-9 ExportNamedDeclaration: listChatSession
  - 基线：源语句 sha256=b0edc14aaa85e16974a5ccede98a5d6531bc11a9770aaf96a83e7d146d41d05b；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/plugins/ai/api/chat.ts
- I00087 `ruoyi-fastapi-frontend/plugins/ai/api/chat.js` lines 12-17 ExportNamedDeclaration: delChatSession
  - 基线：源语句 sha256=61b0717e038e01e4bbc8b57eed574a62957007efdbc1b00632ebbb219898400b；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/plugins/ai/api/chat.ts
- I00088 `ruoyi-fastapi-frontend/plugins/ai/api/chat.js` lines 20-25 ExportNamedDeclaration: getChatSession
  - 基线：源语句 sha256=2201aeb36d2504ebcb998b9425045b4b2c0f9b7c55d50214fa249aba921777bf；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/plugins/ai/api/chat.ts
- I00089 `ruoyi-fastapi-frontend/plugins/ai/api/chat.js` lines 28-33 ExportNamedDeclaration: getUserChatConfig
  - 基线：源语句 sha256=7d6fdd0932b4e35b112fb060ee1326fd0eb75bd286a1c0d2e95a23848aa216e2；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/plugins/ai/api/chat.ts
- I00090 `ruoyi-fastapi-frontend/plugins/ai/api/chat.js` lines 36-42 ExportNamedDeclaration: saveUserChatConfig
  - 基线：源语句 sha256=0860c9565b9a56991630990b7945c651e7eed9d08e2b35834dc080e395fdf5f6；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/plugins/ai/api/chat.ts
- I00091 `ruoyi-fastapi-frontend/plugins/ai/api/chat.js` lines 45-53 ExportNamedDeclaration: cancelChatRun
  - 基线：源语句 sha256=76979b9bf0692a4c3be9b2aeff440095ee493113b5551224faa41ba0ed2b21dc；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/plugins/ai/api/chat.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
