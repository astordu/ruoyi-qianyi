# G042 插件生命周期、配置、诊断与审计

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

插件生命周期、配置、诊断与审计可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；主页面共享 pendingAction/计划结果/批量选择/刷新和详情状态，整组迁移，不再拆82组；实施可分生命周期、配置、依赖/诊断、审计4个步骤续做，全部验收后才通过。

依赖：G002 共用数据与表单适配, G003 时区、日期输入与提交序列化, G005 HTTP 请求、会话提示与导出, G007 字典获取、缓存与标签展示, G010 会话、权限与路由策略, G012 分页与列表工具栏, G016 JSON 编辑器校验与主题, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 列表筛选、批量选择、启停开关、orphan 状态和 capability.blockedOperations 决定可操作性；取消启停恢复，失败通过真实错误结构展示。
2. 安装/升级/卸载/purge 先 dryRun 计划，ok 且 capability 允许才可确认执行；显示步骤/菜单冲突/迁移脚本/错误与修复建议，不跳过预演。
3. 依赖检查、安装预演和 policy.allowed=false 阻断；批量 plan 的依赖顺序/executablePluginIds、continueOnError、成功失败跳过计数完整。
4. 配置按类型归一化，secret 留空保留规则、必填/数值/正则/JSON 校验与提交 values；详情含前后端交付/菜单/权限/migrations，running或failed 可人工标成功，running 可标失败的边界按源条件。
5. 操作审计查询/排序日期范围/详情/导出exportLimit=5000；保留天数读取配置，dryRun 与真正清理分开确认，0天提示特殊语义；secret 配置变化显示不能泄露。
6. 完整5个业务弹窗和主页面结果弹窗都接原请求；normalizePlan/Batch/Action/Log 的缺省、兼容结构和错误兜底不会把失败转为成功。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0094 | ruoyi-fastapi-frontend/src/api/system/plugin.js / L1-L208 module 完整内容 | react-front/src/api/system/plugin.ts |
| I0479 | ruoyi-fastapi-frontend/src/utils/pluginPlanFormatter.js / L1-L191 module 完整内容 | react-front/src/utils/pluginPlanFormatter.ts |
| I0635 | ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginConfigDialog.vue / L85-L314 script-setup 完整内容 | react-front/src/views/system/plugin/components/PluginConfigDialog.tsx |
| I0636 | ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginConfigDialog.vue / L1-L83 template 完整内容 | react-front/src/views/system/plugin/components/PluginConfigDialog.tsx |
| I0637 | ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginConfigDialog.vue / L316-L366 style-1 完整内容 | react-front/src/views/system/plugin/components/PluginConfigDialog.tsx |
| I0638 | ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginConfigDialog.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/plugin/components/PluginConfigDialog.tsx |
| I0639 | ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginDependencyDialog.vue / L139-L265 script-setup 完整内容 | react-front/src/views/system/plugin/components/PluginDependencyDialog.tsx |
| I0640 | ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginDependencyDialog.vue / L1-L137 template 完整内容 | react-front/src/views/system/plugin/components/PluginDependencyDialog.tsx |
| I0641 | ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginDependencyDialog.vue / L267-L342 style-1 完整内容 | react-front/src/views/system/plugin/components/PluginDependencyDialog.tsx |
| I0642 | ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginDependencyDialog.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/plugin/components/PluginDependencyDialog.tsx |
| I0643 | ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginDetailDialog.vue / L228-L361 script-setup 完整内容 | react-front/src/views/system/plugin/components/PluginDetailDialog.tsx |
| I0644 | ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginDetailDialog.vue / L1-L226 template 完整内容 | react-front/src/views/system/plugin/components/PluginDetailDialog.tsx |
| I0645 | ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginDetailDialog.vue / L363-L396 style-1 完整内容 | react-front/src/views/system/plugin/components/PluginDetailDialog.tsx |
| I0646 | ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginDetailDialog.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/plugin/components/PluginDetailDialog.tsx |
| I0647 | ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginDiagnosticDialog.vue / L84-L150 script-setup 完整内容 | react-front/src/views/system/plugin/components/PluginDiagnosticDialog.tsx |
| I0648 | ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginDiagnosticDialog.vue / L1-L82 template 完整内容 | react-front/src/views/system/plugin/components/PluginDiagnosticDialog.tsx |
| I0649 | ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginDiagnosticDialog.vue / L152-L185 style-1 完整内容 | react-front/src/views/system/plugin/components/PluginDiagnosticDialog.tsx |
| I0650 | ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginDiagnosticDialog.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/plugin/components/PluginDiagnosticDialog.tsx |
| I0651 | ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginPlanDialog.vue / L131-L186 script-setup 完整内容 | react-front/src/views/system/plugin/components/PluginPlanDialog.tsx |
| I0652 | ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginPlanDialog.vue / L1-L129 template 完整内容 | react-front/src/views/system/plugin/components/PluginPlanDialog.tsx |
| I0653 | ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginPlanDialog.vue / L188-L246 style-1 完整内容 | react-front/src/views/system/plugin/components/PluginPlanDialog.tsx |
| I0654 | ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginPlanDialog.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/plugin/components/PluginPlanDialog.tsx |
| I0655 | ruoyi-fastapi-frontend/src/views/system/plugin/index.vue / L612-L1661 script-setup 完整内容 | react-front/src/views/system/plugin/index.tsx |
| I0656 | ruoyi-fastapi-frontend/src/views/system/plugin/index.vue / L1-L610 template 完整内容 | react-front/src/views/system/plugin/index.tsx |
| I0657 | ruoyi-fastapi-frontend/src/views/system/plugin/index.vue / L1663-L1786 style-1 完整内容 | react-front/src/views/system/plugin/index.tsx |
| I0658 | ruoyi-fastapi-frontend/src/views/system/plugin/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/plugin/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/system/plugin.js

