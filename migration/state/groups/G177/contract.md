# G177 src/components/ImagePreview/index.vue：完整能力

依赖：G000, G256

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01580 `ruoyi-fastapi-frontend/src/components/ImagePreview/index.vue` lines 18-18 ImportDeclaration: 
  - 基线：源语句 sha256=9ba7d673f7e7d40d378be5cb01aa397488015eb4f529f69c55058d6e9117ef53；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/ImagePreview/index.tsx
- I01581 `ruoyi-fastapi-frontend/src/components/ImagePreview/index.vue` lines 20-33 VariableDeclaration: props
  - 基线：源语句 sha256=7f8f22cd08adb74c26e737aa877ea7834b9eec5d5e79e8c3614d9da09fd2f1b2；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/components/ImagePreview/index.tsx
- I01582 `ruoyi-fastapi-frontend/src/components/ImagePreview/index.vue` lines 35-44 VariableDeclaration: realSrc
  - 基线：源语句 sha256=b55a87f5a71089595dad79785848f85dd99ce1043f8dc875f439ee42aa2de2a6；保留返回、异常及 5 个分支，调用=computed, props.src.split, isExternal。
  - 去向：react-front/src/components/ImagePreview/index.tsx
- I01583 `ruoyi-fastapi-frontend/src/components/ImagePreview/index.vue` lines 46-59 VariableDeclaration: realSrcList
  - 基线：源语句 sha256=b62c2e6c314ea3f243f08b1cebea65ffea007a2ec28de33e6aced2c29aad1490；保留返回、异常及 6 个分支，调用=computed, props.src.split, real_src_list.forEach, isExternal, srcList.push。
  - 去向：react-front/src/components/ImagePreview/index.tsx
- I01584 `ruoyi-fastapi-frontend/src/components/ImagePreview/index.vue` lines 61-63 VariableDeclaration: realWidth
  - 基线：源语句 sha256=7e5b6a35fb44a8d423a959b4006372359376f59555e080481139866f864552e8；保留返回、异常及 1 个分支，调用=computed。
  - 去向：react-front/src/components/ImagePreview/index.tsx
- I01585 `ruoyi-fastapi-frontend/src/components/ImagePreview/index.vue` lines 65-67 VariableDeclaration: realHeight
  - 基线：源语句 sha256=1d8fbe45697db47320246780264830b729b5822f5022569dcdea5577067a750f；保留返回、异常及 1 个分支，调用=computed。
  - 去向：react-front/src/components/ImagePreview/index.tsx
- I01586 `ruoyi-fastapi-frontend/src/components/ImagePreview/index.vue` template lines 1-15（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/components/ImagePreview/index.tsx
- I01587 `ruoyi-fastapi-frontend/src/components/ImagePreview/index.vue` template line 3: v-bind:src
  - 基线：原表达式：`${realSrc}`；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImagePreview/index.tsx
- I01588 `ruoyi-fastapi-frontend/src/components/ImagePreview/index.vue` template line 5: v-bind:style
  - 基线：原表达式：`width:${realWidth};height:${realHeight};`；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImagePreview/index.tsx
- I01589 `ruoyi-fastapi-frontend/src/components/ImagePreview/index.vue` template line 6: v-bind:preview-src-list
  - 基线：原表达式：realSrcList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImagePreview/index.tsx
- I01590 `ruoyi-fastapi-frontend/src/components/ImagePreview/index.vue` template line 9: v-slot:error
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/ImagePreview/index.tsx
- I01591 `ruoyi-fastapi-frontend/src/components/ImagePreview/index.vue` style[0] lines 70-92
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/components/ImagePreview/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
