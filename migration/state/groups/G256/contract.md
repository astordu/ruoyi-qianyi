# G256 src/utils/validate.js：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02924 `ruoyi-fastapi-frontend/src/utils/validate.js` lines 7-16 ExportNamedDeclaration: isPathMatch
  - 基线：源语句 sha256=3aa6dda337c0b90db52aa7c1369fc27c115fea59589f1298867c35540413689f；保留返回、异常及 1 个分支，调用=CallExpression.replace, pattern.replace, regex.test。
  - 去向：react-front/src/utils/validate.ts
- I02925 `ruoyi-fastapi-frontend/src/utils/validate.js` lines 23-28 ExportNamedDeclaration: isEmpty
  - 基线：源语句 sha256=11f174300043c0e5a8ea7e7d5ad469a6313f66ecd1af8080eb7963c3951ccff7；保留返回、异常及 6 个分支，调用=。
  - 去向：react-front/src/utils/validate.ts
- I02926 `ruoyi-fastapi-frontend/src/utils/validate.js` lines 35-37 ExportNamedDeclaration: isHttp
  - 基线：源语句 sha256=d80b5e8d90ae1e0012e68c6b3cacfddfeff09854559e7ba2e4b04374dea8db3a；保留返回、异常及 2 个分支，调用=url.indexOf。
  - 去向：react-front/src/utils/validate.ts
- I02927 `ruoyi-fastapi-frontend/src/utils/validate.js` lines 44-46 ExportNamedDeclaration: isExternal
  - 基线：源语句 sha256=f6d4e678a96a3b6e3659c4b2704e5a6e1299ab7b530685101245760232b2e831；保留返回、异常及 1 个分支，调用=RegExpLiteral.test。
  - 去向：react-front/src/utils/validate.ts
- I02928 `ruoyi-fastapi-frontend/src/utils/validate.js` lines 52-55 ExportNamedDeclaration: validUsername
  - 基线：源语句 sha256=a64d8be1d9676eca19c8569701fc190418aa5db8d55fb3483de8a2bbbfe7aaa9；保留返回、异常及 1 个分支，调用=valid_map.indexOf, str.trim。
  - 去向：react-front/src/utils/validate.ts
- I02929 `ruoyi-fastapi-frontend/src/utils/validate.js` lines 61-64 ExportNamedDeclaration: validURL
  - 基线：源语句 sha256=ce51df89639a82337bff10a1d44775d8cb42c7a884024e7fc0f9db7c40e4df0d；保留返回、异常及 1 个分支，调用=reg.test。
  - 去向：react-front/src/utils/validate.ts
- I02930 `ruoyi-fastapi-frontend/src/utils/validate.js` lines 70-73 ExportNamedDeclaration: validLowerCase
  - 基线：源语句 sha256=126b1b907d5881d2729efe99624b7d7e9d7747e282cc50bc5fe9261fb62ab29c；保留返回、异常及 1 个分支，调用=reg.test。
  - 去向：react-front/src/utils/validate.ts
- I02931 `ruoyi-fastapi-frontend/src/utils/validate.js` lines 79-82 ExportNamedDeclaration: validUpperCase
  - 基线：源语句 sha256=fdb4f780bf5a960e8b1970d89f48d722aa364ec397cb98266c5808298cb4118b；保留返回、异常及 1 个分支，调用=reg.test。
  - 去向：react-front/src/utils/validate.ts
- I02932 `ruoyi-fastapi-frontend/src/utils/validate.js` lines 88-91 ExportNamedDeclaration: validAlphabets
  - 基线：源语句 sha256=e1b57ad84e7dd415fd811bd87563ac2f8df622ad0b7549068783ad109083aac3；保留返回、异常及 1 个分支，调用=reg.test。
  - 去向：react-front/src/utils/validate.ts
- I02933 `ruoyi-fastapi-frontend/src/utils/validate.js` lines 97-100 ExportNamedDeclaration: validEmail
  - 基线：源语句 sha256=ad27448b417600bf1e1a377da55a4cd1c9a56baf3c8cf031136df0cfca14b871；保留返回、异常及 1 个分支，调用=reg.test。
  - 去向：react-front/src/utils/validate.ts
- I02934 `ruoyi-fastapi-frontend/src/utils/validate.js` lines 106-108 ExportNamedDeclaration: isString
  - 基线：源语句 sha256=428a543c769d371a42561397f6bfb7df7cc884b8f37fc545ac57ad65e5db8ad7；保留返回、异常及 2 个分支，调用=。
  - 去向：react-front/src/utils/validate.ts
- I02935 `ruoyi-fastapi-frontend/src/utils/validate.js` lines 114-119 ExportNamedDeclaration: isArray
  - 基线：源语句 sha256=dc05e5b7b093b439d38a7dacead7b975e0b0ce7dda5ff348ef8ff1e571d075e4；保留返回、异常及 3 个分支，调用=Object.prototype.toString.call, Array.isArray。
  - 去向：react-front/src/utils/validate.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
