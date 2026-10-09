# G238 src/utils/generator/html.js：完整能力

依赖：G000, G235

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02649 `ruoyi-fastapi-frontend/src/utils/generator/html.js` lines 2-2 ImportDeclaration: 
  - 基线：源语句 sha256=3a60a4efa58b64cf1de37c90f7de6a8e9343defe0cfefda0917c091349cf83e9；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/generator/html.ts
- I02650 `ruoyi-fastapi-frontend/src/utils/generator/html.js` lines 4-4 VariableDeclaration: confGlobal
  - 基线：源语句 sha256=0474b863e4e81c50359ca736e65165bb42621eebf8269dcfc3d970fc1e9a2d00；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/generator/html.ts
- I02651 `ruoyi-fastapi-frontend/src/utils/generator/html.js` lines 5-5 VariableDeclaration: someSpanIsNot24
  - 基线：源语句 sha256=e58573f764c350c9a42cab43f718486e8128ca10ce3d34865dda710deedf76c0；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/generator/html.ts
- I02652 `ruoyi-fastapi-frontend/src/utils/generator/html.js` lines 7-15 ExportNamedDeclaration: dialogWrapper
  - 基线：源语句 sha256=a492887b4534f9e810f47b4b3716fd9537a5b2c62e9a6f81d8db6d9157fe486e；保留返回、异常及 1 个分支，调用=。
  - 去向：react-front/src/utils/generator/html.ts
- I02653 `ruoyi-fastapi-frontend/src/utils/generator/html.js` lines 17-23 ExportNamedDeclaration: vueTemplate
  - 基线：源语句 sha256=edcb47b48e7dbef4fe0a3f094d2a490f0c799304f7bf23eee8f2ea8338a96847；保留返回、异常及 1 个分支，调用=。
  - 去向：react-front/src/utils/generator/html.ts
- I02654 `ruoyi-fastapi-frontend/src/utils/generator/html.js` lines 25-29 ExportNamedDeclaration: vueScript
  - 基线：源语句 sha256=a2b9a086901c2bb6fe85722bc1b5e640dcc43d0580fc01382edee8ee15f3aec1；保留返回、异常及 1 个分支，调用=。
  - 去向：react-front/src/utils/generator/html.ts
- I02655 `ruoyi-fastapi-frontend/src/utils/generator/html.js` lines 31-35 ExportNamedDeclaration: cssStyle
  - 基线：源语句 sha256=1e6e7953dcb080910c2c613e7bbcb72590e3813ecd50094c6ac9b8238dd28c11；保留返回、异常及 1 个分支，调用=。
  - 去向：react-front/src/utils/generator/html.ts
- I02656 `ruoyi-fastapi-frontend/src/utils/generator/html.js` lines 37-53 FunctionDeclaration: buildFormTemplate
  - 基线：源语句 sha256=4700f5d0d643065036c4fa338cb07955feca37f6e1672499b21b7cdf40a30915；保留返回、异常及 4 个分支，调用=buildFromBtns。
  - 去向：react-front/src/utils/generator/html.ts
- I02657 `ruoyi-fastapi-frontend/src/utils/generator/html.js` lines 55-69 FunctionDeclaration: buildFromBtns
  - 基线：源语句 sha256=02c005b3223c5a6c2e007207474eb7b6f1e6e4daa9d8aecb10f0b5c4fffd5da0；保留返回、异常及 4 个分支，调用=。
  - 去向：react-front/src/utils/generator/html.ts
- I02658 `ruoyi-fastapi-frontend/src/utils/generator/html.js` lines 72-79 FunctionDeclaration: colWrapper
  - 基线：源语句 sha256=387a627849384f4931332e612e3dd8500eb0f2503d5d7f48a194897fad214021；保留返回、异常及 4 个分支，调用=。
  - 去向：react-front/src/utils/generator/html.ts
- I02659 `ruoyi-fastapi-frontend/src/utils/generator/html.js` lines 81-107 VariableDeclaration: layouts
  - 基线：源语句 sha256=587beab178be08e5bc4b3dde51772ab29eaa3b49cbf42c33eb3be6995eaa58de；保留返回、异常及 11 个分支，调用=tags.element.tag, colWrapper, element.children.map, layouts.el.layout, children.join。
  - 去向：react-front/src/utils/generator/html.ts
