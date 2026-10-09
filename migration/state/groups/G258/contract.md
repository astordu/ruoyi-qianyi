# G258 src/views/dashboard/index.vue：状态、输入与依赖接口

依赖：G000, G228, G257

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02946 `ruoyi-fastapi-frontend/src/views/dashboard/index.vue` lines 170-183 ImportDeclaration: 
  - 基线：源语句 sha256=6e9a50587c9813a246d2e6f69b2f39bdaab602eac701a28a5e41411eddb2b44f；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/dashboard/index.context.ts
- I02947 `ruoyi-fastapi-frontend/src/views/dashboard/index.vue` lines 184-184 ImportDeclaration: 
  - 基线：源语句 sha256=a75602b9f7a6b528183f7271f47f6f4722f7d50c89d798f1e6365d66aafb9836；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/dashboard/index.context.ts
- I02948 `ruoyi-fastapi-frontend/src/views/dashboard/index.vue` lines 186-200 ExportDefaultDeclaration: 
  - 基线：源语句 sha256=65a8fb510df5e52eeac3934bc60ff7f50ed784833ce519e80166c0e4ff3296ea；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/dashboard/index.context.ts
- I02949 `ruoyi-fastapi-frontend/src/views/dashboard/index.vue` lines 204-204 ImportDeclaration: 
  - 基线：源语句 sha256=208e5c9279fbfbccb56c96ccff70576516c04e33b808e91d8e20b1e520533887；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/dashboard/index.context.ts
- I02950 `ruoyi-fastapi-frontend/src/views/dashboard/index.vue` lines 205-205 ImportDeclaration: 
  - 基线：源语句 sha256=106eed84730e33996689063d23a4798ea6dc48cad9e6900013acff276d86d239；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/dashboard/index.context.ts
- I02951 `ruoyi-fastapi-frontend/src/views/dashboard/index.vue` lines 206-206 ImportDeclaration: 
  - 基线：源语句 sha256=446860e58a267757fcdcadce475b43a7115034442ba33baa1f5582cdbcb66db9；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/dashboard/index.context.ts
- I02952 `ruoyi-fastapi-frontend/src/views/dashboard/index.vue` lines 208-208 VariableDeclaration: settingsStore
  - 基线：源语句 sha256=3604ebb18e2cd66f7a29e27607556d37b538f1a7beca03dcf6e3c4403535140f；保留返回、异常及 0 个分支，调用=useSettingsStore。
  - 去向：react-front/src/views/dashboard/index.context.ts
- I02953 `ruoyi-fastapi-frontend/src/views/dashboard/index.vue` lines 210-212 ExpressionStatement: 
  - 基线：源语句 sha256=98c66f39a92c1d7b9ab7b286186665cb1744bf0ff26c4a6a7ad4744f17ccc5a0；保留返回、异常及 0 个分支，调用=defineOptions。
  - 去向：react-front/src/views/dashboard/index.context.ts
- I02954 `ruoyi-fastapi-frontend/src/views/dashboard/index.vue` lines 214-222 VariableDeclaration: currentUser
  - 基线：源语句 sha256=b1e3da3bd2fbcd7da373bb5ba36eabfd7c789c09acc0698bdba8f532089746ca；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/dashboard/index.context.ts
- I02955 `ruoyi-fastapi-frontend/src/views/dashboard/index.vue` lines 224-285 VariableDeclaration: projectNotice
  - 基线：源语句 sha256=3f10e66c4c5ccce4c226176a3938bf9a62d0930b5c2aa8cd19dce4e9ceb6a373；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/dashboard/index.context.ts
- I02956 `ruoyi-fastapi-frontend/src/views/dashboard/index.vue` lines 287-398 VariableDeclaration: activities
  - 基线：源语句 sha256=9192db1b41c7cf58d3fc479887d14b91b672aaad1b485208cc1a4523a02fb92b；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/dashboard/index.context.ts
- I02957 `ruoyi-fastapi-frontend/src/views/dashboard/index.vue` lines 400-400 VariableDeclaration: radarContainer
  - 基线：源语句 sha256=fce665cefa26e9bcc5d49d743ac6d6452f32d9a92bc3d4060d6d90bd6faedfc5；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/views/dashboard/index.context.ts
- I02958 `ruoyi-fastapi-frontend/src/views/dashboard/index.vue` lines 401-477 VariableDeclaration: radarData
  - 基线：源语句 sha256=c32fd0aef5bf6678b5007db53b8eff183c4f08fdde0c8bd0f982315742c10559；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/dashboard/index.context.ts
- I02959 `ruoyi-fastapi-frontend/src/views/dashboard/index.vue` lines 478-478 VariableDeclaration: radar
  - 基线：源语句 sha256=203b1f97f2cbdd76e125a676d12e3a89b008a6f43c003b03ab63c0b264a6cb16；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/views/dashboard/index.context.ts
- I02960 `ruoyi-fastapi-frontend/src/views/dashboard/index.vue` lines 479-494 ExpressionStatement: 
  - 基线：源语句 sha256=1c4d1be26518d9244ab63a74a7dadd992f10df2205923a089011a47b79ed3835；保留返回、异常及 0 个分支，调用=onMounted, radar.render。
  - 去向：react-front/src/views/dashboard/index.context.ts
- I02961 `ruoyi-fastapi-frontend/src/views/dashboard/index.vue` lines 496-498 ExpressionStatement: 
  - 基线：源语句 sha256=178ead87b8e431bf9fa2e9aea7e72728dabcd2b8e0111487f1a9a3fc92268e58；保留返回、异常及 0 个分支，调用=onBeforeUnmount, radar.destroy。
  - 去向：react-front/src/views/dashboard/index.context.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
