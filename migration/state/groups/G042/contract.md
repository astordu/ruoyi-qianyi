# G042 src/api/system/plugin.js：完整能力

依赖：G000, G249

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00577 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=cd462474cb30a9a5954fbd44474b2f4e19f6d48d3c7dff5aebf452db4c8517f8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/api/system/plugin.ts
- I00578 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 4-10 ExportNamedDeclaration: listPlugin
  - 基线：源语句 sha256=e75e4b99b3fdca85b2f0b323fe2939de1d574a5d51fe7d8d219093c2c24725e7；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00579 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 13-18 ExportNamedDeclaration: getPlugin
  - 基线：源语句 sha256=fa05f27ce681d948ff8e9efebb6433708f4bf7db1f87bcb24bc6b209a5cd4c50；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00580 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 21-26 ExportNamedDeclaration: enablePlugin
  - 基线：源语句 sha256=ef322222f914a58144c523a451cf3360f03356cd093914cf7ba34d26ffb0738a；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00581 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 29-34 ExportNamedDeclaration: disablePlugin
  - 基线：源语句 sha256=bb37610f9db69c15851371be712ad9b6f5ecad5260440177b06b5f1d29bcb70e；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00582 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 37-42 ExportNamedDeclaration: checkPlugin
  - 基线：源语句 sha256=1f35d8dfb51a4081993bb4dec1ef39ab13ecee7fcf5b6b8e881155c1e8322c84；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00583 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 45-50 ExportNamedDeclaration: healthPlugin
  - 基线：源语句 sha256=d9f02e94174942f190c637c5513ee7b8984bc316e857b6c809e3a4d4caeaca8d；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00584 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 53-58 ExportNamedDeclaration: diagnosePlugin
  - 基线：源语句 sha256=d3487288561a886a346a7c0cb25f0a8945507effce285e054ec0009f9766c0a5；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00585 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 61-67 ExportNamedDeclaration: installPlugin
  - 基线：源语句 sha256=6b88f948ac6e2a01c7196d2760f025cc8797e99ee515d4a6097ec055c0ea3aba；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00586 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 70-76 ExportNamedDeclaration: upgradePlugin
  - 基线：源语句 sha256=eb44251a87a90383490b78803796c073bf0f731bf10691e1a20f82acddd60f45；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00587 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 79-85 ExportNamedDeclaration: uninstallPlugin
  - 基线：源语句 sha256=57708e4b1e6e23e3a5a1a6b01e9eb0d435b953994041a93d44b7649d83009d53；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00588 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 88-94 ExportNamedDeclaration: purgePlugin
  - 基线：源语句 sha256=3b408016562098736a4f1b0c886821be652a528ec187705bdbf450080602b62a；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00589 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 97-102 ExportNamedDeclaration: getPluginConfig
  - 基线：源语句 sha256=aacc97201f96cd7a4253ffd9acd41bd76921725ea5e734c70d53d039332d74c9；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00590 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 105-111 ExportNamedDeclaration: listPluginMigrations
  - 基线：源语句 sha256=714cb28dd91feb10a73a89550aeca757f232102d7d1aa2bfb9a530348b5446a5；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00591 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 114-120 ExportNamedDeclaration: markPluginMigrationSuccess
  - 基线：源语句 sha256=cf7914c29dae64d29b3da94b26502895e5ade7c2994d253b03250067ab8250ae；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00592 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 123-129 ExportNamedDeclaration: markPluginMigrationFailed
  - 基线：源语句 sha256=785ee7905ba147b3f546296edd7635afa65a65cef8dbbcb220376ebb2bb063fb；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00593 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 132-138 ExportNamedDeclaration: updatePluginConfig
  - 基线：源语句 sha256=55dd2d50e8e8ad284c17f37b85641c12a1ff7c42009aec55db72a505823549c3；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00594 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 141-146 ExportNamedDeclaration: checkPluginDependencies
  - 基线：源语句 sha256=3f7c768a328f38b0a4ee62fed10d84120cd2e6a4dc9cf7f9ae9f1f837216be8d；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00595 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 149-158 ExportNamedDeclaration: planPlugins
  - 基线：源语句 sha256=297616d30ce0206c0842d347b1696d95ecc5f2b4cdb1b3f688f5102b8fb1114b；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00596 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 161-172 ExportNamedDeclaration: batchPlugins
  - 基线：源语句 sha256=6c591e0637165cea90bffce0dcf3249dd2eeab094b992eb5075ccc40e5f83888；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00597 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 175-181 ExportNamedDeclaration: listPluginOperationLog
  - 基线：源语句 sha256=3001eadc9bae911fed57fa6093720e3a795546477a51c588ee628dbff631ea9d；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00598 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 184-189 ExportNamedDeclaration: getPluginOperationLog
  - 基线：源语句 sha256=df6f5d466856ff86c78aa9a2bb1d64c188e127f46b7b0dff5e666e1f8921f470；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00599 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 192-198 ExportNamedDeclaration: retainPluginOperationLog
  - 基线：源语句 sha256=57cd09a15bbb3c46470615b5d2c6a6244b4cee88a8fba44df19ce164e4bfaa05；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts
- I00600 `ruoyi-fastapi-frontend/src/api/system/plugin.js` lines 201-207 ExportNamedDeclaration: installPluginDependencies
  - 基线：源语句 sha256=4167de3777c8e3ed6332a3bd42b28ad5551f9911d79a94c51e3fbc6bd4c7d47c；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/plugin.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
