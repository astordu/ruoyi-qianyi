# G240 src/utils/generator/js.js：完整能力

依赖：G000, G235, G242

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02670 `ruoyi-fastapi-frontend/src/utils/generator/js.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=dae150d18ec4760ac14ce8284ee7994cf50b99d3111d639161e6f4001cb153c2；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/generator/js.ts
- I02671 `ruoyi-fastapi-frontend/src/utils/generator/js.js` lines 2-2 ImportDeclaration: 
  - 基线：源语句 sha256=3a60a4efa58b64cf1de37c90f7de6a8e9343defe0cfefda0917c091349cf83e9；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/generator/js.ts
- I02672 `ruoyi-fastapi-frontend/src/utils/generator/js.js` lines 4-8 VariableDeclaration: units
  - 基线：源语句 sha256=52e14a2ee42a73e420b603cba5fef514fc54cdffc38521ebca6f04d8a0d235fe；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/generator/js.ts
- I02673 `ruoyi-fastapi-frontend/src/utils/generator/js.js` lines 16-49 ExportNamedDeclaration: makeUpJs
  - 基线：源语句 sha256=4944857bf082324d035b8f0735d286ab71e0b3da7ebbe395e7fea38fc1686dad；保留返回、异常及 1 个分支，调用=JSON.parse, JSON.stringify, conf.fields.forEach, buildAttributes, buildexport, dataList.join, ruleList.join, optionsList.join, uploadVarList.join, propsList.join, methodList.join。
  - 去向：react-front/src/utils/generator/js.ts
- I02674 `ruoyi-fastapi-frontend/src/utils/generator/js.js` lines 55-107 FunctionDeclaration: buildAttributes
  - 基线：源语句 sha256=700bdc8ed1e5dfcefb14de753d29b9f8ce51c6f5fc8faefe7c474a16fcd58d72；保留返回、异常及 9 个分支，调用=buildData, buildRules, buildOptions, titleCase, buildOptionMethod, buildProps, uploadVarList.push, methodList.push, buildBeforeUpload, buildSubmitUpload, el.children.forEach, buildAttributes。
  - 去向：react-front/src/utils/generator/js.ts
- I02675 `ruoyi-fastapi-frontend/src/utils/generator/js.js` lines 115-124 FunctionDeclaration: buildData
  - 基线：源语句 sha256=2e8138b0cdafaa502875192e372c4b744844a3ba5e11a7ba7e3a601c2be36042；保留返回、异常及 4 个分支，调用=JSON.stringify, dataList.push。
  - 去向：react-front/src/utils/generator/js.ts
- I02676 `ruoyi-fastapi-frontend/src/utils/generator/js.js` lines 132-161 FunctionDeclaration: buildRules
  - 基线：源语句 sha256=3a556c81ca4d1bd1cbff051e0c7efca86db5164f349356e6db40685b70b891b8；保留返回、异常及 10 个分支，调用=Array.isArray, rules.push, conf.regList.forEach, ruleList.push, rules.join。
  - 去向：react-front/src/utils/generator/js.ts
- I02677 `ruoyi-fastapi-frontend/src/utils/generator/js.js` lines 169-176 FunctionDeclaration: buildOptions
  - 基线：源语句 sha256=cebeb5e6d00b0c319bc49735eec860b4a006ddd82e69a72e74f886ac46441301；保留返回、异常及 3 个分支，调用=JSON.stringify, optionsList.push。
  - 去向：react-front/src/utils/generator/js.ts
- I02678 `ruoyi-fastapi-frontend/src/utils/generator/js.js` lines 185-191 FunctionDeclaration: buildOptionMethod
  - 基线：源语句 sha256=77993eb96a48f569f35c708b1e12c56ae589ed113b377b8d3695989e579e5e89；保留返回、异常及 0 个分支，调用=methodList.push。
  - 去向：react-front/src/utils/generator/js.ts
- I02679 `ruoyi-fastapi-frontend/src/utils/generator/js.js` lines 199-210 FunctionDeclaration: buildProps
  - 基线：源语句 sha256=4da0071c607508b2bdff7d58c52622d68c40d28dbf2c9c4b44f291ac01c262ab；保留返回、异常及 4 个分支，调用=JSON.stringify, propsList.push。
  - 去向：react-front/src/utils/generator/js.ts
- I02680 `ruoyi-fastapi-frontend/src/utils/generator/js.js` lines 217-249 FunctionDeclaration: buildBeforeUpload
  - 基线：源语句 sha256=8fdd73e6d9d8e29ef98f2837f651beb70d447327bfdc6da356eb054011019d28；保留返回、异常及 4 个分支，调用=returnList.push, returnList.join。
  - 去向：react-front/src/utils/generator/js.ts
- I02681 `ruoyi-fastapi-frontend/src/utils/generator/js.js` lines 256-261 FunctionDeclaration: buildSubmitUpload
  - 基线：源语句 sha256=575b4efba7900eca2f0bc8d28878bcce417651a6ba960c0fe93799c9dfc0a6c3；保留返回、异常及 1 个分支，调用=。
  - 去向：react-front/src/utils/generator/js.ts
- I02682 `ruoyi-fastapi-frontend/src/utils/generator/js.js` lines 267-370 FunctionDeclaration: buildexport
  - 基线：源语句 sha256=97876fcb8ff7887afe245ffcda785ffce2bb2169fb149c13042cf3a468135aea；保留返回、异常及 2 个分支，调用=。
  - 去向：react-front/src/utils/generator/js.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
