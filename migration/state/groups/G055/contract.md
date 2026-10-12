# G055 AI 会话、图片输入与流式回答

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

AI 会话、图片输入与流式回答可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；会话状态、图片和流处理共同组成聊天页闭环，AiMessage 随页迁；可多次会话续做，不能将单个流事件变成迁移组。后端仍声明 Vue 渲染依赖，React替换包与插件依赖检查的兼容验证需单独记录。

依赖：G005 HTTP 请求、会话提示与导出, G008 SVG 图标与图标选择器, G011 普通与分段文件下载, G023 应用入口与响应式导航布局, G054 AI 模型管理

## 正常、异常与边界检查条件

1. 读取已启用模型并选择首项，切换温度；会话按 createdAt 排序、加载当前会话去重、删除当前后清空，用户配置编辑复制后保存并重读。
2. 发送文本/图片前校验模型，用户与助手消息状态、sessionId/runId、content/reasoning/meta/run_info/metrics/error 逐行JSON流按源处理；这是NDJSON，不改成SSE。跨块残余buffer保留，原done时未消费最后无换行数据的边界列为观察点，错误结束解除loading。
3. 停止生成向后端 cancelChatRun 并终止 AbortController；不要只停止前端显示而让服务端继续运行。
4. 图片最多10张与用户配置MB限制、认证 /common/upload、多张合并与失败提示；visionEnabled与模型图片能力分支按实际源码类型判断，配置字符串/Boolean基线需核对。
5. Markdown/推理折叠、代码高亮/复制、数学/图表能力采用真实 React 渲染替换 markstream-vue，保持消息内容与插件菜单契约；选型不改变后端npm检查声明，兼容性差异在集成登记。
6. 用户向上滚动距离>100暂停自动滚动，接近底部<20恢复；流式更新的RAF/timeout/resize与页面离开清理、图片URL回显和token指标完整。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0018 | ruoyi-fastapi-frontend/plugins/ai/api/chat.js / L1-L54 module 完整内容 | react-front/plugins/ai/api/chat.ts |
| I0020 | ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue / L43-L80 script-setup 完整内容 | react-front/plugins/ai/views/chat/components/AiMessage.tsx |
| I0021 | ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue / L1-L41 template 完整内容 | react-front/plugins/ai/views/chat/components/AiMessage.tsx |
| I0022 | ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue / L82-L182 style-1 完整内容 | react-front/plugins/ai/views/chat/components/AiMessage.tsx |
| I0023 | ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue / SFC 外壳、块属性与全部块间注释 | react-front/plugins/ai/views/chat/components/AiMessage.tsx |
| I0024 | ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue / L413-L900 script-setup 完整内容 | react-front/plugins/ai/views/chat/index.tsx |
| I0025 | ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue / L1-L411 template 完整内容 | react-front/plugins/ai/views/chat/index.tsx |
| I0026 | ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue / L902-L1338 style-1 完整内容 | react-front/plugins/ai/views/chat/index.tsx |
| I0027 | ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/plugins/ai/views/chat/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/plugins/ai/api/chat.js

逻辑定位：listChatSession@L4–9, delChatSession@L12–17, getChatSession@L20–25, getUserChatConfig@L28–33, saveUserChatConfig@L36–42, cancelChatRun@L45–53.
- URL/请求对象 L5: `"get" "/ai/chat/session/list"`; params=`None`, data=`None`
- URL/请求对象 L13: `"delete" "/ai/chat/session/" + sessionId`; params=`None`, data=`None`
- URL/请求对象 L21: `"get" "/ai/chat/session/" + sessionId`; params=`None`, data=`None`
- URL/请求对象 L29: `"get" "/ai/chat/config"`; params=`None`, data=`None`
- URL/请求对象 L37: `"put" "/ai/chat/config"`; params=`None`, data=`data`
- URL/请求对象 L46: `"post" "/ai/chat/cancel"`; params=`None`, data=`{ runId: runId, }`

### ruoyi-fastapi-frontend/plugins/ai/views/chat/components/AiMessage.vue

逻辑定位：toggleReasoning@L77–79.
全部模板事件/权限：click=toggleReasoning@L4.

### ruoyi-fastapi-frontend/plugins/ai/views/chat/index.vue

逻辑定位：generateSessionId@L454–456, loadUserConfig@L496–503, openConfigDialog@L505–508, handleSaveConfig@L510–517, hasMetrics@L519–529, getImageUrl@L531–541, formatTime@L543–551, getModels@L553–563, getSessions@L573–587, loadSession@L589–601, handleDeleteSession@L603–617, sendRequest@L619–722, clearChat@L724–728, copyText@L730–743, triggerImageUpload@L745–752, handleImageInputChange@L754–797, handleSend@L799–815, stopGeneration@L817–839, handleScroll@L841–854, scrollToBottom@L856–878, handleMainAction@L880–886.
全部模板事件/权限：click=clearChat@L11; click=loadSession(session.sessionId)@L23; click=handleDeleteSession(session.sessionId)@L41; click=openConfigDialog@L65; scroll=handleScroll@L84; click=copyText(msg.content)@L152; keydown=handleSend@L233; click=triggerImageUpload@L264; click=chatConfig.isReasoning = !chatConfig.isReasoning@L276; click=handleMainAction@L287; click=showConfigDialog = false@L396; click=handleSaveConfig@L397; change=handleImageInputChange@L408.
