# G291 src/views/system/file/components/FileStatistics.vue：完整能力

依赖：G000, G294

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I05417 `ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue` lines 93-100 ImportDeclaration: 
  - 基线：源语句 sha256=b09230b63c89181e9dda768a5b2f8372dc4356207fd38dc1766c361a35b15540；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/FileStatistics.tsx
- I05418 `ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue` lines 101-101 ImportDeclaration: 
  - 基线：源语句 sha256=87fb0cfcdb7f5235aec4af3e73d3d63d1c863744216f1de5bb59af890dd52fdb；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/FileStatistics.tsx
- I05419 `ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue` lines 103-108 VariableDeclaration: props
  - 基线：源语句 sha256=d16e6788ff0599bb8ed11c8a7ed5c99a39dd7e59123b9ac4ce31b4b36f5dc913；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/views/system/file/components/FileStatistics.tsx
- I05420 `ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue` lines 110-115 FunctionDeclaration: formatPercentage
  - 基线：源语句 sha256=d2fba807d6e7b58629478d38584615f74ecdea0a9ec6cdf670c4d737f9133799；保留返回、异常及 6 个分支，调用=Number, percentage.toFixed。
  - 去向：react-front/src/views/system/file/components/FileStatistics.tsx
- I05421 `ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue` template lines 1-90（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/system/file/components/FileStatistics.tsx
- I05422 `ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue` template interpolation line 14
  - 基线：原显示表达式：stats.totalCount
  - 去向：react-front/src/views/system/file/components/FileStatistics.tsx
- I05423 `ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue` template interpolation line 19
  - 基线：原显示表达式：stats.activeCount
  - 去向：react-front/src/views/system/file/components/FileStatistics.tsx
- I05424 `ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue` template interpolation line 20
  - 基线：原显示表达式：stats.deletedCount
  - 去向：react-front/src/views/system/file/components/FileStatistics.tsx
- I05425 `ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue` template interpolation line 28
  - 基线：原显示表达式：formatFileSize(stats.totalSize)
  - 去向：react-front/src/views/system/file/components/FileStatistics.tsx
- I05426 `ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue` template interpolation line 41
  - 基线：原显示表达式：formatFileSize(stats.publicSize)
  - 去向：react-front/src/views/system/file/components/FileStatistics.tsx
- I05427 `ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue` template interpolation line 46
  - 基线：原显示表达式：formatPercentage(stats.publicSize)
  - 去向：react-front/src/views/system/file/components/FileStatistics.tsx
- I05428 `ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue` template interpolation line 54
  - 基线：原显示表达式：formatFileSize(stats.privateSize)
  - 去向：react-front/src/views/system/file/components/FileStatistics.tsx
- I05429 `ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue` template interpolation line 59
  - 基线：原显示表达式：formatPercentage(stats.privateSize)
  - 去向：react-front/src/views/system/file/components/FileStatistics.tsx
- I05430 `ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue` template interpolation line 67
  - 基线：原显示表达式：stats.expiredCount
  - 去向：react-front/src/views/system/file/components/FileStatistics.tsx
- I05431 `ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue` template interpolation line 72
  - 基线：原显示表达式：stats.retentionExpiringCount
  - 去向：react-front/src/views/system/file/components/FileStatistics.tsx
- I05432 `ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue` template interpolation line 80
  - 基线：原显示表达式：stats.aclExpiringCount
  - 去向：react-front/src/views/system/file/components/FileStatistics.tsx
- I05433 `ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue` style[0] lines 118-272
  - 基线：保留全部选择器、声明和 url；lang=css, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/views/system/file/components/FileStatistics.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
