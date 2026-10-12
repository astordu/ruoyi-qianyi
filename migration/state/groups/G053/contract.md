# G053 代码生成字段与模板配置

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

代码生成字段与模板配置可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G005 HTTP 请求、会话提示与导出, G021 多标签、页面缓存与刷新, G023 应用入口与响应式导航布局, G036 菜单树、路由信息与排序, G038 字典类型与数据管理, G052 代码生成表管理、导入与预览

## 正常、异常与边界检查条件

1. 按 tableId 加载基本/字段/生成信息，多表单 validate 都通过才提交 columns；拖字段排序同步 sort。
2. Python 类型、属性、insert/edit/list/query/查询比较符、必填/唯一、字典和 date/time/datetime 分类全部保持。
3. 单/树/主子表模板、子表关联列、包/模块/业务名、菜单树、Vue2 Element/Vue3 ElementPlus 模板与表单列数保持；view 修改后时间 query 刷新返回。
4. Sortable 生命周期在 React 重建并清理，未通过基本或生成表单时不保存；不能因为 React UI 删除旧模板选项。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0130 | ruoyi-fastapi-frontend/src/api/tool/gen.js / L29-L34 完整导出 getGenTable | react-front/src/api/tool/gen-genedit.ts |
| I0131 | ruoyi-fastapi-frontend/src/api/tool/gen.js / L37-L43 完整导出 updateGenTable | react-front/src/api/tool/gen-genedit.ts |
| I0718 | ruoyi-fastapi-frontend/src/views/tool/gen/basicInfoForm.vue / L33-L48 script-setup 完整内容 | react-front/src/views/tool/gen/basicInfoForm.tsx |
| I0719 | ruoyi-fastapi-frontend/src/views/tool/gen/basicInfoForm.vue / L1-L31 template 完整内容 | react-front/src/views/tool/gen/basicInfoForm.tsx |
| I0720 | ruoyi-fastapi-frontend/src/views/tool/gen/basicInfoForm.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/tool/gen/basicInfoForm.tsx |
| I0724 | ruoyi-fastapi-frontend/src/views/tool/gen/editTable.vue / L134-L223 script-setup 完整内容 | react-front/src/views/tool/gen/editTable.tsx |
| I0725 | ruoyi-fastapi-frontend/src/views/tool/gen/editTable.vue / L1-L132 template 完整内容 | react-front/src/views/tool/gen/editTable.tsx |
| I0726 | ruoyi-fastapi-frontend/src/views/tool/gen/editTable.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/tool/gen/editTable.tsx |
| I0727 | ruoyi-fastapi-frontend/src/views/tool/gen/genInfoForm.vue / L259-L328 script-setup 完整内容 | react-front/src/views/tool/gen/genInfoForm.tsx |
| I0728 | ruoyi-fastapi-frontend/src/views/tool/gen/genInfoForm.vue / L1-L257 template 完整内容 | react-front/src/views/tool/gen/genInfoForm.tsx |
| I0729 | ruoyi-fastapi-frontend/src/views/tool/gen/genInfoForm.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/tool/gen/genInfoForm.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/tool/gen.js

逻辑定位：getGenTable@L29–34, updateGenTable@L37–43.
- URL/请求对象 L30: `'get' '/tool/gen/' + tableId`; params=`None`, data=`None`
- URL/请求对象 L38: `'put' '/tool/gen'`; params=`None`, data=`data`

### ruoyi-fastapi-frontend/src/views/tool/gen/basicInfoForm.vue

全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/views/tool/gen/editTable.vue

逻辑定位：submitForm@L152–177, getFormPromise@L179–185, close@L187–190, onEnd@L214–220.
全部模板事件/权限：click=submitForm()@L127; click=close()@L128.

### ruoyi-fastapi-frontend/src/views/tool/gen/genInfoForm.vue

逻辑定位：subSelectChange@L286–288, tplSelectChange@L290–295, setSubTableColumns@L297–305, getMenuTreeselect@L308–312.
全部模板事件/权限：change=tplSelectChange@L7; click=info.genPath = '/'@L144; change=subSelectChange@L225.
