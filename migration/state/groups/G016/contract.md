# G016 业务依赖、插件和既有测试命令接入

依赖：G000

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I00037 `ruoyi-fastapi-frontend/package.json` JSON scripts.test:plugin
  - 基线：保留 test:plugin 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00038 `ruoyi-fastapi-frontend/package.json` JSON scripts.test:time
  - 基线：保留 test:time 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00041 `ruoyi-fastapi-frontend/package.json` JSON dependencies.@ant-design/icons-vue
  - 基线：保留 @ant-design/icons-vue 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00042 `ruoyi-fastapi-frontend/package.json` JSON dependencies.@antv/g2plot
  - 基线：保留 @antv/g2plot 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00043 `ruoyi-fastapi-frontend/package.json` JSON dependencies.@antv/infographic
  - 基线：保留 @antv/infographic 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00044 `ruoyi-fastapi-frontend/package.json` JSON dependencies.@element-plus/icons-vue
  - 基线：保留 @element-plus/icons-vue 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00045 `ruoyi-fastapi-frontend/package.json` JSON dependencies.@terrastruct/d2
  - 基线：保留 @terrastruct/d2 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00046 `ruoyi-fastapi-frontend/package.json` JSON dependencies.@vueup/vue-quill
  - 基线：保留 @vueup/vue-quill 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00047 `ruoyi-fastapi-frontend/package.json` JSON dependencies.@vueuse/core
  - 基线：保留 @vueuse/core 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00048 `ruoyi-fastapi-frontend/package.json` JSON dependencies.ant-design-vue
  - 基线：保留 ant-design-vue 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00049 `ruoyi-fastapi-frontend/package.json` JSON dependencies.axios
  - 基线：保留 axios 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00050 `ruoyi-fastapi-frontend/package.json` JSON dependencies.clipboard
  - 基线：保留 clipboard 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00051 `ruoyi-fastapi-frontend/package.json` JSON dependencies.dayjs
  - 基线：保留 dayjs 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00052 `ruoyi-fastapi-frontend/package.json` JSON dependencies.echarts
  - 基线：保留 echarts 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00053 `ruoyi-fastapi-frontend/package.json` JSON dependencies.element-plus
  - 基线：保留 element-plus 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00054 `ruoyi-fastapi-frontend/package.json` JSON dependencies.file-saver
  - 基线：保留 file-saver 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00055 `ruoyi-fastapi-frontend/package.json` JSON dependencies.fuse.js
  - 基线：保留 fuse.js 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00056 `ruoyi-fastapi-frontend/package.json` JSON dependencies.js-beautify
  - 基线：保留 js-beautify 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00057 `ruoyi-fastapi-frontend/package.json` JSON dependencies.js-cookie
  - 基线：保留 js-cookie 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00058 `ruoyi-fastapi-frontend/package.json` JSON dependencies.jsencrypt
  - 基线：保留 jsencrypt 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00059 `ruoyi-fastapi-frontend/package.json` JSON dependencies.katex
  - 基线：保留 katex 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00060 `ruoyi-fastapi-frontend/package.json` JSON dependencies.markstream-vue
  - 基线：保留 markstream-vue 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00061 `ruoyi-fastapi-frontend/package.json` JSON dependencies.mermaid
  - 基线：保留 mermaid 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00062 `ruoyi-fastapi-frontend/package.json` JSON dependencies.monaco-editor
  - 基线：保留 monaco-editor 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00063 `ruoyi-fastapi-frontend/package.json` JSON dependencies.nprogress
  - 基线：保留 nprogress 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00064 `ruoyi-fastapi-frontend/package.json` JSON dependencies.pinia
  - 基线：保留 pinia 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00065 `ruoyi-fastapi-frontend/package.json` JSON dependencies.shiki
  - 基线：保留 shiki 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00066 `ruoyi-fastapi-frontend/package.json` JSON dependencies.stream-diffs
  - 基线：保留 stream-diffs 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00067 `ruoyi-fastapi-frontend/package.json` JSON dependencies.stream-markdown
  - 基线：保留 stream-markdown 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00068 `ruoyi-fastapi-frontend/package.json` JSON dependencies.stream-monaco
  - 基线：保留 stream-monaco 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00069 `ruoyi-fastapi-frontend/package.json` JSON dependencies.uuid
  - 基线：保留 uuid 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00071 `ruoyi-fastapi-frontend/package.json` JSON dependencies.vue-cropper
  - 基线：保留 vue-cropper 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00072 `ruoyi-fastapi-frontend/package.json` JSON dependencies.vue-router
  - 基线：保留 vue-router 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00073 `ruoyi-fastapi-frontend/package.json` JSON dependencies.vuedraggable
  - 基线：保留 vuedraggable 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00075 `ruoyi-fastapi-frontend/package.json` JSON devDependencies.less
  - 基线：保留 less 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00076 `ruoyi-fastapi-frontend/package.json` JSON devDependencies.sass-embedded
  - 基线：保留 sass-embedded 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00077 `ruoyi-fastapi-frontend/package.json` JSON devDependencies.unplugin-auto-import
  - 基线：保留 unplugin-auto-import 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00078 `ruoyi-fastapi-frontend/package.json` JSON devDependencies.unplugin-vue-setup-extend-plus
  - 基线：保留 unplugin-vue-setup-extend-plus 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00080 `ruoyi-fastapi-frontend/package.json` JSON devDependencies.vite-plugin-compression
  - 基线：保留 vite-plugin-compression 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00081 `ruoyi-fastapi-frontend/package.json` JSON devDependencies.vite-plugin-monaco-editor-esm
  - 基线：保留 vite-plugin-monaco-editor-esm 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00082 `ruoyi-fastapi-frontend/package.json` JSON devDependencies.vite-plugin-svg-icons
  - 基线：保留 vite-plugin-svg-icons 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json
- I00083 `ruoyi-fastapi-frontend/package.json` JSON overrides.quill
  - 基线：保留 quill 的使用能力；Vue 专属依赖用 React 对应能力替换，普通库按实际引用接入。版本不是行为契约。
  - 去向：react-front/package.json

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
