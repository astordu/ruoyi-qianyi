# G217 src/plugins/download.js：完整能力

依赖：G000, G231, G234, G250

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02534 `ruoyi-fastapi-frontend/src/plugins/download.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=b922f0193d652b2c0de36098fb1aa440be1a522c617f1ee9035355a86f788986；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/plugins/download.ts
- I02535 `ruoyi-fastapi-frontend/src/plugins/download.js` lines 2-2 ImportDeclaration: 
  - 基线：源语句 sha256=a36d063c94cb966c247b61acdc6c28b6dce9aca1ecd048049723e9519488ed11；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/plugins/download.ts
- I02536 `ruoyi-fastapi-frontend/src/plugins/download.js` lines 3-3 ImportDeclaration: 
  - 基线：源语句 sha256=7389186de11cafd7624f8a0e5caccc3af1f087d5a425425c73df6c8827b071b0；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/plugins/download.ts
- I02537 `ruoyi-fastapi-frontend/src/plugins/download.js` lines 4-4 ImportDeclaration: 
  - 基线：源语句 sha256=2ec8863f7e5e99b6e9f4898b63d49c0737c19ccb341a54be6cd435a7da40e781；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/plugins/download.ts
- I02538 `ruoyi-fastapi-frontend/src/plugins/download.js` lines 5-5 ImportDeclaration: 
  - 基线：源语句 sha256=0460519625276597ebbc47c63a83fa0e7bc263f33807a3b88d3b9e952a376716；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/plugins/download.ts
- I02539 `ruoyi-fastapi-frontend/src/plugins/download.js` lines 6-6 ImportDeclaration: 
  - 基线：源语句 sha256=060b2013d0f29f36a12bf90b532d908262a2af00ff53cb9032214853abb1919e；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/plugins/download.ts
- I02540 `ruoyi-fastapi-frontend/src/plugins/download.js` lines 8-8 VariableDeclaration: baseURL
  - 基线：源语句 sha256=b9f2f6ec9e9775535be5d7ecc363df0b7f656018225c87909dba01cad773d470；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/plugins/download.ts
- I02541 `ruoyi-fastapi-frontend/src/plugins/download.js` lines 9-9 VariableDeclaration: DOWNLOAD_CHUNK_SIZE
  - 基线：源语句 sha256=80ac9b579c2fab7f385fddf2f607ee973de3782ba59b290871bb2f42add05be1；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/plugins/download.ts
- I02542 `ruoyi-fastapi-frontend/src/plugins/download.js` lines 10-10 VariableDeclaration: DOWNLOAD_CHUNK_RETRY_COUNT
  - 基线：源语句 sha256=28c622d5cc44c879fca656d31f1b73dd7a64e8381adbdd10487284723044154a；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/plugins/download.ts
- I02543 `ruoyi-fastapi-frontend/src/plugins/download.js` lines 11-11 VariableDeclaration: downloadLoadingInstance
  - 基线：源语句 sha256=bbe0de991a7dbaef70b16ff03fbe01850ca4c95539d8487bb3ddbef07780afde；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/plugins/download.ts
- I02544 `ruoyi-fastapi-frontend/src/plugins/download.js` lines 13-23 FunctionDeclaration: parseContentRange
  - 基线：源语句 sha256=308ad65602e14823e8f5694e32e72162f3c0cc5cecc5f9f784a7334bfddaebae；保留返回、异常及 4 个分支，调用=RegExpLiteral.exec, Number。
  - 去向：react-front/src/plugins/download.ts
- I02545 `ruoyi-fastapi-frontend/src/plugins/download.js` lines 25-27 FunctionDeclaration: isRetryableDownloadError
  - 基线：源语句 sha256=bb59801ce776dd6b705580ebc36d787e9d08b3f916a0cbf16ee5a3a20485c81e；保留返回、异常及 2 个分支，调用=。
  - 去向：react-front/src/plugins/download.ts
- I02546 `ruoyi-fastapi-frontend/src/plugins/download.js` lines 29-50 FunctionDeclaration: requestDownloadChunk
  - 基线：源语句 sha256=3ec6e068dacf8b1ec841ebcf2e1d9b754284549653f4e8cb8f0d0536e2e56d7a；保留返回、异常及 6 个分支，调用=axios, getToken, isRetryableDownloadError。
  - 去向：react-front/src/plugins/download.ts
- I02547 `ruoyi-fastapi-frontend/src/plugins/download.js` lines 52-59 FunctionDeclaration: requestFullDownload
  - 基线：源语句 sha256=f914a023a5507f05f6cc701161adc9b665517263458a5573954b4726e0fa677b；保留返回、异常及 1 个分支，调用=axios, getToken。
  - 去向：react-front/src/plugins/download.ts
- I02548 `ruoyi-fastapi-frontend/src/plugins/download.js` lines 61-108 FunctionDeclaration: downloadByRange
  - 基线：源语句 sha256=56d758818bbe0159b4d1c8943723f59c67c863236288815a807259a07548b512；保留返回、异常及 17 个分支，调用=requestDownloadChunk, requestFullDownload, blobValidate, parseContentRange, chunks.push。
  - 去向：react-front/src/plugins/download.ts
- I02549 `ruoyi-fastapi-frontend/src/plugins/download.js` lines 110-189 ExportDefaultDeclaration: name, resource, file, zip
  - 基线：源语句 sha256=e4429b1668a5025232c6ebc71aa6b56cc0a309fdf2ae3fa9234e804f5e607f74；保留返回、异常及 11 个分支，调用=encodeURIComponent, CallExpression.then, axios, getToken, blobValidate, ThisExpression.saveAs, decodeURIComponent, ThisExpression.printErrMsg, downloadByRange, console.error, ElMessage.error, CallExpression.pop, resource.split, ElLoading.service, CallExpression.catch, downloadLoadingInstance.close, saveAs, data.text, JSON.parse。
  - 去向：react-front/src/plugins/download.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
