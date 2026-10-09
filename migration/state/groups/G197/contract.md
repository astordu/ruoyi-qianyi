# G197 src/layout/components/HeaderNotice/DetailView.vue：完整能力

依赖：G000, G041

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01937 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` lines 56-56 ImportDeclaration: 
  - 基线：源语句 sha256=1828bae8d7fea964cc8226f6b3cb78396349c8b1bb4fb60e096f8aec5a6fc776；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01938 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` lines 58-58 VariableDeclaration: visible
  - 基线：源语句 sha256=131588e506b10f4b16485c9067fceb50053d9acd0559369303f97aa3a383855a；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01939 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` lines 59-59 VariableDeclaration: loading
  - 基线：源语句 sha256=360133162609dea18ceb29cc60a4fd9166a9ed26b0d8544941212d26502f30ef；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01940 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` lines 60-60 VariableDeclaration: detail
  - 基线：源语句 sha256=84830be2b3e1768907f336e2af888b4290fa2a8aa2074e91ce457d071617fafc；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01941 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` lines 62-65 VariableDeclaration: isStatusNormal
  - 基线：源语句 sha256=e547ec327ed4c8e3d17f7093e5bcdd612fbc33b4a652b725082ac1b14886540b；保留返回、异常及 3 个分支，调用=computed。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01942 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` lines 67-70 VariableDeclaration: hasContent
  - 基线：源语句 sha256=7e02720f02c745dbfb838e5eece57e17d55abf4ee2ec8c3f8bc4c15d5c954c11；保留返回、异常及 3 个分支，调用=computed, CallExpression.trim, String。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01943 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` lines 72-101 FunctionDeclaration: open
  - 基线：源语句 sha256=eba9ac4e872808113885d1cd9aa87f911aeb1f4beb65b4cdb1ecb6d00c0379a1；保留返回、异常及 8 个分支，调用=CallExpression.finally, CallExpression.catch, CallExpression.then, getNotice。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01944 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` lines 103-107 FunctionDeclaration: handleClose
  - 基线：源语句 sha256=2b08a84c619d84825e622d608d20ece9d759a47765f5332ac0aebd32e438883b；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01945 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` lines 109-111 ExpressionStatement: 
  - 基线：源语句 sha256=64705ef294d9f2ca1192d1c35cd3874553f37329b77d7c9615d5c7fbc3aae3a4；保留返回、异常及 0 个分支，调用=defineExpose。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01946 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` template lines 1-53（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01947 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` template line 2: v-model:
  - 基线：原表达式：visible；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01948 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` template line 2: v-bind:before-close
  - 基线：原表达式：handleClose；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01949 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` template line 3: v-loading:
  - 基线：原表达式：loading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01950 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` template line 4: v-if:
  - 基线：原表达式：!detail；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01951 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` template line 8: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01952 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` template line 10: v-if:
  - 基线：原表达式：detail.noticeType === '1'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01953 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` template line 13: v-else-if:
  - 基线：原表达式：detail.noticeType === '2'；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01954 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` template line 16: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01955 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` template line 33: v-bind:class
  - 基线：原表达式：['status-dot', isStatusNormal ? 'status-ok' : 'status-off']；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01956 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` template line 45: v-if:
  - 基线：原表达式：hasContent；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01957 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` template line 45: v-html:
  - 基线：原表达式：detail.noticeContent；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01958 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` template line 46: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01959 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` template interpolation line 21
  - 基线：原显示表达式：detail.noticeTitle
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01960 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` template interpolation line 26
  - 基线：原显示表达式：detail.createBy || '—'
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01961 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` template interpolation line 30
  - 基线：原显示表达式：parseTime(detail.createTime) || '—'
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01962 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` template interpolation line 34
  - 基线：原显示表达式：isStatusNormal ? '正常' : '已关闭'
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01963 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` style[0] lines 114-308
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx
- I01964 `ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue` style[1] lines 310-326
  - 基线：保留全部选择器、声明和 url；lang=scss, scoped=False；原样式选择器在 source-audit.json。
  - 去向：react-front/src/layout/components/HeaderNotice/DetailView.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
