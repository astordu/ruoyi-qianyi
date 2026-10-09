# G196 src/layout/components/Copyright/index.vue：完整能力

依赖：G000, G228

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01929 `ruoyi-fastapi-frontend/src/layout/components/Copyright/index.vue` lines 8-8 ImportDeclaration: 
  - 基线：源语句 sha256=88996687f5ac2ffe958aa6952515839565c6f908d46ea4106fe92135e3f788d7；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/Copyright/index.tsx
- I01930 `ruoyi-fastapi-frontend/src/layout/components/Copyright/index.vue` lines 10-10 VariableDeclaration: settingsStore
  - 基线：源语句 sha256=53647c4c620ff8d612232f46d116eb0d1e39a2943e0b2af620b068ca8e6d3ba3；保留返回、异常及 0 个分支，调用=useSettingsStore。
  - 去向：react-front/src/layout/components/Copyright/index.tsx
- I01931 `ruoyi-fastapi-frontend/src/layout/components/Copyright/index.vue` lines 12-12 VariableDeclaration: visible
  - 基线：源语句 sha256=b8e13ec9f31f525bdd069c3fbc86707b28e11ae2516129c3cb89362bc0afd650；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/layout/components/Copyright/index.tsx
- I01932 `ruoyi-fastapi-frontend/src/layout/components/Copyright/index.vue` lines 13-13 VariableDeclaration: content
  - 基线：源语句 sha256=7ebf7d89417c03ebd2dd25cc29fdd6306edae28ebca4105541e42f84293bde2e；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/layout/components/Copyright/index.tsx
- I01933 `ruoyi-fastapi-frontend/src/layout/components/Copyright/index.vue` template lines 1-5（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/layout/components/Copyright/index.tsx
- I01934 `ruoyi-fastapi-frontend/src/layout/components/Copyright/index.vue` template line 2: v-if:
  - 基线：原表达式：visible；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/Copyright/index.tsx
- I01935 `ruoyi-fastapi-frontend/src/layout/components/Copyright/index.vue` template interpolation line 3
  - 基线：原显示表达式：content
  - 去向：react-front/src/layout/components/Copyright/index.tsx
- I01936 `ruoyi-fastapi-frontend/src/layout/components/Copyright/index.vue` style[0] lines 16-31
  - 基线：保留全部选择器、声明和 url；lang=css, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/layout/components/Copyright/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
