# G311 src/views/system/user/profile/index.vue：完整能力

依赖：G000, G045, G187, G230, G312, G313, G314, G315

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I07574 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` lines 69-69 ImportDeclaration: 
  - 基线：源语句 sha256=4400f5abed6d23bf15d451663cdd1257bd8c3afa21a9fab130a6298acc1ec5ef；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07575 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` lines 70-70 ImportDeclaration: 
  - 基线：源语句 sha256=0dc9f21df102bee14c4be6c3a9ce49b14b1a146719f6c3f83b82b4efb670ecc2；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07576 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` lines 71-71 ImportDeclaration: 
  - 基线：源语句 sha256=73fb191c2aac7c5ce207885c222c48598cbd7d298d1de8eaa4ab8dc77728b147；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07577 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` lines 72-72 ImportDeclaration: 
  - 基线：源语句 sha256=0145b9c7154eadfefb80758194cd0f55e93a3a1b849263a93e9daf7d355570bf；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07578 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` lines 73-73 ImportDeclaration: 
  - 基线：源语句 sha256=3705b3a3904d8affa7889768f9b18ef558dd7aa4dc23358c91b008ba2ee166e9；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07579 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` lines 74-74 ImportDeclaration: 
  - 基线：源语句 sha256=1e2bc804c77a92340e9b09f9e843cc40cf2422f7ce49004a43154888aee7c9ed；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07580 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` lines 76-76 VariableDeclaration: route
  - 基线：源语句 sha256=4d0e93888827dba310f5cf48815c617b23da1a2eb2ff3690209994f3b8c71ff7；保留返回、异常及 0 个分支，调用=useRoute。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07581 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` lines 77-77 VariableDeclaration: selectedTab
  - 基线：源语句 sha256=0f35496acd4c6cf66e14fe49967570509d50f39b32802ccac92640717f4acb5d；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07582 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` lines 78-82 VariableDeclaration: state
  - 基线：源语句 sha256=9655655adecc7f0a65a5bd2e8643df62a1f52eae29d58e87252e310cf3d8eba0；保留返回、异常及 0 个分支，调用=reactive。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07583 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` lines 84-91 FunctionDeclaration: getUser
  - 基线：源语句 sha256=d86c4cb924d50f5a8759126de81ba0f1585abd070096f82d18349d7d81d9404d；保留返回、异常及 0 个分支，调用=CallExpression.then, getUserProfile, CallExpression.applyTimezone, useUserStore。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07584 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` lines 91-91 EmptyStatement: 
  - 基线：源语句 sha256=41b805ea7ac014e23556e98bb374702a08344268f92489a02f0880849394a1e4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07585 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` lines 93-99 ExpressionStatement: 
  - 基线：源语句 sha256=30fe322af71582af3463e5ca59783fd672e074d7181d3ac3fd12731e49fe816e；保留返回、异常及 2 个分支，调用=onMounted, getUser。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07586 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` template lines 1-66（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07587 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` template line 3: v-bind:gutter
  - 基线：原表达式：20；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07588 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` template line 4: v-bind:span
  - 基线：原表达式：6；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07589 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` template line 4: v-bind:xs
  - 基线：原表达式：24；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07590 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` template line 6: v-slot:header
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07591 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` template line 30: v-if:
  - 基线：原表达式：state.user.dept；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07592 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` template line 44: v-bind:span
  - 基线：原表达式：18；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07593 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` template line 44: v-bind:xs
  - 基线：原表达式：24；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07594 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` template line 46: v-slot:header
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07595 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` template line 51: v-model:
  - 基线：原表达式：selectedTab；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07596 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` template line 53: v-bind:user
  - 基线：原表达式：state.user；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07597 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` template line 59: v-bind:user
  - 基线：原表达式：state.user；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07598 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` template line 59: v-on:saved
  - 基线：原表达式：state.user.timeZone = $event；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07599 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` template interpolation line 18
  - 基线：原显示表达式：state.user.userName
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07600 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` template interpolation line 22
  - 基线：原显示表达式：state.user.phonenumber
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07601 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` template interpolation line 26
  - 基线：原显示表达式：state.user.email
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07602 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` template interpolation line 30
  - 基线：原显示表达式：state.user.dept.deptName
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07603 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` template interpolation line 30
  - 基线：原显示表达式：state.postGroup
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07604 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` template interpolation line 34
  - 基线：原显示表达式：state.roleGroup
  - 去向：react-front/src/views/system/user/profile/index.tsx
- I07605 `ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue` template interpolation line 38
  - 基线：原显示表达式：parseTime(state.user.createTime) || '-'
  - 去向：react-front/src/views/system/user/profile/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
