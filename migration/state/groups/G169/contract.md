# G169 src/components/DictTag/index.vue：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01343 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` lines 29-29 VariableDeclaration: unmatchArray
  - 基线：源语句 sha256=d0b0b7aec24ebb28e88e129b910bb31ce397dbd797db88fccf6180c67dca44d0；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/DictTag/index.tsx
- I01344 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` lines 31-48 VariableDeclaration: props
  - 基线：源语句 sha256=9bbdcea58932d5a45d9deed6fbcfa591493e97fc5391ee96d9139f45a1b772c6；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/components/DictTag/index.tsx
- I01345 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` lines 50-54 VariableDeclaration: values
  - 基线：源语句 sha256=471b0b8434562c41a799350c5217c5e87169be66e41d1e88973cead526a45de5；保留返回、异常及 9 个分支，调用=computed, Array.isArray, props.value.map, CallExpression.split, String。
  - 去向：react-front/src/components/DictTag/index.tsx
- I01346 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` lines 56-69 VariableDeclaration: unmatch
  - 基线：源语句 sha256=31a5ac3d8efe8d3e428df347b7bb2ec2161798e0754709457d34e5142e34a063；保留返回、异常及 8 个分支，调用=computed, Array.isArray, values.value.forEach, props.options.some, unmatchArray.value.push。
  - 去向：react-front/src/components/DictTag/index.tsx
- I01347 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` lines 71-76 FunctionDeclaration: handleArray
  - 基线：源语句 sha256=63883d4d635e4dc5e7dc1cff55a83e3b2086d4dcf94ff71b4b3978c5b8bdbb08；保留返回、异常及 4 个分支，调用=array.reduce。
  - 去向：react-front/src/components/DictTag/index.tsx
- I01348 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` lines 78-80 FunctionDeclaration: isValueMatch
  - 基线：源语句 sha256=3315b1cfb469983bbd6b7195a0d8ca00119c8b7774b9036eb33c1078b9983cdc；保留返回、异常及 1 个分支，调用=values.value.some。
  - 去向：react-front/src/components/DictTag/index.tsx
- I01349 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` template lines 1-25（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/components/DictTag/index.tsx
- I01350 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` template line 3: v-for:
  - 基线：原表达式：(item, index) in options；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/DictTag/index.tsx
- I01351 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` template line 4: v-if:
  - 基线：原表达式：isValueMatch(item.value)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/DictTag/index.tsx
- I01352 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` template line 6: v-if:
  - 基线：原表达式：(item.elTagType == 'default' || item.elTagType == '') && (item.elTagClass == '' || item.elTagClass == null)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/DictTag/index.tsx
- I01353 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` template line 7: v-bind:key
  - 基线：原表达式：item.value；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/DictTag/index.tsx
- I01354 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` template line 8: v-bind:index
  - 基线：原表达式：index；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/DictTag/index.tsx
- I01355 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` template line 9: v-bind:class
  - 基线：原表达式：item.elTagClass；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/DictTag/index.tsx
- I01356 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` template line 12: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/DictTag/index.tsx
- I01357 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` template line 13: v-bind:disable-transitions
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/DictTag/index.tsx
- I01358 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` template line 14: v-bind:key
  - 基线：原表达式：item.value + ''；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/DictTag/index.tsx
- I01359 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` template line 15: v-bind:index
  - 基线：原表达式：index；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/DictTag/index.tsx
- I01360 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` template line 16: v-bind:type
  - 基线：原表达式：item.elTagType；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/DictTag/index.tsx
- I01361 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` template line 17: v-bind:class
  - 基线：原表达式：item.elTagClass；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/DictTag/index.tsx
- I01362 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` template line 21: v-if:
  - 基线：原表达式：unmatch && showValue；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/DictTag/index.tsx
- I01363 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` template interpolation line 10
  - 基线：原显示表达式：item.label + " "
  - 去向：react-front/src/components/DictTag/index.tsx
- I01364 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` template interpolation line 18
  - 基线：原显示表达式：item.label + " "
  - 去向：react-front/src/components/DictTag/index.tsx
- I01365 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` template interpolation line 22
  - 基线：原显示表达式：unmatchArray | handleArray
  - 去向：react-front/src/components/DictTag/index.tsx
- I01366 `ruoyi-fastapi-frontend/src/components/DictTag/index.vue` style[0] lines 83-87
  - 基线：保留全部选择器、声明和 url；lang=css, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/components/DictTag/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
