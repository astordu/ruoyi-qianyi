# G208V src/layout/components/TagsView/index.vue：页面渲染、事件接线和生命周期

依赖：G000, G187, G207, G208, G208F018, G208F019, G208F020, G208F021, G208F022, G208F023, G208F024, G208F030, G208F031, G208F032, G208F033, G208F034, G208F035, G208F036, G208F037, G208F038, G208F039, G208F040, G208F041, G208F042, G208F043, G208F044, G208F045, G208F046, G208F047, G208F048, G208F049, G208F050, G208F051, G208F052, G208F053, G208F054, G227, G228, G229, G250

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02302 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template lines 1-66（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02303 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 2: v-bind:class
  - 基线：原表达式：{ 'tags-view-container--chrome': tagsViewStyle === 'chrome' }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02304 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 4: v-bind:class
  - 基线：原表达式：{ disabled: !canScrollLeft }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02305 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 4: v-on:click
  - 基线：原表达式：scrollLeft；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02306 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 9: v-on:scroll
  - 基线：原表达式：handleScroll；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02307 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 9: v-on:update-arrows
  - 基线：原表达式：updateArrowState；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02308 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 11: v-for:
  - 基线：原表达式：tag in visitedViews；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02309 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 12: v-bind:key
  - 基线：原表达式：tag.path；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02310 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 13: v-bind:data-path
  - 基线：原表达式：tag.path；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02311 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 14: v-bind:class
  - 基线：原表达式：{ 'active': isActive(tag), 'has-icon': tagsIcon }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02312 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 15: v-bind:to
  - 基线：原表达式：{ path: tag.path, query: tag.query, fullPath: tag.fullPath }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02313 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 17: v-bind:style
  - 基线：原表达式：tagActiveStyle(tag)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02314 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 18: v-on:click
  - 基线：原表达式：!isAffix(tag) ? closeSelectedTag(tag) : ''；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02315 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 19: v-on:contextmenu
  - 基线：原表达式：openMenu(tag, $event)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02316 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 21: v-if:
  - 基线：原表达式：tagsIcon && tag.meta && tag.meta.icon && tag.meta.icon !== '#'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02317 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 21: v-bind:icon-class
  - 基线：原表达式：tag.meta.icon；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02318 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 23: v-if:
  - 基线：原表达式：!isAffix(tag)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02319 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 23: v-on:click
  - 基线：原表达式：closeSelectedTag(tag)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02320 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 30: v-bind:class
  - 基线：原表达式：{ disabled: !canScrollRight }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02321 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 30: v-on:click
  - 基线：原表达式：scrollRight；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02322 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 35: v-on:command
  - 基线：原表达式：handleDropdownCommand；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02323 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 39: v-slot:dropdown
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02324 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 41: v-if:
  - 基线：原表达式：!isAffix(selectedDropdownTag)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02325 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 43: v-bind:disabled
  - 基线：原表达式：isFirstView()；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02326 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 44: v-bind:disabled
  - 基线：原表达式：isLastView()；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02327 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 52: v-on:click
  - 基线：原表达式：refreshSelectedTag(selectedDropdownTag)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02328 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 57: v-show:
  - 基线：原表达式：visible；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02329 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 57: v-bind:style
  - 基线：原表达式：{ left: left + 'px', top: top + 'px' }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02330 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 58: v-on:click
  - 基线：原表达式：refreshSelectedTag(selectedTag)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02331 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 59: v-if:
  - 基线：原表达式：!isAffix(selectedTag)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02332 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 59: v-on:click
  - 基线：原表达式：closeSelectedTag(selectedTag)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02333 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 60: v-on:click
  - 基线：原表达式：closeOthersTags；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02334 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 61: v-if:
  - 基线：原表达式：!isFirstView()；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02335 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 61: v-on:click
  - 基线：原表达式：closeLeftTags；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02336 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 62: v-if:
  - 基线：原表达式：!isLastView()；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02337 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 62: v-on:click
  - 基线：原表达式：closeRightTags；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02338 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template line 63: v-on:click
  - 基线：原表达式：closeAllTags(selectedTag)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02339 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` template interpolation line 22
  - 基线：原显示表达式：tag.title
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02340 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` style[0] lines 321-585
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/layout/components/TagsView/index.tsx
- I02341 `ruoyi-fastapi-frontend/src/layout/components/TagsView/index.vue` style[1] lines 587-661
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=False；原样式选择器在 source-audit.json。
  - 去向：react-front/src/layout/components/TagsView/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