逻辑定位：listPlugin@L4–10, getPlugin@L13–18, enablePlugin@L21–26, disablePlugin@L29–34, checkPlugin@L37–42, healthPlugin@L45–50, diagnosePlugin@L53–58, installPlugin@L61–67, upgradePlugin@L70–76, uninstallPlugin@L79–85, purgePlugin@L88–94, getPluginConfig@L97–102, listPluginMigrations@L105–111, markPluginMigrationSuccess@L114–120, markPluginMigrationFailed@L123–129, updatePluginConfig@L132–138, checkPluginDependencies@L141–146, planPlugins@L149–158, batchPlugins@L161–172, listPluginOperationLog@L175–181, getPluginOperationLog@L184–189, retainPluginOperationLog@L192–198, installPluginDependencies@L201–207.
- URL/请求对象 L5: `'get' '/system/plugin/list'`; params=`query`, data=`None`
- URL/请求对象 L14: `'get' '/system/plugin/' + pluginId`; params=`None`, data=`None`
- URL/请求对象 L22: `'put' '/system/plugin/' + pluginId + '/enable'`; params=`None`, data=`None`
- URL/请求对象 L30: `'put' '/system/plugin/' + pluginId + '/disable'`; params=`None`, data=`None`
- URL/请求对象 L38: `'get' '/system/plugin/' + pluginId + '/check'`; params=`None`, data=`None`
- URL/请求对象 L46: `'get' '/system/plugin/' + pluginId + '/health'`; params=`None`, data=`None`
- URL/请求对象 L54: `'get' '/system/plugin/' + pluginId + '/diagnose'`; params=`None`, data=`None`
- URL/请求对象 L62: `'post' '/system/plugin/' + pluginId + '/install'`; params=`{ dryRun }`, data=`None`
- URL/请求对象 L71: `'post' '/system/plugin/' + pluginId + '/upgrade'`; params=`{ dryRun }`, data=`None`
- URL/请求对象 L80: `'post' '/system/plugin/' + pluginId + '/uninstall'`; params=`{ dryRun }`, data=`None`
- URL/请求对象 L89: `'post' '/system/plugin/' + pluginId + '/purge'`; params=`{ dryRun }`, data=`None`
- URL/请求对象 L98: `'get' '/system/plugin/' + pluginId + '/config'`; params=`None`, data=`None`
- URL/请求对象 L106: `'get' '/system/plugin/' + pluginId + '/migrations'`; params=`{ status }`, data=`None`
- URL/请求对象 L115: `'post' '/system/plugin/' + pluginId + '/migrations/mark-success'`; params=`None`, data=`data`
- URL/请求对象 L124: `'post' '/system/plugin/' + pluginId + '/migrations/mark-failed'`; params=`None`, data=`data`
- URL/请求对象 L133: `'put' '/system/plugin/' + pluginId + '/config'`; params=`None`, data=`data`
- URL/请求对象 L142: `'get' '/system/plugin/' + pluginId + '/dependencies'`; params=`None`, data=`None`
- URL/请求对象 L150: `'get' '/system/plugin/plan'`; params=`{ operation, pluginIds }`, data=`None`
- URL/请求对象 L162: `'post' '/system/plugin/batch'`; params=`None`, data=`{ operation, pluginIds, dryRun, continueOnError }`
- URL/请求对象 L176: `'get' '/system/plugin/operation-log/list'`; params=`query`, data=`None`
- URL/请求对象 L185: `'get' '/system/plugin/operation-log/' + operationId`; params=`None`, data=`None`
- URL/请求对象 L193: `'delete' '/system/plugin/operation-log/retention'`; params=`params`, data=`None`
- URL/请求对象 L202: `'post' '/system/plugin/' + pluginId + '/dependencies/install'`; params=`{ dryRun }`, data=`None`

