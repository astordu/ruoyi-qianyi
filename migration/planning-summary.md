# 全项目 Vue → React 迁移计划（重新开始）

源码快照：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。范围：`ruoyi-fastapi-frontend/` → `react-front/`；339 个文件，748 个内容映射，55 个执行组。

## 轮次与范围

**按“一组完整迁移并验收＝一轮”计算，55 轮能力迁移，再加 1 个整体验收/收尾阶段，基线约 56 个逻辑轮。**
这不是56次CLI调用或56次对话的保证。每组包含选组、实施、验证；大组跨会话续做、验证失败修复和共享依赖复验会增加实际调用/会话次数。当前没有实际耗时或失败率数据，不虚构完成日期或轮次上限。

基础 6 组；公共 14 组；入口 8 组；业务 27 组。10 项集成合同在各组完成后作为一个收尾阶段逐项执行。

旧计划773组是此前会话审阅的比较数据；本轮从源码重新生成，未继承旧进度。此次55组比旧记录减少约93%，覆盖范围没有按组数缩减。

## 分组复核

- 125 个 Vue SFC 各有一个主要交付组，没有一个页面/组件超过5组。所有细粒度函数/模板节点/样式都归所属完整能力，不各自生成执行轮。
- 文件管理、插件管理、表单设计器、AI聊天、任务管理各保留完整业务状态与子组件，组内分步骤续做，不用“状态壳→函数→装配”制造组。
- Cron 的九个内部文件同组；96个SVG图标同组；time.js全部时区/格式化/提交与日期输入同组。
- 字典类型/数据/详情形成同一维护闭环；两个Redis入口形成同一缓存管理能力。用户/角色授权与个人中心是独立真实页面，保留单独能力组。
- 同一源文件跨组只发生在8个共享API模块。按完整导出分区是覆盖映射，不额外创建API函数执行组；目标独立适配文件避免后续组反复改动已通过目标。
- 单内容项组复核：G011 普通与分段文件下载。G011包含一个完整下载模块的四类入口、Range校验、重试/回退与Blob组装，能够独立复用与验证，故保留一组。普通单文件SFC还包括脚本/模板/样式项；不因内容项数自动合并无关能力。

依赖从静态/动态import、glob、模板全局组件、helper、权限指令和资源引用建立；完整边及循环处理理由见 `state/dependency-review.json`。HTTP与会话、主题与导航、路由与视图、iframe与标签的反向关系通过显式接口注入解决，全部真实接线仍需集成验收。

## 保留的原行为与验证缺口

- 时间测试引用的 `ruoyi-fastapi-test/time-contract/contract.mjs` 在工作区缺失。测试本身计入清单；需恢复可信契约或从旧源码建立明确替代用例并记录依据，未标通过。
- AI使用逐行JSON流（NDJSON），不是SSE；React渲染库替换与后端plugin.yaml仍声明Vue npm依赖的兼容性需要真实环境验证，不改后端清单冒充迁移完成。
- 表单设计器及后端代码生成器当前产出Vue文件/模板。这是产品功能，React运行界面迁移仍保留该输出；若要同时生成React业务代码，是另一个范围变更。
- Druid当前页面只显示“我是数据监控”，iframe已注释，按此原行为迁移；Swagger则连接 `/proxy-docs`。不把当前未实现的控制台新增为迁移要求。
- 路由获取Promise失败、redirect查询字符串、字典旧过滤器写法、AI配置字符串布尔判断/无换行尾块、部分请求失败loading等存在原版边界差异观察点。合同明确对照；未运行原版与React浏览器验证，不宣称这些已修复或等价。
- 默认仅排除依赖/产物目录，实际清单排除只有node_modules；未引用的源码/样式/测试/资源仍在339文件内。内容排除只有Vue package-lock.json，新React锁文件由工程组生成。

## 完整执行组

