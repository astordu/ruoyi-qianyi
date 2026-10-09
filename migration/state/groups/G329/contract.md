# G329 src/views/tool/swagger/index.vue：完整能力

依赖：G000, G190

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I08705 `ruoyi-fastapi-frontend/src/views/tool/swagger/index.vue` lines 6-6 ImportDeclaration: 
  - 基线：源语句 sha256=45dcbeadd27b2911f7afa791c0db7892441564d394da4b28741d4e39692866cd；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/tool/swagger/index.tsx
- I08706 `ruoyi-fastapi-frontend/src/views/tool/swagger/index.vue` lines 8-8 VariableDeclaration: url
  - 基线：源语句 sha256=8fef4430da2e23b3417ff94564ab00294c49c79de2d3cbda821c4a7fc50832e0；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/tool/swagger/index.tsx
- I08707 `ruoyi-fastapi-frontend/src/views/tool/swagger/index.vue` template lines 1-3（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/tool/swagger/index.tsx
- I08708 `ruoyi-fastapi-frontend/src/views/tool/swagger/index.vue` template line 2: v-model:src
  - 基线：原表达式：url；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/tool/swagger/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
