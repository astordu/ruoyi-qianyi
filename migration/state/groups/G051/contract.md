# G051 表单设计、属性编辑与代码导出

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

表单设计、属性编辑与代码导出可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；画布、RightPanel 和生成器共享 schema，完整组件配置和导出一起验收；组内续做，不拆属性、函数或选择器为新组。

依赖：G002 共用数据与表单适配, G005 HTTP 请求、会话提示与导出, G008 SVG 图标与图标选择器, G011 普通与分段文件下载, G015 富文本编辑与图片粘贴, G018 通用文件附件上传, G020 图片上传与预览, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 全部 input/select/layout 组件配置、拖拽添加/嵌套/排序/复制/删除、唯一formId/renderKey、当前选择与清空确认保持。
2. RightPanel 字段/表单属性、选项树/数字布尔默认值、时间范围、正则、上传/图标/校验/评分/联动等所有类型配置与画布同步，不用缺省演示控件替代。
3. generate file/dialog 两种 Vue 产品格式，默认 .vue 文件名、html/js/css 生成、格式化/复制/下载保持当前业务输出；迁移的是设计器运行界面，源代码生成产品不会擅自改成 React。
4. schema 中旧 el-* tag 作为产品数据保留，运行画布采用 React 控件映射；字段切换按相同类型复用属性，嵌套 children 递归更新。
5. TreeNode/Icons/CodeType 内部弹窗同组，ClipboardJS 改等价剪贴板并保留成功/失败提示、卸载清理；同一schema导出与旧生成器逐字/规范化比对。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0467 | ruoyi-fastapi-frontend/src/utils/generator/config.js / L1-L453 module 完整内容 | react-front/src/utils/generator/config.ts |
| I0468 | ruoyi-fastapi-frontend/src/utils/generator/css.js / L1-L19 module 完整内容 | react-front/src/utils/generator/css.ts |
| I0469 | ruoyi-fastapi-frontend/src/utils/generator/drawingDefault.js / L1-L37 module 完整内容 | react-front/src/utils/generator/drawingDefault.ts |
| I0470 | ruoyi-fastapi-frontend/src/utils/generator/html.js / L1-L360 module 完整内容 | react-front/src/utils/generator/html.ts |
| I0471 | ruoyi-fastapi-frontend/src/utils/generator/icon.json / L1-L1 configuration 完整内容 | react-front/src/utils/generator/icon.json |
| I0472 | ruoyi-fastapi-frontend/src/utils/generator/js.js / L1-L371 module 完整内容 | react-front/src/utils/generator/js.ts |
| I0473 | ruoyi-fastapi-frontend/src/utils/generator/render.js / L1-L156 module 完整内容 | react-front/src/utils/generator/render.tsx |
| I0697 | ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue / L23-L71 script-setup 完整内容 | react-front/src/views/tool/build/CodeTypeDialog.tsx |
| I0698 | ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue / L1-L21 template 完整内容 | react-front/src/views/tool/build/CodeTypeDialog.tsx |
| I0699 | ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/tool/build/CodeTypeDialog.tsx |
| I0700 | ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue / L27-L68 script-setup 完整内容 | react-front/src/views/tool/build/DraggableItem.tsx |
| I0701 | ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue / L1-L26 template 完整内容 | react-front/src/views/tool/build/DraggableItem.tsx |
| I0702 | ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/tool/build/DraggableItem.tsx |
| I0703 | ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue / L23-L53 script-setup 完整内容 | react-front/src/views/tool/build/IconsDialog.tsx |
| I0704 | ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue / L1-L22 template 完整内容 | react-front/src/views/tool/build/IconsDialog.tsx |
| I0705 | ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue / L54-L115 style-1 完整内容 | react-front/src/views/tool/build/IconsDialog.tsx |
| I0706 | ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/tool/build/IconsDialog.tsx |
| I0707 | ruoyi-fastapi-frontend/src/views/tool/build/RightPanel.vue / L466-L763 script-setup 完整内容 | react-front/src/views/tool/build/RightPanel.tsx |
| I0708 | ruoyi-fastapi-frontend/src/views/tool/build/RightPanel.vue / L1-L464 template 完整内容 | react-front/src/views/tool/build/RightPanel.tsx |
| I0709 | ruoyi-fastapi-frontend/src/views/tool/build/RightPanel.vue / L765-L906 style-1 完整内容 | react-front/src/views/tool/build/RightPanel.tsx |
| I0710 | ruoyi-fastapi-frontend/src/views/tool/build/RightPanel.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/tool/build/RightPanel.tsx |
| I0711 | ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue / L34-L93 script-setup 完整内容 | react-front/src/views/tool/build/TreeNodeDialog.tsx |
| I0712 | ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue / L1-L33 template 完整内容 | react-front/src/views/tool/build/TreeNodeDialog.tsx |
| I0713 | ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/tool/build/TreeNodeDialog.tsx |
| I0714 | ruoyi-fastapi-frontend/src/views/tool/build/index.vue / L98-L314 script-setup 完整内容 | react-front/src/views/tool/build/index.tsx |
| I0715 | ruoyi-fastapi-frontend/src/views/tool/build/index.vue / L1-L96 template 完整内容 | react-front/src/views/tool/build/index.tsx |
| I0716 | ruoyi-fastapi-frontend/src/views/tool/build/index.vue / L316-L660 style-1 完整内容 | react-front/src/views/tool/build/index.tsx |
| I0717 | ruoyi-fastapi-frontend/src/views/tool/build/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/tool/build/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/utils/generator/config.js


