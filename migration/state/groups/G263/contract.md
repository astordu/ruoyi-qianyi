# G263 src/views/monitor/cache/index.vue：完整能力

依赖：G000, G027

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I03139 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` lines 68-68 ImportDeclaration: 
  - 基线：源语句 sha256=b9c2bb0713ea092d41f5cd7ed5e613b12133a1a2412b68559c996e822ab5d4ac；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03140 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` lines 69-69 ImportDeclaration: 
  - 基线：源语句 sha256=88bb173633a74f4e2311184a9113890ea6afb87a2ffb81f5dec5ea2b7712b40f；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03141 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` lines 71-71 VariableDeclaration: cache
  - 基线：源语句 sha256=45267549d21ad6d224a3af1773bc6f59d5d520872a1ac14f40c0c3281bacc93d；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03142 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` lines 72-72 VariableDeclaration: commandstats
  - 基线：源语句 sha256=b47ec9863ab04cc1c297444e5838f47a6c23d87450495016a471f4f64f7653eb；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03143 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` lines 73-73 VariableDeclaration: usedmemory
  - 基线：源语句 sha256=fb1733a78243cd0e2119bbc3857cf1487d2b800539aab44d0f4bcc1c917994be；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03144 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` lines 74-74 VariableDeclaration: 
  - 基线：源语句 sha256=5f11c95d75add065fffa6246968f543edb06a68cc290963d8a011cfc62b1f0af；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03145 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` lines 76-129 FunctionDeclaration: getList
  - 基线：源语句 sha256=f451439fe45e88b37529d5933c95ee07eedbcd1f9e84576c334c87b476e1a364；保留返回、异常及 0 个分支，调用=proxy.$modal.loading, CallExpression.then, getCache, proxy.$modal.closeLoading, echarts.init, commandstatsIntance.setOption, usedmemoryInstance.setOption, parseFloat, window.addEventListener, commandstatsIntance.resize, usedmemoryInstance.resize。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03146 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` lines 131-131 ExpressionStatement: 
  - 基线：源语句 sha256=e966d3b08f869f7c7962cc988172bf8bc4840aa64d83fa58b0a15b31a76e4d3d；保留返回、异常及 0 个分支，调用=getList。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03147 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template lines 1-65（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03148 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template line 3: v-bind:gutter
  - 基线：原表达式：10；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03149 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template line 4: v-bind:span
  - 基线：原表达式：24；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03150 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template line 6: v-slot:header
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03151 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template line 12: v-if:
  - 基线：原表达式：cache.info；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03152 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template line 14: v-if:
  - 基线：原表达式：cache.info；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03153 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template line 16: v-if:
  - 基线：原表达式：cache.info；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03154 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template line 18: v-if:
  - 基线：原表达式：cache.info；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03155 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template line 22: v-if:
  - 基线：原表达式：cache.info；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03156 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template line 24: v-if:
  - 基线：原表达式：cache.info；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03157 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template line 26: v-if:
  - 基线：原表达式：cache.info；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03158 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template line 28: v-if:
  - 基线：原表达式：cache.info；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03159 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template line 32: v-if:
  - 基线：原表达式：cache.info；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03160 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template line 34: v-if:
  - 基线：原表达式：cache.info；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03161 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template line 36: v-if:
  - 基线：原表达式：cache.dbSize；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03162 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template line 38: v-if:
  - 基线：原表达式：cache.info；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03163 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template line 46: v-bind:span
  - 基线：原表达式：12；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03164 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template line 48: v-slot:header
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03165 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template line 55: v-bind:span
  - 基线：原表达式：12；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03166 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template line 57: v-slot:header
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03167 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template interpolation line 12
  - 基线：原显示表达式：cache.info.redis_version
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03168 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template interpolation line 14
  - 基线：原显示表达式：cache.info.redis_mode == "standalone" ? "单机" : "集群"
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03169 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template interpolation line 16
  - 基线：原显示表达式：cache.info.tcp_port
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03170 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template interpolation line 18
  - 基线：原显示表达式：cache.info.connected_clients
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03171 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template interpolation line 22
  - 基线：原显示表达式：cache.info.uptime_in_days
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03172 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template interpolation line 24
  - 基线：原显示表达式：cache.info.used_memory_human
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03173 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template interpolation line 26
  - 基线：原显示表达式：parseFloat(cache.info.used_cpu_user_children).toFixed(2)
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03174 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template interpolation line 28
  - 基线：原显示表达式：cache.info.maxmemory_human
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03175 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template interpolation line 32
  - 基线：原显示表达式：cache.info.aof_enabled == "0" ? "否" : "是"
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03176 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template interpolation line 34
  - 基线：原显示表达式：cache.info.rdb_last_bgsave_status
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03177 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template interpolation line 36
  - 基线：原显示表达式：cache.dbSize
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03178 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template interpolation line 38
  - 基线：原显示表达式：cache.info.instantaneous_input_kbps
  - 去向：react-front/src/views/monitor/cache/index.tsx
- I03179 `ruoyi-fastapi-frontend/src/views/monitor/cache/index.vue` template interpolation line 38
  - 基线：原显示表达式：cache.info.instantaneous_output_kbps
  - 去向：react-front/src/views/monitor/cache/index.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
