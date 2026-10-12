# G039 系统参数管理页面

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

系统参数管理页面可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G003 时区、日期输入与提交序列化, G005 HTTP 请求、会话提示与导出, G007 字典获取、缓存与标签展示, G010 会话、权限与路由策略, G012 分页与列表工具栏, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 参数名称/键名/系统内置/时间筛选与分页、CRUD、选中行、Excel 导出、刷新缓存完整。
2. 名称、键名、键值必填；新增与编辑不同 endpoint method，取消不发送；错误不伪造刷新成功。
3. getConfigKey 读配置公共能力已由 http 提供，新增或修改后其他调用方看到正确配置与缓存变化。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0057 | ruoyi-fastapi-frontend/src/api/system/config.js / L4-L10 完整导出 listConfig | react-front/src/api/system/config.ts |
| I0058 | ruoyi-fastapi-frontend/src/api/system/config.js / L13-L18 完整导出 getConfig | react-front/src/api/system/config.ts |
| I0060 | ruoyi-fastapi-frontend/src/api/system/config.js / L29-L35 完整导出 addConfig | react-front/src/api/system/config.ts |
| I0061 | ruoyi-fastapi-frontend/src/api/system/config.js / L38-L44 完整导出 updateConfig | react-front/src/api/system/config.ts |
| I0062 | ruoyi-fastapi-frontend/src/api/system/config.js / L47-L52 完整导出 delConfig | react-front/src/api/system/config.ts |
| I0063 | ruoyi-fastapi-frontend/src/api/system/config.js / L55-L60 完整导出 refreshCache | react-front/src/api/system/config.ts |
| I0064 | ruoyi-fastapi-frontend/src/api/system/config.js / 模块导入、注释及函数之间全部剩余内容 | react-front/src/api/system/config.ts |
| I0565 | ruoyi-fastapi-frontend/src/views/system/config/index.vue / L173-L318 script-setup 完整内容 | react-front/src/views/system/config/index.tsx |
| I0566 | ruoyi-fastapi-frontend/src/views/system/config/index.vue / L1-L171 template 完整内容 | react-front/src/views/system/config/index.tsx |
| I0567 | ruoyi-fastapi-frontend/src/views/system/config/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/config/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/system/config.js

逻辑定位：listConfig@L4–10, getConfig@L13–18, addConfig@L29–35, updateConfig@L38–44, delConfig@L47–52, refreshCache@L55–60.
- URL/请求对象 L5: `'get' '/system/config/list'`; params=`query`, data=`None`
- URL/请求对象 L14: `'get' '/system/config/' + configId`; params=`None`, data=`None`
- URL/请求对象 L30: `'post' '/system/config'`; params=`None`, data=`data`
- URL/请求对象 L39: `'put' '/system/config'`; params=`None`, data=`data`
- URL/请求对象 L48: `'delete' '/system/config/' + configId`; params=`None`, data=`None`
- URL/请求对象 L56: `'delete' '/system/config/refreshCache'`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/views/system/config/index.vue

逻辑定位：getList@L210–217, cancel@L219–222, reset@L224–234, handleQuery@L236–239, resetQuery@L241–245, handleSelectionChange@L247–251, handleAdd@L253–257, handleUpdate@L259–267, submitForm@L269–287, handleDelete@L289–297, handleExport@L299–303, handleRefreshCache@L305–309.
全部模板事件/权限：keyup=handleQuery@L10; keyup=handleQuery@L19; click=handleQuery@L49; click=resetQuery@L50; click=handleAdd@L60; =['system:config:add']@L61; click=handleUpdate@L70; =['system:config:edit']@L71; click=handleDelete@L80; =['system:config:remove']@L81; click=handleExport@L89; =['system:config:export']@L90; click=handleRefreshCache@L98; =['system:config:remove']@L99; queryTable=getList@L102; selection-change=handleSelectionChange@L105; click=handleUpdate(scope.row)@L124; =['system:config:edit']@L124; click=handleDelete(scope.row)@L125; =['system:config:remove']@L125; pagination=getList@L135; click=submitForm@L165; click=cancel@L166.
