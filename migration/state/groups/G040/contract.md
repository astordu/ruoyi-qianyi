# G040 公告管理、富文本与阅读人

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

公告管理、富文本与阅读人可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G005 HTTP 请求、会话提示与导出, G007 字典获取、缓存与标签展示, G010 会话、权限与路由策略, G012 分页与列表工具栏, G015 富文本编辑与图片粘贴, G019 业务文件上传、进度与重试, G022 顶部公告阅读与详情, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 公告标题/创建人/类型查询、分页、新增编辑删除；标题和类型校验，内容编辑支持 HTML 与业务文件附件。
2. 详情复用 HeaderNotice DetailView，阅读用户弹窗按 noticeId 分页/筛选/关闭清理；批量删除取消不请求。
3. 新增通知后顶部未读/阅读/全部已读与管理页阅读人保持一致；类型标签/状态与权限全部接真实后端。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0084 | ruoyi-fastapi-frontend/src/api/system/notice.js / L4-L10 完整导出 listNotice | react-front/src/api/system/notice.ts |
| I0086 | ruoyi-fastapi-frontend/src/api/system/notice.js / L21-L27 完整导出 addNotice | react-front/src/api/system/notice.ts |
| I0087 | ruoyi-fastapi-frontend/src/api/system/notice.js / L30-L36 完整导出 updateNotice | react-front/src/api/system/notice.ts |
| I0088 | ruoyi-fastapi-frontend/src/api/system/notice.js / L39-L44 完整导出 delNotice | react-front/src/api/system/notice.ts |
| I0092 | ruoyi-fastapi-frontend/src/api/system/notice.js / L73-L79 完整导出 listNoticeReadUsers | react-front/src/api/system/notice.ts |
| I0093 | ruoyi-fastapi-frontend/src/api/system/notice.js / 模块导入、注释及函数之间全部剩余内容 | react-front/src/api/system/notice.ts |
| I0628 | ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue / L48-L105 script-setup 完整内容 | react-front/src/views/system/notice/ReadUsers.tsx |
| I0629 | ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue / L1-L46 template 完整内容 | react-front/src/views/system/notice/ReadUsers.tsx |
| I0630 | ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue / L107-L118 style-1 完整内容 | react-front/src/views/system/notice/ReadUsers.tsx |
| I0631 | ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/notice/ReadUsers.tsx |
| I0632 | ruoyi-fastapi-frontend/src/views/system/notice/index.vue / L163-L298 script-setup 完整内容 | react-front/src/views/system/notice/index.tsx |
| I0633 | ruoyi-fastapi-frontend/src/views/system/notice/index.vue / L1-L161 template 完整内容 | react-front/src/views/system/notice/index.tsx |
| I0634 | ruoyi-fastapi-frontend/src/views/system/notice/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/notice/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/system/notice.js

逻辑定位：listNotice@L4–10, addNotice@L21–27, updateNotice@L30–36, delNotice@L39–44, listNoticeReadUsers@L73–79.
- URL/请求对象 L5: `'get' '/system/notice/list'`; params=`query`, data=`None`
- URL/请求对象 L22: `'post' '/system/notice'`; params=`None`, data=`data`
- URL/请求对象 L31: `'put' '/system/notice'`; params=`None`, data=`data`
- URL/请求对象 L40: `'delete' '/system/notice/' + noticeId`; params=`None`, data=`None`
- URL/请求对象 L74: `'get' '/system/notice/readUsers/list'`; params=`query`, data=`None`

### ruoyi-fastapi-frontend/src/views/system/notice/ReadUsers.vue

逻辑定位：open@L67–74, getList@L76–84, handleQuery@L86–89, resetQuery@L91–94, handleClose@L96–100.
全部模板事件/权限：close=handleClose@L2; keyup=handleQuery@L11; clear=handleQuery@L12; click=handleQuery@L16; click=resetQuery@L17; pagination=getList@L42.

### ruoyi-fastapi-frontend/src/views/system/notice/index.vue

逻辑定位：getList@L199–206, cancel@L208–211, reset@L213–222, handleQuery@L224–227, resetQuery@L229–232, handleSelectionChange@L234–238, handleAdd@L240–244, handleUpdate@L246–254, submitForm@L256–274, handleViewData@L277–279, handleReadUsers@L282–284, handleDelete@L287–295.
全部模板事件/权限：keyup=handleQuery@L10; keyup=handleQuery@L19; click=handleQuery@L33; click=resetQuery@L34; click=handleAdd@L44; =['system:notice:add']@L45; click=handleUpdate@L54; =['system:notice:edit']@L55; click=handleDelete@L64; =['system:notice:remove']@L65; queryTable=getList@L68; selection-change=handleSelectionChange@L71; click=handleViewData(scope.row)@L76; click=handleReadUsers(scope.row)@L97; =['system:notice:list']@L97; click=handleUpdate(scope.row)@L98; =['system:notice:edit']@L98; click=handleDelete(scope.row)@L99; =['system:notice:remove']@L99; pagination=getList@L109; click=submitForm@L153; click=cancel@L154.
