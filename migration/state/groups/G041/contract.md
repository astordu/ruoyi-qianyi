# G041 文件资产管理完整闭环

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

文件资产管理完整闭环可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；保留为一组：所有文件抽屉共用列表选择、统计刷新、权限与文件生命周期，整组交付才称文件管理完成。可按“列表→ACL/转移→审计→保留→对账”续做，内部5步骤不增加执行组或提前标通过。

依赖：G002 共用数据与表单适配, G003 时区、日期输入与提交序列化, G005 HTTP 请求、会话提示与导出, G010 会话、权限与路由策略, G011 普通与分段文件下载, G012 分页与列表工具栏, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 搜索/分页/统计/详情/下载，正常/回收站/清理中/过期状态、单批选择和真实 downloadUrl；被业务引用的文件不得移入回收站。
2. ACL 单文件与批量只处理 private 文件，用户/角色/部门主体搜索异步过期响应不覆盖，deny/包含子部门/有效期 DST 提交与来源显示。转移所有者/部门/上传人权限后刷新。
3. 访问审计查询/时间范围/详情与业务引用抽屉正确按 fileId；移入回收站、恢复、永久清理均确认并保留原因/错误反馈。
4. 保留策略仅影响后续引用：新增编辑删除/停用按源码表单；提醒扫描、标已读、延期必须序列化时区，到期处置理由必填且≤500字，全部引用到期才可处置。
5. 对账任务列表、异常过滤、checkHash 开关、运行时轮询、忽略/隔离/修复/登记孤立文件按 action 发送，register_orphan 必填原文件名；抽屉关闭或卸载停止轮询。
6. FileTable 发出的全部10类业务事件与11个配套组件接线可实际操作，所有抽屉及页面样式按原版对照。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0074 | ruoyi-fastapi-frontend/src/api/system/file.js / L1-L242 module 完整内容 | react-front/src/api/system/file.ts |
| I0581 | ruoyi-fastapi-frontend/src/views/system/file/components/FileAclDrawer.vue / L172-L369 script-setup 完整内容 | react-front/src/views/system/file/components/FileAclDrawer.tsx |
| I0582 | ruoyi-fastapi-frontend/src/views/system/file/components/FileAclDrawer.vue / L1-L170 template 完整内容 | react-front/src/views/system/file/components/FileAclDrawer.tsx |
| I0583 | ruoyi-fastapi-frontend/src/views/system/file/components/FileAclDrawer.vue / L371-L388 style-1 完整内容 | react-front/src/views/system/file/components/FileAclDrawer.tsx |
| I0584 | ruoyi-fastapi-frontend/src/views/system/file/components/FileAclDrawer.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/file/components/FileAclDrawer.tsx |
| I0585 | ruoyi-fastapi-frontend/src/views/system/file/components/FileAuditDrawer.vue / L213-L292 script-setup 完整内容 | react-front/src/views/system/file/components/FileAuditDrawer.tsx |
| I0586 | ruoyi-fastapi-frontend/src/views/system/file/components/FileAuditDrawer.vue / L1-L211 template 完整内容 | react-front/src/views/system/file/components/FileAuditDrawer.tsx |
| I0587 | ruoyi-fastapi-frontend/src/views/system/file/components/FileAuditDrawer.vue / L294-L303 style-1 完整内容 | react-front/src/views/system/file/components/FileAuditDrawer.tsx |
| I0588 | ruoyi-fastapi-frontend/src/views/system/file/components/FileAuditDrawer.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/file/components/FileAuditDrawer.tsx |
| I0589 | ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue / L104-L154 script-setup 完整内容 | react-front/src/views/system/file/components/FileDetailDialog.tsx |
| I0590 | ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue / L1-L102 template 完整内容 | react-front/src/views/system/file/components/FileDetailDialog.tsx |
| I0591 | ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue / L156-L170 style-1 完整内容 | react-front/src/views/system/file/components/FileDetailDialog.tsx |
| I0592 | ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/file/components/FileDetailDialog.tsx |
| I0593 | ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue / L360-L653 script-setup 完整内容 | react-front/src/views/system/file/components/FileReconcileDrawer.tsx |
| I0594 | ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue / L1-L358 template 完整内容 | react-front/src/views/system/file/components/FileReconcileDrawer.tsx |
| I0595 | ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue / L655-L770 style-1 完整内容 | react-front/src/views/system/file/components/FileReconcileDrawer.tsx |
| I0596 | ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/file/components/FileReconcileDrawer.tsx |
| I0597 | ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue / L84-L106 script-setup 完整内容 | react-front/src/views/system/file/components/FileReferenceDrawer.tsx |
| I0598 | ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue / L1-L82 template 完整内容 | react-front/src/views/system/file/components/FileReferenceDrawer.tsx |
| I0599 | ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/file/components/FileReferenceDrawer.tsx |
| I0600 | ruoyi-fastapi-frontend/src/views/system/file/components/FileRetentionPolicyDrawer.vue / L143-L248 script-setup 完整内容 | react-front/src/views/system/file/components/FileRetentionPolicyDrawer.tsx |
| I0601 | ruoyi-fastapi-frontend/src/views/system/file/components/FileRetentionPolicyDrawer.vue / L1-L141 template 完整内容 | react-front/src/views/system/file/components/FileRetentionPolicyDrawer.tsx |
| I0602 | ruoyi-fastapi-frontend/src/views/system/file/components/FileRetentionPolicyDrawer.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/file/components/FileRetentionPolicyDrawer.tsx |
| I0603 | ruoyi-fastapi-frontend/src/views/system/file/components/FileRetentionReminderDrawer.vue / L265-L434 script-setup 完整内容 | react-front/src/views/system/file/components/FileRetentionReminderDrawer.tsx |
| I0604 | ruoyi-fastapi-frontend/src/views/system/file/components/FileRetentionReminderDrawer.vue / L1-L263 template 完整内容 | react-front/src/views/system/file/components/FileRetentionReminderDrawer.tsx |
| I0605 | ruoyi-fastapi-frontend/src/views/system/file/components/FileRetentionReminderDrawer.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/file/components/FileRetentionReminderDrawer.tsx |
| I0606 | ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue / L104-L132 script-setup 完整内容 | react-front/src/views/system/file/components/FileSearchForm.tsx |
| I0607 | ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue / L1-L102 template 完整内容 | react-front/src/views/system/file/components/FileSearchForm.tsx |
| I0608 | ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/file/components/FileSearchForm.tsx |
| I0609 | ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue / L92-L116 script-setup 完整内容 | react-front/src/views/system/file/components/FileStatistics.tsx |
| I0610 | ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue / L1-L90 template 完整内容 | react-front/src/views/system/file/components/FileStatistics.tsx |
| I0611 | ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue / L118-L272 style-1 完整内容 | react-front/src/views/system/file/components/FileStatistics.tsx |
| I0612 | ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/file/components/FileStatistics.tsx |
| I0613 | ruoyi-fastapi-frontend/src/views/system/file/components/FileTable.vue / L255-L288 script-setup 完整内容 | react-front/src/views/system/file/components/FileTable.tsx |
| I0614 | ruoyi-fastapi-frontend/src/views/system/file/components/FileTable.vue / L1-L253 template 完整内容 | react-front/src/views/system/file/components/FileTable.tsx |
| I0615 | ruoyi-fastapi-frontend/src/views/system/file/components/FileTable.vue / L290-L297 style-1 完整内容 | react-front/src/views/system/file/components/FileTable.tsx |
| I0616 | ruoyi-fastapi-frontend/src/views/system/file/components/FileTable.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/file/components/FileTable.tsx |
| I0617 | ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue / L80-L165 script-setup 完整内容 | react-front/src/views/system/file/components/FileTransferDialog.tsx |
| I0618 | ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue / L1-L78 template 完整内容 | react-front/src/views/system/file/components/FileTransferDialog.tsx |
| I0619 | ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue / L167-L175 style-1 完整内容 | react-front/src/views/system/file/components/FileTransferDialog.tsx |
| I0620 | ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/file/components/FileTransferDialog.tsx |
| I0621 | ruoyi-fastapi-frontend/src/views/system/file/components/fileFormatters.js / L1-L147 module 完整内容 | react-front/src/views/system/file/components/fileFormatters.ts |
| I0622 | ruoyi-fastapi-frontend/src/views/system/file/index.vue / L163-L375 script-setup 完整内容 | react-front/src/views/system/file/index.tsx |
| I0623 | ruoyi-fastapi-frontend/src/views/system/file/index.vue / L1-L161 template 完整内容 | react-front/src/views/system/file/index.tsx |
| I0624 | ruoyi-fastapi-frontend/src/views/system/file/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/file/index.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/system/file.js

