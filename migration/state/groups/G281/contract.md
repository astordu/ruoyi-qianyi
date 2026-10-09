# G281 src/views/system/dict/detail.vue：完整能力

依赖：G000, G037

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I04681 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` lines 76-76 ImportDeclaration: 
  - 基线：源语句 sha256=6ee599e82b6bb842ae32c5ee899b94d3e6e3ab42dee804b40eca625242346036；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04682 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` lines 78-81 VariableDeclaration: props
  - 基线：源语句 sha256=8a71df8321a7a38dde2a77b7be8c5a3d0a9eed71fc2607dbe60f86817f1d913b；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04683 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` lines 83-83 ExpressionStatement: 
  - 基线：源语句 sha256=d8dff3d486c65dc5fd53191abe99e098475e62177b927485c99a46dce5e4ee3e；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04684 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` lines 85-85 VariableDeclaration: loading
  - 基线：源语句 sha256=360133162609dea18ceb29cc60a4fd9166a9ed26b0d8544941212d26502f30ef；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04685 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` lines 86-86 VariableDeclaration: dataList
  - 基线：源语句 sha256=3a0158e8c63a70349d6dfea4e819a5fc32ce6cc397af8a83e06047a5fbbe5a87；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04686 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` lines 88-88 VariableDeclaration: normalCount
  - 基线：源语句 sha256=ebc7f31c5b463b87487cba77316519c294bcfb2acd4acf0678880beb6e935529；保留返回、异常及 0 个分支，调用=computed, dataList.value.filter。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04687 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` lines 89-89 VariableDeclaration: disabledCount
  - 基线：源语句 sha256=4399aabdf7353c5e0f5ffb37d5d68fc8fd0d372aba8f9a10d9e204f2988d433c；保留返回、异常及 0 个分支，调用=computed, dataList.value.filter。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04688 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` lines 91-97 ExpressionStatement: 
  - 基线：源语句 sha256=428e9e72d45897b3d803abbabef444a6c606c0e8a6f2ad511cc74cc257d0bbeb；保留返回、异常及 1 个分支，调用=watch, loadData。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04689 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` lines 99-108 FunctionDeclaration: loadData
  - 基线：源语句 sha256=1549df0306e5666c7444da0db737c2b2cbf474f0dca7518f10a1f3e5b09795ee；保留返回、异常及 3 个分支，调用=CallExpression.finally, CallExpression.catch, CallExpression.then, listData。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04690 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template lines 1-73（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04691 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template line 2: v-bind:model-value
  - 基线：原表达式：visible；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04692 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template line 2: v-on:update:model-value
  - 基线：原表达式：$emit('update:visible', $event)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04693 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template line 4: v-slot:header
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04694 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template line 14: v-if:
  - 基线：原表达式：loading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04695 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template line 20: v-else-if:
  - 基线：原表达式：!dataList.length；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04696 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template line 25: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04697 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template line 27: v-bind:gutter
  - 基线：原表达式：12；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04698 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template line 28: v-bind:span
  - 基线：原表达式：disabledCount > 0 ? 8 : 12；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04699 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template line 34: v-bind:span
  - 基线：原表达式：disabledCount > 0 ? 8 : 12；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04700 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template line 40: v-if:
  - 基线：原表达式：disabledCount > 0；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04701 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template line 40: v-bind:span
  - 基线：原表达式：8；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04702 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template line 49: v-for:
  - 基线：原表达式：item in dataList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04703 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template line 49: v-bind:key
  - 基线：原表达式：item.dictCode；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04704 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template line 53: v-if:
  - 基线：原表达式：item.listClass && item.listClass !== 'default'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04705 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template line 53: v-bind:type
  - 基线：原表达式：item.listClass === 'primary' ? undefined : item.listClass；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04706 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template line 54: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04707 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template line 64: v-bind:type
  - 基线：原表达式：item.status === '0' ? 'success' : 'danger'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04708 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template interpolation line 7
  - 基线：原显示表达式：row.dictName
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04709 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template interpolation line 8
  - 基线：原显示表达式：row.dictType
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04710 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template interpolation line 30
  - 基线：原显示表达式：dataList.length
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04711 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template interpolation line 36
  - 基线：原显示表达式：normalCount
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04712 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template interpolation line 42
  - 基线：原显示表达式：disabledCount
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04713 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template interpolation line 53
  - 基线：原显示表达式：item.dictLabel
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04714 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template interpolation line 54
  - 基线：原显示表达式：item.dictLabel
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04715 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template interpolation line 59
  - 基线：原显示表达式：item.dictValue
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04716 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` template interpolation line 65
  - 基线：原显示表达式：item.status === '0' ? '正常' : '停用'
  - 去向：react-front/src/views/system/dict/detail.tsx
- I04717 `ruoyi-fastapi-frontend/src/views/system/dict/detail.vue` style[0] lines 111-202
  - 基线：保留全部选择器、声明和 url；lang=css, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/views/system/dict/detail.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
