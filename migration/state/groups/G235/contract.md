# G235 src/utils/generator/config.js：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02638 `ruoyi-fastapi-frontend/src/utils/generator/config.js` lines 1-12 ExportNamedDeclaration: formConf
  - 基线：源语句 sha256=9c3fec0fbdc7e1b86ea23909e9ef2f8f62ffc179e4a622436f23358537ea70f7；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/generator/config.ts
- I02639 `ruoyi-fastapi-frontend/src/utils/generator/config.js` lines 14-107 ExportNamedDeclaration: inputComponents
  - 基线：源语句 sha256=9c36a5a95d0d973477df5032bb2b41ecf125c49d7b887798e5d461415d3250cb；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/generator/config.ts
- I02640 `ruoyi-fastapi-frontend/src/utils/generator/config.js` lines 109-410 ExportNamedDeclaration: selectComponents
  - 基线：源语句 sha256=256d6a4595019760f9ef3e8c88ef5a3ffc0e374cb27dd6bc85d549a9c65c4309；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/generator/config.ts
- I02641 `ruoyi-fastapi-frontend/src/utils/generator/config.js` lines 412-439 ExportNamedDeclaration: layoutComponents
  - 基线：源语句 sha256=1bdcb08ce452a8f7833395db82cd049588282ea0f81124b7ddfdd156d9e87328；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/generator/config.ts
- I02642 `ruoyi-fastapi-frontend/src/utils/generator/config.js` lines 442-452 ExportNamedDeclaration: trigger
  - 基线：源语句 sha256=bc1fb0c7d82698fcaddf8b45fc49ee3e2d9a1cfdc992258e69e8f31290ccaa69；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/generator/config.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
