# G044 src/api/system/role.js：完整能力

依赖：G000, G249

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00607 `ruoyi-fastapi-frontend/src/api/system/role.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=cd462474cb30a9a5954fbd44474b2f4e19f6d48d3c7dff5aebf452db4c8517f8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/api/system/role.ts
- I00608 `ruoyi-fastapi-frontend/src/api/system/role.js` lines 4-10 ExportNamedDeclaration: listRole
  - 基线：源语句 sha256=03875202cb42818206c77e60877e0336b73ddc466a4e459d1fc6532a5fd87d94；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/role.ts
- I00609 `ruoyi-fastapi-frontend/src/api/system/role.js` lines 13-18 ExportNamedDeclaration: getRole
  - 基线：源语句 sha256=7678c8bdf42d2e1f39d2ba7863abcdae8baaa0aa4ecca99438b82fd4b2b72897；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/role.ts
- I00610 `ruoyi-fastapi-frontend/src/api/system/role.js` lines 21-27 ExportNamedDeclaration: addRole
  - 基线：源语句 sha256=f1b972cc60c7b1f4990eb9fc21c99e3dbabf9afc7b17a4cf9fb081a2da0049ae；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/role.ts
- I00611 `ruoyi-fastapi-frontend/src/api/system/role.js` lines 30-36 ExportNamedDeclaration: updateRole
  - 基线：源语句 sha256=f0b1ae965d1e38ca8fabbd4f586a1a1d348b849ec920fc6fcaf9500c415dc708；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/role.ts
- I00612 `ruoyi-fastapi-frontend/src/api/system/role.js` lines 39-45 ExportNamedDeclaration: dataScope
  - 基线：源语句 sha256=46c69ee63f1ce3bcd45ee1ddc63798d73add76991be8c829a54aca104379bd6a；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/role.ts
- I00613 `ruoyi-fastapi-frontend/src/api/system/role.js` lines 48-58 ExportNamedDeclaration: changeRoleStatus
  - 基线：源语句 sha256=11465c2ec52259aefbf69117916c7da16178f5be92e8b7e4e5e9143e564985bc；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/role.ts
- I00614 `ruoyi-fastapi-frontend/src/api/system/role.js` lines 61-66 ExportNamedDeclaration: delRole
  - 基线：源语句 sha256=8f4e4e43bb6e80ad68431f90aca7fd7f00fc00f7186fd6a83ee2f884dd156e80；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/role.ts
- I00615 `ruoyi-fastapi-frontend/src/api/system/role.js` lines 69-75 ExportNamedDeclaration: allocatedUserList
  - 基线：源语句 sha256=9a37cbdda1d6a8babd695a575b366a089e3718b2dbc7f629db4a782821fadab3；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/role.ts
- I00616 `ruoyi-fastapi-frontend/src/api/system/role.js` lines 78-84 ExportNamedDeclaration: unallocatedUserList
  - 基线：源语句 sha256=1f76677c1696d07e820e98105a500e54997cd177b9f65ecdf798ca40bee24dc4；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/role.ts
- I00617 `ruoyi-fastapi-frontend/src/api/system/role.js` lines 87-93 ExportNamedDeclaration: authUserCancel
  - 基线：源语句 sha256=1062afb83deb04c514f5b4f712bfcaf85af636e64a57d4e35488316a74a05eb5；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/role.ts
- I00618 `ruoyi-fastapi-frontend/src/api/system/role.js` lines 96-102 ExportNamedDeclaration: authUserCancelAll
  - 基线：源语句 sha256=6f8dd04d692659ecf8a2af9731f05a2266644aa208b09c2b2770f56b0ad3160d；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/role.ts
- I00619 `ruoyi-fastapi-frontend/src/api/system/role.js` lines 105-111 ExportNamedDeclaration: authUserSelectAll
  - 基线：源语句 sha256=ec8ecfb836ca44d1a80f1c29d646a368b190b56fe58211ca4d9144d54adc8efe；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/role.ts
- I00620 `ruoyi-fastapi-frontend/src/api/system/role.js` lines 114-119 ExportNamedDeclaration: deptTreeSelect
  - 基线：源语句 sha256=4fc9e6da8d6eeafbb8824dab454ff4f8c4c89a0f0e0990ce9e7390a8eeaaec93；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/system/role.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
