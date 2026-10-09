# G250 src/utils/ruoyi.js：完整能力

依赖：G000, G253F033, G253F039

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02766 `ruoyi-fastapi-frontend/src/utils/ruoyi.js` lines 8-8 ImportDeclaration: 
  - 基线：源语句 sha256=cbb71e050eaecb661fa37a91c69b466e8bc7eb0f83176562b012a85463f81de4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/ruoyi.ts
- I02767 `ruoyi-fastapi-frontend/src/utils/ruoyi.js` lines 11-13 ExportNamedDeclaration: parseTime
  - 基线：源语句 sha256=78dfe629d443c7ee2b88972f56a9c389601e7121f4b47c5719aa9c9e7f3ea68b；保留返回、异常及 1 个分支，调用=formatBusinessTime。
  - 去向：react-front/src/utils/ruoyi.ts
- I02768 `ruoyi-fastapi-frontend/src/utils/ruoyi.js` lines 16-20 ExportNamedDeclaration: resetForm
  - 基线：源语句 sha256=1f4a0be7b15ccdf6989e7f1517086abc7427f84c124e7ea10fb98dd33e923f53；保留返回、异常及 1 个分支，调用=ThisExpression.$refs.refName.resetFields。
  - 去向：react-front/src/utils/ruoyi.ts
- I02769 `ruoyi-fastapi-frontend/src/utils/ruoyi.js` lines 23-34 ExportNamedDeclaration: addDateRange
  - 基线：源语句 sha256=4a249ff403e5511dafd7f8b2f49e3bf044b509b6faedddded6a025145707388f；保留返回、异常及 3 个分支，调用=Array.isArray, normalizeRangeBoundary。
  - 去向：react-front/src/utils/ruoyi.ts
- I02770 `ruoyi-fastapi-frontend/src/utils/ruoyi.js` lines 37-52 ExportNamedDeclaration: selectDictLabel
  - 基线：源语句 sha256=18a5cf62fd3dc08f2366f919736cee1399031af9a1f12280e5872686701e45a4；保留返回、异常及 6 个分支，调用=CallExpression.some, Object.keys, actions.push, actions.join。
  - 去向：react-front/src/utils/ruoyi.ts
- I02771 `ruoyi-fastapi-frontend/src/utils/ruoyi.js` lines 55-78 ExportNamedDeclaration: selectDictLabels
  - 基线：源语句 sha256=d97623b9df73b25de062f91c70d47579a6dba3b083dcec5a1cf6dff774adfd43；保留返回、异常及 8 个分支，调用=Array.isArray, value.join, value.split, CallExpression.some, Object.keys, actions.push, CallExpression.substring, actions.join。
  - 去向：react-front/src/utils/ruoyi.ts
- I02772 `ruoyi-fastapi-frontend/src/utils/ruoyi.js` lines 81-93 ExportNamedDeclaration: sprintf
  - 基线：源语句 sha256=d171f66156a225aee26cba32ce9e382201833d2c4675f06fcbf0512730e3a007；保留返回、异常及 5 个分支，调用=str.replace。
  - 去向：react-front/src/utils/ruoyi.ts
- I02773 `ruoyi-fastapi-frontend/src/utils/ruoyi.js` lines 96-101 ExportNamedDeclaration: parseStrEmpty
  - 基线：源语句 sha256=3d256dc5b7c96cfe39ba075c6c940dcf0dbb1a3d63ba977e3f718f16f429f041；保留返回、异常及 5 个分支，调用=。
  - 去向：react-front/src/utils/ruoyi.ts
- I02774 `ruoyi-fastapi-frontend/src/utils/ruoyi.js` lines 104-117 ExportNamedDeclaration: mergeRecursive
  - 基线：源语句 sha256=0b37ae4b4b031af3e3ec5737e594612b069b466e18cd2b2f6f4fcb229971bb3e；保留返回、异常及 3 个分支，调用=mergeRecursive。
  - 去向：react-front/src/utils/ruoyi.ts
- I02775 `ruoyi-fastapi-frontend/src/utils/ruoyi.js` lines 117-117 EmptyStatement: 
  - 基线：源语句 sha256=41b805ea7ac014e23556e98bb374702a08344268f92489a02f0880849394a1e4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/ruoyi.ts
- I02776 `ruoyi-fastapi-frontend/src/utils/ruoyi.js` lines 126-168 ExportNamedDeclaration: handleTree
  - 基线：源语句 sha256=370466e7f2a5b2f287fc63522615f99fbf5a23088ab836a82e0cf3f19828e0cc；保留返回、异常及 8 个分支，调用=childrenListMap.parentId.push, tree.push, adaptToChildrenList。
  - 去向：react-front/src/utils/ruoyi.ts
- I02777 `ruoyi-fastapi-frontend/src/utils/ruoyi.js` lines 174-200 ExportNamedDeclaration: tansParams
  - 基线：源语句 sha256=3f759d7f61828d028629788a0b5918376f6a86b325a9bc0b5a2a1382bbd7d463；保留返回、异常及 12 个分支，调用=Object.keys, encodeURIComponent, Array.isArray。
  - 去向：react-front/src/utils/ruoyi.ts
- I02778 `ruoyi-fastapi-frontend/src/utils/ruoyi.js` lines 204-213 ExportNamedDeclaration: getNormalPath
  - 基线：源语句 sha256=7cb5cc1359fa0968c1472b5ade4af8f9ada3cc8e868e4e2ee787dd6872278e73；保留返回、异常及 7 个分支，调用=p.replace, res.slice。
  - 去向：react-front/src/utils/ruoyi.ts
- I02779 `ruoyi-fastapi-frontend/src/utils/ruoyi.js` lines 216-218 ExportNamedDeclaration: blobValidate
  - 基线：源语句 sha256=d302a9c7ffb0a692d42d0c135ddeaf2331bc30c71b0ffdfe65c5a74693106781；保留返回、异常及 1 个分支，调用=。
  - 去向：react-front/src/utils/ruoyi.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