逻辑定位：listFile@L4–10, getFileStats@L13–19, listFileReconcileIssue@L22–28, listFileReconcileRun@L31–37, getFileReconcileStats@L40–45, startFileReconcile@L48–54, handleFileReconcileIssue@L57–63, listFileRetentionPolicy@L66–71, addFileRetentionPolicy@L74–80, updateFileRetentionPolicy@L83–89, delFileRetentionPolicy@L92–97, listFileRetentionReminder@L100–106, scanFileRetentionReminder@L109–114, readFileRetentionReminder@L117–122, extendFileRetention@L125–131, disposeExpiredFile@L134–140, getFile@L143–148, listFileReference@L151–156, listFileAccessLog@L159–165, listFileAcl@L168–173, searchFileAclSubjects@L176–182, getFileAclDeptTree@L185–190, saveFileAcl@L193–199, batchSaveFileAcl@L202–208, transferFile@L211–217, restoreFile@L220–225, purgeFile@L228–233, delFile@L236–241.
- URL/请求对象 L5: `'get' '/system/file/list'`; params=`query`, data=`None`
- URL/请求对象 L14: `'get' '/system/file/stats'`; params=`query`, data=`None`
- URL/请求对象 L23: `'get' '/system/file/reconcile/issues/list'`; params=`query`, data=`None`
- URL/请求对象 L32: `'get' '/system/file/reconcile/runs/list'`; params=`query`, data=`None`
- URL/请求对象 L41: `'get' '/system/file/reconcile/stats'`; params=`None`, data=`None`
- URL/请求对象 L49: `'post' '/system/file/reconcile/run'`; params=`None`, data=`data`
- URL/请求对象 L58: `'put' '/system/file/reconcile/issues/' + issueId`; params=`None`, data=`data`
- URL/请求对象 L67: `'get' '/system/file/retention-policy/list'`; params=`None`, data=`None`
- URL/请求对象 L75: `'post' '/system/file/retention-policy'`; params=`None`, data=`data`
- URL/请求对象 L84: `'put' '/system/file/retention-policy'`; params=`None`, data=`data`
- URL/请求对象 L93: `'delete' '/system/file/retention-policy/' + encodeURIComponent(businessType)`; params=`None`, data=`None`
- URL/请求对象 L101: `'get' '/system/file/retention-reminder/list'`; params=`query`, data=`None`
- URL/请求对象 L110: `'post' '/system/file/retention-reminder/scan'`; params=`None`, data=`None`
- URL/请求对象 L118: `'put' '/system/file/retention-reminder/' + noticeIds + '/read'`; params=`None`, data=`None`
- URL/请求对象 L126: `'put' '/system/file/retention-reminder/' + noticeId + '/extend'`; params=`None`, data=`data`
- URL/请求对象 L135: `'put' '/system/file/retention-reminder/' + noticeId + '/dispose'`; params=`None`, data=`data`
- URL/请求对象 L144: `'get' '/system/file/' + fileId`; params=`None`, data=`None`
- URL/请求对象 L152: `'get' '/system/file/' + fileId + '/reference/list'`; params=`None`, data=`None`
- URL/请求对象 L160: `'get' '/system/file/' + fileId + '/access-log/list'`; params=`query`, data=`None`
- URL/请求对象 L169: `'get' '/system/file/' + fileId + '/acl/list'`; params=`None`, data=`None`
- URL/请求对象 L177: `'get' '/system/file/acl/subjects'`; params=`query`, data=`None`
- URL/请求对象 L186: `'get' '/system/file/acl/dept-tree'`; params=`None`, data=`None`
- URL/请求对象 L194: `'put' '/system/file/' + fileId + '/acl'`; params=`None`, data=`data`
- URL/请求对象 L203: `'put' '/system/file/acl/batch'`; params=`None`, data=`data`
- URL/请求对象 L212: `'put' '/system/file/' + fileIds + '/transfer'`; params=`None`, data=`data`
- URL/请求对象 L221: `'put' '/system/file/' + fileIds + '/restore'`; params=`None`, data=`None`
- URL/请求对象 L229: `'delete' '/system/file/purge/' + fileIds`; params=`None`, data=`None`
- URL/请求对象 L237: `'delete' '/system/file/' + fileIds`; params=`None`, data=`None`

