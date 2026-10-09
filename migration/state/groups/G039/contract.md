# G039 src/api/system/file.js：完整能力

依赖：G000, G249

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00529 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=cd462474cb30a9a5954fbd44474b2f4e19f6d48d3c7dff5aebf452db4c8517f8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/api/system/file.ts
- I00530 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 4-10 ExportNamedDeclaration: listFile
  - 基线：源语句 sha256=1aea97c06872cdd385ae88ee784c770cc6af034c80dd20ea090a8690440a7d42；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00531 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 13-19 ExportNamedDeclaration: getFileStats
  - 基线：源语句 sha256=d6274d9fce4f92a9ad4204c45b0cdd7f9e56348708b6da32d35dd1f11bc2ae5d；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00532 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 22-28 ExportNamedDeclaration: listFileReconcileIssue
  - 基线：源语句 sha256=69577c816addd0494bbb289402f34ad195cf95816da9beaf39eb52d2d52bbc3f；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00533 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 31-37 ExportNamedDeclaration: listFileReconcileRun
  - 基线：源语句 sha256=acaab3e093a175cb031eb5ceb8f87d53a9f9f676f7dfaa42b6f2b13efcf0653f；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00534 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 40-45 ExportNamedDeclaration: getFileReconcileStats
  - 基线：源语句 sha256=cbd3929846eef6c64a2584deb6d10299d505c099e9d428d69948041e9c649160；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00535 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 48-54 ExportNamedDeclaration: startFileReconcile
  - 基线：源语句 sha256=cd8e4f8bfbf1ca516c2d18716b54ac7a3b9162e78eff765655722b675cbfeea5；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00536 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 57-63 ExportNamedDeclaration: handleFileReconcileIssue
  - 基线：源语句 sha256=45f07ce2a1df7b79e1f40ac9a4b9473b8013841c3c61a2a898b566e4add43734；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00537 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 66-71 ExportNamedDeclaration: listFileRetentionPolicy
  - 基线：源语句 sha256=beefeeb778ef6d89604b32dcc6057607a0fb488385c549dcd207d0fd013a3d9e；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00538 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 74-80 ExportNamedDeclaration: addFileRetentionPolicy
  - 基线：源语句 sha256=7181b1a9594e8173480bff82041c2777ec516106f78b5c889849faa31a27c433；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00539 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 83-89 ExportNamedDeclaration: updateFileRetentionPolicy
  - 基线：源语句 sha256=3509e4ac76f3ef0b952ea2a207b166a9ddbd3aa10d9ec76460ffbdd40841ff44；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00540 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 92-97 ExportNamedDeclaration: delFileRetentionPolicy
  - 基线：源语句 sha256=32e00cded401d50f308342254fe576e56158614c45d8f6de3d19fdb6b84abb9b；保留返回、异常及 1 个分支，调用=request, encodeURIComponent。
  - 去向：react-front/src/api/system/file.ts
- I00541 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 100-106 ExportNamedDeclaration: listFileRetentionReminder
  - 基线：源语句 sha256=3c84dfa42f8f36d4f5089ae7ea725dd3fdd215bb391eedd6d6d531cb5f1f6eeb；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00542 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 109-114 ExportNamedDeclaration: scanFileRetentionReminder
  - 基线：源语句 sha256=bd9f733c48ac5c6612573e17c8bd26ac2d10c600e0310df85f28fc508f67893c；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00543 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 117-122 ExportNamedDeclaration: readFileRetentionReminder
  - 基线：源语句 sha256=6af299dac6344a04cf22928891f92129b5b3240bbb69dabd2b65168063ca6c4d；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00544 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 125-131 ExportNamedDeclaration: extendFileRetention
  - 基线：源语句 sha256=71aad0a989a35950b4dd78f3db50db69882391ab7f822d631f6642e449256b3e；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00545 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 134-140 ExportNamedDeclaration: disposeExpiredFile
  - 基线：源语句 sha256=0b90800c3ce385898c56b185309ff3564eecbaaacae0d9b3f4def3e6825b3810；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00546 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 143-148 ExportNamedDeclaration: getFile
  - 基线：源语句 sha256=784a9ea334f0aad500ce6182f3318d9f01f612004170327aa1de3df0bbdcd06e；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00547 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 151-156 ExportNamedDeclaration: listFileReference
  - 基线：源语句 sha256=3bc25ab3ce49753625920afed4dcf38ab40fc9e0d78f18da7ff8e14b5d7c8429；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00548 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 159-165 ExportNamedDeclaration: listFileAccessLog
  - 基线：源语句 sha256=d77dadd5781b4cf7af73523a2ece9aa8bbd49af552c39b85b1fcb9f48708c40c；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00549 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 168-173 ExportNamedDeclaration: listFileAcl
  - 基线：源语句 sha256=c21bb0ba172044d88f7f0718e4a83a8366561d2a01227780e9a7a2c81510da19；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00550 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 176-182 ExportNamedDeclaration: searchFileAclSubjects
  - 基线：源语句 sha256=5c20440498c2a2de14651a0eb48b9cc62529693c96aa37b745399b9db86a6747；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00551 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 185-190 ExportNamedDeclaration: getFileAclDeptTree
  - 基线：源语句 sha256=4d1dd4578f22a4bb7fd6b53b5e793141fecdb4c1d9f619ff624436f2cec6c46b；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00552 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 193-199 ExportNamedDeclaration: saveFileAcl
  - 基线：源语句 sha256=d3124a76ecc8e59b7d11b047d78fbd07cafb7230256e3d2804ed8a41b53a6908；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00553 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 202-208 ExportNamedDeclaration: batchSaveFileAcl
  - 基线：源语句 sha256=db31c244c4edab5ee0869de9086c6ae3de1fcc1049ad5366b29d0bd0665299d4；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00554 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 211-217 ExportNamedDeclaration: transferFile
  - 基线：源语句 sha256=fdb74a43cd6383d1b1c815402c3b770057f10c759a24806f1dd97c9649e80a56；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00555 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 220-225 ExportNamedDeclaration: restoreFile
  - 基线：源语句 sha256=f825c828c25f8741e535b8e65a1be93a5c9c1b922c5beb3b5bd4f8246c5f0951；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00556 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 228-233 ExportNamedDeclaration: purgeFile
  - 基线：源语句 sha256=5ac9fde85d9bb6efcc36b519e7fb12b9bf63b43115c296c34c9481453876d8d4；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts
- I00557 `ruoyi-fastapi-frontend/src/api/system/file.js` lines 236-241 ExportNamedDeclaration: delFile
  - 基线：源语句 sha256=17f1b7b4ac0b4e6e801d770f45e5cff82ca763afcc6ff6b63477284bade51fcb；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/file.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
