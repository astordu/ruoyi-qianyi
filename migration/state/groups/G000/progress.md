# G000 实施记录

React 19 + TypeScript 7 + Vite 8 建立在原本为空的 react-front；保留中文标题、原启动 HTML 与加载动画、favicon、四套环境键值、代理和构建产物命名。React Router 与 Ant Design 延续既定目标架构，当前组尚不需要，后续组接入。

31 个源内容项的目标定位已写 plan.json。额外工程文件和本组测试已登记 group.targets。IE 源文件实际在 html/ie.html，按入口引用复制到目标 public/html/ie.html；该源文件自身所属的后续资源组仍待验证，不提前计完成。

原版基线从源码取得，加载态使用原 HTML 运行夹具；没有运行 Vue 业务页面，没有后端写操作。首次基线/复制命令因路径和工作目录失败，已纠正；首次类型检查发现 TS7 删除 baseUrl，改用相对 paths 后通过。未隐藏失败或删除断言。

App.tsx 当前为工程启动诊断，不能算任何业务页面迁移。原 main.js 的全部插件、全局注册、业务路由/权限守卫仍在各自组等待；压缩、SVG symbol 与 Monaco workers 未宣称完成。

公共影响：目标第一次初始化，没有已迁移业务组受到影响。源 Vue 与后端均只读。接下来执行本组验证并由 record 命令记账，本轮不选第二组。

验证已完成：record 命令登记 G000 passed；最后 check 显示 1/773 小组通过，源快照一致，无失效验证；本轮结束，未选择第二组。
