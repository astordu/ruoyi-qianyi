# G275 src/views/monitor/transportCrypto/index.vue：状态、输入与依赖接口

依赖：G000, G034, G250

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I04112 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 333-333 ImportDeclaration: 
  - 基线：源语句 sha256=3db48a9f34d2c13fbdebaac48d52186ea78df8045e664ce5ad61b7fcb8d81ac8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts
- I04113 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 334-334 ImportDeclaration: 
  - 基线：源语句 sha256=6928361d5730d3e3a41971c66c5ba4a0bcfc5b4e4b4a5700e6ef47b23ae889a6；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts
- I04114 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 335-335 ImportDeclaration: 
  - 基线：源语句 sha256=f4210f54c2fef87c2ea42a60e139c2c6fd988c4f38b6f8bc6228141892bb3ec3；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts
- I04115 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 337-337 VariableDeclaration: 
  - 基线：源语句 sha256=d3917068104e0f2158733e5e758c09ff6781b09fc4b90611c9a30e2625c695d6；保留返回、异常及 0 个分支，调用=getCurrentInstance。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts
- I04116 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 339-339 VariableDeclaration: loading
  - 基线：源语句 sha256=360133162609dea18ceb29cc60a4fd9166a9ed26b0d8544941212d26502f30ef；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts
- I04117 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 340-340 VariableDeclaration: autoRefresh
  - 基线：源语句 sha256=7fe32ea76d460d41c819aebbd8374b2c269ed35ac7fea05f2ec2badcf061e51b；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts
- I04118 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 341-341 VariableDeclaration: failureReasonChartRef
  - 基线：源语句 sha256=7eead735370e3700631ac271103bc54107b24d4901a0da9c192be347b0b5f520；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts
- I04119 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 342-342 VariableDeclaration: kidStatsChartRef
  - 基线：源语句 sha256=192a9dd68f8c2b511f93491db1ff271cd2ca5ecb3de1f49733e0e9b47e8cefd0；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts
- I04120 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 343-343 VariableDeclaration: selectedFailureReason
  - 基线：源语句 sha256=93ff56bf59884732c1aaa56c190d54ff9e2605812a1e7316736ec9482f2460ce；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts
- I04121 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 344-344 VariableDeclaration: selectedKid
  - 基线：源语句 sha256=d30da60523874b75d687e8f125d4af924a161958a9cb647bd369271634802648；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts
- I04122 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 345-353 VariableDeclaration: monitorData
  - 基线：源语句 sha256=6428d61397bcdda7a2323b3a41637d31c944b52bbd42aa94558889cd82fc4f9a；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts
- I04123 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 355-355 VariableDeclaration: refreshTimer
  - 基线：源语句 sha256=5c4b2fdc7a0b2348584f3e0746ab2fe596aa0d821db5b4b79ccdeb425152c021；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts
- I04124 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 356-356 VariableDeclaration: failureReasonChartInstance
  - 基线：源语句 sha256=5f63b50e3ada91ab083ed579f315dd762d25cbe83f4e9b47760713bc989dd981；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts
- I04125 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 357-357 VariableDeclaration: kidStatsChartInstance
  - 基线：源语句 sha256=edc7ee52c15c38b872e9a8aac4e4a11af4aed9cebf24dbf37e19e871e1aaa9b9；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts
- I04126 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 359-363 VariableDeclaration: modeLabelMap
  - 基线：源语句 sha256=9a101fc3e9b224f9c1a5ff7b25c14133a96c5d581b992f2cfdead985247ab968；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts
- I04127 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 365-369 VariableDeclaration: monitorScopeLabelMap
  - 基线：源语句 sha256=d62b722380e479757dd2e2a77a4e240b4684b303d244077fda971dd6e905facb；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts
- I04169 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 848-850 ExpressionStatement: 
  - 基线：源语句 sha256=8507bf4dc1885e16a9f8824b547da86731a176709aeccb1708f16915d0ba8d8e；保留返回、异常及 0 个分支，调用=watch, resetRefreshTimer。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts
- I04170 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 852-856 ExpressionStatement: 
  - 基线：源语句 sha256=74aab97fb286a78c21813bf0016dd33d6117f6da48bc954b6d43a875fc11dbf2；保留返回、异常及 0 个分支，调用=watch, nextTick, renderFailureReasonChart。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts
- I04171 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 858-862 ExpressionStatement: 
  - 基线：源语句 sha256=eafae0644198fa664a054c3dbbc27548b4dc14ab8e7d9fe55fbeb20ec3005bf8；保留返回、异常及 0 个分支，调用=watch, nextTick, renderKidStatsChart。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts
- I04172 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 864-868 ExpressionStatement: 
  - 基线：源语句 sha256=62d085f0feacabe3c35f4b0f37712275c65f226fe3dddcfb12adbcbee2e28f72；保留返回、异常及 0 个分支，调用=onMounted, loadMonitorData, resetRefreshTimer, window.addEventListener。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts
- I04173 `ruoyi-fastapi-frontend/src/views/monitor/transportCrypto/index.vue` lines 870-877 ExpressionStatement: 
  - 基线：源语句 sha256=48f9a8e455fae4ccc05b5e663d7b6427b24a1525cedbdc60e19b9e8ce7e7b586；保留返回、异常及 1 个分支，调用=onBeforeUnmount, clearInterval, window.removeEventListener, destroyCharts。
  - 去向：react-front/src/views/monitor/transportCrypto/index.context.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
