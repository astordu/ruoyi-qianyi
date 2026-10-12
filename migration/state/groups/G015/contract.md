# G015 富文本编辑与图片粘贴

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

富文本编辑与图片粘贴可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G005 HTTP 请求、会话提示与导出, G009 系统主题与布局偏好

## 正常、异常与边界检查条件

1. HTML modelValue、内容变化、readonly/height/minHeight 与工具栏配置保持旧编辑行为；Quill 实例和事件卸载清理。
2. 粘贴剪贴板图片和按钮上传都先按图片类型、默认 5MB 限制校验，成功在当前光标插入 baseAPI+路径；业务失败/网络失败关闭 loading 并提示。
3. 输入空内容与外部更新分别验证，光标位置与图片预览按原 UI 核对，不能用普通 textarea 替代。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0301 | ruoyi-fastapi-frontend/src/components/Editor/index.vue / L29-L196 script-setup 完整内容 | react-front/src/components/Editor/index.tsx |
| I0302 | ruoyi-fastapi-frontend/src/components/Editor/index.vue / L1-L27 template 完整内容 | react-front/src/components/Editor/index.tsx |
| I0303 | ruoyi-fastapi-frontend/src/components/Editor/index.vue / L198-L276 style-1 完整内容 | react-front/src/components/Editor/index.tsx |
| I0304 | ruoyi-fastapi-frontend/src/components/Editor/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/Editor/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/components/Editor/index.vue

逻辑定位：handleBeforeUpload@L133–150, handleUploadSuccess@L153–167, handleUploadError@L170–172, handlePasteCapture@L175–187, insertImage@L189–195.
全部模板事件/权限：textChange=(e) => $emit('update:modelValue', content)@L22.
