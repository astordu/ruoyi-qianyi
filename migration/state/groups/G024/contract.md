# G024 src/App.vue：完整能力

依赖：G000, G228, G252, G253F023

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00441 `ruoyi-fastapi-frontend/src/App.vue` lines 6-6 ImportDeclaration: 
  - 基线：源语句 sha256=88996687f5ac2ffe958aa6952515839565c6f908d46ea4106fe92135e3f788d7；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/App.tsx
- I00442 `ruoyi-fastapi-frontend/src/App.vue` lines 7-7 ImportDeclaration: 
  - 基线：源语句 sha256=f00234927a82d6dda0e854cdc6bd4e18a8ac0f1cb1a6670d355e2a40714f55c0；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/App.tsx
- I00443 `ruoyi-fastapi-frontend/src/App.vue` lines 8-8 ImportDeclaration: 
  - 基线：源语句 sha256=7140ea1fce265da332dd1069c3b2aadea03a33c39a83bc595dfc6d1d0b9965ed；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/App.tsx
- I00444 `ruoyi-fastapi-frontend/src/App.vue` lines 11-15 FunctionDeclaration: refreshTimezoneOnVisible
  - 基线：源语句 sha256=ed4152376347355f53755a962d3b1f7668a464346aa084ec9bf273f149398a52；保留返回、异常及 1 个分支，调用=refreshDeviceTimezone。
  - 去向：react-front/src/App.tsx
- I00445 `ruoyi-fastapi-frontend/src/App.vue` lines 17-24 ExpressionStatement: 
  - 基线：源语句 sha256=c1bec47ed213ce3d9f91468209dc2ad44829b2f11469383a9604a9de8f423a85；保留返回、异常及 0 个分支，调用=onMounted, window.addEventListener, document.addEventListener, nextTick, handleThemeStyle, useSettingsStore。
  - 去向：react-front/src/App.tsx
- I00446 `ruoyi-fastapi-frontend/src/App.vue` lines 25-28 ExpressionStatement: 
  - 基线：源语句 sha256=dc2ad7eac65488401888edc85b40820cc4dc762d30456d0dbdc54a4405d31fb7；保留返回、异常及 0 个分支，调用=onUnmounted, window.removeEventListener, document.removeEventListener。
  - 去向：react-front/src/App.tsx
- I00447 `ruoyi-fastapi-frontend/src/App.vue` template lines 1-3（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/App.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
