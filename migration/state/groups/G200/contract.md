# G200 src/layout/components/InnerLink/index.vue：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02012 `ruoyi-fastapi-frontend/src/layout/components/InnerLink/index.vue` lines 14-22 VariableDeclaration: props
  - 基线：源语句 sha256=d98116c7198b89f21e4a97a082871304af35c31684f0d67e9d88843ef4a09eb9；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/layout/components/InnerLink/index.tsx
- I02013 `ruoyi-fastapi-frontend/src/layout/components/InnerLink/index.vue` lines 24-24 VariableDeclaration: loading
  - 基线：源语句 sha256=5415ee241f95eb9cfef5170fff01a1c08aa550e8c765197630c087d46cc09640；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/InnerLink/index.tsx
- I02014 `ruoyi-fastapi-frontend/src/layout/components/InnerLink/index.vue` lines 25-25 VariableDeclaration: height
  - 基线：源语句 sha256=c08af6a82c3b45e9c126e341c2b9bf17472c4ea6da4b7dfd60f08f4dda663829；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/InnerLink/index.tsx
- I02015 `ruoyi-fastapi-frontend/src/layout/components/InnerLink/index.vue` lines 26-26 VariableDeclaration: iframeRef
  - 基线：源语句 sha256=95d9a4442f8a84b09bc7862bb8b64dbe59c516463dd201ec71136985c46c70a0；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/InnerLink/index.tsx
- I02016 `ruoyi-fastapi-frontend/src/layout/components/InnerLink/index.vue` lines 28-34 ExpressionStatement: 
  - 基线：源语句 sha256=d552e62310c57f1af4e85ef70984dac22a8cfc2d73abec8d36a87240da9d4203；保留返回、异常及 1 个分支，调用=onMounted。
  - 去向：react-front/src/layout/components/InnerLink/index.tsx
- I02017 `ruoyi-fastapi-frontend/src/layout/components/InnerLink/index.vue` template lines 1-11（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/layout/components/InnerLink/index.tsx
- I02018 `ruoyi-fastapi-frontend/src/layout/components/InnerLink/index.vue` template line 2: v-bind:style
  - 基线：原表达式：'height:' + height；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/InnerLink/index.tsx
- I02019 `ruoyi-fastapi-frontend/src/layout/components/InnerLink/index.vue` template line 2: v-loading:
  - 基线：原表达式：loading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/InnerLink/index.tsx
- I02020 `ruoyi-fastapi-frontend/src/layout/components/InnerLink/index.vue` template line 4: v-bind:id
  - 基线：原表达式：iframeId；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/InnerLink/index.tsx
- I02021 `ruoyi-fastapi-frontend/src/layout/components/InnerLink/index.vue` template line 6: v-bind:src
  - 基线：原表达式：src；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/InnerLink/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
