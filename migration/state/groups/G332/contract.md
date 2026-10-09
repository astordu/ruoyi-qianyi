# G332 tests/plugins/run-plugin-tests.js：完整能力

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I08727 `ruoyi-fastapi-frontend/tests/plugins/run-plugin-tests.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=01195c35667d8fb9e425f21533ee3dedf553d508108209878ea8856db9f995ab；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/tests/plugins/run-plugin-tests.ts
- I08728 `ruoyi-fastapi-frontend/tests/plugins/run-plugin-tests.js` lines 2-2 ImportDeclaration: 
  - 基线：源语句 sha256=05b23cf26124b8de241e57f00310bb46263cc134f320097577b690fd40b8a67d；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/tests/plugins/run-plugin-tests.ts
- I08729 `ruoyi-fastapi-frontend/tests/plugins/run-plugin-tests.js` lines 3-3 ImportDeclaration: 
  - 基线：源语句 sha256=da9e33f239d38ec2fd1173672647d352582a1693922a7f4e8f819726746c8909；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/tests/plugins/run-plugin-tests.ts
- I08730 `ruoyi-fastapi-frontend/tests/plugins/run-plugin-tests.js` lines 5-5 VariableDeclaration: __filename
  - 基线：源语句 sha256=c671bd0ee6c971e8a140e3d2e72ae47a9975f20f6433a226a4572fc91871d05f；保留返回、异常及 0 个分支，调用=fileURLToPath。
  - 去向：react-front/tests/plugins/run-plugin-tests.ts
- I08731 `ruoyi-fastapi-frontend/tests/plugins/run-plugin-tests.js` lines 6-6 VariableDeclaration: __dirname
  - 基线：源语句 sha256=c60f54ea59da55f7d20506e0b876430fd628270315fca09111f1b33b32480592；保留返回、异常及 0 个分支，调用=dirname。
  - 去向：react-front/tests/plugins/run-plugin-tests.ts
- I08732 `ruoyi-fastapi-frontend/tests/plugins/run-plugin-tests.js` lines 8-24 VariableDeclaration: collectTestFiles
  - 基线：源语句 sha256=1b60d7758841574e440127c84995937adabd8873b1a1b5b6a068e41cbc16ac41；保留返回、异常及 4 个分支，调用=readdirSync, join, entry.isDirectory, testFiles.push, collectTestFiles, entry.isFile, entry.name.endsWith, testFiles.sort。
  - 去向：react-front/tests/plugins/run-plugin-tests.ts
- I08733 `ruoyi-fastapi-frontend/tests/plugins/run-plugin-tests.js` lines 26-26 VariableDeclaration: testFiles
  - 基线：源语句 sha256=9280586d3f286fac003948c5b13685ff33804107b2581373a4eee5c8180b653e；保留返回、异常及 0 个分支，调用=collectTestFiles。
  - 去向：react-front/tests/plugins/run-plugin-tests.ts
- I08734 `ruoyi-fastapi-frontend/tests/plugins/run-plugin-tests.js` lines 28-53 IfStatement: 
  - 基线：源语句 sha256=61a98641266273317fc9044ec802e8c4d11a389084bafe4f09309eca17c9d826；保留返回、异常及 4 个分支，调用=console.error, relative, Import, pathToFileURL, console.log。
  - 去向：react-front/tests/plugins/run-plugin-tests.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
