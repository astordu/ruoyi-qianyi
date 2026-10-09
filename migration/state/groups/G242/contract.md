# G242 src/utils/index.js：完整能力

依赖：G000, G250

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02691 `ruoyi-fastapi-frontend/src/utils/index.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=58aad1c455e34a8b8e951729ee896935dc27b797c79617352c88d167494b6000；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/index.ts
- I02692 `ruoyi-fastapi-frontend/src/utils/index.js` lines 6-8 ExportNamedDeclaration: formatDate
  - 基线：源语句 sha256=4a38d9ee6a9c77d8983d3165a9d78d4684af4e4e0cf3f98a9c03b23394b16208；保留返回、异常及 2 个分支，调用=parseTime。
  - 去向：react-front/src/utils/index.ts
- I02693 `ruoyi-fastapi-frontend/src/utils/index.js` lines 15-34 ExportNamedDeclaration: formatTime
  - 基线：源语句 sha256=aa5c52fd994eb07536ec6e6157dd423c2d65a5e0369095dbf7082a7a7d37fadd；保留返回、异常及 12 个分支，调用=parseTime, NewExpression.getTime, Date.now, Math.ceil。
  - 去向：react-front/src/utils/index.ts
- I02694 `ruoyi-fastapi-frontend/src/utils/index.js` lines 40-53 ExportNamedDeclaration: getQueryObject
  - 基线：源语句 sha256=7c4f12c59c269d0a6cb4577658225748a86f2fa7ff82cad1e4798847bae0a815；保留返回、异常及 3 个分支，调用=url.substring, url.lastIndexOf, search.replace, decodeURIComponent, String。
  - 去向：react-front/src/utils/index.ts
- I02695 `ruoyi-fastapi-frontend/src/utils/index.js` lines 59-69 ExportNamedDeclaration: byteLength
  - 基线：源语句 sha256=7a0b95c521f599c1f6e9ee02bc55af3e62d8e06098f246c2119c5b21f73afa55；保留返回、异常及 7 个分支，调用=str.charCodeAt。
  - 去向：react-front/src/utils/index.ts
- I02696 `ruoyi-fastapi-frontend/src/utils/index.js` lines 75-83 ExportNamedDeclaration: cleanArray
  - 基线：源语句 sha256=d7df7ec8eaf89f7353e989cc5a92bcdf2a2a49cb39149ce07b778dd4307c7540；保留返回、异常及 2 个分支，调用=newArray.push。
  - 去向：react-front/src/utils/index.ts
- I02697 `ruoyi-fastapi-frontend/src/utils/index.js` lines 89-97 ExportNamedDeclaration: param
  - 基线：源语句 sha256=9df18163a3c3a38004349f55611607d21cd4c0963b273e8d2e65b6cadb1892a6；保留返回、异常及 6 个分支，调用=CallExpression.join, cleanArray, CallExpression.map, Object.keys, encodeURIComponent。
  - 去向：react-front/src/utils/index.ts
- I02698 `ruoyi-fastapi-frontend/src/utils/index.js` lines 103-119 ExportNamedDeclaration: param2Obj
  - 基线：源语句 sha256=e5f0b5028811f010e4592ff38c902a9e150ffb5cedf70bd5591822b61912bda7；保留返回、异常及 4 个分支，调用=CallExpression.replace, decodeURIComponent, url.split, search.split, searchArr.forEach, v.indexOf, v.substring。
  - 去向：react-front/src/utils/index.ts
- I02699 `ruoyi-fastapi-frontend/src/utils/index.js` lines 125-129 ExportNamedDeclaration: html2Text
  - 基线：源语句 sha256=dd9b7327d31a68063998535a849d1470eddc113243465e7affeb88258e8c5e53；保留返回、异常及 2 个分支，调用=document.createElement。
  - 去向：react-front/src/utils/index.ts
- I02700 `ruoyi-fastapi-frontend/src/utils/index.js` lines 137-153 ExportNamedDeclaration: objectMerge
  - 基线：源语句 sha256=a523edf11fc339368ab73c4fee67fc9dffedda815dc372ccf310e20c050d4684；保留返回、异常及 5 个分支，调用=Array.isArray, source.slice, CallExpression.forEach, Object.keys, objectMerge。
  - 去向：react-front/src/utils/index.ts
- I02701 `ruoyi-fastapi-frontend/src/utils/index.js` lines 159-173 ExportNamedDeclaration: toggleClass
  - 基线：源语句 sha256=c97996318b60845c6bf319f29050ca401e7f0474908a9abf42d7296783c6ae03；保留返回、异常及 4 个分支，调用=classString.indexOf, classString.substr。
  - 去向：react-front/src/utils/index.ts
- I02702 `ruoyi-fastapi-frontend/src/utils/index.js` lines 179-185 ExportNamedDeclaration: getTime
  - 基线：源语句 sha256=11e7b7cc2b9b21ae98a6e7d28662f59ce170c2ce6ca61152348e553b07ae27ac；保留返回、异常及 3 个分支，调用=NewExpression.getTime, NewExpression.toDateString。
  - 去向：react-front/src/utils/index.ts
- I02703 `ruoyi-fastapi-frontend/src/utils/index.js` lines 193-226 ExportNamedDeclaration: debounce
  - 基线：源语句 sha256=391440c847560116ae1a4d9d040b2b1efefccfb44efb66700270563e12038174；保留返回、异常及 9 个分支，调用=setTimeout, func.apply。
  - 去向：react-front/src/utils/index.ts
- I02704 `ruoyi-fastapi-frontend/src/utils/index.js` lines 235-248 ExportNamedDeclaration: deepClone
  - 基线：源语句 sha256=47aee1580850bbde37d19da4dabb2cf12720b0ce6ad92978873ab9296f6d56ee；保留返回、异常及 7 个分支，调用=CallExpression.forEach, Object.keys, deepClone。
  - 去向：react-front/src/utils/index.ts
- I02705 `ruoyi-fastapi-frontend/src/utils/index.js` lines 254-256 ExportNamedDeclaration: uniqueArr
  - 基线：源语句 sha256=285d48033f558ac0cb9b4c424943238170cd722a912565357e0d735286473723；保留返回、异常及 1 个分支，调用=Array.from。
  - 去向：react-front/src/utils/index.ts
- I02706 `ruoyi-fastapi-frontend/src/utils/index.js` lines 261-265 ExportNamedDeclaration: createUniqueString
  - 基线：源语句 sha256=0dc2712ff1aac454654be11d59d01f2a553f24fb8596f70e32f2c627c28251c7；保留返回、异常及 1 个分支，调用=parseInt, Math.random, UnaryExpression.toString。
  - 去向：react-front/src/utils/index.ts
- I02707 `ruoyi-fastapi-frontend/src/utils/index.js` lines 273-275 ExportNamedDeclaration: hasClass
  - 基线：源语句 sha256=7cf22820b04e5df7f0fa5321400743ba1b809ff51d79b2b6ea6300379840c943；保留返回、异常及 1 个分支，调用=ele.className.match。
  - 去向：react-front/src/utils/index.ts
- I02708 `ruoyi-fastapi-frontend/src/utils/index.js` lines 282-284 ExportNamedDeclaration: addClass
  - 基线：源语句 sha256=bfebd158c7482ad348144e51f461867281a23826e197d2d80d3df9aced4fae3c；保留返回、异常及 1 个分支，调用=hasClass。
  - 去向：react-front/src/utils/index.ts
- I02709 `ruoyi-fastapi-frontend/src/utils/index.js` lines 291-296 ExportNamedDeclaration: removeClass
  - 基线：源语句 sha256=b4d5ad3bdd7cf4732e1e86b546eae3e6c8ca81e7658aaf18145b4d7601b5892c；保留返回、异常及 1 个分支，调用=hasClass, ele.className.replace。
  - 去向：react-front/src/utils/index.ts
- I02710 `ruoyi-fastapi-frontend/src/utils/index.js` lines 298-307 ExportNamedDeclaration: makeMap
  - 基线：源语句 sha256=f46151104da24cebff78c730c5819bec5f2c7aa7157148db4e49dd9165cfb3e9；保留返回、异常及 2 个分支，调用=Object.create, str.split, val.toLowerCase。
  - 去向：react-front/src/utils/index.ts
- I02711 `ruoyi-fastapi-frontend/src/utils/index.js` lines 309-309 ExportNamedDeclaration: exportDefault
  - 基线：源语句 sha256=58331d114312f796dc5f47298370a6683211860289a8e9a6b3fba92ac970f7da；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/index.ts
- I02712 `ruoyi-fastapi-frontend/src/utils/index.js` lines 311-350 ExportNamedDeclaration: beautifierConf
  - 基线：源语句 sha256=64dfc9f24f5db402e9ecfc73b3fa77c87d5d734eeeeb2d4916bb770cce5284fb；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/index.ts
- I02713 `ruoyi-fastapi-frontend/src/utils/index.js` lines 353-355 ExportNamedDeclaration: titleCase
  - 基线：源语句 sha256=136e366d69de5fe828ca8da9db186ce1bd0d06ab91bf0a2d26ce81f3640cf9cf；保留返回、异常及 1 个分支，调用=str.replace, L.toUpperCase。
  - 去向：react-front/src/utils/index.ts
- I02714 `ruoyi-fastapi-frontend/src/utils/index.js` lines 358-360 ExportNamedDeclaration: camelCase
  - 基线：源语句 sha256=5bcc4341414a305493b938199818f6f7f5020db524a803bbd407c65660dd6739；保留返回、异常及 1 个分支，调用=str.replace, CallExpression.toUpperCase, str1.substr。
  - 去向：react-front/src/utils/index.ts
- I02715 `ruoyi-fastapi-frontend/src/utils/index.js` lines 362-364 ExportNamedDeclaration: isNumberStr
  - 基线：源语句 sha256=f3ec30547984aed74db3c1daf6a36dc48ea2bfb291f4a4ef99d27d230b47f259；保留返回、异常及 1 个分支，调用=RegExpLiteral.test。
  - 去向：react-front/src/utils/index.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
