# G310 src/views/system/user/index.vue：状态、输入与依赖接口

依赖：G000, G045, G171, G189, G232, G245, G250, G253F025, G316

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I07390 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 454-454 ImportDeclaration: 
  - 基线：源语句 sha256=5ded6eea1b8b6b5a422c9929d852248cb6a5f6bab74a1bf6350e8bf942cda7ae；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07391 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 455-455 ImportDeclaration: 
  - 基线：源语句 sha256=7a850a102748f38e8f7f8d01d9d692b6099475bd37a0ef262d56709d17bb14c5；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07392 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 456-456 ImportDeclaration: 
  - 基线：源语句 sha256=d2363693bb2463f3ab07157fcac0fcf035dad0d72adce0da8135e3999a67ea13；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07393 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 457-457 ImportDeclaration: 
  - 基线：源语句 sha256=7396f70cbce50cb20e1708a6fe9b8b00d0657e40b83dee9ebe9d4d2f40acb882；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07394 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 458-458 ImportDeclaration: 
  - 基线：源语句 sha256=5bd645450abdc3cf121741837838eeca960201472f0941de1cc2eb30ad4b2975；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07395 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 459-468 ImportDeclaration: 
  - 基线：源语句 sha256=65c686ff0fd855634c894e0876e90eaa389491452b8393d4bc5667fb05b92ff5；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07396 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 470-470 VariableDeclaration: router
  - 基线：源语句 sha256=5921d8bbcfc7da27a18289d8a47cc51136866f8fdbebe22e9d1d1135aa55e0e6；保留返回、异常及 0 个分支，调用=useRouter。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07397 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 471-471 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07398 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 472-472 VariableDeclaration: 
  - 基线：源语句 sha256=54ed066c118540640ab14effe504c0f2b13c66eabbbea246313592666accf427；保留返回、异常及 0 个分支，调用=usePasswordRule。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07399 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 473-476 VariableDeclaration: 
  - 基线：源语句 sha256=8b98bd29c7e534a52c5460b99973e1caedc7ed2b143a84ce751f4b8e06083494；保留返回、异常及 0 个分支，调用=proxy.useDict。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07400 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 478-478 VariableDeclaration: userList
  - 基线：源语句 sha256=27329f009483a63c964b05b2e6dcbf3a61052d302dbb204b9efcc11efd5d485b；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07401 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 479-479 VariableDeclaration: open
  - 基线：源语句 sha256=a542e4df0517d4fd7db7dda3114abbaf21c848158a19f33261b636975b69e307；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07402 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 480-480 VariableDeclaration: loading
  - 基线：源语句 sha256=c6d283c2f3ea7c9a46a2b20e0ef90bfcf6ffbde99656d9a424ad43f7d28f2aba；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07403 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 481-481 VariableDeclaration: showSearch
  - 基线：源语句 sha256=484353ab3c6f747541b20072d8cc3a9816d7c60d7a687326a0ab4d6700d69e17；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07404 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 482-482 VariableDeclaration: ids
  - 基线：源语句 sha256=470784de1db68be78831742511d0069dcbb9f19878d3ca4a6d5a2ad0370b79f0；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07405 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 483-483 VariableDeclaration: single
  - 基线：源语句 sha256=d8b92433028a1ee7912903c3a8cf52435102e8d5f5c98809c169ecda5a0c1d2a；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07406 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 484-484 VariableDeclaration: multiple
  - 基线：源语句 sha256=1e95758ba50bec4821d45483dad55ab07195518d0ab2626c714ec7b128480ffc；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07407 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 485-485 VariableDeclaration: total
  - 基线：源语句 sha256=3ea22b280c119d04a2e23fb7967b98534357cc6c46eb2621b3817c605f822958；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07408 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 486-486 VariableDeclaration: title
  - 基线：源语句 sha256=6452e9e4e944a2ca0aaab11c2229fadd77c42d71c76662caecb1fe68378567dd；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07409 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 487-487 VariableDeclaration: dateRange
  - 基线：源语句 sha256=645ab2e4a50a3ccee4a3e4ae7d6fa25173814ae1fe56176486474669de8e0b86；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07410 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 488-488 VariableDeclaration: deptOptions
  - 基线：源语句 sha256=89ece75b7981d142385506dd0f4b4e4699f10004542924195ca31feb5d02aa80；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07411 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 489-489 VariableDeclaration: enabledDeptOptions
  - 基线：源语句 sha256=12e10b13527198f860fc004479859bc222bf4823858ca9325994a7ccdb7e7e49；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07412 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 490-490 VariableDeclaration: initPassword
  - 基线：源语句 sha256=63102942b0cfeaecc1b669d9f3b60f75084d0f78a3024d8069b6cc9cd346d431；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07413 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 491-491 VariableDeclaration: postOptions
  - 基线：源语句 sha256=14c35a277c34848c0dd324e55433e5a82701d044295513895884d2f151a51c5c；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07414 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 492-492 VariableDeclaration: roleOptions
  - 基线：源语句 sha256=11c62a40edc1ceb3466bc09585ceb4ac496deeb362e3c311dee8abe7bb7d35cc；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07415 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 495-503 VariableDeclaration: columns
  - 基线：源语句 sha256=ea7cceb275b63ad08d9e649b62a4a0cdeec5034837ea39f8426bee6d8ef30c12；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07416 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 505-543 VariableDeclaration: data
  - 基线：源语句 sha256=e35a5e6fa8b1bbb617cf23414e6cbb0a2d47b7e79e93dce087c6b2c5ae7e63c2；保留返回、异常及 0 个分支，调用=reactive。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07417 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 545-545 VariableDeclaration: 
  - 基线：源语句 sha256=1302c7f6c9f01c8414a694cd88e708a5a66cf40450bbd6957204a754bd0d4050；保留返回、异常及 0 个分支，调用=toRefs。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07438 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 754-760 ExpressionStatement: 
  - 基线：源语句 sha256=f1e92498f1b59718370577cc84ff173a3aeaffefea6c5a17a450e5b2cf42e527；保留返回、异常及 0 个分支，调用=onMounted, getDeptTree, getList, CallExpression.then, proxy.getConfigKey。
  - 去向：react-front/src/views/system/user/index.context.ts
- I07439 `ruoyi-fastapi-frontend/src/views/system/user/index.vue` lines 762-766 ExpressionStatement: 
  - 基线：源语句 sha256=17ffa6410b29708eb725aa6841db9de40066edef1ed09032f679fbd2d0c31972；保留返回、异常及 1 个分支，调用=watch, handleQuery。
  - 去向：react-front/src/views/system/user/index.context.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。

依赖复核：default 导入 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` 对应完整渲染/导出装配 G189V，不能只依赖其状态接口组。
