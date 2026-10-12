# G019 业务文件上传、进度与重试

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

业务文件上传、进度与重试可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G005 HTTP 请求、会话提示与导出, G009 系统主题与布局偏好, G011 普通与分段文件下载

## 正常、异常与边界检查条件

1. 模型只接收含 fileId 的对象数组；输出 fileId/name/url 与 getFileIds 保持，不能降为逗号 URL 字符串。
2. 文件数含正在上传数量，扩展名/大小/逗号名校验；uploadData 的数组逐值 append，忽略 null/undefined，进度依 event.total 更新。
3. 成功必须含 fileId 与 downloadUrl；失败文件独立显示可重试/删除，重试保留文件与上传参数；禁用/排序/清空和所有请求结束后的状态一致。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0257 | ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue / L105-L513 script-setup 完整内容 | react-front/src/components/BusinessFileUpload/index.tsx |
| I0258 | ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue / L1-L103 template 完整内容 | react-front/src/components/BusinessFileUpload/index.tsx |
| I0259 | ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue / L515-L565 style-1 完整内容 | react-front/src/components/BusinessFileUpload/index.tsx |
| I0260 | ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/BusinessFileUpload/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/components/BusinessFileUpload/index.vue

逻辑定位：default@L112–112, default@L122–122, default@L137–137, handleBeforeUpload@L183–212, handleUploadRequest@L220–222, uploadFile@L231–254, onUploadProgress@L244–248, appendUploadData@L262–273, handleUploadSuccess@L282–296, handleUploadError@L305–314, handleRetry@L322–331, handleDownload@L339–341, handleDelete@L349–351, handleRemoveFailed@L359–363, updateModel@L371–381, getFileIds@L388–390, initSortable@L397–414, onEnd@L407–412, clearInternalFiles@L421–425, uploadingCount@L432–435, normalizeFileList@L443–458, toModelFile@L466–472, getFileExtension@L480–483, getFileName@L491–494, getErrorMessage@L502–504.
- URL/请求对象 L235: `"post" props.action`; params=`None`, data=`formData`
- URL/请求对象 L286: `(非请求URL对象) response.downloadUrl`; params=`None`, data=`None`
- URL/请求对象 L449: `(非请求URL对象) item.url || item.downloadUrl || item.fileName || ""`; params=`None`, data=`None`
- URL/请求对象 L467: `(非请求URL对象) file.url`; params=`None`, data=`None`
全部模板事件/权限：click=handleDownload(file)@L46; click=handleDelete(file.fileId)@L54; click=handleRetry(file)@L87; click=handleRemoveFailed(file.uid)@L95.
