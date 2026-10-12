# G020 图片上传与预览

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

图片上传与预览可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G005 HTTP 请求、会话提示与导出, G009 系统主题与布局偏好

## 正常、异常与边界检查条件

1. 默认数量5、5MB、png/jpg/jpeg，类型/MIME/扩展名与逗号名称规则按源实现；本地 blob URL 不写回最终字符串。
2. 旧字符串/数组/绝对相对 URL 回显，上传并发成功计数聚合、排序/删除/禁用/预览弹窗与 modelValue 相互一致。
3. ImagePreview 单图/多图、宽高、失败占位、预览列表与 baseAPI 前缀不重加；错误路径释放 loading 并按原版提示。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0325 | ruoyi-fastapi-frontend/src/components/ImagePreview/index.vue / L17-L68 script-setup 完整内容 | react-front/src/components/ImagePreview/index.tsx |
| I0326 | ruoyi-fastapi-frontend/src/components/ImagePreview/index.vue / L1-L15 template 完整内容 | react-front/src/components/ImagePreview/index.tsx |
| I0327 | ruoyi-fastapi-frontend/src/components/ImagePreview/index.vue / L70-L92 style-1 完整内容 | react-front/src/components/ImagePreview/index.tsx |
| I0328 | ruoyi-fastapi-frontend/src/components/ImagePreview/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/ImagePreview/index.tsx |
| I0329 | ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue / L50-L247 script-setup 完整内容 | react-front/src/components/ImageUpload/index.tsx |
| I0330 | ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue / L1-L48 template 完整内容 | react-front/src/components/ImageUpload/index.tsx |
| I0331 | ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue / L249-L258 style-1 完整内容 | react-front/src/components/ImageUpload/index.tsx |
| I0332 | ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/ImageUpload/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/components/ImagePreview/index.vue

全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/components/ImageUpload/index.vue

逻辑定位：default@L79–79, handleBeforeUpload@L134–166, handleExceed@L169–171, handleUploadSuccess@L174–185, handleDelete@L188–195, uploadedSuccessfully@L198–206, handleUploadError@L209–212, handlePictureCardPreview@L215–218, listToString@L221–230, onEnd@L238–242.
- URL/请求对象 L120: `(非请求URL对象) baseUrl + item`; params=`None`, data=`None`
- URL/请求对象 L122: `(非请求URL对象) item`; params=`None`, data=`None`
- URL/请求对象 L176: `(非请求URL对象) res.fileName`; params=`None`, data=`None`
全部模板事件/权限：.
