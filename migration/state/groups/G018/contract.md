# G018 通用文件附件上传

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

通用文件附件上传可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G005 HTTP 请求、会话提示与导出, G009 系统主题与布局偏好, G011 普通与分段文件下载

## 正常、异常与边界检查条件

1. 默认数量 5、大小 5MB、doc/docx/xls/xlsx/ppt/pptx/txt/pdf 类型；逗号文件名拒绝，多文件上传聚合完成才写 modelValue。
2. 字符串/数组输入归一化、baseAPI 路径回显、删除、拖动排序后按旧逗号格式输出；禁用与 drag/tip props 保留。
3. 业务 code 失败与网络失败撤销正在上传计数并关闭提示；/common/files/ 资源使用认证下载，其他地址走原下载入口。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0308 | ruoyi-fastapi-frontend/src/components/FileUpload/index.vue / L48-L250 script-setup 完整内容 | react-front/src/components/FileUpload/index.tsx |
| I0309 | ruoyi-fastapi-frontend/src/components/FileUpload/index.vue / L1-L46 template 完整内容 | react-front/src/components/FileUpload/index.tsx |
| I0310 | ruoyi-fastapi-frontend/src/components/FileUpload/index.vue / L252-L276 style-1 完整内容 | react-front/src/components/FileUpload/index.tsx |
| I0311 | ruoyi-fastapi-frontend/src/components/FileUpload/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/FileUpload/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/components/FileUpload/index.vue

逻辑定位：default@L81–81, handleBeforeUpload@L133–160, handleExceed@L163–165, handleUploadError@L168–171, handleUploadSuccess@L174–185, handleFileDownload@L188–193, handleDelete@L196–199, uploadedSuccessfully@L202–210, getFileName@L213–220, listToString@L223–232, onEnd@L241–245.
- URL/请求对象 L121: `(非请求URL对象) item`; params=`None`, data=`None`
- URL/请求对象 L176: `(非请求URL对象) res.fileName`; params=`None`, data=`None`
全部模板事件/权限：click=handleFileDownload($event, file)@L36; click=handleDelete(index)@L41.
