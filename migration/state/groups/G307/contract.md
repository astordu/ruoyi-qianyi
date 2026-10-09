# G307 src/views/system/role/index.vue：状态、输入与依赖接口

依赖：G000, G040, G044, G232, G250, G253F025

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I07123 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 246-246 ImportDeclaration: 
  - 基线：源语句 sha256=5ded6eea1b8b6b5a422c9929d852248cb6a5f6bab74a1bf6350e8bf942cda7ae；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07124 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 247-247 ImportDeclaration: 
  - 基线：源语句 sha256=386e0d042415316a489677517b6933343f13defd4538d30060de3e8392979de8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07125 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 248-248 ImportDeclaration: 
  - 基线：源语句 sha256=c6718f72f1358a60d777b13a51a57b28f41afcbcb58d2bfc86be7026b1e49a8d；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07126 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 250-250 VariableDeclaration: router
  - 基线：源语句 sha256=5921d8bbcfc7da27a18289d8a47cc51136866f8fdbebe22e9d1d1135aa55e0e6；保留返回、异常及 0 个分支，调用=useRouter。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07127 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 251-251 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07128 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 252-252 VariableDeclaration: 
  - 基线：源语句 sha256=e39eef28f5bbe01b170f2bfb21463bd64109f87928694efa0dd8eb360768e609；保留返回、异常及 0 个分支，调用=proxy.useDict。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07129 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 254-254 VariableDeclaration: roleList
  - 基线：源语句 sha256=6fe45bd20701cdaf09ab2ae95021b0c97b35104d1d262e880553fbed1e854196；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07130 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 255-255 VariableDeclaration: open
  - 基线：源语句 sha256=a542e4df0517d4fd7db7dda3114abbaf21c848158a19f33261b636975b69e307；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07131 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 256-256 VariableDeclaration: loading
  - 基线：源语句 sha256=c6d283c2f3ea7c9a46a2b20e0ef90bfcf6ffbde99656d9a424ad43f7d28f2aba；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07132 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 257-257 VariableDeclaration: showSearch
  - 基线：源语句 sha256=484353ab3c6f747541b20072d8cc3a9816d7c60d7a687326a0ab4d6700d69e17；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07133 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 258-258 VariableDeclaration: ids
  - 基线：源语句 sha256=470784de1db68be78831742511d0069dcbb9f19878d3ca4a6d5a2ad0370b79f0；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07134 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 259-259 VariableDeclaration: single
  - 基线：源语句 sha256=d8b92433028a1ee7912903c3a8cf52435102e8d5f5c98809c169ecda5a0c1d2a；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07135 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 260-260 VariableDeclaration: multiple
  - 基线：源语句 sha256=1e95758ba50bec4821d45483dad55ab07195518d0ab2626c714ec7b128480ffc；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07136 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 261-261 VariableDeclaration: total
  - 基线：源语句 sha256=3ea22b280c119d04a2e23fb7967b98534357cc6c46eb2621b3817c605f822958；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07137 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 262-262 VariableDeclaration: title
  - 基线：源语句 sha256=6452e9e4e944a2ca0aaab11c2229fadd77c42d71c76662caecb1fe68378567dd；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07138 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 263-263 VariableDeclaration: dateRange
  - 基线：源语句 sha256=645ab2e4a50a3ccee4a3e4ae7d6fa25173814ae1fe56176486474669de8e0b86；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07139 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 264-264 VariableDeclaration: menuOptions
  - 基线：源语句 sha256=aa6f219d637ba0a755a162a075eb4a9213231a429125b79e42f9e187d9d55645；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07140 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 265-265 VariableDeclaration: menuExpand
  - 基线：源语句 sha256=b1636572c2a6d29eb95c8a5af279fcaf68d03ca8cebebbf4bbf927d3b6c9bb58；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07141 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 266-266 VariableDeclaration: menuNodeAll
  - 基线：源语句 sha256=83d872058a3d9da51486f909594125131c29f4537c7f60c697b66c7d2153dad4；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07142 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 267-267 VariableDeclaration: deptExpand
  - 基线：源语句 sha256=43b1bb5fdb10a930adc9fe25d215fa51f9b4e0964825b54b5cc8f0f695463fe1；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07143 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 268-268 VariableDeclaration: deptNodeAll
  - 基线：源语句 sha256=55bdbe90df2476bd982f7ce517a76196d67845689b3ddebe1dd8bf6c1f4c6c6b；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07144 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 269-269 VariableDeclaration: deptOptions
  - 基线：源语句 sha256=236d0e7c904cd13eca18f821c6ce9044c96c113c5ffc8c000b9d24335913858e；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07145 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 270-270 VariableDeclaration: openDataScope
  - 基线：源语句 sha256=eadf95d1405d21d1b3e08a4f1ffcee96e8527ddcf3588693b833deca37d9a006；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07146 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 271-271 VariableDeclaration: menuRef
  - 基线：源语句 sha256=cbd241631b9c355dfff1134434ab7db18e20db51308d5c6939f5618b15eca208；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07147 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 272-272 VariableDeclaration: deptRef
  - 基线：源语句 sha256=5dc1ab3f347092c42023352d9f995fa890455e838454faaec13c2ea00139cbaa；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07148 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 275-281 VariableDeclaration: dataScopeOptions
  - 基线：源语句 sha256=3e4babdcab9992a959c85a0b7d7bb0c0bfd55073335c8b07d1d06f86988c1323；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07149 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 283-297 VariableDeclaration: data
  - 基线：源语句 sha256=b8f15eb21b0e0555ef0b255897c974a0c14abc67f055ea701417d98dc5f1f8ff；保留返回、异常及 0 个分支，调用=reactive。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07150 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 299-299 VariableDeclaration: 
  - 基线：源语句 sha256=1302c7f6c9f01c8414a694cd88e708a5a66cf40450bbd6957204a754bd0d4050；保留返回、异常及 0 个分支，调用=toRefs。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07177 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 560-560 ExpressionStatement: 
  - 基线：源语句 sha256=e966d3b08f869f7c7962cc988172bf8bc4840aa64d83fa58b0a15b31a76e4d3d；保留返回、异常及 0 个分支，调用=getList。
  - 去向：react-front/src/views/system/role/index.context.ts
- I07178 `ruoyi-fastapi-frontend/src/views/system/role/index.vue` lines 562-566 ExpressionStatement: 
  - 基线：源语句 sha256=17ffa6410b29708eb725aa6841db9de40066edef1ed09032f679fbd2d0c31972；保留返回、异常及 1 个分支，调用=watch, handleQuery。
  - 去向：react-front/src/views/system/role/index.context.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
