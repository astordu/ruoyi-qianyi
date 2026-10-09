# G020 plugins/ai/views/chat/components/AiMessage.vue：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00099 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` lines 44-44 ImportDeclaration: 
  - 基线：源语句 sha256=733fabf846833b78660382426f1ac813688c660925182115b33bc720a5979bb6；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00100 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` lines 45-45 ImportDeclaration: 
  - 基线：源语句 sha256=b342041bc3d1772ad59411cc5d81ed7af69a715afe07da7e6294bfab27f2e666；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00101 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` lines 46-46 ImportDeclaration: 
  - 基线：源语句 sha256=787e1b11f1fc82bb9faa1f99e9952d06a898a0396d2043698865084a5e66d0e6；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00102 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` lines 47-47 ImportDeclaration: 
  - 基线：源语句 sha256=073cb9ad5e6d4cb4ead89ba4005850e2c5f18afbf34ebd82d1dd3b5acb1218bc；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00103 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` lines 48-48 ImportDeclaration: 
  - 基线：源语句 sha256=67c17e3cc3254bac90f54daf1aa87135c660b0df235df05f2966c6ecb7ead7a2；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00104 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` lines 49-49 ImportDeclaration: 
  - 基线：源语句 sha256=5eb24c46c3850525dbd961c0a95650494f41c2b2bea5fda871a66aeb8d0357b7；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00105 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` lines 51-51 ExpressionStatement: 
  - 基线：源语句 sha256=1e2d08b9c62ccaa234c56510f1fc830a94a9df2cd684d26c306889252c6c4e21；保留返回、异常及 0 个分支，调用=enableMermaid。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00106 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` lines 52-52 ExpressionStatement: 
  - 基线：源语句 sha256=6fb505d64bc7564fbcf2ee7e0033d6356480265072f4b874e4ca8144c7fb07ee；保留返回、异常及 0 个分支，调用=enableKatex。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00107 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` lines 54-54 VariableDeclaration: isDark
  - 基线：源语句 sha256=528915e44bfc1622e1db7d0f8c50d2885f14c34baa8e651ddc02ce07c1db0af6；保留返回、异常及 0 个分支，调用=useDark。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00108 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` lines 56-69 VariableDeclaration: props
  - 基线：源语句 sha256=0b25094e0500928b7a54e742a3b0ad4e77b7028b8bcc3989e810611f05743e1d；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00109 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` lines 71-71 VariableDeclaration: isReasoningExpanded
  - 基线：源语句 sha256=3a9997636064e627e84b30e087fa74b62ecba201d473c5af49afa99f7ff7d2b4；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00110 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` lines 73-75 VariableDeclaration: isThinkingComplete
  - 基线：源语句 sha256=6a9befa97d2411bcd2a0161e41dbf3d2393158bb64da063e9b775dd885f90a2b；保留返回、异常及 1 个分支，调用=computed。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00111 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` lines 77-79 FunctionDeclaration: toggleReasoning
  - 基线：源语句 sha256=4e9491626f6304792607e64656aa5a8cfe8e040b1f0aa8212312ebda65012f67；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00112 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` template lines 1-41（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00113 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` template line 3: v-if:
  - 基线：原表达式：reasoningContent；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00114 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` template line 4: v-on:click
  - 基线：原表达式：toggleReasoning；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00115 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` template line 5: v-bind:class
  - 基线：原表达式：{ 'is-expanded': isReasoningExpanded }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00116 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` template line 9: v-if:
  - 基线：原表达式：!isThinkingComplete；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00117 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` template line 13: v-show:
  - 基线：原表达式：isReasoningExpanded；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00118 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` template line 15: v-bind:content
  - 基线：原表达式：reasoningContent；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00119 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` template line 16: v-bind:is-dark
  - 基线：原表达式：isDark；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00120 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` template line 17: v-bind:final
  - 基线：原表达式：!loading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00121 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` template line 25: v-bind:content
  - 基线：原表达式：content；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00122 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` template line 26: v-bind:is-dark
  - 基线：原表达式：isDark；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00123 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` template line 27: v-bind:final
  - 基线：原表达式：!loading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00124 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` template line 33: v-if:
  - 基线：原表达式：loading && !content && !reasoningContent；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx
- I00125 `ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue` style[0] lines 82-182
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=False；原样式选择器在 source-audit.json。
  - 去向：react-front/plugins/ai/views/chat/components/AiMessage.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
