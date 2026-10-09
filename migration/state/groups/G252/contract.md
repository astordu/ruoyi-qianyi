# G252 src/utils/theme.js：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02785 `ruoyi-fastapi-frontend/src/utils/theme.js` lines 2-12 ExportNamedDeclaration: handleThemeStyle
  - 基线：源语句 sha256=c4d6a4a78538ce273f529797113e8305aa2c0dd6ea4a6c4cc2468c856dd06b22；保留返回、异常及 2 个分支，调用=document.documentElement.classList.contains, softenPrimaryForDark, document.documentElement.style.setProperty, getLightColor, getDarkColor。
  - 去向：react-front/src/utils/theme.ts
- I02786 `ruoyi-fastapi-frontend/src/utils/theme.js` lines 15-20 ExportNamedDeclaration: mixHexColors
  - 基线：源语句 sha256=ac452b19ef850b7605cd7c2f34100af187314ea34dadb5abc1983c88363f7a79；保留返回、异常及 1 个分支，调用=hexToRgb, CallExpression.replace, String, ArrayExpression.map, Math.round, rgbToHex。
  - 去向：react-front/src/utils/theme.ts
- I02787 `ruoyi-fastapi-frontend/src/utils/theme.js` lines 23-25 ExportNamedDeclaration: softenPrimaryForDark
  - 基线：源语句 sha256=5404a627a0f5c1e1350254a19936c73ba278edc68854755facefbe9cf7364f92；保留返回、异常及 1 个分支，调用=mixHexColors。
  - 去向：react-front/src/utils/theme.ts
- I02788 `ruoyi-fastapi-frontend/src/utils/theme.js` lines 28-35 ExportNamedDeclaration: hexToRgb
  - 基线：源语句 sha256=65e7698dd96bd30973562b3a5465f282e84ad84cc54eeb5e248b1172ece9fa58；保留返回、异常及 1 个分支，调用=str.replace, str.match, parseInt。
  - 去向：react-front/src/utils/theme.ts
- I02789 `ruoyi-fastapi-frontend/src/utils/theme.js` lines 38-46 ExportNamedDeclaration: rgbToHex
  - 基线：源语句 sha256=271c23018649a0bb70eceff5cce6bc4dcb464afd7a228b50bb2288c848a04c87；保留返回、异常及 2 个分支，调用=r.toString, g.toString, b.toString, hexs.join。
  - 去向：react-front/src/utils/theme.ts
- I02790 `ruoyi-fastapi-frontend/src/utils/theme.js` lines 49-55 ExportNamedDeclaration: getLightColor
  - 基线：源语句 sha256=5a33c0c3fdc672dd461595609874c2cb2ae9c466f333e291a001f369257d1caf；保留返回、异常及 1 个分支，调用=hexToRgb, Math.floor, rgbToHex。
  - 去向：react-front/src/utils/theme.ts
- I02791 `ruoyi-fastapi-frontend/src/utils/theme.js` lines 58-64 ExportNamedDeclaration: getDarkColor
  - 基线：源语句 sha256=ba460708306d6327b984db5ef1ff1f78f91bfdbf3e73b4727c37f8116e77dc3a；保留返回、异常及 1 个分支，调用=hexToRgb, Math.floor, rgbToHex。
  - 去向：react-front/src/utils/theme.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
