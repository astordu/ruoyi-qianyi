# G189 src/components/TreePanel/index.vue：状态、输入与依赖接口

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01796 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` lines 75-179 VariableDeclaration: props
  - 基线：源语句 sha256=e5e02fa7833e95723110c17e39a6c5d351a421cb8d1daee8a0e61c020cdd04ab；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/components/TreePanel/index.context.ts
- I01797 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` lines 181-190 VariableDeclaration: emit
  - 基线：源语句 sha256=5592cbde223c57fb409731003e70e0e18f15fcfcc5ab957f3f06557b56ceb936；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/components/TreePanel/index.context.ts
- I01798 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` lines 192-192 VariableDeclaration: treeRef
  - 基线：源语句 sha256=f5c4234b55193fae2567ab3dc32eb0570b80af785f3b933fd382f3d2a2f068ae；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/TreePanel/index.context.ts
- I01799 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` lines 195-195 VariableDeclaration: searchKeyword
  - 基线：源语句 sha256=e56cbb638a00ec4379ed4182c77bf61dc3c59d3cd1ab7e211807238cb1ed31a2；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/TreePanel/index.context.ts
- I01800 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` lines 196-196 VariableDeclaration: collapsed
  - 基线：源语句 sha256=150bb31e84e7bdb891812d96a5c129a53b5b391a6ee334a0c1abc23a9f204a50；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/TreePanel/index.context.ts
- I01801 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` lines 197-197 VariableDeclaration: sidebarWidth
  - 基线：源语句 sha256=46bc29f7e062cd65de1179173a2422fadc8fd5ce8849e015963afe3dc803e6c1；保留返回、异常及 1 个分支，调用=ref。
  - 去向：react-front/src/components/TreePanel/index.context.ts
- I01802 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` lines 198-198 VariableDeclaration: isResizing
  - 基线：源语句 sha256=b83aa334e12ea45691b07b2d0bd74776648c28412e3010794f3293c4d2303705；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/TreePanel/index.context.ts
- I01803 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` lines 199-199 VariableDeclaration: startX
  - 基线：源语句 sha256=6047c0398ebac481f14c5ac52d26e23f7c196f3bd729fb083f73b02e697f4c2d；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/TreePanel/index.context.ts
- I01804 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` lines 200-200 VariableDeclaration: startWidth
  - 基线：源语句 sha256=00804cd8e090200d330909f103cb369a03eb0c90aa6f07c3a22ac40f99316ec7；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/TreePanel/index.context.ts
- I01805 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` lines 201-201 VariableDeclaration: saveWidthTimer
  - 基线：源语句 sha256=d502f49de25fffccf0acb22ef5732751e3dada76580c01baec254ed328bd2928；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/TreePanel/index.context.ts
- I01806 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` lines 202-202 VariableDeclaration: rafId
  - 基线：源语句 sha256=1e432be038fb7ec41c28f6bfd075d53f38fbdc9720e2ddb63410d3b6efd0e236；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/TreePanel/index.context.ts
- I01807 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` lines 203-203 VariableDeclaration: isLoadingFromStorage
  - 基线：源语句 sha256=9919b2c82d76a59b23af79e699addd50655392d56f99b6d58e3347148b2779df；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/TreePanel/index.context.ts
- I01808 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` lines 204-204 VariableDeclaration: expandedAll
  - 基线：源语句 sha256=cf438708f3b4e14919563c48b98388d1ccc1a472653224011f55162c2e84e509；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/TreePanel/index.context.ts
- I01809 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` lines 207-212 VariableDeclaration: isExpandedAll
  - 基线：源语句 sha256=c38b11bb053e01c6dba86fc3244d4e59c083001fd5ca566c1a67d39d57f22ccf；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/components/TreePanel/index.context.ts
- I01811 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` lines 224-229 ExpressionStatement: 
  - 基线：源语句 sha256=e253e613a4d1b9c38a56f9ee0e4c7b80d3b7935f40cfe63f138bef04c05eac7d；保留返回、异常及 1 个分支，调用=watch, handleCollapseChange, emit。
  - 去向：react-front/src/components/TreePanel/index.context.ts
- I01812 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` lines 232-241 ExpressionStatement: 
  - 基线：源语句 sha256=509a27dcd07bbcc2394f56ab8400f4655e43ab6373b25e8650b0f060723d7541；保留返回、异常及 1 个分支，调用=watch, nextTick, expandAllNodes, collapseAllNodes, emit。
  - 去向：react-front/src/components/TreePanel/index.context.ts
- I01813 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` lines 244-249 ExpressionStatement: 
  - 基线：源语句 sha256=959b81769a03fad5c2a323207e67e9468f69eb3043021a39e1405269be9a9cb7；保留返回、异常及 1 个分支，调用=watch, treeRef.value.filter, emit。
  - 去向：react-front/src/components/TreePanel/index.context.ts
- I01844 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` lines 509-525 ExpressionStatement: 
  - 基线：源语句 sha256=5d35792073d246ee1a52a5b66de00ee077fef24e6b4148aab7aa193584e7fe1a；保留返回、异常及 0 个分支，调用=defineExpose。
  - 去向：react-front/src/components/TreePanel/index.context.ts
- I01845 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` lines 527-543 ExpressionStatement: 
  - 基线：源语句 sha256=62703064cf165ec658cd9433376f7905cd2445c83a329b78458e2f8ff33bea8d；保留返回、异常及 4 个分支，调用=onMounted, getSavedWidth, nextTick, expandAllNodes。
  - 去向：react-front/src/components/TreePanel/index.context.ts
- I01846 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` lines 545-547 ExpressionStatement: 
  - 基线：源语句 sha256=7b5a65085bd59632f65e5f87db6903816d64bb9266c00dbe7674b0580a382a33；保留返回、异常及 0 个分支，调用=onBeforeUnmount, cleanup。
  - 去向：react-front/src/components/TreePanel/index.context.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
