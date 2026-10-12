# G017 Excel 导入弹窗

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

Excel 导入弹窗可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G005 HTTP 请求、会话提示与导出

## 正常、异常与边界检查条件

1. open 重置覆盖更新开关和文件队列，仅一个 xls/xlsx 可提交；无文件或后缀不符提示且不发送。
2. action 拼接 baseAPI，updateSupport 是 0/1，携带 Token；上传中禁用操作，成功关闭清理并展示 response.msg 后触发 success。
3. templateAction 未给不显示模板入口，给定时下载对应前缀命名 xlsx；关闭重新打开状态清空，上传失败按原表现登记并对照。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0305 | ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue / L25-L137 script-setup 完整内容 | react-front/src/components/ExcelImportDialog/index.tsx |
| I0306 | ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue / L1-L23 template 完整内容 | react-front/src/components/ExcelImportDialog/index.tsx |
| I0307 | ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/ExcelImportDialog/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/components/ExcelImportDialog/index.vue

逻辑定位：open@L79–87, handleClose@L90–94, handleDownloadTemplate@L97–99, handleProgress@L102–104, handleFileChange@L107–109, handleFileRemove@L112–114, handleSuccess@L117–124, handleSubmit@L127–134.
全部模板事件/权限：close=handleClose@L2; click=handleDownloadTemplate@L12; click=handleSubmit@L18; click=visible = false@L19.
