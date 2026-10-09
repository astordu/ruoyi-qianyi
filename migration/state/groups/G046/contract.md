# G046 src/api/tool/gen.js：完整能力

依赖：G000, G249

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00639 `ruoyi-fastapi-frontend/src/api/tool/gen.js` lines 1-1 ImportDeclaration: 
  - 基线：源语句 sha256=cd462474cb30a9a5954fbd44474b2f4e19f6d48d3c7dff5aebf452db4c8517f8；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/api/tool/gen.ts
- I00640 `ruoyi-fastapi-frontend/src/api/tool/gen.js` lines 4-9 ExportNamedDeclaration: listDataSources
  - 基线：源语句 sha256=6340dd82040f53929e5291c1a47471911d866712e1eede7d0847ad855a85e70a；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/tool/gen.ts
- I00641 `ruoyi-fastapi-frontend/src/api/tool/gen.js` lines 12-18 ExportNamedDeclaration: listTable
  - 基线：源语句 sha256=bd8edd8fae24c5d21248de8eacd3914287b8ce965c217ad4674ab4bb185b5608；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/tool/gen.ts
- I00642 `ruoyi-fastapi-frontend/src/api/tool/gen.js` lines 20-26 ExportNamedDeclaration: listDbTable
  - 基线：源语句 sha256=e06a37e16671a5174ec13287ab0044b32a0fb4fd984c3cd7b37fa033482b9c7b；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/tool/gen.ts
- I00643 `ruoyi-fastapi-frontend/src/api/tool/gen.js` lines 29-34 ExportNamedDeclaration: getGenTable
  - 基线：源语句 sha256=f4eed47c2e945aa69415c9448bb01eeb0088b6f0b338a2e35631d23a67edca70；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/tool/gen.ts
- I00644 `ruoyi-fastapi-frontend/src/api/tool/gen.js` lines 37-43 ExportNamedDeclaration: updateGenTable
  - 基线：源语句 sha256=b3fd4fc7d1b3744900e003ec192a833a450d7d137008c04a0a156ddd85257815；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/tool/gen.ts
- I00645 `ruoyi-fastapi-frontend/src/api/tool/gen.js` lines 46-52 ExportNamedDeclaration: importTable
  - 基线：源语句 sha256=babbf2ce9aebcc5ad1fbd12cbf4d9d2f84b71d22639d48e77efa579b1ee2aee4；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/tool/gen.ts
- I00646 `ruoyi-fastapi-frontend/src/api/tool/gen.js` lines 55-61 ExportNamedDeclaration: createTable
  - 基线：源语句 sha256=5260adc83f1cb18b0ffb8d36355461da5c5c045e192696e19bee5c8340946bc2；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/tool/gen.ts
- I00647 `ruoyi-fastapi-frontend/src/api/tool/gen.js` lines 64-69 ExportNamedDeclaration: previewTable
  - 基线：源语句 sha256=ff7b101ad5f75bc89203f53d32b5b9b48ba226b79f217163007afa6b5fe61fca；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/tool/gen.ts
- I00648 `ruoyi-fastapi-frontend/src/api/tool/gen.js` lines 72-77 ExportNamedDeclaration: delTable
  - 基线：源语句 sha256=31cc0ead292abfe0f7096e4662586a778830e9a16c1242d0f05611d918aa2ef8；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/tool/gen.ts
- I00649 `ruoyi-fastapi-frontend/src/api/tool/gen.js` lines 80-86 ExportNamedDeclaration: genCode
  - 基线：源语句 sha256=d963ae26f3fbd4d3db2653a7741935359a55c1c72bc0d4098a58c60db7430f34；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/tool/gen.ts
- I00650 `ruoyi-fastapi-frontend/src/api/tool/gen.js` lines 89-95 ExportNamedDeclaration: synchDb
  - 基线：源语句 sha256=49e089e7b0acee55af274c88ff2c02899b8cbcbe4f9a6bf3a6199513fdecc8e1；保留返回、异常及 1 个分支，调用=request。
  - 去向：react-front/src/api/tool/gen.ts

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
