# G206 src/layout/components/Sidebar/index.vue：完整能力

依赖：G000, G156, G204, G205, G224, G227, G228

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02191 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` lines 28-28 ImportDeclaration: 
  - 基线：源语句 sha256=6921dd99d1b9a22bd059b15740833c5da8046215bc2777abcfc560749481c611；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02192 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` lines 29-29 ImportDeclaration: 
  - 基线：源语句 sha256=22caf177eff8874ef88d9540fe96276e7daaf375bf3d02087f8b45b8b6ad5742；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02193 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` lines 30-30 ImportDeclaration: 
  - 基线：源语句 sha256=2889e171f5099c6e951bf66dac31ed6ec65613ee20d32a235ff5626fb300ca0e；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02194 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` lines 31-31 ImportDeclaration: 
  - 基线：源语句 sha256=b6ad1bf6c41f923901306683414efcc226cc2299d4a2d3ca4208a8af934a00cf；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02195 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` lines 32-32 ImportDeclaration: 
  - 基线：源语句 sha256=88996687f5ac2ffe958aa6952515839565c6f908d46ea4106fe92135e3f788d7；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02196 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` lines 33-33 ImportDeclaration: 
  - 基线：源语句 sha256=efbb342d84aefbc6dc4b206f290d81fe87a23b34796df1ad0da69cd6a90b7ea3；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02197 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` lines 35-35 VariableDeclaration: route
  - 基线：源语句 sha256=19ffaf888604ba2654aa25f29ba0210e96226ea7089e9e15dc5c05cf276b3a9f；保留返回、异常及 0 个分支，调用=useRoute。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02198 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` lines 36-36 VariableDeclaration: appStore
  - 基线：源语句 sha256=060bc36594e85646e5cc27ede11c88fb8230b9d84a9ac50cfd6e4bbef468bdf4；保留返回、异常及 0 个分支，调用=useAppStore。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02199 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` lines 37-37 VariableDeclaration: settingsStore
  - 基线：源语句 sha256=53647c4c620ff8d612232f46d116eb0d1e39a2943e0b2af620b068ca8e6d3ba3；保留返回、异常及 0 个分支，调用=useSettingsStore。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02200 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` lines 38-38 VariableDeclaration: permissionStore
  - 基线：源语句 sha256=8aea4ee78c3bc335fb25695e39a02e09a8551a4b638040cc30c3a575ef5ec2ed；保留返回、异常及 0 个分支，调用=usePermissionStore。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02201 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` lines 40-40 VariableDeclaration: sidebarRouters
  - 基线：源语句 sha256=35762d606aa16c1a4e0f6513c605d1fcd3de6d0c36e009bac77fe084d8b47c67；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02202 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` lines 41-41 VariableDeclaration: showLogo
  - 基线：源语句 sha256=77296823e3d9f87f6fbdf51118cc8ea80d01374444e000c257ae50034dc5c626；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02203 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` lines 42-42 VariableDeclaration: sideTheme
  - 基线：源语句 sha256=d60604e5b40937dc00b9859604d4b3e83c9d5adcaa9832c617d3ca1be5977b8d；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02204 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` lines 43-43 VariableDeclaration: theme
  - 基线：源语句 sha256=4151e7b9b3773f9a424ce1f499b146b014780f6c8359f951b275d448f3633def；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02205 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` lines 44-44 VariableDeclaration: isCollapse
  - 基线：源语句 sha256=6b4f2ff31a36becd479b03756f2f5d58412e4069536e3f8d4aa4e1520b499538；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02206 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` lines 47-52 VariableDeclaration: getMenuBackground
  - 基线：源语句 sha256=e1857340cf7b7b7d2d8c85d869245d1d379d7bf2190b1b997a484028c92e59fe；保留返回、异常及 4 个分支，调用=computed。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02207 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` lines 55-60 VariableDeclaration: getMenuTextColor
  - 基线：源语句 sha256=9b32dcc4ddc962696058661125d64e3a4854ba38cf60e56ca29a38677dd1f73d；保留返回、异常及 4 个分支，调用=computed。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02208 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` lines 62-68 VariableDeclaration: activeMenu
  - 基线：源语句 sha256=ff8f03d87c1a4fb7cb9f2e2053350f7bb9d644456d4fe395f9381f9c4064ab04；保留返回、异常及 3 个分支，调用=computed。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02209 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` template lines 1-25（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02210 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` template line 2: v-bind:class
  - 基线：原表达式：['sidebar-theme-wrapper', {'has-logo':showLogo}, sideTheme]；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02211 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` template line 3: v-if:
  - 基线：原表达式：showLogo；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02212 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` template line 3: v-bind:collapse
  - 基线：原表达式：isCollapse；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02213 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` template line 6: v-bind:default-active
  - 基线：原表达式：activeMenu；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02214 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` template line 7: v-bind:collapse
  - 基线：原表达式：isCollapse；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02215 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` template line 8: v-bind:background-color
  - 基线：原表达式：getMenuBackground；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02216 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` template line 9: v-bind:text-color
  - 基线：原表达式：getMenuTextColor；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02217 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` template line 10: v-bind:unique-opened
  - 基线：原表达式：true；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02218 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` template line 11: v-bind:active-text-color
  - 基线：原表达式：theme；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02219 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` template line 12: v-bind:collapse-transition
  - 基线：原表达式：false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02220 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` template line 14: v-bind:class
  - 基线：原表达式：sideTheme；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02221 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` template line 17: v-for:
  - 基线：原表达式：(route, index) in sidebarRouters；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02222 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` template line 18: v-bind:key
  - 基线：原表达式：route.path + index；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02223 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` template line 19: v-bind:item
  - 基线：原表达式：route；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02224 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` template line 20: v-bind:base-path
  - 基线：原表达式：route.path；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx
- I02225 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/index.vue` style[0] lines 71-104
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/layout/components/Sidebar/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