### ruoyi-fastapi-frontend/src/utils/pluginPlanFormatter.js

逻辑定位：normalizePluginPlanResponse@L1–26, normalizePluginBatchResponse@L28–46, getPlanOperationLabel@L48–55, getPlanReadyTagType@L57–59, getPlanBlockerStatusLabel@L61–73, getValidationLevelLabel@L75–83, getValidationLevelTagType@L85–93, normalizePluginActionResult@L95–120, normalizePluginOperationLogDetail@L122–138, buildOperationValidationItems@L140–162, buildOperationConfigChanges@L164–180, buildOperationFailedSuggestion@L182–190.

### ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginConfigDialog.vue

逻辑定位：default@L100–100, submit@L158–172, normalizeConfigValueForForm@L174–185, buildConfigSubmitValues@L187–201, getConfigItemRules@L203–218, isSecretConfigItem@L220–222, buildNumberConfigValidator@L224–245, buildPatternConfigValidator@L247–264, validateJsonConfig@L266–277, formatConfigJsonValue@L279–289, getConfigInputPlaceholder@L291–293, hasConfigMeta@L295–303, formatConfigGroupLabel@L305–313.
全部模板事件/权限：update:model-value=emit('update:modelValue', $event)@L2; click=formatConfigJsonValue(item)@L46; click=submit@L76; =['system:plugin:edit']@L77; click=emit('update:modelValue', false)@L79.

### ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginDependencyDialog.vue

逻辑定位：default@L150–150, formatPolicyList@L224–226, formatPolicyItemMessage@L228–234, copyDependencyCommand@L236–245, copyText@L247–264.
全部模板事件/权限：update:model-value=emit('update:modelValue', $event)@L2; click=copyDependencyCommand(scope.row.commandText)@L85; click=emit('dry-run')@L125; click=emit('install')@L130; =['system:plugin:edit']@L131; click=emit('update:modelValue', false)@L133.

### ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginDetailDialog.vue

逻辑定位：default@L238–238, default@L258–258, formatYesNo@L308–313, formatDetailTags@L315–317, getFrontendDeliveryLabel@L319–328, normalizeDetailItems@L330–332, getMigrationStatusLabel@L334–342, getMigrationStatusTagType@L344–352, canMarkMigrationSuccess@L354–356, canMarkMigrationFailed@L358–360.
全部模板事件/权限：update:model-value=emit('update:modelValue', $event)@L2; click=emit('mark-migration-success', scope.row)@L170; =['system:plugin:edit']@L171; click=emit('mark-migration-failed', scope.row)@L179; =['system:plugin:edit']@L180; click=emit('repair')@L219; =['system:plugin:edit']@L220; click=emit('update:modelValue', false)@L222.

### ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginDiagnosticDialog.vue

逻辑定位：default@L98–98.
全部模板事件/权限：update:model-value=emit('update:modelValue', $event)@L2; click=emit('update:modelValue', false)@L78.

### ruoyi-fastapi-frontend/src/views/system/plugin/components/PluginPlanDialog.vue

全部模板事件/权限：update:model-value=emit('update:modelValue', $event)@L2; update:model-value=emit('update:continueOnError', $event)@L116; click=emit('execute')@L122; =['system:plugin:edit']@L123; click=emit('update:modelValue', false)@L125.

### ruoyi-fastapi-frontend/src/views/system/plugin/index.vue