### ruoyi-fastapi-frontend/src/utils/generator/css.js

逻辑定位：addCss@L6–12, makeUpCss@L14–18.

### ruoyi-fastapi-frontend/src/utils/generator/drawingDefault.js

逻辑定位：initDrawingDefaultValue@L3–33, cleanDrawingDefaultValue@L35–37.

### ruoyi-fastapi-frontend/src/utils/generator/html.js

逻辑定位：dialogWrapper@L7–15, vueTemplate@L17–23, vueScript@L25–29, cssStyle@L31–35, buildFormTemplate@L37–53, buildFromBtns@L55–69, colWrapper@L72–79, colFormItem@L82–94, rowFormItem@L95–106, 'el-button'@L110–121, 'el-input'@L122–140, 'el-input-number'@L141–151, 'el-select'@L152–162, 'el-radio-group'@L163–170, 'el-checkbox-group'@L171–180, 'el-switch'@L181–191, 'el-cascader'@L192–203, 'el-slider'@L204–213, 'el-time-picker'@L214–227, 'el-date-picker'@L228–241, 'el-rate'@L242–250, 'el-color-picker'@L251–258, 'el-upload'@L259–274, attrBuilder@L277–285, buildElButtonChild@L288–294, buildElInputChild@L297–306, buildElSelectChild@L308–314, buildElRadioGroupChild@L316–324, buildElCheckboxGroupChild@L326–334, buildElUploadChild@L336–342, makeUpHtml@L344–359.

### ruoyi-fastapi-frontend/src/utils/generator/icon.json


### ruoyi-fastapi-frontend/src/utils/generator/js.js

逻辑定位：makeUpJs@L16–49, buildAttributes@L55–107, buildData@L115–124, buildRules@L132–161, buildOptions@L169–176, buildOptionMethod@L185–191, buildProps@L199–210, buildBeforeUpload@L217–249, buildSubmitUpload@L256–261, buildexport@L267–370.

### ruoyi-fastapi-frontend/src/utils/generator/render.js

逻辑定位：useVModel@L23–28, 'onUpdate:modelValue'@L26–26, default@L31–33, options@L36–41, options@L44–51, options@L54–61, 'list-type'@L64–79, 'tip'@L85–91, render@L97–149.

### ruoyi-fastapi-frontend/src/views/tool/build/CodeTypeDialog.vue

逻辑定位：onOpen@L56–60, onClose@L61–63, handelConfirm@L64–70.
全部模板事件/权限：open=onOpen@L2; close=onClose@L2; click=onClose@L17; click=handelConfirm@L18.

