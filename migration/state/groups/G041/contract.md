# G041 src/api/system/notice.js：完整能力

依赖：G000, G249

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00567 `ruoyi-fastapi-frontend/src/api/system/notice.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=cd462474cb30a9a5954fbd44474b2f4e19f6d48d3c7dff5aebf452db4c8517f8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/api/system/notice.ts
- I00568 `ruoyi-fastapi-frontend/src/api/system/notice.js` lines 4-10 ExportNamedDeclaration: listNotice
  - 基线：源语句 sha256=6eb5909cfe7bfe0d9b7fa2224d5186fc8922d157bee912358f94653d84f3d638；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/notice.ts
- I00569 `ruoyi-fastapi-frontend/src/api/system/notice.js` lines 13-18 ExportNamedDeclaration: getNotice
  - 基线：源语句 sha256=2d05e39e30139729b092a274ded9521a216bc209d4cff2e5d2c1d71069074473；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/notice.ts
- I00570 `ruoyi-fastapi-frontend/src/api/system/notice.js` lines 21-27 ExportNamedDeclaration: addNotice
  - 基线：源语句 sha256=b1d97e1b00fff8dae3e091efdd44ced9f73db4778bdd54afbe36ccaa6cd08e56；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/notice.ts
- I00571 `ruoyi-fastapi-frontend/src/api/system/notice.js` lines 30-36 ExportNamedDeclaration: updateNotice
  - 基线：源语句 sha256=54566899dc5e98ef49a88b6d205003c61b4643c884bc7dd8517f5531d9986def；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/notice.ts
- I00572 `ruoyi-fastapi-frontend/src/api/system/notice.js` lines 39-44 ExportNamedDeclaration: delNotice
  - 基线：源语句 sha256=4a4023628f9891cd13f4259f0ebabfa1cb6fb5141fa61f2ee11058e77cc27f4f；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/notice.ts
- I00573 `ruoyi-fastapi-frontend/src/api/system/notice.js` lines 47-52 ExportNamedDeclaration: listNoticeTop
  - 基线：源语句 sha256=29d8a47c2bbc121bc7c16c2d33971eb1fa63ded051d1933c834961d6c302c1df；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/notice.ts
- I00574 `ruoyi-fastapi-frontend/src/api/system/notice.js` lines 55-61 ExportNamedDeclaration: markNoticeRead
  - 基线：源语句 sha256=8db0335b0a676085ccdc073285f1473537463e482d46c470a49b2337be2be6b8；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/notice.ts
- I00575 `ruoyi-fastapi-frontend/src/api/system/notice.js` lines 64-70 ExportNamedDeclaration: markNoticeReadAll
  - 基线：源语句 sha256=cdd8a1c2a2fc3b47362e92c78bfb7e361e22480f73f84208417001ee36ff0210；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/notice.ts
- I00576 `ruoyi-fastapi-frontend/src/api/system/notice.js` lines 73-79 ExportNamedDeclaration: listNoticeReadUsers
  - 基线：源语句 sha256=1c995bc05b27d30c97a6d251d250e4b33cdc40417164b5a9132c2e353d275b90；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/notice.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