逻辑定位：formatPluginTime@L713–727, getList@L769–779, handleSelectionChange@L782–784, canSelectForBatch@L786–788, clearSelectedPlugins@L791–794, handleQuery@L797–801, resetQuery@L804–807, handleEnabledChange@L810–834, getEnabledSwitchOperation@L836–838, isEnabledSwitchBlocked@L840–843, getEnabledSwitchTooltip@L845–855, handleDetail@L858–870, loadPluginMigrationHistory@L873–887, handleMarkMigrationSuccess@L890–914, handleMarkMigrationFailed@L917–941, handleConfig@L944–957, submitConfig@L960–970, handleCheck@L973–985, handleHealth@L988–1008, handleDiagnose@L1011–1031, handleDependencies@L1034–1052, handleDependencyDryRun@L1055–1068, handleDependencyInstall@L1071–1093, handlePlan@L1096–1113, getBatchTargetPluginIds@L1116–1118, handleExecuteBatch@L1121–1143, handleOperationLog@L1146–1152, handleOperationLogQuery@L1155–1158, resetOperationLogQuery@L1161–1164, resetOperationLogSearchState@L1166–1172, resetOperationLogRetentionState@L1174–1178, buildOperationLogQueryParams@L1180–1182, loadOperationLogRetentionPolicy@L1184–1192, getOperationLogList@L1195–1205, handleOperationLogDetail@L1208–1215, handleOperationLogExport@L1218–1226, handleOperationLogRetentionPreview@L1229–1241, handleOperationLogRetentionClean@L1244–1262, buildOperationLogRetentionConfirmMessage@L1264–1270, handleInstallDryRun@L1273–1290, handleUpgradeDryRun@L1293–1310, handleUninstallDryRun@L1313–1330, handlePurgeDryRun@L1333–1350, handleExecutePendingAction@L1353–1383, showActionResult@L1386–1391, handleRepairFromDetail@L1394–1398, getStatusLabel@L1400–1403, getStatusTagType@L1405–1408, canInstall@L1410–1412, canUpgrade@L1414–1416, canUninstall@L1418–1420, isOrphanPlugin@L1422–1424, canExecuteActionResult@L1426–1428, isOperationBlocked@L1430–1432, isCapabilityOperationBlocked@L1434–1436, getCapabilityReason@L1438–1440, getDependencyPolicyReason@L1442–1448, getOperationTooltip@L1450–1452, getDependencyTagType@L1454–1459, formatDependencyInstalled@L1461–1466, formatDependencyVersionSatisfied@L1468–1473, normalizeActionResult@L1475–1477, buildErrorActionResult@L1479–1499, buildErrorBatchResult@L1501–1525, getErrorMessage@L1527–1535, serializeError@L1537–1550, isUserCancel@L1552–1554, formatBoolean@L1556–1561, formatPlanDependencies@L1563–1565, formatPluginIdsForDisplay@L1567–1574, formatConfigDefaultValue@L1576–1588, formatConfigConstraint@L1590–1605, formatConfigOption@L1607–1613, formatPluginOperation@L1615–1617, getOperationLogStatusLabel@L1619–1623, getOperationLogStatusTagType@L1625–1629, formatRetentionMessage@L1631–1635, formatActionPlanState@L1637–1654, formatJson@L1656–1658.
全部模板事件/权限：keyup=handleQuery@L9; keyup=handleQuery@L17; click=handleQuery@L32; click=resetQuery@L33; click=handlePlan('install')@L39; =['system:plugin:query']@L39; click=handlePlan('enable')@L42; =['system:plugin:query']@L42; click=handlePlan('upgrade')@L45; =['system:plugin:query']@L45; click=handleOperationLog@L48; =['system:plugin:query']@L48; close=clearSelectedPlugins@L57; queryTable=getList@L61; selection-change=handleSelectionChange@L64; change=handleEnabledChange(scope.row)@L83; =['system:plugin:edit']@L84; click=handleDetail(scope.row)@L105; =['system:plugin:query']@L105; click=handleConfig(scope.row)@L108; =['system:plugin:query']@L108; click=handleDependencies(scope.row)@L111; =['system:plugin:query']@L111; click=handleCheck(scope.row)@L114; =['system:plugin:query']@L114; click=handleHealth(scope.row)@L117; =['system:plugin:query']@L117; click=handleDiagnose(scope.row)@L120; =['system:plugin:query']@L120; click=handleInstallDryRun(scope.row)@L123; =['system:plugin:edit']@L123; click=handleUpgradeDryRun(scope.row)@L126; =['system:plugin:edit']@L126; click=handleUninstallDryRun(scope.row)@L129; =['system:plugin:edit']@L129; click=handlePurgeDryRun(scope.row)@L132; =['system:plugin:remove']@L132; pagination=getList@L144; repair=handleRepairFromDetail@L156; mark-migration-success=handleMarkMigrationSuccess@L157; mark-migration-failed=handleMarkMigrationFailed@L158; dry-run=handleDependencyDryRun@L170; install=handleDependencyInstall@L171; execute=handleExecuteBatch(false)@L197; keyup=handleOperationLogQuery@L209; click=handleOperationLogQuery@L233; click=resetOperationLogQuery@L234; click=handleOperationLogRetentionPreview@L250; click=handleOperationLogRetentionClean@L256; =['system:plugin:edit']@L257; click=handleOperationLogExport@L280; =['system:plugin:export']@L281; queryTable=getOperationLogList@L285; click=handleOperationLogDetail(scope.row)@L312; pagination=getOperationLogList@L322; click=operationLogOpen = false@L327; click=operationLogDetailOpen = false@L443; submit=submitConfig@L455; click=handleExecutePendingAction@L595; =['system:plugin:edit']@L596; click=handleExecutePendingAction@L602; =['system:plugin:remove']@L603; click=actionOpen = false@L605.