| 组 | 交付能力 | 类别 | 前置组 |
| --- | --- | --- | --- |
| [G001](state/groups/G001/contract.md) | React 工程、环境与部署 | 基础 | 无 |
| [G002](state/groups/G002/contract.md) | 共用数据与表单适配 | 基础 | G001, G003 |
| [G003](state/groups/G003/contract.md) | 时区、日期输入与提交序列化 | 基础 | G001 |
| [G004](state/groups/G004/contract.md) | 传输加密策略与请求响应协议 | 基础 | G001, G002 |
| [G005](state/groups/G005/contract.md) | HTTP 请求、会话提示与导出 | 基础 | G002, G003, G004 |
| [G006](state/groups/G006/contract.md) | 密码规则与记住密码适配 | 基础 | G002, G005 |
| [G007](state/groups/G007/contract.md) | 字典获取、缓存与标签展示 | 公共 | G005 |
| [G008](state/groups/G008/contract.md) | SVG 图标与图标选择器 | 公共 | G001 |
| [G009](state/groups/G009/contract.md) | 系统主题与布局偏好 | 公共 | G001, G002, G005 |
| [G010](state/groups/G010/contract.md) | 会话、权限与路由策略 | 入口 | G002, G003, G005, G006, G009 |
| [G011](state/groups/G011/contract.md) | 普通与分段文件下载 | 公共 | G002, G005 |
| [G012](state/groups/G012/contract.md) | 分页与列表工具栏 | 公共 | G002, G009 |
| [G013](state/groups/G013/contract.md) | 树面板查询、选择与调整 | 公共 | G009 |
| [G014](state/groups/G014/contract.md) | Cron 编辑与运行时间预览 | 公共 | G003, G005 |
| [G015](state/groups/G015/contract.md) | 富文本编辑与图片粘贴 | 公共 | G005, G009 |
| [G016](state/groups/G016/contract.md) | JSON 编辑器校验与主题 | 公共 | G001, G009 |
| [G017](state/groups/G017/contract.md) | Excel 导入弹窗 | 公共 | G005 |
| [G018](state/groups/G018/contract.md) | 通用文件附件上传 | 公共 | G005, G009, G011 |
| [G019](state/groups/G019/contract.md) | 业务文件上传、进度与重试 | 公共 | G005, G009, G011 |
| [G020](state/groups/G020/contract.md) | 图片上传与预览 | 公共 | G002, G005, G009 |
| [G021](state/groups/G021/contract.md) | 多标签、页面缓存与刷新 | 入口 | G002, G008, G009, G010 |
| [G022](state/groups/G022/contract.md) | 顶部公告阅读与详情 | 入口 | G002, G005, G008, G009 |
| [G023](state/groups/G023/contract.md) | 应用入口与响应式导航布局 | 入口 | G002, G003, G005, G007, G008, G009, G010, G011, G012, G013, G014, G015, G016, G017, G018, G019, G020, G021, G022, G029 |
| [G024](state/groups/G024/contract.md) | 登录页面完整流程 | 入口 | G006, G008, G009, G010 |
| [G025](state/groups/G025/contract.md) | 账号注册页面 | 入口 | G006, G008, G009, G010, G024 |
| [G026](state/groups/G026/contract.md) | 锁屏页面与解锁 | 入口 | G003, G009, G010 |
| [G027](state/groups/G027/contract.md) | 首页工作台 | 业务 | G009, G023 |
| [G028](state/groups/G028/contract.md) | 401 与 404 错误页面 | 入口 | G009, G010 |
| [G029](state/groups/G029/contract.md) | 内嵌页面与接口/数据源控制台 | 公共 | G001, G002, G009 |
| [G030](state/groups/G030/contract.md) | 用户管理页面 | 业务 | G002, G003, G005, G006, G007, G010, G012, G013, G017, G023 |
| [G031](state/groups/G031/contract.md) | 按用户分配角色 | 业务 | G002, G005, G012, G021, G023 |
| [G032](state/groups/G032/contract.md) | 个人中心资料、头像、密码与时区 | 业务 | G002, G003, G005, G006, G008, G010, G021, G023 |
| [G033](state/groups/G033/contract.md) | 角色与菜单/数据权限管理 | 业务 | G002, G003, G005, G007, G010, G012, G023 |
| [G034](state/groups/G034/contract.md) | 按角色分配与取消用户 | 业务 | G002, G005, G007, G010, G012, G021, G023 |
| [G035](state/groups/G035/contract.md) | 部门树管理 | 业务 | G002, G005, G007, G010, G012, G023 |
| [G036](state/groups/G036/contract.md) | 菜单树、路由信息与排序 | 业务 | G002, G005, G007, G008, G010, G012, G023 |
| [G037](state/groups/G037/contract.md) | 岗位管理页面 | 业务 | G002, G005, G007, G010, G012, G023 |
| [G038](state/groups/G038/contract.md) | 字典类型与数据管理 | 业务 | G002, G003, G005, G007, G010, G012, G021, G023 |
| [G039](state/groups/G039/contract.md) | 系统参数管理页面 | 业务 | G002, G003, G005, G007, G010, G012, G023 |
| [G040](state/groups/G040/contract.md) | 公告管理、富文本与阅读人 | 业务 | G002, G005, G007, G010, G012, G015, G019, G022, G023 |
| [G041](state/groups/G041/contract.md) | 文件资产管理完整闭环 | 业务 | G002, G003, G005, G010, G011, G012, G023 |
| [G042](state/groups/G042/contract.md) | 插件生命周期、配置、诊断与审计 | 业务 | G002, G003, G005, G007, G010, G012, G016, G023 |
| [G043](state/groups/G043/contract.md) | Redis 缓存概览与键维护 | 业务 | G005, G023 |
| [G044](state/groups/G044/contract.md) | 定时任务配置、运行与同步 | 业务 | G002, G003, G005, G007, G010, G012, G014, G016, G023 |
| [G045](state/groups/G045/contract.md) | 调度日志查询与清理 | 业务 | G002, G003, G005, G007, G010, G012, G021, G023, G044 |
| [G046](state/groups/G046/contract.md) | 登录日志与账号解锁 | 业务 | G002, G003, G005, G007, G010, G012, G023 |
| [G047](state/groups/G047/contract.md) | 在线会话与强退 | 业务 | G002, G005, G010, G012, G023 |
| [G048](state/groups/G048/contract.md) | 操作日志与请求详情 | 业务 | G002, G003, G005, G007, G010, G012, G023 |
| [G049](state/groups/G049/contract.md) | 服务与主机监控 | 业务 | G002, G005, G023 |
| [G050](state/groups/G050/contract.md) | 传输加密监控与联动图表 | 业务 | G002, G004, G005, G023 |
| [G051](state/groups/G051/contract.md) | 表单设计、属性编辑与代码导出 | 业务 | G002, G005, G008, G011, G015, G018, G020, G023 |
| [G052](state/groups/G052/contract.md) | 代码生成表管理、导入与预览 | 业务 | G002, G005, G010, G011, G012, G021, G023 |
| [G053](state/groups/G053/contract.md) | 代码生成字段与模板配置 | 业务 | G002, G005, G021, G023, G036, G038, G052 |
| [G054](state/groups/G054/contract.md) | AI 模型管理 | 业务 | G002, G005, G007, G010, G012, G023 |
| [G055](state/groups/G055/contract.md) | AI 会话、图片输入与流式回答 | 业务 | G005, G008, G011, G023, G054 |

