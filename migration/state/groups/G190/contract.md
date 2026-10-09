# G190 src/components/iFrame/index.vue：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01894 `ruoyi-fastapi-frontend/src/components/iFrame/index.vue` lines 12-17 VariableDeclaration: props
  - 基线：源语句 sha256=b97062c08e274f137fcf8bea42cf0d7c9bd4f746ab1808e19d6e70881d159365；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/components/iFrame/index.tsx
- I01895 `ruoyi-fastapi-frontend/src/components/iFrame/index.vue` lines 19-19 VariableDeclaration: height
  - 基线：源语句 sha256=78beb0caadfe6d355c72553d36bed68936db9a3ddf6c299d2717c65acb5c4fc6；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/iFrame/index.tsx
- I01896 `ruoyi-fastapi-frontend/src/components/iFrame/index.vue` lines 20-20 VariableDeclaration: loading
  - 基线：源语句 sha256=5415ee241f95eb9cfef5170fff01a1c08aa550e8c765197630c087d46cc09640；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/iFrame/index.tsx
- I01897 `ruoyi-fastapi-frontend/src/components/iFrame/index.vue` lines 21-21 VariableDeclaration: url
  - 基线：源语句 sha256=08eaeaa94b16d44dedf548fc8bbbc7385419bc829c5ac4e2ff0f6a16cf0f678a；保留返回、异常及 0 个分支，调用=computed。
  - 去向：react-front/src/components/iFrame/index.tsx
- I01898 `ruoyi-fastapi-frontend/src/components/iFrame/index.vue` lines 23-30 ExpressionStatement: temp
  - 基线：源语句 sha256=d3ddc08057d5b7440632831df57a65fa952952ec14bd64a06a505e752891f137；保留返回、异常及 0 个分支，调用=onMounted, setTimeout。
  - 去向：react-front/src/components/iFrame/index.tsx
- I01899 `ruoyi-fastapi-frontend/src/components/iFrame/index.vue` template lines 1-9（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/components/iFrame/index.tsx
- I01900 `ruoyi-fastapi-frontend/src/components/iFrame/index.vue` template line 2: v-loading:
  - 基线：原表达式：loading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/iFrame/index.tsx
- I01901 `ruoyi-fastapi-frontend/src/components/iFrame/index.vue` template line 2: v-bind:style
  - 基线：原表达式：'height:' + height；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/iFrame/index.tsx
- I01902 `ruoyi-fastapi-frontend/src/components/iFrame/index.vue` template line 4: v-bind:src
  - 基线：原表达式：url；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/iFrame/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
