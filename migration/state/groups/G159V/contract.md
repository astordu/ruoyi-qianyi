# G159V src/components/BusinessFileUpload/index.vue：页面渲染、事件接线和生命周期

依赖：G000, G159, G159F012, G159F013, G159F014, G159F015, G159F016, G159F017, G159F018, G159F019, G159F020, G159F021, G159F022, G159F023, G159F024, G159F025, G159F026, G159F027, G159F028, G159F029, G159F030, G159F031, G249

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00831 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template lines 1-103（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00832 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 4: v-if:
  - 基线：原表达式：!disabled；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00833 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 7: v-bind:show-file-list
  - 基线：原表达式：false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00834 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 8: v-bind:before-upload
  - 基线：原表达式：handleBeforeUpload；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00835 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 9: v-bind:http-request
  - 基线：原表达式：handleUploadRequest；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00836 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 10: v-bind:on-success
  - 基线：原表达式：handleUploadSuccess；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00837 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 11: v-bind:on-error
  - 基线：原表达式：handleUploadError；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00838 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 15: v-if:
  - 基线：原表达式：showTip && !disabled；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00839 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 17: v-if:
  - 基线：原表达式：fileSize；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00840 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 20: v-if:
  - 基线：原表达式：fileType.length；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00841 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 27: v-if:
  - 基线：原表达式：fileList.length；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00842 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 32: v-for:
  - 基线：原表达式：file in fileList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00843 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 33: v-bind:key
  - 基线：原表达式：file.fileId；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00844 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 37: v-bind:title
  - 基线：原表达式：file.name；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00845 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 44: v-bind:underline
  - 基线：原表达式：false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00846 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 46: v-on:click
  - 基线：原表达式：handleDownload(file)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00847 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 51: v-if:
  - 基线：原表达式：!disabled；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00848 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 52: v-bind:underline
  - 基线：原表达式：false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00849 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 54: v-on:click
  - 基线：原表达式：handleDelete(file.fileId)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00850 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 63: v-if:
  - 基线：原表达式：pendingFileList.length；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00851 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 67: v-for:
  - 基线：原表达式：file in pendingFileList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00852 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 68: v-bind:key
  - 基线：原表达式：file.uid；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00853 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 72: v-bind:title
  - 基线：原表达式：file.name；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00854 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 75: v-if:
  - 基线：原表达式：file.status === 'uploading'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00855 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 78: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00856 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 78: v-bind:content
  - 基线：原表达式：file.error；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00857 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 82: v-if:
  - 基线：原表达式：file.status === 'failed'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00858 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 84: v-if:
  - 基线：原表达式：!disabled；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00859 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 85: v-bind:underline
  - 基线：原表达式：false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00860 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 87: v-on:click
  - 基线：原表达式：handleRetry(file)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00861 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 92: v-if:
  - 基线：原表达式：!disabled；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00862 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 93: v-bind:underline
  - 基线：原表达式：false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00863 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template line 95: v-on:click
  - 基线：原表达式：handleRemoveFailed(file.uid)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00864 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template interpolation line 18
  - 基线：原显示表达式：fileSize
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00865 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template interpolation line 21
  - 基线：原显示表达式：fileType.join("/")
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00866 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template interpolation line 23
  - 基线：原显示表达式：limit
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00867 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template interpolation line 37
  - 基线：原显示表达式：file.name
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00868 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` template interpolation line 72
  - 基线：原显示表达式：file.name
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx
- I00869 `ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue` style[0] lines 515-565
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/components/BusinessFileUpload/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
