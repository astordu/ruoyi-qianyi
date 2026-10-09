# G319 src/views/tool/build/IconsDialog.vue：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I07887 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` lines 24-24 ImportDeclaration: 
  - 基线：源语句 sha256=367a290266eb4dd72c9f571fea68c4d9ac937a7ac0db2d0757cd1b2f6a31ecaf；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07888 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` lines 25-25 ImportDeclaration: 
  - 基线：源语句 sha256=8c0475d774038c4c81b252ca3ca3cb315afb58675ae97d942dcf692d9c5b43df；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07889 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` lines 27-27 VariableDeclaration: iconList
  - 基线：源语句 sha256=5b703c04144b83d367e45c1691e715270151f5f382ff434b94fc83484bec2765；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07890 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` lines 28-28 VariableDeclaration: originList
  - 基线：源语句 sha256=6c2ae6922f5ed258ae8604fb132609ddfe0700af1857bd1e69d1b5474921daef；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07891 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` lines 29-29 VariableDeclaration: key
  - 基线：源语句 sha256=9fc1fa1dc2b0a733000a1c19382bd8c395d01054d9e50d43f757d206dd1a9f7e；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07892 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` lines 30-30 VariableDeclaration: active
  - 基线：源语句 sha256=1b6ef9005df51d2a4893c9c73d12f912743458cb088417d9d8fb5f6a808525dc；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07893 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` lines 31-31 VariableDeclaration: emit
  - 基线：源语句 sha256=7f063f77725320cd985b742db5881248d94c8d199cca8a81154433ddb5c363a5；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07894 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` lines 32-32 VariableDeclaration: value
  - 基线：源语句 sha256=b13bae5e6b88477bd79a5529a32e41ffa0d1376aed422d7aac33fcf27f7be12a；保留返回、异常及 0 个分支，调用=defineModel。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07895 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` lines 33-36 ForOfStatement: 
  - 基线：源语句 sha256=655615655e44a162d23a60be9a150116f768b309ff6d87d93f799b05e90479a6；保留返回、异常及 0 个分支，调用=Object.entries, iconList.value.push, originList.push。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07896 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` lines 38-38 FunctionDeclaration: onOpen
  - 基线：源语句 sha256=863d64a1504182c28bc4a152004a182e29d6358bdabb87fc0dbd09672702ea67；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07897 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` lines 39-39 FunctionDeclaration: onClose
  - 基线：源语句 sha256=0f06818b29b5987625958437b4a782c1be98e123f92f265d199ce231990b7841；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07898 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` lines 40-44 FunctionDeclaration: onSelect
  - 基线：源语句 sha256=875c63c752caf0a901fb771444f83ea402fa903d06756afa0bcb750a820db0a5；保留返回、异常及 0 个分支，调用=emit。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07899 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` lines 46-52 ExpressionStatement: 
  - 基线：源语句 sha256=e75bfb4568f1220c23a4904d4519be6fda66ee802dd43584b6d4b9daffa22b85；保留返回、异常及 1 个分支，调用=watch, originList.filter, name.indexOf。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07900 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` template lines 1-22（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07901 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` template line 3: v-model:
  - 基线：原表达式：value；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07902 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` template line 3: v-bind:close-on-click-modal
  - 基线：原表达式：false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07903 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` template line 3: v-bind:modal-append-to-body
  - 基线：原表达式：false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07904 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` template line 3: v-on:open
  - 基线：原表达式：onOpen；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07905 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` template line 4: v-on:close
  - 基线：原表达式：onClose；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07906 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` template line 5: v-slot:header
  - 基线：原表达式：{ close, titleId, titleClass }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07907 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` template line 7: v-model:
  - 基线：原表达式：key；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07908 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` template line 7: v-bind:style
  - 基线：原表达式：{ width: '260px' }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07909 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` template line 11: v-for:
  - 基线：原表达式：icon in iconList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07910 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` template line 11: v-bind:key
  - 基线：原表达式：icon；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07911 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` template line 11: v-bind:class
  - 基线：原表达式：active === icon ? 'active-item' : ''；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07912 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` template line 11: v-on:click
  - 基线：原表达式：onSelect(icon)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07913 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` template line 13: v-bind:size
  - 基线：原表达式：30；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07914 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` template line 14: v-bind:is
  - 基线：原表达式：icon；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07915 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` template interpolation line 16
  - 基线：原显示表达式：icon
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx
- I07916 `ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue` style[0] lines 54-115
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/views/tool/build/IconsDialog.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