## 逐页面/组件范围

| 原组件/页面 | 主要执行组 | 数量 |
| --- | --- | --- |
| plugins/ai/views/chat/components/AiMessage.vue | G055 | 1 |
| plugins/ai/views/chat/index.vue | G055 | 1 |
| plugins/ai/views/model/index.vue | G054 | 1 |
| src/App.vue | G023 | 1 |
| src/components/Breadcrumb/index.vue | G023 | 1 |
| src/components/BusinessDateTimePicker/index.vue | G003 | 1 |
| src/components/BusinessFileUpload/index.vue | G019 | 1 |
| src/components/Crontab/day.vue | G014 | 1 |
| src/components/Crontab/hour.vue | G014 | 1 |
| src/components/Crontab/index.vue | G014 | 1 |
| src/components/Crontab/min.vue | G014 | 1 |
| src/components/Crontab/month.vue | G014 | 1 |
| src/components/Crontab/result.vue | G014 | 1 |
| src/components/Crontab/second.vue | G014 | 1 |
| src/components/Crontab/week.vue | G014 | 1 |
| src/components/Crontab/year.vue | G014 | 1 |
| src/components/DictTag/index.vue | G007 | 1 |
| src/components/Editor/index.vue | G015 | 1 |
| src/components/ExcelImportDialog/index.vue | G017 | 1 |
| src/components/FileUpload/index.vue | G018 | 1 |
| src/components/Hamburger/index.vue | G023 | 1 |
| src/components/HeaderSearch/index.vue | G023 | 1 |
| src/components/IconSelect/index.vue | G008 | 1 |
| src/components/ImagePreview/index.vue | G020 | 1 |
| src/components/ImageUpload/index.vue | G020 | 1 |
| src/components/JsonEditor/index.vue | G016 | 1 |
| src/components/Pagination/index.vue | G012 | 1 |
| src/components/ParentView/index.vue | G023 | 1 |
| src/components/RightToolbar/index.vue | G012 | 1 |
| src/components/RuoYi/Doc/index.vue | G023 | 1 |
| src/components/RuoYi/Git/index.vue | G023 | 1 |
| src/components/Screenfull/index.vue | G023 | 1 |
| src/components/SizeSelect/index.vue | G023 | 1 |
| src/components/SvgIcon/index.vue | G008 | 1 |
| src/components/TreePanel/index.vue | G013 | 1 |
| src/components/iFrame/index.vue | G029 | 1 |
| src/layout/components/AppMain.vue | G023 | 1 |
| src/layout/components/Copyright/index.vue | G023 | 1 |
| src/layout/components/HeaderNotice/DetailView.vue | G022 | 1 |
| src/layout/components/HeaderNotice/index.vue | G022 | 1 |
| src/layout/components/IframeToggle/index.vue | G029 | 1 |
| src/layout/components/InnerLink/index.vue | G029 | 1 |
| src/layout/components/Navbar.vue | G023 | 1 |
| src/layout/components/Settings/index.vue | G009 | 1 |
| src/layout/components/Sidebar/Link.vue | G023 | 1 |
| src/layout/components/Sidebar/Logo.vue | G023 | 1 |
| src/layout/components/Sidebar/SidebarItem.vue | G023 | 1 |
| src/layout/components/Sidebar/index.vue | G023 | 1 |
| src/layout/components/TagsView/ScrollPane.vue | G021 | 1 |
| src/layout/components/TagsView/index.vue | G021 | 1 |
| src/layout/components/TopBar/index.vue | G023 | 1 |
| src/layout/components/TopNav/index.vue | G023 | 1 |
| src/layout/index.vue | G023 | 1 |
| src/views/dashboard/editable-link-group.vue | G027 | 1 |
| src/views/dashboard/index.vue | G027 | 1 |
| src/views/error/401.vue | G028 | 1 |
| src/views/error/404.vue | G028 | 1 |
| src/views/lock.vue | G026 | 1 |
| src/views/login.vue | G024 | 1 |
| src/views/monitor/cache/index.vue | G043 | 1 |
| src/views/monitor/cache/list.vue | G043 | 1 |
| src/views/monitor/druid/index.vue | G029 | 1 |
| src/views/monitor/job/detail.vue | G044 | 1 |
| src/views/monitor/job/index.vue | G044 | 1 |
| src/views/monitor/job/log.vue | G045 | 1 |
| src/views/monitor/job/runtime.vue | G044 | 1 |
| src/views/monitor/logininfor/index.vue | G046 | 1 |
| src/views/monitor/online/index.vue | G047 | 1 |
| src/views/monitor/operlog/detail.vue | G048 | 1 |
| src/views/monitor/operlog/index.vue | G048 | 1 |
| src/views/monitor/server/index.vue | G049 | 1 |
| src/views/monitor/transportCrypto/index.vue | G050 | 1 |
| src/views/redirect/index.vue | G021 | 1 |
| src/views/register.vue | G025 | 1 |
| src/views/system/config/index.vue | G039 | 1 |
| src/views/system/dept/index.vue | G035 | 1 |
| src/views/system/dict/data.vue | G038 | 1 |
| src/views/system/dict/detail.vue | G038 | 1 |
| src/views/system/dict/index.vue | G038 | 1 |
| src/views/system/file/components/FileAclDrawer.vue | G041 | 1 |
| src/views/system/file/components/FileAuditDrawer.vue | G041 | 1 |
| src/views/system/file/components/FileDetailDialog.vue | G041 | 1 |
| src/views/system/file/components/FileReconcileDrawer.vue | G041 | 1 |
| src/views/system/file/components/FileReferenceDrawer.vue | G041 | 1 |
| src/views/system/file/components/FileRetentionPolicyDrawer.vue | G041 | 1 |
| src/views/system/file/components/FileRetentionReminderDrawer.vue | G041 | 1 |
| src/views/system/file/components/FileSearchForm.vue | G041 | 1 |
| src/views/system/file/components/FileStatistics.vue | G041 | 1 |
| src/views/system/file/components/FileTable.vue | G041 | 1 |
| src/views/system/file/components/FileTransferDialog.vue | G041 | 1 |
| src/views/system/file/index.vue | G041 | 1 |
| src/views/system/menu/index.vue | G036 | 1 |
| src/views/system/notice/ReadUsers.vue | G040 | 1 |
| src/views/system/notice/index.vue | G040 | 1 |
| src/views/system/plugin/components/PluginConfigDialog.vue | G042 | 1 |
| src/views/system/plugin/components/PluginDependencyDialog.vue | G042 | 1 |
| src/views/system/plugin/components/PluginDetailDialog.vue | G042 | 1 |
| src/views/system/plugin/components/PluginDiagnosticDialog.vue | G042 | 1 |
| src/views/system/plugin/components/PluginPlanDialog.vue | G042 | 1 |
| src/views/system/plugin/index.vue | G042 | 1 |
| src/views/system/post/index.vue | G037 | 1 |
| src/views/system/role/authUser.vue | G034 | 1 |
| src/views/system/role/index.vue | G033 | 1 |
| src/views/system/role/selectUser.vue | G034 | 1 |
| src/views/system/user/authRole.vue | G031 | 1 |
| src/views/system/user/index.vue | G030 | 1 |
| src/views/system/user/profile/index.vue | G032 | 1 |
| src/views/system/user/profile/resetPwd.vue | G032 | 1 |
| src/views/system/user/profile/timezoneSettings.vue | G032 | 1 |
| src/views/system/user/profile/userAvatar.vue | G032 | 1 |
| src/views/system/user/profile/userInfo.vue | G032 | 1 |
| src/views/system/user/view.vue | G030 | 1 |
| src/views/tool/build/CodeTypeDialog.vue | G051 | 1 |
| src/views/tool/build/DraggableItem.vue | G051 | 1 |
| src/views/tool/build/IconsDialog.vue | G051 | 1 |
| src/views/tool/build/RightPanel.vue | G051 | 1 |
| src/views/tool/build/TreeNodeDialog.vue | G051 | 1 |
| src/views/tool/build/index.vue | G051 | 1 |
| src/views/tool/gen/basicInfoForm.vue | G053 | 1 |
| src/views/tool/gen/createTable.vue | G052 | 1 |
| src/views/tool/gen/editTable.vue | G053 | 1 |
| src/views/tool/gen/genInfoForm.vue | G053 | 1 |
| src/views/tool/gen/importTable.vue | G052 | 1 |
| src/views/tool/gen/index.vue | G052 | 1 |
| src/views/tool/swagger/index.vue | G029 | 1 |

