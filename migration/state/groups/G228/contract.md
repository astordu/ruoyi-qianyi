# G228 src/store/modules/settings.js：完整能力

依赖：G000, G222, G252

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02596 `ruoyi-fastapi-frontend/src/store/modules/settings.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=c9c128b54ab88c97d92ae51e2a1065c1ade8d91f9c9c2e9070a7b4c15774f713；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/settings.ts
- I02597 `ruoyi-fastapi-frontend/src/store/modules/settings.js` lines 2-2 ImportDeclaration: 
  - 基线：源语句 sha256=d020cb48a73c7bff244478daacb33690e2b8d91d9c134d801e3fc27bfe2c4260；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/settings.ts
- I02598 `ruoyi-fastapi-frontend/src/store/modules/settings.js` lines 3-3 ImportDeclaration: 
  - 基线：源语句 sha256=87e5678a9afb2147bacfe557e3a6712f261cf6de0d10ad6033356e406c1083a8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/settings.ts
- I02599 `ruoyi-fastapi-frontend/src/store/modules/settings.js` lines 4-4 ImportDeclaration: 
  - 基线：源语句 sha256=f00234927a82d6dda0e854cdc6bd4e18a8ac0f1cb1a6670d355e2a40714f55c0；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/settings.ts
- I02600 `ruoyi-fastapi-frontend/src/store/modules/settings.js` lines 6-6 VariableDeclaration: isDark
  - 基线：源语句 sha256=2cbabc39f9274d1a47eb9dc0752060dbb4aac7ae39ca940db6b1890e6a728420；保留返回、异常及 0 个分支，调用=useDark。
  - 去向：react-front/src/store/modules/settings.ts
- I02601 `ruoyi-fastapi-frontend/src/store/modules/settings.js` lines 7-7 VariableDeclaration: toggleDark
  - 基线：源语句 sha256=31408585c0aea41df997772a27eab8770592be86d13c17744da2837aa2782f9b；保留返回、异常及 0 个分支，调用=useToggle。
  - 去向：react-front/src/store/modules/settings.ts
- I02602 `ruoyi-fastapi-frontend/src/store/modules/settings.js` lines 9-9 VariableDeclaration: 
  - 基线：源语句 sha256=b77b0ed7b6d4321b28dd7e4369294d84c3d96eb51982e51e3a4b979132150734；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/settings.ts
- I02603 `ruoyi-fastapi-frontend/src/store/modules/settings.js` lines 11-11 VariableDeclaration: storageSetting
  - 基线：源语句 sha256=46deec8f9d7a3e69b8d2488bdebdde88071ee895a0f4caa210692b27da7348c4；保留返回、异常及 1 个分支，调用=JSON.parse, localStorage.getItem。
  - 去向：react-front/src/store/modules/settings.ts
- I02604 `ruoyi-fastapi-frontend/src/store/modules/settings.js` lines 13-55 VariableDeclaration: useSettingsStore
  - 基线：源语句 sha256=650e32d8378c622adae28234e9a911ff618edddd8f5b4cb162f5af9c533aa3ef；保留返回、异常及 12 个分支，调用=defineStore, ThisExpression.hasOwnProperty, useDynamicTitle, toggleDark, nextTick, handleThemeStyle。
  - 去向：react-front/src/store/modules/settings.ts
- I02605 `ruoyi-fastapi-frontend/src/store/modules/settings.js` lines 57-57 ExportDefaultDeclaration: 
  - 基线：源语句 sha256=9769b379298f9ebd92c60fc6d0fb31ae1324a10f2a66b38fe6f3371a0c9f729f；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/store/modules/settings.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