### ruoyi-fastapi-frontend/src/views/tool/build/DraggableItem.vue

逻辑定位：activeItem@L44–46, copyItem@L47–49, deleteItem@L50–52, getComponentData@L54–60.
全部模板事件/权限：click=activeItem(element)@L2; click=activeItem(element)@L7; activeItem=activeItem(scoped.element)@L13; copyItem=copyItem(scoped.element, element.children)@L14; deleteItem=deleteItem(scoped.index, element.children)@L15; click=copyItem(element)@L19; click=deleteItem(index)@L22.

### ruoyi-fastapi-frontend/src/views/tool/build/IconsDialog.vue

逻辑定位：onOpen@L38–38, onClose@L39–39, onSelect@L40–44.
全部模板事件/权限：open=onOpen@L3; close=onClose@L4; click=onSelect(icon)@L11.

### ruoyi-fastapi-frontend/src/views/tool/build/RightPanel.vue

逻辑定位：label@L577–579, addReg@L610–615, addSelectItem@L616–621, addTreeItem@L623–627, renderContent@L629–657, onClick@L641–644, onClick@L651–653, append@L658–664, remove@L665–670, addNode@L671–673, setOptionValue@L675–677, setDefaultValue@L678–689, onDefaultValueInput@L691–702, onSwitchValueInput@L704–710, setTimeValue@L712–717, spanChange@L719–721, multipleChange@L723–725, dateTypeChange@L727–729, rangeChange@L731–733, rateTextChange@L735–737, rateScoreChange@L739–741, colorFormatChange@L743–747, openIconsDialog@L749–752, setIcon@L754–756, tagChange@L758–762.
全部模板事件/权限：change=tagChange@L18; change=spanChange@L46; input=onDefaultValueInput@L72; input=$set(activeData, 'min', $event ? $event : undefined)@L76; input=$set(activeData, 'max', $event ? $event : undefined)@L80; click=openIconsDialog('prefix-icon')@L91; click=openIconsDialog('suffix-icon')@L100; input=onSwitchValueInput($event, 'active-value')@L152; input=onSwitchValueInput($event, 'inactive-value')@L156; change=dateTypeChange@L160; input=setTimeValue($event)@L214; input=setOptionValue(element, $event)@L227; click=activeData.options.splice(index, 1)@L228; click=addSelectItem@L238; click=addTreeItem@L274; change=rateTextChange@L302; change=rateScoreChange@L305; change=rangeChange@L311; change=colorFormatChange@L318; change=multipleChange@L376; click=activeData.regList.splice(index, 1)@L397; click=addReg@L411; select=setIcon@L460; commit=addNode@L461.

### ruoyi-fastapi-frontend/src/views/tool/build/TreeNodeDialog.vue

逻辑定位：onOpen@L71–76, onClose@L78–80, handelConfirm@L82–92.
全部模板事件/权限：open=onOpen@L4; close=onClose@L4; click=handelConfirm@L27; click=onClose@L28.

### ruoyi-fastapi-frontend/src/views/tool/build/index.vue

逻辑定位：activeFormItem@L132–135, copy@L136–140, download@L141–145, empty@L146–153, onEnd@L155–160, addComponent@L162–166, cloneComponent@L168–185, drawingItemCopy@L187–192, createIdAndKey@L195–207, drawingItemDelete@L209–217, tagChange@L219–235, updateDrawingList@L238–247, generate@L248–262, execDownload@L264–268, execCopy@L270–272, AssembleFormData@L273–275, generateCode@L276–283, text@L301–305.
全部模板事件/权限：end=onEnd@L16; click=addComponent(element)@L18; end=onEnd@L31; click=addComponent(element)@L33; end=onEnd@L46; click=addComponent(element)@L48; click=download@L61; click=copy@L64; click=empty@L67; activeItem=activeFormItem@L79; copyItem=drawingItemCopy@L79; deleteItem=drawingItemDelete@L80; tag-change=tagChange@L91; confirm=generate@L93.
