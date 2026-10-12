# G038 字典类型与数据管理

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

字典类型与数据管理可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；类型与数据页面共同组成字典维护闭环，detail 直接读数据、data 读类型，合组保留真实依赖而非拆函数消除循环。

依赖：G002 共用数据与表单适配, G003 时区、日期输入与提交序列化, G005 HTTP 请求、会话提示与导出, G007 字典获取、缓存与标签展示, G010 会话、权限与路由策略, G012 分页与列表工具栏, G021 多标签、页面缓存与刷新, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 字典类型 CRUD/搜索/分页/导出与详情前100条、进入类型数据页完整；route dictId 查类型后设置 dictType。
2. 字典数据标签/键值/排序必填，样式属性、回显样式、状态、默认值与导出保留。
3. 数据新增修改删除后使对应缓存失效，类型刷新缓存清空全局字典；返回关闭打开正确标签，不留下旧类型数据。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0066 | ruoyi-fastapi-frontend/src/api/system/dict/data.js / L4-L10 完整导出 listData | react-front/src/api/system/dict/data.ts |
| I0067 | ruoyi-fastapi-frontend/src/api/system/dict/data.js / L13-L18 完整导出 getData | react-front/src/api/system/dict/data.ts |
| I0069 | ruoyi-fastapi-frontend/src/api/system/dict/data.js / L29-L35 完整导出 addData | react-front/src/api/system/dict/data.ts |
| I0070 | ruoyi-fastapi-frontend/src/api/system/dict/data.js / L38-L44 完整导出 updateData | react-front/src/api/system/dict/data.ts |
| I0071 | ruoyi-fastapi-frontend/src/api/system/dict/data.js / L47-L52 完整导出 delData | react-front/src/api/system/dict/data.ts |
| I0072 | ruoyi-fastapi-frontend/src/api/system/dict/data.js / 模块导入、注释及函数之间全部剩余内容 | react-front/src/api/system/dict/data.ts |
| I0073 | ruoyi-fastapi-frontend/src/api/system/dict/type.js / L1-L61 module 完整内容 | react-front/src/api/system/dict/type.ts |
| I0571 | ruoyi-fastapi-frontend/src/views/system/dict/data.vue / L178-L350 script-setup 完整内容 | react-front/src/views/system/dict/data.tsx |
| I0572 | ruoyi-fastapi-frontend/src/views/system/dict/data.vue / L1-L176 template 完整内容 | react-front/src/views/system/dict/data.tsx |
| I0573 | ruoyi-fastapi-frontend/src/views/system/dict/data.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/dict/data.tsx |
| I0574 | ruoyi-fastapi-frontend/src/views/system/dict/detail.vue / L75-L109 script-setup 完整内容 | react-front/src/views/system/dict/detail.tsx |
| I0575 | ruoyi-fastapi-frontend/src/views/system/dict/detail.vue / L1-L73 template 完整内容 | react-front/src/views/system/dict/detail.tsx |
| I0576 | ruoyi-fastapi-frontend/src/views/system/dict/detail.vue / L111-L202 style-1 完整内容 | react-front/src/views/system/dict/detail.tsx |
| I0577 | ruoyi-fastapi-frontend/src/views/system/dict/detail.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/dict/detail.tsx |
| I0578 | ruoyi-fastapi-frontend/src/views/system/dict/index.vue / L184-L341 script-setup 完整内容 | react-front/src/views/system/dict/index.tsx |
| I0579 | ruoyi-fastapi-frontend/src/views/system/dict/index.vue / L1-L182 template 完整内容 | react-front/src/views/system/dict/index.tsx |
| I0580 | ruoyi-fastapi-frontend/src/views/system/dict/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/dict/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/system/dict/data.js

