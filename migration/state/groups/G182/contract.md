# G182 src/components/RightToolbar/index.vue：完整能力

依赖：G000, G216

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01711 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 43-43 ImportDeclaration: 
  - 基线：源语句 sha256=819249c9809a1e47bb12de03da21c4c25f60b908825d07094d219578c4c835ec；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01712 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 45-76 VariableDeclaration: props
  - 基线：源语句 sha256=e6f8e4bb0bc60b5ecb129833ce2d04fd2007a99d5ad0ed983e5bf201b984689e；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01713 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 78-78 VariableDeclaration: emits
  - 基线：源语句 sha256=60333f3f0681b2c0aef6e3fd54518c80abe601ca58ef8477ad158261ee5d049f；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01714 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 81-81 VariableDeclaration: value
  - 基线：源语句 sha256=20ab7b0c09fedd5ad4e5cd52b3eaa1a08be220aae2adf59379aecf7e1a393170；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01715 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 83-83 VariableDeclaration: title
  - 基线：源语句 sha256=3c95f0b2189f9dc79cb87527b4a7277715be2cfec63319a6c626294795dfe3d0；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01716 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 85-85 VariableDeclaration: open
  - 基线：源语句 sha256=48efe1aea2c9ae0f92ccf055fafa57c58c3d9241e25b126f875a7017ff7c8686；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01717 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 87-93 VariableDeclaration: style
  - 基线：源语句 sha256=7b7a432384f6fd333c899c5808abd0297fdbcd219b8ed331c95a1ec3568ea900；保留返回、异常及 2 个分支，调用=computed。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01718 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 96-99 VariableDeclaration: isChecked
  - 基线：源语句 sha256=da334fe5573c25a31f504bf09d8a702a05849682a9ba5ca7faac302fa433bbc2；保留返回、异常及 1 个分支，调用=computed, Array.isArray, props.columns.every, CallExpression.every, Object.values。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01719 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 100-100 VariableDeclaration: isIndeterminate
  - 基线：源语句 sha256=dacab20f8b9970d3c71fdb977db29ca1fa1a15b46273d556d908ed9b47c44ff7；保留返回、异常及 3 个分支，调用=computed, Array.isArray, props.columns.some, CallExpression.some, Object.values。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01720 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 101-101 VariableDeclaration: transferData
  - 基线：源语句 sha256=f73795fa4e230aeab3d149245ca78062a0734a2df626a56f21dba1fcbaa9eaa4；保留返回、异常及 1 个分支，调用=computed, Array.isArray, props.columns.map, CallExpression.map, Object.keys。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01721 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 104-104 VariableDeclaration: 
  - 基线：源语句 sha256=d3917068104e0f2158733e5e758c09ff6781b09fc4b90611c9a30e2625c695d6；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01722 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 105-113 FunctionDeclaration: toggleSearch
  - 基线：源语句 sha256=70cc083e013d4a770d6e24f8223b0c4915492b924d27d5a756ef845444aa4ae4；保留返回、异常及 4 个分支，调用=el.querySelector, emits, animateSearch。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01723 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 114-133 FunctionDeclaration: animateSearch
  - 基线：源语句 sha256=b7884046310f59f736fdd38a9e357dd8705115d41d24ca5838454e9d1a606499；保留返回、异常及 1 个分支，调用=Object.assign, requestAnimationFrame, setTimeout, emits, clear, nextTick。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01724 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 136-138 FunctionDeclaration: refresh
  - 基线：源语句 sha256=59b6935efd8d7694f3732b82568a3ded7be3d2eab6539443be8f3e15fce67ff1；保留返回、异常及 0 个分支，调用=emits。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01725 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 141-153 FunctionDeclaration: dataChange
  - 基线：源语句 sha256=5ea28faa1941183dfd29ddae0537da04a9667636100073186ed557ce85233212；保留返回、异常及 1 个分支，调用=Array.isArray, data.includes, CallExpression.forEach, Object.keys, saveStorage。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01726 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 156-158 FunctionDeclaration: showColumn
  - 基线：源语句 sha256=475dd28af582fed0eea099585a29e088ff6f7cdfa68a5f36560f8e781da53fa9；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01727 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 161-176 IfStatement: 
  - 基线：源语句 sha256=4231f40eb193983470f4bd89d7a447c54046e2743fcad746d2d0c2395edeac31；保留返回、异常及 7 个分支，调用=cache.local.getJSON, Array.isArray, props.columns.forEach, CallExpression.forEach, Object.keys。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01728 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 177-192 IfStatement: 
  - 基线：源语句 sha256=1cfb79ba53838cce24efde0f115a8aca0ffdff1660a2310421a68cb4bfd8120a；保留返回、异常及 4 个分支，调用=Array.isArray, value.value.push, parseInt, CallExpression.forEach, Object.keys。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01729 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 195-202 FunctionDeclaration: checkboxChange
  - 基线：源语句 sha256=15fa04d1f58652ca1e515d7cec6cf856c58e903dc4282fac8678d16cadeb3ac6；保留返回、异常及 1 个分支，调用=Array.isArray, props.columns.filter, saveStorage。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01730 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 205-213 FunctionDeclaration: toggleCheckAll
  - 基线：源语句 sha256=88b475a00876eb38d7628291f7943618e66ecedb8af7fb7e5607e137446ce8e9；保留返回、异常及 1 个分支，调用=Array.isArray, props.columns.forEach, CallExpression.forEach, Object.values, saveStorage。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01731 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` lines 216-227 FunctionDeclaration: saveStorage
  - 基线：源语句 sha256=931117b245f4e4ae0b99549013e1f8d3ce6ec1de709048931cab50e16881d7d6；保留返回、异常及 4 个分支，调用=Array.isArray, props.columns.forEach, CallExpression.forEach, Object.keys, cache.local.setJSON。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01732 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template lines 1-40（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01733 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 2: v-bind:style
  - 基线：原表达式：style；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01734 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 4: v-bind:content
  - 基线：原表达式：showSearch ? '隐藏搜索' : '显示搜索'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01735 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 4: v-if:
  - 基线：原表达式：search；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01736 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 5: v-on:click
  - 基线：原表达式：toggleSearch()；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01737 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 8: v-on:click
  - 基线：原表达式：refresh()；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01738 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 10: v-if:
  - 基线：原表达式：Object.keys(columns).length > 0；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01739 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 11: v-on:click
  - 基线：原表达式：showColumn()；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01740 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 11: v-if:
  - 基线：原表达式：showColumnsType == 'transfer'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01741 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 12: v-bind:hide-on-click
  - 基线：原表达式：false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01742 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 12: v-if:
  - 基线：原表达式：showColumnsType == 'checkbox'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01743 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 14: v-slot:dropdown
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01744 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 18: v-bind:indeterminate
  - 基线：原表达式：isIndeterminate；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01745 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 18: v-model:
  - 基线：原表达式：isChecked；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01746 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 18: v-on:change
  - 基线：原表达式：toggleCheckAll；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01747 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 21: v-for:
  - 基线：原表达式：(item, key) in columns；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01748 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 21: v-bind:key
  - 基线：原表达式：item.key；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01749 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 23: v-model:
  - 基线：原表达式：item.visible；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01750 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 23: v-on:change
  - 基线：原表达式：checkboxChange($event, key)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01751 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 23: v-bind:label
  - 基线：原表达式：item.label；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01752 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 31: v-bind:title
  - 基线：原表达式：title；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01753 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 31: v-model:
  - 基线：原表达式：open；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01754 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 33: v-bind:titles
  - 基线：原表达式：['显示', '隐藏']；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01755 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 34: v-model:
  - 基线：原表达式：value；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01756 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 35: v-bind:data
  - 基线：原表达式：transferData；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01757 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` template line 36: v-on:change
  - 基线：原表达式：dataChange；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/RightToolbar/index.tsx
- I01758 `ruoyi-fastapi-frontend/src/components/RightToolbar/index.vue` style[0] lines 230-249
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/components/RightToolbar/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
