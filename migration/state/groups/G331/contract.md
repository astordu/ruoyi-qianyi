# G331 tests/plugins/pluginViewResolver.test.js：完整能力

依赖：G000, G248

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I08715 `ruoyi-fastapi-frontend/tests/plugins/pluginViewResolver.test.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=a4635e5c72089cbfa239a6a50420de223fe688748a52da7028ae0a399c6e3152；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/tests/plugins/pluginViewResolver.test.ts
- I08716 `ruoyi-fastapi-frontend/tests/plugins/pluginViewResolver.test.js` lines 3-3 ImportDeclaration: 
  - 基线：源语句 sha256=329847895183d9473ce18734b0218870987da499504da19ee2a932a442ea6eb1；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/tests/plugins/pluginViewResolver.test.ts
- I08717 `ruoyi-fastapi-frontend/tests/plugins/pluginViewResolver.test.js` lines 5-5 ExpressionStatement: 
  - 基线：源语句 sha256=72140d925577d768d933bbcfcdd3741a89da176c4a5ab5c8fd76e5f27c631348；保留返回、异常及 0 个分支，调用=assert.equal, resolvePluginViewPath。
  - 去向：react-front/tests/plugins/pluginViewResolver.test.ts
- I08718 `ruoyi-fastapi-frontend/tests/plugins/pluginViewResolver.test.js` lines 6-6 ExpressionStatement: 
  - 基线：源语句 sha256=c6ecd692f37d3049bcc60ad7504e20eb9aa21d156a6c0d4b6ca7b881f9d290c7；保留返回、异常及 0 个分支，调用=assert.equal, resolvePluginViewPath。
  - 去向：react-front/tests/plugins/pluginViewResolver.test.ts
- I08719 `ruoyi-fastapi-frontend/tests/plugins/pluginViewResolver.test.js` lines 7-7 ExpressionStatement: 
  - 基线：源语句 sha256=d457dc4cb2a77793e942f26d8cc9994ad2141787e88251b666c2b6aba6c521d9；保留返回、异常及 0 个分支，调用=assert.equal, resolvePluginViewPath。
  - 去向：react-front/tests/plugins/pluginViewResolver.test.ts
- I08720 `ruoyi-fastapi-frontend/tests/plugins/pluginViewResolver.test.js` lines 8-8 ExpressionStatement: 
  - 基线：源语句 sha256=0515dc4245f84090bf8203d3b3d4509c04c26ebb9f841927b8e7050b172a29a5；保留返回、异常及 0 个分支，调用=assert.equal, resolvePluginViewPath。
  - 去向：react-front/tests/plugins/pluginViewResolver.test.ts
- I08721 `ruoyi-fastapi-frontend/tests/plugins/pluginViewResolver.test.js` lines 9-9 ExpressionStatement: 
  - 基线：源语句 sha256=cc983606400e6be34dd5f5acd535e6c128aa0b2bf43ba15fd86ecb3bbdf52cc2；保留返回、异常及 0 个分支，调用=assert.equal, resolvePluginViewPath。
  - 去向：react-front/tests/plugins/pluginViewResolver.test.ts
- I08722 `ruoyi-fastapi-frontend/tests/plugins/pluginViewResolver.test.js` lines 10-10 ExpressionStatement: 
  - 基线：源语句 sha256=d1fde348b3710611da9790c7e552695f134d4d386df1b13e7ddfd489cf147a77；保留返回、异常及 0 个分支，调用=assert.equal, resolvePluginViewPath。
  - 去向：react-front/tests/plugins/pluginViewResolver.test.ts
- I08723 `ruoyi-fastapi-frontend/tests/plugins/pluginViewResolver.test.js` lines 11-11 ExpressionStatement: 
  - 基线：源语句 sha256=9c748289d76702d7b2b37f2e95a8d12b4ec898cddb10c0ebecbb0b348501f064；保留返回、异常及 0 个分支，调用=assert.equal, resolvePluginViewPath。
  - 去向：react-front/tests/plugins/pluginViewResolver.test.ts
- I08724 `ruoyi-fastapi-frontend/tests/plugins/pluginViewResolver.test.js` lines 12-12 ExpressionStatement: 
  - 基线：源语句 sha256=0dd75c5e441e3dc849a8b3162a21c0ca55d6ff1504940f273e36fc08067e1cc4；保留返回、异常及 0 个分支，调用=assert.equal, resolvePluginViewPath。
  - 去向：react-front/tests/plugins/pluginViewResolver.test.ts
- I08725 `ruoyi-fastapi-frontend/tests/plugins/pluginViewResolver.test.js` lines 13-13 ExpressionStatement: 
  - 基线：源语句 sha256=69cc763254073b5acfc099b51406d2c727c5bd7afd09b618acb6ac5d63fd86a9；保留返回、异常及 0 个分支，调用=assert.equal, resolvePluginViewPath。
  - 去向：react-front/tests/plugins/pluginViewResolver.test.ts
- I08726 `ruoyi-fastapi-frontend/tests/plugins/pluginViewResolver.test.js` lines 14-14 ExpressionStatement: 
  - 基线：源语句 sha256=d12567fb619fc9001142512d9177d1589266f84eb77de55cdadd638a1443cf65；保留返回、异常及 0 个分支，调用=assert.equal, resolvePluginViewPath。
  - 去向：react-front/tests/plugins/pluginViewResolver.test.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
