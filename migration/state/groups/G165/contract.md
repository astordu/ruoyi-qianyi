# G165 src/components/Crontab/result.vue：完整能力

依赖：G000, G028, G253F033

本组以以下完整源段为行为基线。实施前重读源码，选定同输入、输出、异常、状态与副作用案例；测试不得从目标实现倒推。

逐项合同（函数内所有分支、模板事件/插值、静态模板与全部样式均保留）：

- I01163 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` lines 16-16 ImportDeclaration: 
  - 基线：源语句 sha256=c96626dab5b188b462677c3b57366afd29db60c839effc1d99e98e6139fa40a4；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/Crontab/result.tsx
- I01164 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` lines 17-17 ImportDeclaration: 
  - 基线：源语句 sha256=f2c3ea9218322e89dc8d9ea031dbdffda0e5289f328a390fd5ecd276f36e7d84；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/Crontab/result.tsx
- I01165 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` lines 19-28 VariableDeclaration: props
  - 基线：源语句 sha256=9b8fe84a95433a962ffdcc07085969f6c528b385e76fd99925dff2c55cc69191；保留返回、异常及 0 个分支，调用=defineProps。
  - 去向：react-front/src/components/Crontab/result.tsx
- I01166 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` lines 29-29 VariableDeclaration: resultList
  - 基线：源语句 sha256=70bf2df2047f865cbbffccbc5fab99dd32f9c2ebdc4aae9ed224bb3ca441fb4e；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/result.tsx
- I01167 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` lines 30-30 VariableDeclaration: resultTimeZone
  - 基线：源语句 sha256=8310936f5de96172bef20be3f4bf5f19f415d7fb0dd624b4e990cf3afe079fb0；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/result.tsx
- I01168 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` lines 31-31 VariableDeclaration: loading
  - 基线：源语句 sha256=360133162609dea18ceb29cc60a4fd9166a9ed26b0d8544941212d26502f30ef；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/result.tsx
- I01169 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` lines 32-32 VariableDeclaration: errorMessage
  - 基线：源语句 sha256=fa92ad5a68aa0ac1feb49b49e20ff57ef534bdc203ffd873a77fddd4dab31664；保留返回、异常及 0 个分支，调用=ref。
  - 去向：react-front/src/components/Crontab/result.tsx
- I01170 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` lines 33-33 VariableDeclaration: previewRequestSequence
  - 基线：源语句 sha256=156a7c9b425cd3454b5d9e7df4383e3af0b649fe8bba37fa9fc356367f9c703f；保留返回、异常及 0 个分支，调用=。
  - 去向：react-front/src/components/Crontab/result.tsx
- I01171 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` lines 35-69 ExpressionStatement: 
  - 基线：源语句 sha256=aee18fc5de24d578e96a91e4be52fabc5ec171746fdcbc2f58508c87063c9b5e；保留返回、异常及 8 个分支，调用=watch, setTimeout, previewJob, onCleanup, clearTimeout, controller.abort。
  - 去向：react-front/src/components/Crontab/result.tsx
- I01172 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` template lines 1-13（完整静态文本/DOM/插槽）
  - 基线：保持完整原模板的文案、层级、props/slots 和条件挂载/隐藏语义；组件样式替换仍需原界面对照。
  - 去向：react-front/src/components/Crontab/result.tsx
- I01173 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` template line 2: v-bind:aria-busy
  - 基线：原表达式：loading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/result.tsx
- I01174 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` template line 4: v-if:
  - 基线：原表达式：errorMessage；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/result.tsx
- I01175 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` template line 5: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/result.tsx
- I01176 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` template line 6: v-if:
  - 基线：原表达式：loading；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/result.tsx
- I01177 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` template line 7: v-else-if:
  - 基线：原表达式：!resultList.length；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/result.tsx
- I01178 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` template line 8: v-for:
  - 基线：原表达式：item in resultList；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/result.tsx
- I01179 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` template line 8: v-else:
  - 基线：原表达式：；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/result.tsx
- I01180 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` template line 8: v-bind:key
  - 基线：原表达式：item；分别验证受控值/事件参数/分支/列表键。
  - 去向：react-front/src/components/Crontab/result.tsx
- I01181 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` template interpolation line 3
  - 基线：原显示表达式：resultTimeZone
  - 去向：react-front/src/components/Crontab/result.tsx
- I01182 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` template interpolation line 4
  - 基线：原显示表达式：errorMessage
  - 去向：react-front/src/components/Crontab/result.tsx
- I01183 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` template interpolation line 9
  - 基线：原显示表达式：formatBusinessTime(item, 'YYYY-MM-DD HH:mm:ss Z', resultTimeZone)
  - 去向：react-front/src/components/Crontab/result.tsx
- I01184 `ruoyi-fastapi-frontend/src/components/Crontab/result.vue` style[0] lines 72-76
  - 基线：保留全部选择器、声明和 url；lang=css, scoped=True；原样式选择器在 source-audit.json。
  - 去向：react-front/src/components/Crontab/result.tsx

验证：纯函数直接比较原/新正常、空值、边界及异常；状态动作比较变化与清理；API 比较 method/url/参数/错误；组件独立挂载比较 props、受控值、回调和交互；页面比较操作与请求；资源比内容与真实加载。

大文件函数组使用显式注入的共享状态/依赖接口，保留原调用次序；生命周期启动及页面按钮接线由 V 组验证。循环闭环成员不得拆掉依赖或增加占位实现。

全文件结构审阅已经完成，语义等价仍待逐组实施与验证。当前合同中的源段是检查范围，真正的案例、固定条件与运行证据应在实施前记录 baseline.md；必要条件缺失则不通过。

待集成：所属 J 合同及 dependency-edges.json 的运行时回调、动态 import、glob、全局注册；本组通过仅证明实际执行的本组条件。
