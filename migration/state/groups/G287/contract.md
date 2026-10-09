# G287 src/views/system/file/components/FileReferenceDrawer.vue：完整能力

依赖：G000, G039

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I05206 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` lines 85-85 ImportDeclaration: 
  - 基线：源语句 sha256=a226e152855ce33925c24c401642f2bbed2dd4a06ba33c399d1812243e06550c；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05207 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` lines 87-87 VariableDeclaration: visible
  - 基线：源语句 sha256=1e5831fe2e56f6cc177d5ecfd848b4a6a30d10008c0fed3fc9f2ab7bcf3c3453；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05208 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` lines 88-88 VariableDeclaration: loading
  - 基线：源语句 sha256=0f2d86fe0699597a69087a478d5543264e008a02dbd9826dd2138c7409858393；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05209 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` lines 89-89 VariableDeclaration: fileName
  - 基线：源语句 sha256=002d68d0f126e088bacfdbc8f608f68deeccca37344c0fcc0fa31a91662553f3；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05210 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` lines 90-90 VariableDeclaration: referenceList
  - 基线：源语句 sha256=8f22e0727d976c6f24d0229a9adca3c5963d91a3f88ce3efeaa3a0bf7cc9a95d；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05211 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` lines 92-103 FunctionDeclaration: open
  - 基线：源语句 sha256=8132e72aa174a4bf5d51428797762584a43407c0f5794c0a1caefc883c3b61ae；保留返回、异常及 0 个分支，调用=CallExpression.finally, CallExpression.then, listFileReference。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05212 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` lines 105-105 ExpressionStatement: 
  - 基线：源语句 sha256=2e56640d2586072b42b8ea1f2cbd05f1d669da4f3e9e5617eb50a334cf1e3d67；保留返回、异常及 0 个分支，调用=defineExpose。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05213 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template lines 1-82（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05214 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template line 3: v-bind:title
  - 基线：原表达式：`业务引用 - ${fileName}`；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05215 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template line 4: v-model:
  - 基线：原表达式：visible；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05216 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template line 11: v-bind:closable
  - 基线：原表达式：false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05217 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template line 15: v-loading:
  - 基线：原表达式：loading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05218 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template line 15: v-bind:data
  - 基线：原表达式：referenceList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05219 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template line 21: v-bind:show-overflow-tooltip
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05220 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template line 28: v-bind:show-overflow-tooltip
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05221 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template line 30: v-slot:default
  - 基线：原表达式：scope；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05222 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template line 37: v-bind:show-overflow-tooltip
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05223 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template line 45: v-slot:default
  - 基线：原表达式：scope；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05224 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template line 54: v-slot:default
  - 基线：原表达式：scope；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05225 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template line 55: v-if:
  - 基线：原表达式：scope.row.legacy；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05226 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template line 58: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05227 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template line 66: v-bind:show-overflow-tooltip
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05228 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template line 68: v-slot:default
  - 基线：原表达式：scope；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05229 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template line 76: v-slot:default
  - 基线：原表达式：scope；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05230 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template interpolation line 30
  - 基线：原显示表达式：scope.row.businessName || "-"
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05231 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template interpolation line 46
  - 基线：原显示表达式：scope.row.retentionExpireTime
              ? parseTime(scope.row.retentionExpireTime)
              : "永久保留"
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05232 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template interpolation line 68
  - 基线：原显示表达式：scope.row.createBy || "-"
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx
- I05233 `ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue` template interpolation line 77
  - 基线：原显示表达式：parseTime(scope.row.createTime) || "-"
  - 去向：react-front/src/views/system/file/components/FileReferenceDrawer.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