## 跨组API源码复核

- ruoyi-fastapi-frontend/src/api/monitor/job.js: G014, G044；具体完整导出归属见 plan.json，目标按能力独立适配。
- ruoyi-fastapi-frontend/src/api/system/config.js: G005, G039；具体完整导出归属见 plan.json，目标按能力独立适配。
- ruoyi-fastapi-frontend/src/api/system/dict/data.js: G007, G038；具体完整导出归属见 plan.json，目标按能力独立适配。
- ruoyi-fastapi-frontend/src/api/system/menu.js: G010, G036；具体完整导出归属见 plan.json，目标按能力独立适配。
- ruoyi-fastapi-frontend/src/api/system/notice.js: G022, G040；具体完整导出归属见 plan.json，目标按能力独立适配。
- ruoyi-fastapi-frontend/src/api/system/role.js: G033, G034；具体完整导出归属见 plan.json，目标按能力独立适配。
- ruoyi-fastapi-frontend/src/api/system/user.js: G030, G031, G032；具体完整导出归属见 plan.json，目标按能力独立适配。
- ruoyi-fastapi-frontend/src/api/tool/gen.js: G052, G053；具体完整导出归属见 plan.json，目标按能力独立适配。

## 审阅、验证与交接

`state/inventory.json` 由固定盘点脚本生成；`source-audit.json` 全文解析所有源内容；`plan.json` 保存逐项映射；55份组合同含具体正常/异常/边界条件，10份集成合同含最终真实接线场景。
结构检查 `migration_state.py check` 只能证明清单/登记/快照/依赖合法，不证明业务等价；所有组和集成均为pending，active_group/active_feature为空。React目录仍为空。本阶段只生成计划，未选下一组或实施业务。
下一阶段用 `migration-next-group` 按依赖自动选唯一组，读合同后完整实施与验证；第一组应是G001工程基础。
