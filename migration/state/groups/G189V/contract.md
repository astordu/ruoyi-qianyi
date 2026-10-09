# G189V src/components/TreePanel/index.vue：页面渲染、事件接线和生命周期

依赖：G000, G189, G189F014, G189F018, G189F019, G189F020, G189F021, G189F022, G189F023, G189F024, G189F025, G189F026, G189F027, G189F028, G189F029, G189F030, G189F031, G189F032, G189F033, G189F034, G189F035, G189F036, G189F037, G189F038, G189F039, G189F040, G189F041, G189F042, G189F043, G189F044, G189F045, G189F046, G189F047

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01847 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template lines 1-72（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01848 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 2: v-bind:class
  - 基线：原表达式：{ collapsed: collapsed, resizing: isResizing, 'no-initial-transition': isLoadingFromStorage}；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01849 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 2: v-bind:style
  - 基线：原表达式：{ width: sidebarWidth + 'px' }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01850 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 4: v-if:
  - 基线：原表达式：!collapsed；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01851 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 4: v-on:mousedown
  - 基线：原表达式：startResize；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01852 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 4: v-on:touchstart
  - 基线：原表达式：startResize；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01853 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 4: v-bind:class
  - 基线：原表达式：{ active: isResizing }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01854 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 6: v-show:
  - 基线：原表达式：!collapsed；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01855 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 7: v-bind:is
  - 基线：原表达式：titleIcon；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01856 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 9: v-show:
  - 基线：原表达式：!collapsed；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01857 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 10: v-bind:content
  - 基线：原表达式：isExpandedAll ? '收起全部' : '展开全部'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01858 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 11: v-on:click
  - 基线：原表达式：toggleExpandAll；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01859 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 12: v-if:
  - 基线：原表达式：isExpandedAll；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01860 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 13: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01861 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 17: v-on:click
  - 基线：原表达式：handleRefresh；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01862 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 25: v-bind:content
  - 基线：原表达式：collapsed ? '展开' : '收起'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01863 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 26: v-on:click
  - 基线：原表达式：toggleCollapsed；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01864 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 27: v-if:
  - 基线：原表达式：collapsed；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01865 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 28: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01866 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 33: v-show:
  - 基线：原表达式：!collapsed；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01867 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 33: v-if:
  - 基线：原表达式：showSearch；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01868 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 34: v-model:
  - 基线：原表达式：searchKeyword；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01869 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 34: v-bind:placeholder
  - 基线：原表达式：searchPlaceholder；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01870 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 35: v-slot:prefix
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01871 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 41: v-show:
  - 基线：原表达式：!collapsed；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01872 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 44: v-bind:data
  - 基线：原表达式：treeData；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01873 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 45: v-bind:props
  - 基线：原表达式：treeProps；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01874 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 46: v-bind:expand-on-click-node
  - 基线：原表达式：expandOnClickNode；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01875 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 47: v-bind:filter-node-method
  - 基线：原表达式：filterNodeMethod；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01876 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 48: v-bind:default-expand-all
  - 基线：原表达式：defaultExpandAll；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01877 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 49: v-bind:default-expanded-keys
  - 基线：原表达式：defaultExpandedKeys；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01878 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 50: v-bind:node-key
  - 基线：原表达式：nodeKey；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01879 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 51: v-bind:check-strictly
  - 基线：原表达式：checkStrictly；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01880 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 52: v-bind:show-checkbox
  - 基线：原表达式：showCheckbox；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01881 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 53: v-on:node-click
  - 基线：原表达式：onNodeClick；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01882 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 54: v-on:check
  - 基线：原表达式：onCheck；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01883 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 55: v-on:node-expand
  - 基线：原表达式：onNodeExpand；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01884 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 56: v-on:node-collapse
  - 基线：原表达式：onNodeCollapse；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01885 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 58: v-slot:default
  - 基线：原表达式：{ node, data }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01886 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 59: v-bind:node
  - 基线：原表达式：node；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01887 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 59: v-bind:data
  - 基线：原表达式：data；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01888 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 62: v-if:
  - 基线：原表达式：data.children && data.children.length；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01889 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 63: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01890 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template line 65: v-bind:title
  - 基线：原表达式：node.label；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01891 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template interpolation line 7
  - 基线：原显示表达式：title
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01892 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` template interpolation line 65
  - 基线：原显示表达式：node.label
  - 去向：react-front/src/components/TreePanel/index.tsx
- I01893 `ruoyi-fastapi-frontend/src/components/TreePanel/index.vue` style[0] lines 550-756
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/components/TreePanel/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
