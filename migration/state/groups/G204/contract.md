# G204 src/layout/components/Sidebar/Logo.vue：完整能力

依赖：G000, G148, G156, G228

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02138 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` lines 17-17 ImportDeclaration: 
  - 基线：源语句 sha256=211709ea2c25dea8500c5402a39791f1a1cde850bc1280331ebf8bf58f3935d2；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx
- I02139 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` lines 18-18 ImportDeclaration: 
  - 基线：源语句 sha256=88996687f5ac2ffe958aa6952515839565c6f908d46ea4106fe92135e3f788d7；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx
- I02140 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` lines 19-19 ImportDeclaration: 
  - 基线：源语句 sha256=2889e171f5099c6e951bf66dac31ed6ec65613ee20d32a235ff5626fb300ca0e；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx
- I02141 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` lines 21-26 ExpressionStatement: 
  - 基线：源语句 sha256=cca7c42b7d2c70f07d663f527967b25b8b264daed2fddc6a73006327b74514d6；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx
- I02142 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` lines 28-28 VariableDeclaration: title
  - 基线：源语句 sha256=02222f0009b239b60ede837919ce88126a7b40cb72e40af1c600484384a02e71；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx
- I02143 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` lines 29-29 VariableDeclaration: settingsStore
  - 基线：源语句 sha256=3604ebb18e2cd66f7a29e27607556d37b538f1a7beca03dcf6e3c4403535140f；保留返回、异常及 0 个分支，调用=useSettingsStore。
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx
- I02144 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` lines 30-30 VariableDeclaration: sideTheme
  - 基线：源语句 sha256=d60604e5b40937dc00b9859604d4b3e83c9d5adcaa9832c617d3ca1be5977b8d；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx
- I02145 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` lines 33-41 VariableDeclaration: getLogoBackground
  - 基线：源语句 sha256=f96ed269bda286e20df09cae2afc9c80a655e7a86252c4ab4d9a6384bd8dd283；保留返回、异常及 6 个分支，调用=computed。
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx
- I02146 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` lines 44-52 VariableDeclaration: getLogoTextColor
  - 基线：源语句 sha256=7421a57f11c39984704a3a3653765a7b91a4de764d9cf030d9e9a104f7c339c0；保留返回、异常及 6 个分支，调用=computed。
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx
- I02147 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` template lines 1-14（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx
- I02148 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` template line 2: v-bind:class
  - 基线：原表达式：{ 'collapse': collapse }；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx
- I02149 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` template line 4: v-if:
  - 基线：原表达式：collapse；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx
- I02150 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` template line 5: v-if:
  - 基线：原表达式：logo；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx
- I02151 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` template line 5: v-bind:src
  - 基线：原表达式：logo；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx
- I02152 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` template line 6: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx
- I02153 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` template line 8: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx
- I02154 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` template line 9: v-if:
  - 基线：原表达式：logo；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx
- I02155 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` template line 9: v-bind:src
  - 基线：原表达式：logo；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx
- I02156 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` template interpolation line 6
  - 基线：原显示表达式：title
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx
- I02157 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` template interpolation line 10
  - 基线：原显示表达式：title
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx
- I02158 `ruoyi-fastapi-frontend/src/layout/components/Sidebar/Logo.vue` style[0] lines 55-102
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/layout/components/Sidebar/Logo.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
