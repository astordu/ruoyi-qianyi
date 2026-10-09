# G159 src/components/BusinessFileUpload/index.vue：状态、输入与依赖接口

依赖：G000, G249

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00796 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` lines 106-106 ImportDeclaration: 
  - 基线：源语句 sha256=61e91c1ede8a9285d8357e07bda32e48170c71df8aa8a5c4a0dfd9830d2be5e2；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/BusinessFileUpload/index.context.ts
- I00797 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` lines 107-107 ImportDeclaration: 
  - 基线：源语句 sha256=321d68bf0c129816c1132fd45d904e124d5cb012a641c00edcac841e5854df55；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/BusinessFileUpload/index.context.ts
- I00798 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` lines 109-154 VariableDeclaration: props
  - 基线：源语句 sha256=ae92b7cb5144f6f1e7161422640af0e50bdd26bfad7abccf9de8fd1fc610bc22；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/components/BusinessFileUpload/index.context.ts
- I00799 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` lines 156-156 VariableDeclaration: emit
  - 基线：源语句 sha256=92ed5e93617dcbdeb07889bd9a4f330d0270b7a547b34ee82249e6a18190be4d；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/components/BusinessFileUpload/index.context.ts
- I00800 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` lines 157-157 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/components/BusinessFileUpload/index.context.ts
- I00801 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` lines 158-158 VariableDeclaration: fileUploadRef
  - 基线：源语句 sha256=606f2fedfd488ab3c4a9bc635f3fcb74f0b49cbbb33df3760c6da9499af8211e；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/BusinessFileUpload/index.context.ts
- I00802 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` lines 159-159 VariableDeclaration: uploadFileListRef
  - 基线：源语句 sha256=250aa76459886c1743a9002bff442aba97075b3191d6af88b46e615773101ac0；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/BusinessFileUpload/index.context.ts
- I00803 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` lines 160-160 VariableDeclaration: fileList
  - 基线：源语句 sha256=ddad872b2ccb910eaf948cd720efd3d35c69ef319d802a8d495fa66220f7064c；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/BusinessFileUpload/index.context.ts
- I00804 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` lines 161-161 VariableDeclaration: pendingFileList
  - 基线：源语句 sha256=60fb54424f43136f7da9c96b05bb8e03510212a4c6a694db7eb9c530e3a73526；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/BusinessFileUpload/index.context.ts
- I00805 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` lines 162-162 VariableDeclaration: sortable
  - 基线：源语句 sha256=9fd09c77c4ddf945e9dd66858b3634a21484af9d0773442bced9a4d1c0f44418；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/BusinessFileUpload/index.context.ts
- I00806 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` lines 164-166 VariableDeclaration: showTip
  - 基线：源语句 sha256=8556191242339467f68de98a296200b3d5b283156486ab48dcc188bbec98c8d2；保留返回、异常及 2 个分支，调用=computed。
  - 去向：react-front/src/components/BusinessFileUpload/index.context.ts
- I00807 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` lines 168-175 ExpressionStatement: 
  - 基线：源语句 sha256=61b4d4bea1ed1e96d9e1b5ab965b81c4c8b9bd05b642e2bd4d8af8a64970ac13；保留返回、异常及 0 个分支，调用=watch, normalizeFileList, nextTick。
  - 去向：react-front/src/components/BusinessFileUpload/index.context.ts
- I00828 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` lines 506-506 ExpressionStatement: 
  - 基线：源语句 sha256=ff74dd8b69e2922d6417347a7030c1e71f6cbe0c31b0010f6e9d776cda7578a6；保留返回、异常及 0 个分支，调用=onMounted, nextTick。
  - 去向：react-front/src/components/BusinessFileUpload/index.context.ts
- I00829 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` lines 508-510 ExpressionStatement: 
  - 基线：源语句 sha256=4c57b1e2a8d27e3b8b05b5a3089866f5aa11272d83d177cacf20a886e5d6d59b；保留返回、异常及 0 个分支，调用=onBeforeUnmount, sortable.destroy。
  - 去向：react-front/src/components/BusinessFileUpload/index.context.ts
- I00830 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` lines 512-512 ExpressionStatement: 
  - 基线：源语句 sha256=c469d52397445fda391072b3835fc8b441cb6bdcb723e15b433bb1375f758801；保留返回、异常及 0 个分支，调用=defineExpose。
  - 去向：react-front/src/components/BusinessFileUpload/index.context.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
