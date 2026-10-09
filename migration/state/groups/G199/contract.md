# G199 src/layout/components/IframeToggle/index.vue：完整能力

依赖：G000, G200, G229

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02001 `ruoyi-fastapi-frontend/src/layout/components/IframeToggle/index.vue` lines 12-12 ImportDeclaration: 
  - 基线：源语句 sha256=aaf01770d3070a77012b8cc6b30dd0bcae07880f2123aaf8fc1c540c843fef04；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/IframeToggle/index.tsx
- I02002 `ruoyi-fastapi-frontend/src/layout/components/IframeToggle/index.vue` lines 13-13 ImportDeclaration: 
  - 基线：源语句 sha256=56752ab9b817fab8e182a56ca834d7b287ef24e941f643beb3daa321865243d6；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/IframeToggle/index.tsx
- I02003 `ruoyi-fastapi-frontend/src/layout/components/IframeToggle/index.vue` lines 15-15 VariableDeclaration: route
  - 基线：源语句 sha256=19ffaf888604ba2654aa25f29ba0210e96226ea7089e9e15dc5c05cf276b3a9f；保留返回、异常及 0 个分支，调用=useRoute。
  - 去向：react-front/src/layout/components/IframeToggle/index.tsx
- I02004 `ruoyi-fastapi-frontend/src/layout/components/IframeToggle/index.vue` lines 16-16 VariableDeclaration: tagsViewStore
  - 基线：源语句 sha256=54979c873f4ea877dd740da47626e4cebeb4a6a351abda6b267ca8159472ca66；保留返回、异常及 0 个分支，调用=useTagsViewStore。
  - 去向：react-front/src/layout/components/IframeToggle/index.tsx
- I02005 `ruoyi-fastapi-frontend/src/layout/components/IframeToggle/index.vue` lines 18-24 FunctionDeclaration: iframeUrl
  - 基线：源语句 sha256=0092c330c7f2e64e494fff964bdb0b4f90a66ac867045e41c7d21e9edc7aad41；保留返回、异常及 3 个分支，调用=Object.keys, CallExpression.join, CallExpression.map。
  - 去向：react-front/src/layout/components/IframeToggle/index.tsx
- I02006 `ruoyi-fastapi-frontend/src/layout/components/IframeToggle/index.vue` template lines 1-9（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/layout/components/IframeToggle/index.tsx
- I02007 `ruoyi-fastapi-frontend/src/layout/components/IframeToggle/index.vue` template line 3: v-for:
  - 基线：原表达式：(item, index) in tagsViewStore.iframeViews；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/IframeToggle/index.tsx
- I02008 `ruoyi-fastapi-frontend/src/layout/components/IframeToggle/index.vue` template line 4: v-bind:key
  - 基线：原表达式：item.path；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/IframeToggle/index.tsx
- I02009 `ruoyi-fastapi-frontend/src/layout/components/IframeToggle/index.vue` template line 5: v-bind:iframeId
  - 基线：原表达式：'iframe' + index；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/IframeToggle/index.tsx
- I02010 `ruoyi-fastapi-frontend/src/layout/components/IframeToggle/index.vue` template line 6: v-show:
  - 基线：原表达式：route.path === item.path；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/IframeToggle/index.tsx
- I02011 `ruoyi-fastapi-frontend/src/layout/components/IframeToggle/index.vue` template line 7: v-bind:src
  - 基线：原表达式：iframeUrl(item.meta.link, item.query)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/IframeToggle/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
