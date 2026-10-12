# G011 普通与分段文件下载

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

普通与分段文件下载可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G005 HTTP 请求、会话提示与导出

## 正常、异常与边界检查条件

1. name/resource/file/zip/saveAs 四种下载入口与 encoded 文件名、delete 参数、Bearer Header、错误 JSON 提示保持源码语义。
2. Range 块大小 8MB；网络/5xx 最多额外重试两次，4xx 不重试。首块 416 回退完整下载，中途 416 报错。
3. 206 Content-Range 必须连续、大小一致且 total>end；组装最终 Blob，200 返回整文件；resource 使用响应文件名，file 缺失文件名回退路径尾段，zip loading 成败都关闭。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0449 | ruoyi-fastapi-frontend/src/plugins/download.js / L1-L191 module 完整内容 | react-front/src/plugins/download.ts |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/plugins/download.js

逻辑定位：parseContentRange@L13–23, isRetryableDownloadError@L25–27, requestDownloadChunk@L29–50, requestFullDownload@L52–59, downloadByRange@L61–108, name@L111–127, resource@L128–141, file@L142–156, zip@L157–179, saveAs@L180–182, printErrMsg@L183–188.
- URL/请求对象 L33: `'get' url`; params=`None`, data=`None`
- URL/请求对象 L53: `'get' url`; params=`None`, data=`None`
- URL/请求对象 L113: `'get' url`; params=`None`, data=`None`
- URL/请求对象 L160: `'get' url`; params=`None`, data=`None`
