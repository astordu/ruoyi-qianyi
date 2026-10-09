# G198 src/layout/components/HeaderNotice/index.vue：完整能力

依赖：G000, G041, G187, G197

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01965 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` lines 41-41 ImportDeclaration: 
  - 基线：源语句 sha256=974ab8c6464be310b97602efa97611d1399b555d2b1b552f350d28fbfb6f4aa8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01966 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` lines 42-42 ImportDeclaration: 
  - 基线：源语句 sha256=4fe55595ae527de4a0d9aad2b8397f63df621ae265f06ab66e8b70c22157c4f2；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01967 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` lines 44-44 VariableDeclaration: noticePopover
  - 基线：源语句 sha256=4d1421cb2c043d2d2f151363b7eb03121604e88237c84ce9881b0f927c5b5dd6；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01968 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` lines 45-45 VariableDeclaration: noticeList
  - 基线：源语句 sha256=a61b6e48c7be7fcb1caa3aeb3b1c5af581b474fbf898c76cbec5fce5e0a94a0f；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01969 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` lines 46-46 VariableDeclaration: unreadCount
  - 基线：源语句 sha256=7de6a8488a823bf3dc0941c85b3bf1d8c1f49bf500923722d4260f457c7c0e26；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01970 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` lines 47-47 VariableDeclaration: noticeLoading
  - 基线：源语句 sha256=e672fd3cb033a4b802dab990b53a1b105be56b65972d34849ddae15417ed55a7；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01971 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` lines 48-48 VariableDeclaration: noticeVisible
  - 基线：源语句 sha256=dc7fd035f7064dd7f6b95fff82432d9cc42e5754b754aaa847f2b6233ca1c024；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01972 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` lines 49-49 VariableDeclaration: noticeLeaveTimer
  - 基线：源语句 sha256=e1c3b4370c0bdf8b7dddf5c8c55bef28f38b1369fc410ba3764a7ea78dd84d52；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01973 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` lines 50-50 VariableDeclaration: 
  - 基线：源语句 sha256=d3917068104e0f2158733e5e758c09ff6781b09fc4b90611c9a30e2625c695d6；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01974 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` lines 53-61 FunctionDeclaration: loadNoticeTop
  - 基线：源语句 sha256=8dbfd8e1fe192c6dde60b4ca8de5baefa8de4e73e05ef0606bffc03a4e8fe12f；保留返回、异常及 2 个分支，调用=CallExpression.finally, CallExpression.then, listNoticeTop, noticeList.value.filter。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01975 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` lines 63-63 ExpressionStatement: 
  - 基线：源语句 sha256=1679a7c3a30c228dd2f92ab1d0955e2d5b152e0e50ffa31e8c2d3366480ae736；保留返回、异常及 0 个分支，调用=onMounted, loadNoticeTop。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01976 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` lines 66-79 FunctionDeclaration: onNoticeEnter
  - 基线：源语句 sha256=9cc1b7c2b63a97a15dc2ff0b148b3af89d8a4e05af3aefd24e0748e47d452893；保留返回、异常及 2 个分支，调用=clearTimeout, nextTick, popper.addEventListener, setTimeout。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01977 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` lines 82-84 FunctionDeclaration: onNoticeLeave
  - 基线：源语句 sha256=16c95058881292971e47aaa12f8d4c5562937dc9fa6ef2438b01fed3eebe6971；保留返回、异常及 0 个分支，调用=setTimeout。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01978 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` lines 87-95 FunctionDeclaration: previewNotice
  - 基线：源语句 sha256=63bd4327c1f80f88b22ec355e9dbc3177d497b09982b27122304a6ad600873bc；保留返回、异常及 2 个分支，调用=CallExpression.catch, markNoticeRead, noticeList.value.indexOf, Math.max, proxy.$refs.noticeViewRef.open。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01979 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` lines 98-104 FunctionDeclaration: markAllRead
  - 基线：源语句 sha256=29da4c8f2a1cffd05898fcf5f5e4332e4aaf2a188ab2d4a0283c36c88ada9be9；保留返回、异常及 2 个分支，调用=CallExpression.join, noticeList.value.map, CallExpression.catch, markNoticeReadAll。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01980 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` template lines 1-38（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01981 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` template line 3: v-bind:width
  - 基线：原表达式：320；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01982 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` template line 3: v-model:visible
  - 基线：原表达式：noticeVisible；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01983 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` template line 7: v-on:click
  - 基线：原表达式：markAllRead；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01984 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` template line 9: v-if:
  - 基线：原表达式：noticeLoading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01985 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` template line 12: v-else-if:
  - 基线：原表达式：noticeList.length === 0；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01986 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` template line 16: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01987 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` template line 17: v-for:
  - 基线：原表达式：item in noticeList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01988 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` template line 17: v-bind:key
  - 基线：原表达式：item.noticeId；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01989 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` template line 17: v-bind:class
  - 基线：原表达式：{ 'is-read': item.isRead }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01990 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` template line 17: v-on:click
  - 基线：原表达式：previewNotice(item)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01991 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` template line 18: v-bind:type
  - 基线：原表达式：item.noticeType === '1' ? 'warning' : 'success'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01992 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` template line 27: v-slot:reference
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01993 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` template line 28: v-on:mouseenter
  - 基线：原表达式：onNoticeEnter；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01994 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` template line 28: v-on:mouseleave
  - 基线：原表达式：onNoticeLeave；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01995 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` template line 30: v-if:
  - 基线：原表达式：unreadCount > 0；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01996 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` template interpolation line 19
  - 基线：原显示表达式：item.noticeType === '1' ? '通知' : '公告'
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01997 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` template interpolation line 21
  - 基线：原显示表达式：item.noticeTitle
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01998 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` template interpolation line 22
  - 基线：原显示表达式：parseTime(item.createTime) || '-'
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I01999 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` template interpolation line 30
  - 基线：原显示表达式：unreadCount
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx
- I02000 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue` style[0] lines 107-184
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/layout/components/HeaderNotice/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
