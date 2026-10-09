# G157 src/components/Breadcrumb/index.vue：完整能力

依赖：G000, G227

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00761 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` lines 13-13 ImportDeclaration: 
  - 基线：源语句 sha256=efbb342d84aefbc6dc4b206f290d81fe87a23b34796df1ad0da69cd6a90b7ea3；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/Breadcrumb/index.tsx
- I00762 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` lines 15-15 VariableDeclaration: route
  - 基线：源语句 sha256=4d0e93888827dba310f5cf48815c617b23da1a2eb2ff3690209994f3b8c71ff7；保留返回、异常及 0 个分支，调用=useRoute。
  - 去向：react-front/src/components/Breadcrumb/index.tsx
- I00763 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` lines 16-16 VariableDeclaration: router
  - 基线：源语句 sha256=4493bc84540aad888c32c80251d8de79e93d311f4a9a11bb353ecaee4838a473；保留返回、异常及 0 个分支，调用=useRouter。
  - 去向：react-front/src/components/Breadcrumb/index.tsx
- I00764 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` lines 17-17 VariableDeclaration: permissionStore
  - 基线：源语句 sha256=8aea4ee78c3bc335fb25695e39a02e09a8551a4b638040cc30c3a575ef5ec2ed；保留返回、异常及 0 个分支，调用=usePermissionStore。
  - 去向：react-front/src/components/Breadcrumb/index.tsx
- I00765 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` lines 18-18 VariableDeclaration: levelList
  - 基线：源语句 sha256=1a215659445c8de3b88ee8d9184d9ac8ba63d616f55355f3ac2bbce8d5dd4469；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Breadcrumb/index.tsx
- I00766 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` lines 20-40 FunctionDeclaration: getBreadcrumb
  - 基线：源语句 sha256=b21f68eab2fb60eb6cba31fe05657737d5adecb9ca97a5119a3f589f381b0ed8；保留返回、异常及 7 个分支，调用=findPathNum, CallExpression.map, route.path.match, item.slice, getMatched, route.matched.filter, isDashboard, ArrayExpression.concat, matched.filter。
  - 去向：react-front/src/components/Breadcrumb/index.tsx
- I00767 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` lines 41-49 FunctionDeclaration: findPathNum
  - 基线：源语句 sha256=f24dac388dcf79a82719992594d0f86c77a6dca8a77a31eac48e5dc90d3bc2ba；保留返回、异常及 1 个分支，调用=str.indexOf。
  - 去向：react-front/src/components/Breadcrumb/index.tsx
- I00768 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` lines 50-59 FunctionDeclaration: getMatched
  - 基线：源语句 sha256=d3a4979128b960d1792894ff268af3164f766f984ffb75de9d1a086de997e52c；保留返回、异常及 4 个分支，调用=routeList.find, AssignmentExpression.toLowerCase, matched.push, pathList.shift, getMatched。
  - 去向：react-front/src/components/Breadcrumb/index.tsx
- I00769 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` lines 60-66 FunctionDeclaration: isDashboard
  - 基线：源语句 sha256=7174ee4e53468e581a0a7725050d0069d8f073f8fb5a72adb485e8a60d40f2ac；保留返回、异常及 4 个分支，调用=name.trim。
  - 去向：react-front/src/components/Breadcrumb/index.tsx
- I00770 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` lines 67-74 FunctionDeclaration: handleLink
  - 基线：源语句 sha256=0495801f4a12efe708b8561402db49c9f8e8a4380dc52246f61b6d1d6ad11a7c；保留返回、异常及 2 个分支，调用=router.push。
  - 去向：react-front/src/components/Breadcrumb/index.tsx
- I00771 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` lines 76-82 ExpressionStatement: 
  - 基线：源语句 sha256=311c818dfee7df9fa03b839647d336a241a107089e08a889bc21ee2afd8f92d0；保留返回、异常及 2 个分支，调用=watchEffect, route.path.startsWith, getBreadcrumb。
  - 去向：react-front/src/components/Breadcrumb/index.tsx
- I00772 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` lines 83-83 ExpressionStatement: 
  - 基线：源语句 sha256=6ea75e6de2280b9c7cb52d1eeab08e2a7301412b2cb798b99a6f8735c7d29eff；保留返回、异常及 0 个分支，调用=getBreadcrumb。
  - 去向：react-front/src/components/Breadcrumb/index.tsx
- I00773 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` template lines 1-10（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/components/Breadcrumb/index.tsx
- I00774 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` template line 4: v-for:
  - 基线：原表达式：(item, index) in levelList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Breadcrumb/index.tsx
- I00775 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` template line 4: v-bind:key
  - 基线：原表达式：item.path；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Breadcrumb/index.tsx
- I00776 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` template line 5: v-if:
  - 基线：原表达式：item.redirect === 'noRedirect' || index == levelList.length - 1；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Breadcrumb/index.tsx
- I00777 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` template line 6: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Breadcrumb/index.tsx
- I00778 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` template line 6: v-on:click
  - 基线：原表达式：handleLink(item)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Breadcrumb/index.tsx
- I00779 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` template interpolation line 5
  - 基线：原显示表达式：item.meta.title
  - 去向：react-front/src/components/Breadcrumb/index.tsx
- I00780 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` template interpolation line 6
  - 基线：原显示表达式：item.meta.title
  - 去向：react-front/src/components/Breadcrumb/index.tsx
- I00781 `ruoyi-fastapi-frontend/src/components/Breadcrumb/index.vue` style[0] lines 86-97
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/components/Breadcrumb/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
