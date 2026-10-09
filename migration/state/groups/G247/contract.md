# G247 src/utils/pluginPlanFormatter.js：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02733 `ruoyi-fastapi-frontend/src/utils/pluginPlanFormatter.js` lines 1-26 ExportNamedDeclaration: normalizePluginPlanResponse
  - 基线：源语句 sha256=057dd01929f3a7f5ea11cb6788a20568be31727cc090e272191a133ef7833e72；保留返回、异常及 13 个分支，调用=Array.isArray, orderedPluginIds.filter, requestedPluginIdSet.has, Boolean, Number.isInteger。
  - 去向：react-front/src/utils/pluginPlanFormatter.ts
- I02734 `ruoyi-fastapi-frontend/src/utils/pluginPlanFormatter.js` lines 28-46 ExportNamedDeclaration: normalizePluginBatchResponse
  - 基线：源语句 sha256=27a3bae636725541e900f95f7c8d771b6ea37347e835b5faddb372eaab4d5f70；保留返回、异常及 9 个分支，调用=normalizePluginPlanResponse, Boolean, Array.isArray, Number.isInteger。
  - 去向：react-front/src/utils/pluginPlanFormatter.ts
- I02735 `ruoyi-fastapi-frontend/src/utils/pluginPlanFormatter.js` lines 48-55 ExportNamedDeclaration: getPlanOperationLabel
  - 基线：源语句 sha256=e5febf933d0243547d5d49917ddb47c9e4259bba974d80c34f76e64647d28117；保留返回、异常及 4 个分支，调用=operationOptions.find, String。
  - 去向：react-front/src/utils/pluginPlanFormatter.ts
- I02736 `ruoyi-fastapi-frontend/src/utils/pluginPlanFormatter.js` lines 57-59 ExportNamedDeclaration: getPlanReadyTagType
  - 基线：源语句 sha256=21900328cf36e6f750868130fb1e18afda67a677c2b6cef318f8a691c41010a3；保留返回、异常及 2 个分支，调用=。
  - 去向：react-front/src/utils/pluginPlanFormatter.ts
- I02737 `ruoyi-fastapi-frontend/src/utils/pluginPlanFormatter.js` lines 61-73 ExportNamedDeclaration: getPlanBlockerStatusLabel
  - 基线：源语句 sha256=c9b4154907e1cf0a355eb5577318b19be16c976b940a8fece6e218567c109258；保留返回、异常及 3 个分支，调用=。
  - 去向：react-front/src/utils/pluginPlanFormatter.ts
- I02738 `ruoyi-fastapi-frontend/src/utils/pluginPlanFormatter.js` lines 75-83 ExportNamedDeclaration: getValidationLevelLabel
  - 基线：源语句 sha256=a4906cd6d86d45ca67bb5c63e3edc0018fdc8e11386a431e255a6eee6b296126；保留返回、异常及 3 个分支，调用=。
  - 去向：react-front/src/utils/pluginPlanFormatter.ts
- I02739 `ruoyi-fastapi-frontend/src/utils/pluginPlanFormatter.js` lines 85-93 ExportNamedDeclaration: getValidationLevelTagType
  - 基线：源语句 sha256=d04632b21efd3891c8366a17b462de1e5a937cca0c35c0d7b409cbca5a35d463；保留返回、异常及 2 个分支，调用=。
  - 去向：react-front/src/utils/pluginPlanFormatter.ts
- I02740 `ruoyi-fastapi-frontend/src/utils/pluginPlanFormatter.js` lines 95-120 ExportNamedDeclaration: normalizePluginActionResult
  - 基线：源语句 sha256=271b46cfdc58e99cd13626503b59c96fa6060891d5df18112245ba8d2a80eb98；保留返回、异常及 15 个分支，调用=Array.isArray。
  - 去向：react-front/src/utils/pluginPlanFormatter.ts
- I02741 `ruoyi-fastapi-frontend/src/utils/pluginPlanFormatter.js` lines 122-138 ExportNamedDeclaration: normalizePluginOperationLogDetail
  - 基线：源语句 sha256=56b88dad865249edda350df856580d360b3167694ef8266ab7fd806f44a14a51；保留返回、异常及 8 个分支，调用=Array.isArray, buildOperationValidationItems, buildOperationConfigChanges, buildOperationFailedSuggestion。
  - 去向：react-front/src/utils/pluginPlanFormatter.ts
- I02742 `ruoyi-fastapi-frontend/src/utils/pluginPlanFormatter.js` lines 140-162 FunctionDeclaration: buildOperationValidationItems
  - 基线：源语句 sha256=5cd4d9e532c5a3fbafdf6f2adc193cae0d7a8564015137d0a90c45ab36440b3d；保留返回、异常及 22 个分支，调用=Array.isArray, validationGroups.flatMap, items.map, category.includes。
  - 去向：react-front/src/utils/pluginPlanFormatter.ts
- I02743 `ruoyi-fastapi-frontend/src/utils/pluginPlanFormatter.js` lines 164-180 FunctionDeclaration: buildOperationConfigChanges
  - 基线：源语句 sha256=70c6084f16ce55241033c51754e5cc6d1652f450a19f3b6eae63ebbe452a78bb；保留返回、异常及 6 个分支，调用=Array.isArray, changedKeys.map。
  - 去向：react-front/src/utils/pluginPlanFormatter.ts
- I02744 `ruoyi-fastapi-frontend/src/utils/pluginPlanFormatter.js` lines 182-190 FunctionDeclaration: buildOperationFailedSuggestion
  - 基线：源语句 sha256=a5ae72feac7cf4bf19d9f37d38237893eef8751d164550f0b4d8ddeab9eeb88f；保留返回、异常及 5 个分支，调用=。
  - 去向：react-front/src/utils/pluginPlanFormatter.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
