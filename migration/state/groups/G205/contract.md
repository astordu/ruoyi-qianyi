# G205 src/layout/components/Sidebar/SidebarItem.vue：完整能力

依赖：G000, G187, G203, G250, G256

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02159 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` lines 31-31 ImportDeclaration: 
  - 基线：源语句 sha256=f66a8e181b51bf3ddb875b67d0b529175756e08ffaf5d1611f25438e9344d850；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02160 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` lines 32-32 ImportDeclaration: 
  - 基线：源语句 sha256=5c274263924ae94fe8bd63a65907a318d38ff4370fb39fca7a0e95643d533ad3；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02161 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` lines 33-33 ImportDeclaration: 
  - 基线：源语句 sha256=8a7cf6589682c7c62a14023574b67d2639dd45e581c104ac2ed99db272c6d63e；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02162 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` lines 35-49 VariableDeclaration: props
  - 基线：源语句 sha256=35c56f7ba7303311404436705a59559e8f118a58d9ad50e6050dae6e3c76ffc7；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02163 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` lines 51-51 VariableDeclaration: onlyOneChild
  - 基线：源语句 sha256=1670a0f12838d14330e91054ef79f0ad7cf3b27b7239bb1404c40808df6fdf07；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02164 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` lines 53-77 FunctionDeclaration: hasOneShowingChild
  - 基线：源语句 sha256=b65cbecca8debb40a15a8e5d3537afc97dbf69935a38248a01dc6f036db6b49e；保留返回、异常及 9 个分支，调用=children.filter。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02165 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` lines 77-77 EmptyStatement: 
  - 基线：源语句 sha256=41b805ea7ac014e23556e98bb374702a08344268f92489a02f0880849394a1e4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02166 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` lines 79-91 FunctionDeclaration: resolvePath
  - 基线：源语句 sha256=ddbf1b64be314ebbdd1b3e064db3467544e5854e6f32c67d681f9d2831c6314e；保留返回、异常及 7 个分支，调用=isExternal, JSON.parse, getNormalPath。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02167 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` lines 93-99 FunctionDeclaration: hasTitle
  - 基线：源语句 sha256=8cd27ec9efc4a76c723c9fb72e1ffee5b5c49fba6c756f47abd2e4d061779c6e；保留返回、异常及 3 个分支，调用=。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02168 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template lines 1-28（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02169 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template line 2: v-if:
  - 基线：原表达式：!item.hidden；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02170 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template line 3: v-if:
  - 基线：原表达式：hasOneShowingChild(item.children, item) && (!onlyOneChild.children || onlyOneChild.noShowingChildren) && !item.alwaysShow；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02171 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template line 4: v-if:
  - 基线：原表达式：onlyOneChild.meta；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02172 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template line 4: v-bind:to
  - 基线：原表达式：resolvePath(onlyOneChild.path, onlyOneChild.query)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02173 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template line 5: v-bind:index
  - 基线：原表达式：resolvePath(onlyOneChild.path)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02174 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template line 5: v-bind:class
  - 基线：原表达式：{ 'submenu-title-noDropdown': !isNest }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02175 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template line 6: v-bind:icon-class
  - 基线：原表达式：onlyOneChild.meta.icon || (item.meta && item.meta.icon)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02176 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template line 7: v-slot:title
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02177 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template line 7: v-bind:title
  - 基线：原表达式：hasTitle(onlyOneChild.meta.title)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02178 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template line 12: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02179 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template line 12: v-bind:index
  - 基线：原表达式：resolvePath(item.path)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02180 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template line 13: v-if:
  - 基线：原表达式：item.meta；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02181 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template line 13: v-slot:title
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02182 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template line 14: v-bind:icon-class
  - 基线：原表达式：item.meta && item.meta.icon；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02183 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template line 15: v-bind:title
  - 基线：原表达式：hasTitle(item.meta.title)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02184 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template line 19: v-for:
  - 基线：原表达式：(child, index) in item.children；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02185 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template line 20: v-bind:key
  - 基线：原表达式：child.path + index；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02186 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template line 21: v-bind:is-nest
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02187 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template line 22: v-bind:item
  - 基线：原表达式：child；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02188 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template line 23: v-bind:base-path
  - 基线：原表达式：resolvePath(child.path)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02189 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template interpolation line 7
  - 基线：原显示表达式：onlyOneChild.meta.title
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx
- I02190 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/SidebarItem.vue` template interpolation line 15
  - 基线：原显示表达式：item.meta.title
  - 去向：react-front/src/layout/components/Sidebar/SidebarItem.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
