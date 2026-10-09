# G040 src/api/system/menu.js：完整能力

依赖：G000, G249

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00558 `ruoyi-fastapi-frontend/src/api/system/menu.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=cd462474cb30a9a5954fbd44474b2f4e19f6d48d3c7dff5aebf452db4c8517f8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/api/system/menu.ts
- I00559 `ruoyi-fastapi-frontend/src/api/system/menu.js` lines 4-10 ExportNamedDeclaration: listMenu
  - 基线：源语句 sha256=010cd51eb61b0dbfe6f6a78b97ea8ddfe51828a54196803851571afa41360d6c；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/menu.ts
- I00560 `ruoyi-fastapi-frontend/src/api/system/menu.js` lines 13-18 ExportNamedDeclaration: getMenu
  - 基线：源语句 sha256=c7ca74c4c650e29beb00d566892de51cdefdee8dbbd1907b324413a551094796；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/menu.ts
- I00561 `ruoyi-fastapi-frontend/src/api/system/menu.js` lines 21-26 ExportNamedDeclaration: treeselect
  - 基线：源语句 sha256=81b07d9073e4a5aa4651c901dadd51993b8f81678d4c77f1f3159f6f4e3fc5a0；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/menu.ts
- I00562 `ruoyi-fastapi-frontend/src/api/system/menu.js` lines 29-34 ExportNamedDeclaration: roleMenuTreeselect
  - 基线：源语句 sha256=bfdb97e450b1ec433d7927114a90082722e128f48b1f531d86792979f0071787；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/menu.ts
- I00563 `ruoyi-fastapi-frontend/src/api/system/menu.js` lines 37-43 ExportNamedDeclaration: addMenu
  - 基线：源语句 sha256=c52e04917868a5445bb101321ab942189f8eea18cc9177ef2257cca67ac73fa5；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/menu.ts
- I00564 `ruoyi-fastapi-frontend/src/api/system/menu.js` lines 46-52 ExportNamedDeclaration: updateMenu
  - 基线：源语句 sha256=ecd5fbc5f9e059856816712a489b98e699669d961818c083932cbb7ce3e8b104；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/menu.ts
- I00565 `ruoyi-fastapi-frontend/src/api/system/menu.js` lines 55-61 ExportNamedDeclaration: updateMenuSort
  - 基线：源语句 sha256=cb24b71bda0756ff1fb651ac95f420e6ed311144fb0371d97435c9a0c7f28b14；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/menu.ts
- I00566 `ruoyi-fastapi-frontend/src/api/system/menu.js` lines 64-69 ExportNamedDeclaration: delMenu
  - 基线：源语句 sha256=bec1021676f78cc71ee9a7561c9af5ee7823396395c14ca31074fa5bf53310b0；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/menu.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
