# G285 src/views/system/file/components/FileDetailDialog.vue：完整能力

依赖：G000, G294

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I05000 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` lines 105-110 ImportDeclaration: 
  - 基线：源语句 sha256=dee1d922e249323ce222d8a080467a428febd2cf44b81001caec87d5e9792a70；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05001 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` lines 112-117 ExpressionStatement: 
  - 基线：源语句 sha256=19e2684aee2f502212c2f10180c68c5999a9295db02bf3261ec2469d2d45930a；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05002 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` lines 119-119 VariableDeclaration: emit
  - 基线：源语句 sha256=06385257fe856c63f1cd639349de6f5bcd28a1872634153802462c3a0f19b49d；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05003 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` lines 120-123 VariableDeclaration: open
  - 基线：源语句 sha256=2a4f8eeb3f764d71b00c9a8997021c975d613f6a27b00946b76fda216f07ecee；保留返回、异常及 0 个分支，调用=defineModel。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05004 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` lines 125-143 FunctionDeclaration: uploaderPermissionLabel
  - 基线：源语句 sha256=3728960c676e723fea581b14b619d0d818437f45ce028571925ee8737be02948；保留返回、异常及 10 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05005 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` lines 145-153 FunctionDeclaration: uploaderPermissionTagType
  - 基线：源语句 sha256=c4726e8853378645c1b91241d343146cdb8315f377ae8501514962df06e9fcb2；保留返回、异常及 5 个分支，调用=。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05006 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template lines 1-102（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05007 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template line 4: v-model:
  - 基线：原表达式：open；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05008 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template line 9: v-bind:column
  - 基线：原表达式：2；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05009 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template line 14: v-bind:span
  - 基线：原表达式：2；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05010 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template line 37: v-if:
  - 基线：原表达式：detail.accessType === 'private' && detail.uploadUserId；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05011 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template line 38: v-bind:type
  - 基线：原表达式：uploaderPermissionTagType(detail)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05012 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template line 43: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05013 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template line 59: v-if:
  - 基线：原表达式：detail.referenceCount；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05014 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template line 62: v-on:click
  - 基线：原表达式：emit('reference', detail)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05015 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template line 66: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05016 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template line 89: v-bind:span
  - 基线：原表达式：2；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05017 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template line 92: v-bind:span
  - 基线：原表达式：2；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05018 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template line 96: v-slot:footer
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05019 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template line 98: v-on:click
  - 基线：原表达式：open = false；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05020 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 15
  - 基线：原显示表达式：detail.fileId
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05021 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 18
  - 基线：原显示表达式：detail.originalName
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05022 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 21
  - 基线：原显示表达式：detail.storedName
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05023 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 24
  - 基线：原显示表达式：accessTypeLabel(detail.accessType)
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05024 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 27
  - 基线：原显示表达式：statusLabel(detail.status)
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05025 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 30
  - 基线：原显示表达式：detail.createBy || "-"
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05026 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 33
  - 基线：原显示表达式：detail.uploadUserId || "-"
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05027 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 41
  - 基线：原显示表达式：uploaderPermissionLabel(detail)
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05028 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 43
  - 基线：原显示表达式：uploaderPermissionLabel(detail)
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05029 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 46
  - 基线：原显示表达式：detail.ownerName || detail.ownerUserId || "-"
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05030 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 49
  - 基线：原显示表达式：detail.deptName || detail.deptId || "-"
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05031 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 52
  - 基线：原显示表达式：storageStatusLabel(detail.storageStatus)
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05032 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 55
  - 基线：原显示表达式：detail.aclEntryCount || 0
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05033 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 64
  - 基线：原显示表达式：detail.referenceCount
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05034 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 69
  - 基线：原显示表达式：detail.aclVersion ?? "-"
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05035 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 72
  - 基线：原显示表达式：formatFileSize(detail.fileSize)
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05036 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 75
  - 基线：原显示表达式：detail.contentType || "-"
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05037 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 78
  - 基线：原显示表达式：detail.extension || "-"
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05038 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 81
  - 基线：原显示表达式：parseTime(detail.createTime)
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05039 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 84
  - 基线：原显示表达式：parseTime(detail.expireTime) || "-"
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05040 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 87
  - 基线：原显示表达式：parseTime(detail.deletedTime) || "-"
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05041 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 90
  - 基线：原显示表达式：detail.storageKey
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05042 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` template interpolation line 93
  - 基线：原显示表达式：detail.fileHash
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx
- I05043 `ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue` style[0] lines 156-170
  - 基线：保留全部选择器、声明和 url；lang=css, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/views/system/file/components/FileDetailDialog.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
