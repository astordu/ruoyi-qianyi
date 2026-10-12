# G013 树面板查询、选择与调整

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

树面板查询、选择与调整可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G009 系统主题与布局偏好

## 正常、异常与边界检查条件

1. 过滤、刷新、展开/收起、节点点击/勾选、当前节点与 checkedKeys 暴露方法可调用；自定义 filterMethod 优先。
2. 鼠标/触摸拖宽限制 minWidth/maxWidth，RAF 合并移动与宽度保存；折叠不覆盖原宽度，非法缓存宽度忽略，enableStorage=false 不写入。
3. disabled/showCheckbox/搜索空值/无树数据/宽度重置按 props 执行；卸载结束监听、RAF、延时保存并恢复 user-select。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0366 | ruoyi-fastapi-frontend/src/components/TreePanel/index.vue / L74-L548 script-setup 完整内容 | react-front/src/components/TreePanel/index.tsx |
| I0367 | ruoyi-fastapi-frontend/src/components/TreePanel/index.vue / L1-L72 template 完整内容 | react-front/src/components/TreePanel/index.tsx |
| I0368 | ruoyi-fastapi-frontend/src/components/TreePanel/index.vue / L550-L756 style-1 完整内容 | react-front/src/components/TreePanel/index.tsx |
| I0369 | ruoyi-fastapi-frontend/src/components/TreePanel/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/TreePanel/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/components/TreePanel/index.vue

逻辑定位：default@L79–79, default@L109–112, default@L142–142, get@L208–208, set@L209–211, filterNodeMethod@L215–221, cleanup@L252–261, handleCollapseChange@L264–272, getSavedWidth@L275–291, saveWidthToStorage@L294–301, toggleCollapsed@L304–306, toggleExpandAll@L309–311, expandAllNodes@L314–322, getAllNodes@L325–336, traverse@L327–333, collapseAllNodes@L339–347, handleRefresh@L350–352, onNodeClick@L355–357, onCheck@L360–362, onNodeExpand@L365–367, onNodeCollapse@L370–372, setCurrentKey@L374–378, getCurrentNode@L380–385, getCurrentKey@L387–392, setCheckedKeys@L394–398, getCheckedKeys@L400–405, getCheckedNodes@L407–412, clearSearch@L414–419, filter@L421–423, startResize@L425–440, handleResizeMove@L442–458, stopResize@L460–475, disableUserSelect@L477–482, enableUserSelect@L484–489, resetWidth@L491–494, getCurrentWidth@L496–498, setWidth@L500–507.
全部模板事件/权限：mousedown=startResize@L4; touchstart=startResize@L4; click=toggleExpandAll@L11; click=handleRefresh@L17; click=toggleCollapsed@L26; node-click=onNodeClick@L53; check=onCheck@L54; node-expand=onNodeExpand@L55; node-collapse=onNodeCollapse@L56.
