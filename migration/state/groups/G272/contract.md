# G272 src/views/monitor/operlog/detail.vue：完整能力

依赖：G000, G232, G250

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I03894 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` lines 115-115 VariableDeclaration: 
  - 基线：源语句 sha256=d3917068104e0f2158733e5e758c09ff6781b09fc4b90611c9a30e2625c695d6；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03895 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` lines 117-120 VariableDeclaration: props
  - 基线：源语句 sha256=8a71df8321a7a38dde2a77b7be8c5a3d0a9eed71fc2607dbe60f86817f1d913b；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03896 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` lines 122-122 VariableDeclaration: emit
  - 基线：源语句 sha256=9f1c4d41811d8dbf0894fee5d0c9e691123c8545254d1148e8addc78b46700bb；保留返回、异常及 0 个分支，调用=defineEmits。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03897 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` lines 124-127 VariableDeclaration: dialogVisible
  - 基线：源语句 sha256=a7554b3c62b73417c49c018aaea5184cab4ad5d93d1675b011aa79d1afa82799；保留返回、异常及 0 个分支，调用=computed, emit。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03898 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` lines 129-129 VariableDeclaration: 
  - 基线：源语句 sha256=3488a0848d4a299e58e4d7daa467400f451ef0c8eabb3fd4c231a4214fc3d442；保留返回、异常及 0 个分支，调用=proxy.useDict。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03899 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` lines 131-131 VariableDeclaration: form
  - 基线：源语句 sha256=313b72d7763324780e8c54b21ab16e43336b9cf1e1d6fc56a7aefad7dd0ffc4f；保留返回、异常及 1 个分支，调用=computed。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03900 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` lines 132-132 VariableDeclaration: typeLabel
  - 基线：源语句 sha256=bf89086b753b890ba7d4161446f6eb15b6c08f436cac617bb3b1808ee2a5767f；保留返回、异常及 1 个分支，调用=computed, proxy.selectDictLabel。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03901 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` lines 134-137 FunctionDeclaration: formatJson
  - 基线：源语句 sha256=4a5ae474ce590f48db5c34381a57cf66a526cbd4dcfa27013842332a0f270983；保留返回、异常及 5 个分支，调用=JSON.stringify, JSON.parse。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03902 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` lines 139-152 FunctionDeclaration: copyText
  - 基线：源语句 sha256=4e4479e0ec0c5c466bcb634e88fc504eecad517105da8e35aae66011c941b42d；保留返回、异常及 1 个分支，调用=formatJson, CallExpression.then, navigator.clipboard.writeText, ElMessage, document.createElement, document.body.appendChild, ta.select, document.execCommand, document.body.removeChild。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03903 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template lines 1-112（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03904 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 2: v-model:
  - 基线：原表达式：dialogVisible；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03905 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 2: v-on:close
  - 基线：原表达式：$emit('update:visible', false)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03906 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 8: v-bind:span
  - 基线：原表达式：12；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03907 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 11: v-bind:span
  - 基线：原表达式：12；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03908 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 16: v-bind:span
  - 基线：原表达式：12；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03909 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 19: v-bind:span
  - 基线：原表达式：12；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03910 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 22: v-if:
  - 基线：原表达式：form.status === 0；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03911 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 23: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03912 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 33: v-bind:span
  - 基线：原表达式：12；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03913 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 36: v-bind:span
  - 基线：原表达式：12；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03914 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 36: v-if:
  - 基线：原表达式：form.deptName；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03915 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 41: v-bind:span
  - 基线：原表达式：24；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03916 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 54: v-bind:span
  - 基线：原表达式：24；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03917 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 58: v-bind:class
  - 基线：原表达式：'method-tag method-' + form.requestMethod；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03918 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 65: v-bind:span
  - 基线：原表达式：24；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03919 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 70: v-bind:span
  - 基线：原表达式：12；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03920 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 82: v-bind:icon
  - 基线：原表达式：CopyDocument；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03921 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 82: v-on:click
  - 基线：原表达式：copyText(form.operParam)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03922 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 95: v-bind:icon
  - 基线：原表达式：CopyDocument；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03923 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 95: v-on:click
  - 基线：原表达式：copyText(form.jsonResult)；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03924 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template line 103: v-if:
  - 基线：原表达式：form.status !== 0；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03925 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template interpolation line 9
  - 基线：原显示表达式：form.title
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03926 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template interpolation line 12
  - 基线：原显示表达式：typeLabel
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03927 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template interpolation line 17
  - 基线：原显示表达式：parseTime(form.operTime) || '-'
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03928 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template interpolation line 34
  - 基线：原显示表达式：form.operName
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03929 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template interpolation line 37
  - 基线：原显示表达式：form.deptName
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03930 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template interpolation line 44
  - 基线：原显示表达式：form.operIp
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03931 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template interpolation line 44
  - 基线：原显示表达式：form.operLocation
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03932 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template interpolation line 58
  - 基线：原显示表达式：form.requestMethod
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03933 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template interpolation line 59
  - 基线：原显示表达式：form.operUrl
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03934 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template interpolation line 66
  - 基线：原显示表达式：form.method
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03935 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template interpolation line 71
  - 基线：原显示表达式：form.costTime
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03936 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template interpolation line 84
  - 基线：原显示表达式：formatJson(form.operParam)
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03937 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template interpolation line 97
  - 基线：原显示表达式：formatJson(form.jsonResult)
  - 去向：react-front/src/views/monitor/operlog/detail.tsx
- I03938 `ruoyi-fastapi-frontend/src/views/monitor/operlog/detail.vue` template interpolation line 106
  - 基线：原显示表达式：form.errorMsg
  - 去向：react-front/src/views/monitor/operlog/detail.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
