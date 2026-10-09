# G253 src/utils/time.js：状态、输入与依赖接口

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I02792 `ruoyi-fastapi-frontend/src/utils/time.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=d144ae029085bebc3008517b4e2366591cfc5559ba291f15f5a04d66de6a6fca；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/time.context.ts
- I02793 `ruoyi-fastapi-frontend/src/utils/time.js` lines 2-2 ImportDeclaration: 
  - 基线：源语句 sha256=d1d6c1d4794824077e91d6f890c6cd7f699ab0324e3184648f31aeb886691587；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/time.context.ts
- I02794 `ruoyi-fastapi-frontend/src/utils/time.js` lines 3-3 ImportDeclaration: 
  - 基线：源语句 sha256=883c1b2a6762ca8297c60d4c4f4714145bb35e43548cc1c068fe88ea32c7b2d3；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/time.context.ts
- I02795 `ruoyi-fastapi-frontend/src/utils/time.js` lines 4-4 ImportDeclaration: 
  - 基线：源语句 sha256=f422561f40fed26e79121b385d3648ed4599c811191f26cad11189e818d7440d；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/time.context.ts
- I02796 `ruoyi-fastapi-frontend/src/utils/time.js` lines 6-6 ExpressionStatement: 
  - 基线：源语句 sha256=fb90ce598f636aaf13e5fe04f91aeeb736f0574942c115d3b0d5fe377b05053b；保留返回、异常及 0 个分支，调用=dayjs.extend。
  - 去向：react-front/src/utils/time.context.ts
- I02797 `ruoyi-fastapi-frontend/src/utils/time.js` lines 8-8 VariableDeclaration: DATE_ONLY_PATTERN
  - 基线：源语句 sha256=9f9fdec85efaeab05baf207d7d1f52a2efcfc812f85a62b9236d25de366b2756；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/time.context.ts
- I02798 `ruoyi-fastapi-frontend/src/utils/time.js` lines 9-9 VariableDeclaration: WALL_TIME_PATTERN
  - 基线：源语句 sha256=9d7af41d39912735f73ce754d3f8bdccb7f8004dc65a49563fab7b3faad4d8ce；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/time.context.ts
- I02799 `ruoyi-fastapi-frontend/src/utils/time.js` lines 10-10 VariableDeclaration: RFC3339_PATTERN
  - 基线：源语句 sha256=84911de755a05c20b5910a9b875fd26de72cd77e92d81eeb47b2435777129395；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/time.context.ts
- I02800 `ruoyi-fastapi-frontend/src/utils/time.js` lines 11-11 VariableDeclaration: WEEKDAYS
  - 基线：源语句 sha256=962f1e648bcfc46ded970c595bcf87eb5eda69884a0e4249a73bcea0a169a2ea；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/time.context.ts
- I02801 `ruoyi-fastapi-frontend/src/utils/time.js` lines 12-12 VariableDeclaration: MILLISECONDS_PER_SECOND
  - 基线：源语句 sha256=b84caa9ba3ec5d01bda8178b11cb21d80561a8b80dc1302692f503c861763a2d；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/time.context.ts
- I02802 `ruoyi-fastapi-frontend/src/utils/time.js` lines 13-13 VariableDeclaration: MILLISECONDS_PER_MINUTE
  - 基线：源语句 sha256=13eccfb38d675bfc067f0cacd44f1a0791618300648f61a420d042550958f5d4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/time.context.ts
- I02803 `ruoyi-fastapi-frontend/src/utils/time.js` lines 14-14 VariableDeclaration: MILLISECONDS_PER_HOUR
  - 基线：源语句 sha256=d344c6a427ffea9ef42c2aa47e85b7b7cb2b303f8b0056cffd7afb4512fe0a4e；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/time.context.ts
- I02804 `ruoyi-fastapi-frontend/src/utils/time.js` lines 15-15 VariableDeclaration: ORIGINAL_TIME_FIELDS
  - 基线：源语句 sha256=9f84e0eac10fac37e7035c0aeedaa1fb82a5393ba72d1f5f3064a93894f67cf2；保留返回、异常及 0 个分支，调用=Symbol。
  - 去向：react-front/src/utils/time.context.ts
- I02805 `ruoyi-fastapi-frontend/src/utils/time.js` lines 16-16 VariableDeclaration: timezoneFormatters
  - 基线：源语句 sha256=bba6541a53f9cb5c32efdbb50cca7be36d10d9f0bf29757f4915657a3ccad664；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/utils/time.context.ts
- I02806 `ruoyi-fastapi-frontend/src/utils/time.js` lines 18-18 VariableDeclaration: businessTimezone
  - 基线：源语句 sha256=50e514efe2df442eab018b9c2b1d76feef08e34b913c7d922ae0cab9e85885f2；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/utils/time.context.ts
- I02807 `ruoyi-fastapi-frontend/src/utils/time.js` lines 19-19 VariableDeclaration: userTimezone
  - 基线：源语句 sha256=46738e49e6966ad7ba56243e6e8a97917b034aace08b32c8733375d27cf43b09；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/utils/time.context.ts
- I02808 `ruoyi-fastapi-frontend/src/utils/time.js` lines 20-20 VariableDeclaration: deviceTimezone
  - 基线：源语句 sha256=88439c013123b191df03a6f298e63bc04e7f6337b6c930a2d27d2f06965f9d66；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/utils/time.context.ts
- I02809 `ruoyi-fastapi-frontend/src/utils/time.js` lines 25-36 ExportNamedDeclaration: TimeInputError
  - 基线：源语句 sha256=16ba83a50ac6d38a6217b34a9d8d611e9bcb48ac2b8593dddd1c44f89533d484；保留返回、异常及 0 个分支，调用=Super。
  - 去向：react-front/src/utils/time.context.ts
- I02835 `ruoyi-fastapi-frontend/src/utils/time.js` lines 523-523 ExpressionStatement: 
  - 基线：源语句 sha256=708ab367af25f68ac2f7f11b186534dc3f941e41f1a2ebabe0f46b1fd8f6b4d2；保留返回、异常及 0 个分支，调用=setBusinessTimezone。
  - 去向：react-front/src/utils/time.context.ts
- I02836 `ruoyi-fastapi-frontend/src/utils/time.js` lines 524-524 ExpressionStatement: 
  - 基线：源语句 sha256=abb5f07d45239ee7d1e5ccc2be3caa986911b093cd59d9071ef644ec7f054911；保留返回、异常及 0 个分支，调用=refreshDeviceTimezone。
  - 去向：react-front/src/utils/time.context.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
