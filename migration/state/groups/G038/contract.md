# G038 src/api/system/dict/type.js：完整能力

依赖：G000, G249

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00521 `ruoyi-fastapi-frontend/src/api/system/dict/type.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=cd462474cb30a9a5954fbd44474b2f4e19f6d48d3c7dff5aebf452db4c8517f8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/api/system/dict/type.ts
- I00522 `ruoyi-fastapi-frontend/src/api/system/dict/type.js` lines 4-10 ExportNamedDeclaration: listType
  - 基线：源语句 sha256=c57fa26a7947cccb41ecf14e345ce3621ff7f154deb6a5ffdea952116c742486；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/dict/type.ts
- I00523 `ruoyi-fastapi-frontend/src/api/system/dict/type.js` lines 13-18 ExportNamedDeclaration: getType
  - 基线：源语句 sha256=996d971c0a4df701c4cb9646ea42ae5af2bbd98c1b4e40cccd1d179a013101b0；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/dict/type.ts
- I00524 `ruoyi-fastapi-frontend/src/api/system/dict/type.js` lines 21-27 ExportNamedDeclaration: addType
  - 基线：源语句 sha256=0dc13cb4f44d10828dc7879ebb7d71f964b936242e73cde0964d62998e302aa2；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/dict/type.ts
- I00525 `ruoyi-fastapi-frontend/src/api/system/dict/type.js` lines 30-36 ExportNamedDeclaration: updateType
  - 基线：源语句 sha256=8fcd9e85e0afc9e6f7bd5d6cac8ed52c4f327b271df8e038d7c5c9733d76fa52；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/dict/type.ts
- I00526 `ruoyi-fastapi-frontend/src/api/system/dict/type.js` lines 39-44 ExportNamedDeclaration: delType
  - 基线：源语句 sha256=eb97cdb650fd05444b72029e9ee1a0d4550cd6f53b123e4839dd34deea2456d2；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/dict/type.ts
- I00527 `ruoyi-fastapi-frontend/src/api/system/dict/type.js` lines 47-52 ExportNamedDeclaration: refreshCache
  - 基线：源语句 sha256=88cc30637f418ad418da1bee7c5104c612ff1c72a0a7c85425777281fb5b2521；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/dict/type.ts
- I00528 `ruoyi-fastapi-frontend/src/api/system/dict/type.js` lines 55-60 ExportNamedDeclaration: optionselect
  - 基线：源语句 sha256=f85160180cbd551ac0bb56685a7110616506bd2f88717f91472a1de35d26ed21；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/dict/type.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
