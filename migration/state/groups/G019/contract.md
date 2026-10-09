# G019 plugins/ai/api/model.js：完整能力

依赖：G000, G249

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00092 `ruoyi-fastapi-frontend/plugins/ai/api/model.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=61e91c1ede8a9285d8357e07bda32e48170c71df8aa8a5c4a0dfd9830d2be5e2；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/plugins/ai/api/model.ts
- I00093 `ruoyi-fastapi-frontend/plugins/ai/api/model.js` lines 4-10 ExportNamedDeclaration: listModel
  - 基线：源语句 sha256=326fb7a196a0716a21115b9db3b7f1fde59cfb62cf1f48976876be16e4baccea；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/plugins/ai/api/model.ts
- I00094 `ruoyi-fastapi-frontend/plugins/ai/api/model.js` lines 13-18 ExportNamedDeclaration: listModelAll
  - 基线：源语句 sha256=cfb96a33252362e190fde9f401a647c51496674b964c0d87bff57d65bfdec660；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/plugins/ai/api/model.ts
- I00095 `ruoyi-fastapi-frontend/plugins/ai/api/model.js` lines 21-26 ExportNamedDeclaration: getModel
  - 基线：源语句 sha256=3aef415695b29d297a1ea728cb6e1ea07ec57c3fe88e4da38e513d4503a55a9d；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/plugins/ai/api/model.ts
- I00096 `ruoyi-fastapi-frontend/plugins/ai/api/model.js` lines 29-35 ExportNamedDeclaration: addModel
  - 基线：源语句 sha256=469ba7d42405a2c92848e90b6bffd9b7b4bb8dab4015d931e34620dba7052973；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/plugins/ai/api/model.ts
- I00097 `ruoyi-fastapi-frontend/plugins/ai/api/model.js` lines 38-44 ExportNamedDeclaration: updateModel
  - 基线：源语句 sha256=c3ad31d055447d7c03f2870ac1a14f3e8b56d45f0594928bd6736c4fe838b326；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/plugins/ai/api/model.ts
- I00098 `ruoyi-fastapi-frontend/plugins/ai/api/model.js` lines 47-52 ExportNamedDeclaration: delModel
  - 基线：源语句 sha256=1184cc465a15590be0db67560940b577b2a4f8b291f613148391fb54d2362790；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/plugins/ai/api/model.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
