# G186 src/components/SizeSelect/index.vue：完整能力

依赖：G000, G187, G224

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01773 `ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue` lines 19-19 ImportDeclaration: 
  - 基线：源语句 sha256=34ecbe398bac672bb380b5e803e854de7dbaa27c8329e5b119497695825600a9；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/SizeSelect/index.tsx
- I01774 `ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue` lines 21-21 VariableDeclaration: appStore
  - 基线：源语句 sha256=7b3a0f4a2972628d233f2511cad1b9efc491c3d72675b029d06eb2d78409ed14；保留返回、异常及 0 个分支，调用=useAppStore。
  - 去向：react-front/src/components/SizeSelect/index.tsx
- I01775 `ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue` lines 22-22 VariableDeclaration: size
  - 基线：源语句 sha256=56750a1cc96c8d1c6d6367d585e583205b457c68bb8c98b88d0cb8f1ce4a7903；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/components/SizeSelect/index.tsx
- I01776 `ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue` lines 23-23 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/components/SizeSelect/index.tsx
- I01777 `ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue` lines 24-28 VariableDeclaration: sizeOptions
  - 基线：源语句 sha256=b98da3156229f75be9d97ac5571d8f0d3f363b7b7abce0aad11050fa45a27d1b；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/SizeSelect/index.tsx
- I01778 `ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue` lines 30-34 FunctionDeclaration: handleSetSize
  - 基线：源语句 sha256=f14adef891e757ddb8d49b046ccd842d6279d55d8e875845e04a8fe054bf3aef；保留返回、异常及 0 个分支，调用=proxy.$modal.loading, appStore.setSize, setTimeout。
  - 去向：react-front/src/components/SizeSelect/index.tsx
- I01779 `ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue` template lines 1-16（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/components/SizeSelect/index.tsx
- I01780 `ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue` template line 3: v-on:command
  - 基线：原表达式：handleSetSize；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/SizeSelect/index.tsx
- I01781 `ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue` template line 7: v-slot:dropdown
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/SizeSelect/index.tsx
- I01782 `ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue` template line 9: v-for:
  - 基线：原表达式：item of sizeOptions；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/SizeSelect/index.tsx
- I01783 `ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue` template line 9: v-bind:key
  - 基线：原表达式：item.value；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/SizeSelect/index.tsx
- I01784 `ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue` template line 9: v-bind:disabled
  - 基线：原表达式：size === item.value；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/SizeSelect/index.tsx
- I01785 `ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue` template line 9: v-bind:command
  - 基线：原表达式：item.value；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/SizeSelect/index.tsx
- I01786 `ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue` template interpolation line 10
  - 基线：原显示表达式：item.label
  - 去向：react-front/src/components/SizeSelect/index.tsx
- I01787 `ruoyi-fastapi-frontend/src/components/SizeSelect/index.vue` style[0] lines 37-43
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/components/SizeSelect/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
