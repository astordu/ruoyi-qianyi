# G254 src/utils/transportCrypto.js：状态、输入与依赖接口

依赖：G000, G216, G255

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02840 `ruoyi-fastapi-frontend/src/utils/transportCrypto.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=b922f0193d652b2c0de36098fb1aa440be1a522c617f1ee9035355a86f788986；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCrypto.context.ts
- I02841 `ruoyi-fastapi-frontend/src/utils/transportCrypto.js` lines 3-9 ImportDeclaration: 
  - 基线：源语句 sha256=b7d9397da3778a9ca3fe4f2f58b82061f413922f0ab8fba368c7cf8accf87568；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCrypto.context.ts
- I02842 `ruoyi-fastapi-frontend/src/utils/transportCrypto.js` lines 10-10 ImportDeclaration: 
  - 基线：源语句 sha256=819249c9809a1e47bb12de03da21c4c25f60b908825d07094d219578c4c835ec；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCrypto.context.ts
- I02843 `ruoyi-fastapi-frontend/src/utils/transportCrypto.js` lines 12-12 VariableDeclaration: TRANSPORT_BASE_URL
  - 基线：源语句 sha256=dbd4119f25a0f520194b7708c1f58c7507a9bfd6d464578b05a1c78676cbaec3；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCrypto.context.ts
- I02844 `ruoyi-fastapi-frontend/src/utils/transportCrypto.js` lines 13-13 VariableDeclaration: TRANSPORT_ENABLE_HEADER
  - 基线：源语句 sha256=02812ef57db1029824152bef36193481d1bc6843d82a31f0c3f822740fff9616；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCrypto.context.ts
- I02845 `ruoyi-fastapi-frontend/src/utils/transportCrypto.js` lines 14-14 VariableDeclaration: TRANSPORT_KEY_ID_HEADER
  - 基线：源语句 sha256=0fda03c585131dcdd998a7dd7978d16863dfead47981bea5e078bf80298a039f；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCrypto.context.ts
- I02846 `ruoyi-fastapi-frontend/src/utils/transportCrypto.js` lines 15-15 VariableDeclaration: ENCRYPTED_RESPONSE_HEADER
  - 基线：源语句 sha256=f317eaaff1dfeb97605f337909183674af9298744e47e66e712c100066b1c632；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCrypto.context.ts
- I02847 `ruoyi-fastapi-frontend/src/utils/transportCrypto.js` lines 16-16 VariableDeclaration: DEFAULT_TRANSPORT_ENVELOPE_VERSION
  - 基线：源语句 sha256=001ff3aa33730c3790fbe890e784f4743ac610fc661f3f5af0b4a95f80a15502；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCrypto.context.ts
- I02848 `ruoyi-fastapi-frontend/src/utils/transportCrypto.js` lines 18-21 VariableDeclaration: transportClient
  - 基线：源语句 sha256=5616867358f3222ad6bfe3234ef5a23cd3cc6c1ea8fabda8e746d8c53330c66e；保留返回、异常及 0 个分支，调用=axios.create。
  - 去向：react-front/src/utils/transportCrypto.context.ts
- I02849 `ruoyi-fastapi-frontend/src/utils/transportCrypto.js` lines 23-23 VariableDeclaration: cachedKeyMeta
  - 基线：源语句 sha256=bd960d15ee60816e9520cc08d4fa90cd5b9b2f971aeaa98c19c4d0cc34adca15；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCrypto.context.ts
- I02850 `ruoyi-fastapi-frontend/src/utils/transportCrypto.js` lines 24-24 VariableDeclaration: inflightKeyMetaPromise
  - 基线：源语句 sha256=508a0ba04baa32713177741d53da727fb36c1711029ce8cd42363bcdb19a36d3；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCrypto.context.ts
- I02851 `ruoyi-fastapi-frontend/src/utils/transportCrypto.js` lines 25-25 VariableDeclaration: KEY_REFRESH_BUFFER_MIN_SECONDS
  - 基线：源语句 sha256=504e8a569f99faa3915774aabdc9e7d109d1aa54cd1f342aca60895938e4a22c；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCrypto.context.ts
- I02852 `ruoyi-fastapi-frontend/src/utils/transportCrypto.js` lines 26-26 VariableDeclaration: KEY_REFRESH_BUFFER_MAX_SECONDS
  - 基线：源语句 sha256=5c97857a439a7e2a96e9e25363ae69ae1c4c6681cb53fee7481087a085573821；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCrypto.context.ts
- I02853 `ruoyi-fastapi-frontend/src/utils/transportCrypto.js` lines 27-27 VariableDeclaration: TRANSPORT_KEY_META_CACHE_KEY
  - 基线：源语句 sha256=d56a44457881ca343594687bf83416c8cc6b63082698a9938e7b4862cbf34149；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCrypto.context.ts
- I02854 `ruoyi-fastapi-frontend/src/utils/transportCrypto.js` lines 28-28 VariableDeclaration: TRANSPORT_RETRYABLE_ERROR_MESSAGES
  - 基线：源语句 sha256=ec29cbeed693090a1877e5418623846f3111b03942d103eb3cfebcffb80589a5；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/transportCrypto.context.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