### ruoyi-fastapi-frontend/src/views/system/file/components/FileAclDrawer.vue

逻辑定位：open@L203–255, builtinSourceLabel@L257–265, builtinSourceType@L267–275, addEntry@L277–287, removeEntry@L289–291, handleSubjectTypeChange@L293–297, handleSubjectVisible@L299–303, searchSubjectOptions@L305–318, submit@L320–366, saveAcl@L338–357.
全部模板事件/权限：click=addEntry@L68; change=handleSubjectTypeChange(scope.row)@L77; visible-change= visible => handleSubjectVisible(scope.row, visible) @L108; click=removeEntry(scope.$index)@L155; click=submit@L163; click=visible = false@L166.

### ruoyi-fastapi-frontend/src/views/system/file/components/FileAuditDrawer.vue

逻辑定位：open@L245–257, getList@L259–272, handleQuery@L274–277, resetQuery@L279–284, handleDetail@L286–289.
全部模板事件/权限：closed=detailOpen = false@L7; keyup=handleQuery@L53; click=handleQuery@L68; click=resetQuery@L71; click=handleDetail(scope.row)@L131; pagination=getList@L142; click=visible = false@L146; click=detailOpen = false@L207.

### ruoyi-fastapi-frontend/src/views/system/file/components/FileDetailDialog.vue

