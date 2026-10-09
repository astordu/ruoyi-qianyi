# G244 src/utils/jsencrypt.js：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02721 `ruoyi-fastapi-frontend/src/utils/jsencrypt.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=02449ad390618ad45ccabfa8dd8e5d645583c4305d7bc4706083b1a32575da68；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/jsencrypt.ts
- I02722 `ruoyi-fastapi-frontend/src/utils/jsencrypt.js` lines 5-6 VariableDeclaration: publicKey
  - 基线：源语句 sha256=a338748634156705ecb71947e3a4bdde63ee0e668eeee0c3de2daa771b1c1c96；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/jsencrypt.ts
- I02723 `ruoyi-fastapi-frontend/src/utils/jsencrypt.js` lines 8-15 VariableDeclaration: privateKey
  - 基线：源语句 sha256=77fac920a08fb5e222ee458a30fd24e30e39329ec9c38ec1cbaf953f00894729；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/jsencrypt.ts
- I02724 `ruoyi-fastapi-frontend/src/utils/jsencrypt.js` lines 18-22 ExportNamedDeclaration: encrypt
  - 基线：源语句 sha256=8d2938120195822ae1a4c26531e176e504db1ca881dc22ae2b63f5a2c7b025c0；保留返回、异常及 1 个分支，调用=encryptor.setPublicKey, encryptor.encrypt。
  - 去向：react-front/src/utils/jsencrypt.ts
- I02725 `ruoyi-fastapi-frontend/src/utils/jsencrypt.js` lines 25-29 ExportNamedDeclaration: decrypt
  - 基线：源语句 sha256=1c64c8481c02f16079ce555edebf91bba640653f35e898d7cd053a62f8edc022；保留返回、异常及 1 个分支，调用=encryptor.setPrivateKey, encryptor.decrypt。
  - 去向：react-front/src/utils/jsencrypt.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
