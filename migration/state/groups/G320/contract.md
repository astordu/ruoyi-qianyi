# G320 src/views/tool/build/RightPanel.vue：状态、输入与依赖接口

依赖：G000, G235, G242, G319, G321

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I07917 `ruoyi-fastapi-frontend/src/views/tool/build/RightPanel.vue` lines 467-467 ImportDeclaration: 
  - 基线：源语句 sha256=9fa8b3a34350cc4bcf17ad78a2451458e277a1735bc2c83c21c07548fa5c28bb；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/tool/build/RightPanel.context.ts
- I07918 `ruoyi-fastapi-frontend/src/views/tool/build/RightPanel.vue` lines 468-468 ImportDeclaration: 
  - 基线：源语句 sha256=bab4ac6fe41a36f90a86eb5e9f9b07600856b84fbed54b758ac9d71f167acfde；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/tool/build/RightPanel.context.ts
- I07919 `ruoyi-fastapi-frontend/src/views/tool/build/RightPanel.vue` lines 469-469 ImportDeclaration: 
  - 基线：源语句 sha256=170619486e9a83fb0d46eaf018be27fd3c11f175c8ad18b2e4aee786d469bbcd；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/tool/build/RightPanel.context.ts
- I07920 `ruoyi-fastapi-frontend/src/views/tool/build/RightPanel.vue` lines 470-470 ImportDeclaration: 
  - 基线：源语句 sha256=a2d3b952105e8fe263a057ee78bd03c0936f089b949bc3ed2a6447bbf695d60e；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/tool/build/RightPanel.context.ts
- I07921 `ruoyi-fastapi-frontend/src/views/tool/build/RightPanel.vue` lines 471-471 ImportDeclaration: 
  - 基线：源语句 sha256=7df55abec7d63726b219acbc24f96421b8bcf65056b6e6bd2d1085b77990d28f；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/tool/build/RightPanel.context.ts
- I07922 `ruoyi-fastapi-frontend/src/views/tool/build/RightPanel.vue` lines 473-473 VariableDeclaration: 
  - 基线：源语句 sha256=d3917068104e0f2158733e5e758c09ff6781b09fc4b90611c9a30e2625c695d6；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/views/tool/build/RightPanel.context.ts
- I07923 `ruoyi-fastapi-frontend/src/views/tool/build/RightPanel.vue` lines 474-483 VariableDeclaration: dateTimeFormat
  - 基线：源语句 sha256=80cd85026303395adf652309e8a2f3e0092157ea3d3f7a297e547e285f55d3e8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/tool/build/RightPanel.context.ts
- I07924 `ruoyi-fastapi-frontend/src/views/tool/build/RightPanel.vue` lines 484-488 VariableDeclaration: props
  - 基线：源语句 sha256=2cf2001ab0e8194317b27ff0d381106d4102620f4a3bc71967913b46b5639c12；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/views/tool/build/RightPanel.context.ts
- I07925 `ruoyi-fastapi-frontend/src/views/tool/build/RightPanel.vue` lines 490-581 VariableDeclaration: data
  - 基线：源语句 sha256=3c5549837476b3850bad0cb5666c66a29a054fdce8782d347dce0a78bf0893d0；保留返回、异常及 2 个分支，调用=reactive。
  - 去向：react-front/src/views/tool/build/RightPanel.context.ts
- I07926 `ruoyi-fastapi-frontend/src/views/tool/build/RightPanel.vue` lines 583-583 VariableDeclaration: 
  - 基线：源语句 sha256=695e47d4e88271618cc98b2202f5ed77eec62d0cbbfce749e3701cc8b13acb4a；保留返回、异常及 0 个分支，调用=toRefs。
  - 去向：react-front/src/views/tool/build/RightPanel.context.ts
- I07929 `ruoyi-fastapi-frontend/src/views/tool/build/RightPanel.vue` lines 597-606 VariableDeclaration: tagList
  - 基线：源语句 sha256=3e68ca28f79ebff7af8af3fabc0848f671d283287ed9fe74713d725ad0a31c72；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/tool/build/RightPanel.context.ts
- I07930 `ruoyi-fastapi-frontend/src/views/tool/build/RightPanel.vue` lines 608-608 VariableDeclaration: emit
  - 基线：源语句 sha256=f700ab3cf756e99b5030fe5ba809309b1251cad56b4ac933fcf1de4139f28d01；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/views/tool/build/RightPanel.context.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