逻辑定位：listData@L4–10, getData@L13–18, addData@L29–35, updateData@L38–44, delData@L47–52.
- URL/请求对象 L5: `'get' '/system/dict/data/list'`; params=`query`, data=`None`
- URL/请求对象 L14: `'get' '/system/dict/data/' + dictCode`; params=`None`, data=`None`
- URL/请求对象 L30: `'post' '/system/dict/data'`; params=`None`, data=`data`
- URL/请求对象 L39: `'put' '/system/dict/data'`; params=`None`, data=`data`
- URL/请求对象 L48: `'delete' '/system/dict/data/' + dictCode`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/api/system/dict/type.js

逻辑定位：listType@L4–10, getType@L13–18, addType@L21–27, updateType@L30–36, delType@L39–44, refreshCache@L47–52, optionselect@L55–60.
- URL/请求对象 L5: `'get' '/system/dict/type/list'`; params=`query`, data=`None`
- URL/请求对象 L14: `'get' '/system/dict/type/' + dictId`; params=`None`, data=`None`
- URL/请求对象 L22: `'post' '/system/dict/type'`; params=`None`, data=`data`
- URL/请求对象 L31: `'put' '/system/dict/type'`; params=`None`, data=`data`
- URL/请求对象 L40: `'delete' '/system/dict/type/' + dictId`; params=`None`, data=`None`
- URL/请求对象 L48: `'delete' '/system/dict/type/refreshCache'`; params=`None`, data=`None`
- URL/请求对象 L56: `'get' '/system/dict/type/optionselect'`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/views/system/dict/data.vue

逻辑定位：getTypes@L227–233, getTypeList@L236–240, getList@L242–249, cancel@L251–254, reset@L256–268, handleQuery@L270–273, handleClose@L275–278, resetQuery@L280–284, handleAdd@L286–291, handleSelectionChange@L293–297, handleUpdate@L299–307, submitForm@L309–329, handleDelete@L331–340, handleExport@L342–346.
全部模板事件/权限：keyup=handleQuery@L20; click=handleQuery@L34; click=resetQuery@L35; click=handleAdd@L45; =['system:dict:add']@L46; click=handleUpdate@L55; =['system:dict:edit']@L56; click=handleDelete@L65; =['system:dict:remove']@L66; click=handleExport@L74; =['system:dict:export']@L75; click=handleClose@L83; queryTable=getList@L86; selection-change=handleSelectionChange@L89; click=handleUpdate(scope.row)@L113; =['system:dict:edit']@L113; click=handleDelete(scope.row)@L114; =['system:dict:remove']@L114; pagination=getList@L124; click=submitForm@L170; click=cancel@L171.

### ruoyi-fastapi-frontend/src/views/system/dict/detail.vue

逻辑定位：default@L80–80, loadData@L99–108.
全部模板事件/权限：update:model-value=$emit('update:visible', $event)@L2.

### ruoyi-fastapi-frontend/src/views/system/dict/index.vue

逻辑定位：getList@L224–231, cancel@L233–236, reset@L238–247, handleQuery@L249–252, resetQuery@L254–258, handleAdd@L260–264, handleSelectionChange@L266–270, handleViewData@L272–275, handleDataList@L277–279, handleUpdate@L281–289, submitForm@L291–309, handleDelete@L311–319, handleExport@L321–325, handleRefreshCache@L327–332.
全部模板事件/权限：keyup=handleQuery@L10; keyup=handleQuery@L19; click=handleQuery@L49; click=resetQuery@L50; click=handleAdd@L60; =['system:dict:add']@L61; click=handleUpdate@L70; =['system:dict:edit']@L71; click=handleDelete@L80; =['system:dict:remove']@L81; click=handleExport@L89; =['system:dict:export']@L90; click=handleRefreshCache@L98; =['system:dict:remove']@L99; queryTable=getList@L102; selection-change=handleSelectionChange@L105; click=handleViewData(scope.row)@L111; click=handleUpdate(scope.row)@L127; =['system:dict:edit']@L127; click=handleDataList(scope.row)@L128; =['system:dict:edit']@L128; click=handleDelete(scope.row)@L129; =['system:dict:remove']@L129; pagination=getList@L139; click=submitForm@L174; click=cancel@L175.
