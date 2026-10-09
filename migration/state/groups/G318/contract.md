# G318 src/views/tool/build/DraggableItem.vue：完整能力

依赖：G000, G241

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I07845 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` lines 28-28 ImportDeclaration: 
  - 基线：源语句 sha256=69bbbdfe0713981a4ee41f1ce415b388fb708d0e342bd0cab1c2e656919ec594；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07846 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` lines 29-29 ImportDeclaration: 
  - 基线：源语句 sha256=19dac988290c48c5ea58721efa75a882449bd67f1b3860aebbacd65d0c131121；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07847 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` lines 31-39 VariableDeclaration: props
  - 基线：源语句 sha256=9872a0b7ab16755a1e93543389e42c1cc2b5c7226042561752777a1866241822；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07848 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` lines 40-40 VariableDeclaration: className
  - 基线：源语句 sha256=9e1edeb3a03140a503a1a9626b774c07a94eb22189e9aa617a30b01f87fafb25；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07849 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` lines 41-41 VariableDeclaration: draggableItemRef
  - 基线：源语句 sha256=502bcd3683de568e0d8dc94c74c35dcc58a2c89911b61ae1d14bef0e4ddf1499；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07850 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` lines 42-42 VariableDeclaration: emits
  - 基线：源语句 sha256=6d7de3f8b73a027b2977f29e471ff9bcdbf8e524ede5e4810c5de684ec287683；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07851 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` lines 44-46 FunctionDeclaration: activeItem
  - 基线：源语句 sha256=2f932ea9cc3dded65b0c127cadd00fd16f27a052e21893b7fd060b20b583f1c0；保留返回、异常及 0 个分支，调用=emits。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07852 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` lines 47-49 FunctionDeclaration: copyItem
  - 基线：源语句 sha256=17e832481f9a3b6cb566aaef437d712ed7777c6f9600aeb24447242fc5670e92；保留返回、异常及 1 个分支，调用=emits。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07853 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` lines 50-52 FunctionDeclaration: deleteItem
  - 基线：源语句 sha256=6a12ee635d8348f9363e543fd58936fdd5f5f354cf8803ad1f3feffc611c28fe；保留返回、异常及 1 个分支，调用=emits。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07854 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` lines 54-60 FunctionDeclaration: getComponentData
  - 基线：源语句 sha256=4ebd3240e1527686fa333d885c5fcdc817a5223b627861028281d5fdaf673405；保留返回、异常及 1 个分支，调用=。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07855 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` lines 62-67 ExpressionStatement: 
  - 基线：源语句 sha256=afb04133261a56769709f880d5d533fab5edc61ef1a7348b6e318f76f6abcd32；保留返回、异常及 3 个分支，调用=watch。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07856 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template lines 1-26（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07857 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 2: v-bind:span
  - 基线：原表达式：element.span；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07858 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 2: v-bind:class
  - 基线：原表达式：className；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07859 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 2: v-on:click
  - 基线：原表达式：activeItem(element)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07860 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 3: v-bind:label
  - 基线：原表达式：element.label；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07861 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 3: v-bind:label-width
  - 基线：原表达式：element.labelWidth ? element.labelWidth + 'px' : null；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07862 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 4: v-bind:required
  - 基线：原表达式：element.required；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07863 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 4: v-if:
  - 基线：原表达式：element.layout === 'colFormItem'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07864 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 5: v-bind:key
  - 基线：原表达式：element.tag；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07865 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 5: v-bind:conf
  - 基线：原表达式：element；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07866 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 5: v-model:
  - 基线：原表达式：element.defaultValue；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07867 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 7: v-bind:gutter
  - 基线：原表达式：element.gutter；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07868 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 7: v-bind:class
  - 基线：原表达式：element.class；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07869 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 7: v-on:click
  - 基线：原表达式：activeItem(element)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07870 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 7: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07871 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 9: v-bind:animation
  - 基线：原表达式：340；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07872 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 9: v-bind:list
  - 基线：原表达式：element.children；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07873 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 10: v-bind:component-data
  - 基线：原表达式：getComponentData()；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07874 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 11: v-slot:item
  - 基线：原表达式：scoped；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07875 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 12: v-bind:key
  - 基线：原表达式：scoped.element.renderKey；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07876 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 12: v-bind:drawing-list
  - 基线：原表达式：element.children；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07877 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 12: v-bind:element
  - 基线：原表达式：scoped.element；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07878 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 13: v-bind:index
  - 基线：原表达式：index；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07879 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 13: v-bind:active-id
  - 基线：原表达式：activeId；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07880 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 13: v-bind:form-conf
  - 基线：原表达式：formConf；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07881 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 13: v-on:activeItem
  - 基线：原表达式：activeItem(scoped.element)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07882 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 14: v-on:copyItem
  - 基线：原表达式：copyItem(scoped.element, element.children)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07883 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 15: v-on:deleteItem
  - 基线：原表达式：deleteItem(scoped.index, element.children)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07884 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 19: v-on:click
  - 基线：原表达式：copyItem(element)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07885 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template line 22: v-on:click
  - 基线：原表达式：deleteItem(index)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx
- I07886 `ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue` template interpolation line 8
  - 基线：原显示表达式：element.componentName
  - 去向：react-front/src/views/tool/build/DraggableItem.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