逻辑定位：default@L115–115, uploaderPermissionLabel@L125–143, uploaderPermissionTagType@L145–153.
全部模板事件/权限：click=emit('reference', detail)@L62; click=open = false@L98.

### ruoyi-fastapi-frontend/src/views/system/file/components/FileReconcileDrawer.vue

逻辑定位：validator@L418–424, open@L459–464, refreshAll@L466–470, getStats@L472–476, getIssueList@L478–488, getRunList@L490–500, handleStart@L502–512, handleIssueQuery@L514–517, resetIssueQuery@L519–524, handleTabChange@L526–530, handleCommand@L532–541, submitHandle@L543–565, startPolling@L567–573, handleClosed@L575–579, formatLocation@L581–583, formatOptionalSize@L585–587, issueTypeLabel@L589–591, severityLabel@L593–595, severityTagType@L597–599, issueStatusLabel@L601–608, issueStatusType@L610–617, runStatusLabel@L619–625, runStatusType@L627–633, actionLabel@L635–648.
全部模板事件/权限：closed=handleClosed@L7; click=handleStart@L64; tab-change=handleTabChange@L71; keyup=handleIssueQuery@L85; click=handleIssueQuery@L129; click=resetIssueQuery@L132; command=handleCommand($event, scope.row)@L221; pagination=getIssueList@L252; pagination=getRunList@L306; click=handleOpen = false@L351; click=submitHandle@L352.

### ruoyi-fastapi-frontend/src/views/system/file/components/FileReferenceDrawer.vue

逻辑定位：open@L92–103.
全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/views/system/file/components/FileRetentionPolicyDrawer.vue

逻辑定位：open@L173–176, getList@L178–187, resetForm@L189–197, handleAdd@L199–203, handleEdit@L205–215, submit@L217–234, handleDelete@L236–245.
全部模板事件/权限：click=handleAdd@L17; click=handleEdit(scope.row)@L69; click=handleDelete(scope.row)@L77; click=submit@L134; click=formOpen = false@L137.

### ruoyi-fastapi-frontend/src/views/system/file/components/FileRetentionReminderDrawer.vue

逻辑定位：open@L309–313, getList@L315–325, handleQuery@L327–330, resetQuery@L332–336, handleScan@L338–352, handleSelectionChange@L354–356, handleRead@L358–363, isExpired@L365–367, handleExtend@L369–377, submitExtend@L379–396, handleDispose@L398–425, inputValidator@L409–414, defaultExtendTime@L427–431.
全部模板事件/权限：keyup=handleQuery@L27; click=handleQuery@L53; click=resetQuery@L56; click=handleScan@L66; =['system:file:edit']@L67; click=handleRead@L78; selection-change=handleSelectionChange@L87; click=handleExtend(scope.row)@L182; =['system:file:edit']@L183; click=handleDispose(scope.row)@L201; =['system:file:remove']@L202; pagination=getList@L214; click=submitExtend@L256; click=extendOpen = false@L259.