- I02660 `ruoyi-fastapi-frontend/src/utils/generator/html.js` lines 109-275 VariableDeclaration: tags
  - 基线：源语句 sha256=7ec0229f22afad977308f48cdb701ea078cfa3ade7929314fdbb045d4368eb25；保留返回、异常及 85 个分支，调用=attrBuilder, buildElButtonChild, buildElInputChild, buildElSelectChild, buildElRadioGroupChild, buildElCheckboxGroupChild, JSON.stringify, buildElUploadChild。
  - 去向：react-front/src/utils/generator/html.ts
- I02661 `ruoyi-fastapi-frontend/src/utils/generator/html.js` lines 277-285 FunctionDeclaration: attrBuilder
  - 基线：源语句 sha256=c1b79f3ecb3fe4898ed0cacbe341cc428d30b1f2a11c442830cfa044d5ef02ed；保留返回、异常及 6 个分支，调用=。
  - 去向：react-front/src/utils/generator/html.ts
- I02662 `ruoyi-fastapi-frontend/src/utils/generator/html.js` lines 288-294 FunctionDeclaration: buildElButtonChild
  - 基线：源语句 sha256=4372ce83479abd3a9c62f08ec9c96efa1b23678d9a8e30efa8392bf15bfa102a；保留返回、异常及 2 个分支，调用=children.push, children.join。
  - 去向：react-front/src/utils/generator/html.ts
- I02663 `ruoyi-fastapi-frontend/src/utils/generator/html.js` lines 297-306 FunctionDeclaration: buildElInputChild
  - 基线：源语句 sha256=e6ba6a21ff7c86ca34bb69005cd353da138def8863a265a803a2a11bbb85b311；保留返回、异常及 3 个分支，调用=children.push, children.join。
  - 去向：react-front/src/utils/generator/html.ts
- I02664 `ruoyi-fastapi-frontend/src/utils/generator/html.js` lines 308-314 FunctionDeclaration: buildElSelectChild
  - 基线：源语句 sha256=982aa7dee268e1a10c553da160917369339c0e2fc698541a440be12e715d319c；保留返回、异常及 3 个分支，调用=children.push, children.join。
  - 去向：react-front/src/utils/generator/html.ts
- I02665 `ruoyi-fastapi-frontend/src/utils/generator/html.js` lines 316-324 FunctionDeclaration: buildElRadioGroupChild
  - 基线：源语句 sha256=e1d746924feeb0b0b72c0658deaebc12fe4d44beb27ec5d02b76ee02b1a09ef8；保留返回、异常及 5 个分支，调用=children.push, children.join。
  - 去向：react-front/src/utils/generator/html.ts
- I02666 `ruoyi-fastapi-frontend/src/utils/generator/html.js` lines 326-334 FunctionDeclaration: buildElCheckboxGroupChild
  - 基线：源语句 sha256=c7c64a2d994d986c8410b1390fdb3f8c43c45c2101bcfde7cc079cbc148840bb；保留返回、异常及 5 个分支，调用=children.push, children.join。
  - 去向：react-front/src/utils/generator/html.ts
- I02667 `ruoyi-fastapi-frontend/src/utils/generator/html.js` lines 336-342 FunctionDeclaration: buildElUploadChild
  - 基线：源语句 sha256=b318fb08b5199df08177597e9e2ff88401168a09c1e8f0ac3b1787cdc8351dfe；保留返回、异常及 3 个分支，调用=list.push, list.join。
  - 去向：react-front/src/utils/generator/html.ts
- I02668 `ruoyi-fastapi-frontend/src/utils/generator/html.js` lines 344-359 ExportNamedDeclaration: makeUpHtml
  - 基线：源语句 sha256=43eeb33c82f000beaedeb60a57cfef71065dcf888bc95b1298fd0fae22dca1bd；保留返回、异常及 2 个分支，调用=conf.fields.some, conf.fields.forEach, htmlList.push, layouts.el.layout, htmlList.join, buildFormTemplate, dialogWrapper。
  - 去向：react-front/src/utils/generator/html.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
