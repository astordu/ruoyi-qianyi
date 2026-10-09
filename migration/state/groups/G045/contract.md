# G045 src/api/system/user.js：完整能力

依赖：G000, G249, G250

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00621 `ruoyi-fastapi-frontend/src/api/system/user.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=cd462474cb30a9a5954fbd44474b2f4e19f6d48d3c7dff5aebf452db4c8517f8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/api/system/user.ts
- I00622 `ruoyi-fastapi-frontend/src/api/system/user.js` lines 2-2 ImportDeclaration: 
  - 基线：源语句 sha256=a55c25638bb45b4c33ba30e881315948dbb00858b987ded70260a5428baddde3；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/api/system/user.ts
- I00623 `ruoyi-fastapi-frontend/src/api/system/user.js` lines 5-11 ExportNamedDeclaration: listUser
  - 基线：源语句 sha256=fd002aeddd2ebd7a31757d4b06fb6ac9faed6a9024a2ec31bdbb4710adb402f1；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/user.ts
- I00624 `ruoyi-fastapi-frontend/src/api/system/user.js` lines 14-19 ExportNamedDeclaration: getUser
  - 基线：源语句 sha256=babb27ff8944a9e208ee3efaa5324a746cfccc5870ce754408e5d279381dc008；保留返回、异常及 1 个分支，调用=request, parseStrEmpty。
  - 去向：react-front/src/api/system/user.ts
- I00625 `ruoyi-fastapi-frontend/src/api/system/user.js` lines 22-28 ExportNamedDeclaration: addUser
  - 基线：源语句 sha256=ab263c18c4397d3c54b31ea0e6f79210ebd8e3d9ee6de0ac084787aab3460d6d；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/user.ts
- I00626 `ruoyi-fastapi-frontend/src/api/system/user.js` lines 31-37 ExportNamedDeclaration: updateUser
  - 基线：源语句 sha256=7285990ce1f2d4663aa662d23371578d4b9b3b8858d1d1de93e04fe644844abd；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/user.ts
- I00627 `ruoyi-fastapi-frontend/src/api/system/user.js` lines 40-45 ExportNamedDeclaration: delUser
  - 基线：源语句 sha256=448ed694266d7dafd49931e354c120ad9c0840af6a7796d42d4a9396616749fb；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/user.ts
- I00628 `ruoyi-fastapi-frontend/src/api/system/user.js` lines 48-58 ExportNamedDeclaration: resetUserPwd
  - 基线：源语句 sha256=8b9a959b63078f738e7cf3cf0a4e34bbe91020fc8f420a2b420ed2adbfd7cf2c；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/user.ts
- I00629 `ruoyi-fastapi-frontend/src/api/system/user.js` lines 61-71 ExportNamedDeclaration: changeUserStatus
  - 基线：源语句 sha256=a7d24f41b4a851851e990f45df6f00a04f375c9de3a762b68e8a68c44690d9f6；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/user.ts
- I00630 `ruoyi-fastapi-frontend/src/api/system/user.js` lines 74-79 ExportNamedDeclaration: getUserProfile
  - 基线：源语句 sha256=bcfc72d3be7e2fb4ad49d9fdbd6c4d674e11e03f749b17fa586053514ff89c1d；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/user.ts
- I00631 `ruoyi-fastapi-frontend/src/api/system/user.js` lines 82-84 ExportNamedDeclaration: getTimezoneOptions
  - 基线：源语句 sha256=3a9e7cbb615333d3ec13031aa60a56bc340431534e4f8dfd50a5740aa93b5472；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/user.ts
- I00632 `ruoyi-fastapi-frontend/src/api/system/user.js` lines 87-89 ExportNamedDeclaration: updateUserTimezone
  - 基线：源语句 sha256=5bf69ba288c035b14f6849dc703fd52f029707d966d93de2d11b70e4464b6f5b；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/user.ts
- I00633 `ruoyi-fastapi-frontend/src/api/system/user.js` lines 92-98 ExportNamedDeclaration: updateUserProfile
  - 基线：源语句 sha256=d11f5d78272ac9f10279377de3348a5599e34dfcc7957bf6285a53d14d695952；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/user.ts
- I00634 `ruoyi-fastapi-frontend/src/api/system/user.js` lines 101-111 ExportNamedDeclaration: updateUserPwd
  - 基线：源语句 sha256=03b50d686c4545abca1aff57085c1e951af88d424a550e70940eb05d45533d51；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/user.ts
- I00635 `ruoyi-fastapi-frontend/src/api/system/user.js` lines 114-121 ExportNamedDeclaration: uploadAvatar
  - 基线：源语句 sha256=5d60841a51218160f56eded7a589deef676c631425cd1c00b057f82f7349e156；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/user.ts
- I00636 `ruoyi-fastapi-frontend/src/api/system/user.js` lines 124-129 ExportNamedDeclaration: getAuthRole
  - 基线：源语句 sha256=7ba6641d8c78237e42c565786297007754ba24ae387b16247ecd81505dc104bd；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/user.ts
- I00637 `ruoyi-fastapi-frontend/src/api/system/user.js` lines 132-138 ExportNamedDeclaration: updateAuthRole
  - 基线：源语句 sha256=970210c5e7c1cb5d64a471225d054c9d096d2e874f841a4c74a775bb2762cb1a；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/user.ts
- I00638 `ruoyi-fastapi-frontend/src/api/system/user.js` lines 141-146 ExportNamedDeclaration: deptTreeSelect
  - 基线：源语句 sha256=b7d495018dc1e6d62d91098a2d7923562517ecec6bcdbb1fa319d485efa781a6；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/user.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