### ruoyi-fastapi-frontend/src/views/system/file/components/FileSearchForm.vue

逻辑定位：default@L112–112, default@L123–123, handleReset@L127–131.
全部模板事件/权限：keyup=emit('query')@L15; keyup=emit('query')@L47; keyup=emit('query')@L56; click=emit('query')@L98; click=handleReset@L99.

### ruoyi-fastapi-frontend/src/views/system/file/components/FileStatistics.vue

逻辑定位：formatPercentage@L110–115.
全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/views/system/file/components/FileTable.vue

逻辑定位：default@L268–268.
全部模板事件/权限：selection-change=emit('selection-change', $event)@L5; click=emit('reference', scope.row)@L93; click=emit('view', scope.row)@L140; =['system:file:query']@L141; click=emit('download', scope.row)@L153; =['system:file:download']@L154; click=emit('acl', scope.row)@L168; =['system:file:edit']@L169; click=emit('transfer', scope.row)@L181; =['system:file:transfer']@L182; click=emit('audit', scope.row)@L190; =['system:file:query']@L191; =['system:file:remove']@L205; click=emit('delete', scope.row)@L218; =['system:file:remove']@L219; click=emit('restore', scope.row)@L231; =['system:file:restore']@L232; click=emit('purge', scope.row)@L246; =['system:file:purge']@L247.

### ruoyi-fastapi-frontend/src/views/system/file/components/FileTransferDialog.vue

逻辑定位：open@L111–128, searchUsers@L130–139, handleUserChange@L141–146, submit@L148–162.
全部模板事件/权限：visible-change=visible => visible && searchUsers('')@L17; change=handleUserChange@L18; click=submit@L71; click=visible = false@L74.

### ruoyi-fastapi-frontend/src/views/system/file/components/fileFormatters.js

逻辑定位：formatFileSize@L3–9, accessTypeLabel@L11–13, statusLabel@L15–21, expirationLabel@L23–29, expirationTagType@L31–36, isAclExpiring@L38–42, storageStatusLabel@L44–51, storageStatusTagType@L53–60, actionLabel@L62–75, resultLabel@L77–84, resultTagType@L86–93, parseOperationDetail@L95–106, auditDetailKeyLabel@L108–146.

### ruoyi-fastapi-frontend/src/views/system/file/index.vue

逻辑定位：getList@L233–247, handleQuery@L250–253, resetQuery@L256–259, handleSelectionChange@L262–280, handleView@L283–288, handleDownload@L291–296, handleReference@L299–301, handleAcl@L304–306, handleTransfer@L309–311, handleAudit@L314–316, handleDelete@L319–339, handleRestore@L342–354, handlePurge@L357–369.
全部模板事件/权限：query=handleQuery@L8; reset=resetQuery@L9; click=handleAcl()@L21; =['system:file:edit']@L22; click=handleTransfer()@L33; =['system:file:transfer']@L34; click=handleRestore()@L45; =['system:file:restore']@L46; click=handlePurge()@L57; =['system:file:purge']@L58; click=handleDelete()@L75; =['system:file:remove']@L76; click=retentionPolicyDrawerRef?.open()@L88; =['system:file:edit']@L89; click=reconcileDrawerRef?.open()@L99; =['system:file:reconcile']@L100; click=retentionReminderDrawerRef?.open()@L110; =['system:file:list']@L111; queryTable=getList@L118; selection-change=handleSelectionChange@L125; view=handleView@L126; download=handleDownload@L127; reference=handleReference@L128; acl=handleAcl@L129; transfer=handleTransfer@L130; audit=handleAudit@L131; delete=handleDelete@L132; restore=handleRestore@L133; purge=handlePurge@L134; pagination=getList@L142; reference=handleReference@L148; refresh=getList@L154; refresh=getList@L156; refresh=getList@L157; refresh=getList@L159.
