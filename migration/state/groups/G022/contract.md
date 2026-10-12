# G022 顶部公告阅读与详情

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

顶部公告阅读与详情可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G005 HTTP 请求、会话提示与导出, G008 SVG 图标与图标选择器, G009 系统主题与布局偏好

## 正常、异常与边界检查条件

1. listTop 回显 unreadCount；预览未读公告才 markRead 并更新计数，全部已读使用实际 ids，空列表不请求。
2. DetailView.open 支持对象预载和 id 查询，通知/公告/消息标签、HTML 内容、空数据及关闭清理保留。
3. 悬浮通知弹层、进入/离开计时与监听不累加；读取/全部读取请求失败按源状态和统一提示重放。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0085 | ruoyi-fastapi-frontend/src/api/system/notice.js / L13-L18 完整导出 getNotice | react-front/src/api/system/notice-headernotice.ts |
| I0089 | ruoyi-fastapi-frontend/src/api/system/notice.js / L47-L52 完整导出 listNoticeTop | react-front/src/api/system/notice-headernotice.ts |
| I0090 | ruoyi-fastapi-frontend/src/api/system/notice.js / L55-L61 完整导出 markNoticeRead | react-front/src/api/system/notice-headernotice.ts |
| I0091 | ruoyi-fastapi-frontend/src/api/system/notice.js / L64-L70 完整导出 markNoticeReadAll | react-front/src/api/system/notice-headernotice.ts |
| I0386 | ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue / L55-L112 script-setup 完整内容 | react-front/src/layout/components/HeaderNotice/DetailView.tsx |
| I0387 | ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue / L1-L53 template 完整内容 | react-front/src/layout/components/HeaderNotice/DetailView.tsx |
| I0388 | ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue / L114-L308 style-1 完整内容 | react-front/src/layout/components/HeaderNotice/DetailView.tsx |
| I0389 | ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue / L310-L326 style-2 完整内容 | react-front/src/layout/components/HeaderNotice/DetailView.tsx |
| I0390 | ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/layout/components/HeaderNotice/DetailView.tsx |
| I0391 | ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue / L40-L105 script-setup 完整内容 | react-front/src/layout/components/HeaderNotice/index.tsx |
| I0392 | ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue / L1-L38 template 完整内容 | react-front/src/layout/components/HeaderNotice/index.tsx |
| I0393 | ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue / L107-L184 style-1 完整内容 | react-front/src/layout/components/HeaderNotice/index.tsx |
| I0394 | ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/layout/components/HeaderNotice/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/system/notice.js

逻辑定位：getNotice@L13–18, listNoticeTop@L47–52, markNoticeRead@L55–61, markNoticeReadAll@L64–70.
- URL/请求对象 L14: `'get' '/system/notice/' + noticeId`; params=`None`, data=`None`
- URL/请求对象 L48: `'get' '/system/notice/listTop'`; params=`None`, data=`None`
- URL/请求对象 L56: `'post' '/system/notice/markRead'`; params=`{ noticeId }`, data=`None`
- URL/请求对象 L65: `'post' '/system/notice/markReadAll'`; params=`{ ids }`, data=`None`

### ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/DetailView.vue

逻辑定位：open@L72–101, handleClose@L103–107.
全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/layout/components/HeaderNotice/index.vue

逻辑定位：loadNoticeTop@L53–61, onNoticeEnter@L66–79, onNoticeLeave@L82–84, previewNotice@L87–95, markAllRead@L98–104.
全部模板事件/权限：click=markAllRead@L7; click=previewNotice(item)@L17; mouseenter=onNoticeEnter@L28; mouseleave=onNoticeLeave@L28.
