"""Human-selected capability boundaries, not a file/function-to-group heuristic."""
GROUPS = []
def g(key, title, phase, patterns, cases, outcome=None, deps=(), notes=''):
    GROUPS.append(dict(key=key, title=title, phase=phase, patterns=patterns.split('|'),
                       cases=cases, outcome=outcome or title+'可完整使用并按原版行为验证',
                       deps=list(deps), notes=notes))

g('build','React 工程、环境与部署','基础',
  '.env.*|.gitignore|Dockerfile|LICENSE|bin/*|html/ie.html|index.html|package.json|package-lock.json|vite.config.js|vite/plugins/*|public/favicon.ico',[
  '开发代理 /dev-api 去掉前缀后指向原后端；多环境 API 前缀、标题、端口与源码键名保持对应，报告不保存环境变量值。',
  'dev、production、stage、docker 模式能启动或构建；产物入口、static/js 与 static/[ext] 路径、原压缩开关按旧配置核对。',
  '深层 history URL 在 MySQL/PostgreSQL 两种 Nginx 配置刷新可回到 index.html，/docker-api/ 转发仍匹配各自服务。',
  'React+TypeScript+Vite+React Router+Ant Design+Context 工程显式导入依赖；替换 Vue 自动导入/setup 插件，SVG/Monaco/压缩能力按真实需要接入。',
  '启动加载动画、favicon、IE 提示页、许可证和 Windows 启动/打包脚本都有去向；Vue npm 锁文件仅登记排除，React 根据新 manifest 生成自己的锁文件。'],
  outcome='空 React 工程可启动、按四种环境构建并部署；业务迁移有统一工具链')
g('data','共用数据与表单适配','基础',
  'src/utils/index.js|src/utils/ruoyi.js|src/utils/validate.js|src/plugins/cache.js|src/directive/common/copyText.js|src/utils/scroll-to.js',[
  'tansParams 对数组、嵌套对象、空字符串/null/undefined 使用旧键名与编码规则；param/param2Obj/getQueryObject 保留各自区别，不合并成改变业务的单一算法。',
  'handleTree 在根父节点缺失、子节点先于父节点时仍按旧 id/parentId 规则组树；字典单值/多值的未匹配值和分隔符规则保留。',
  '深拷贝、对象合并、去重、数字/URL/外链判断、字符串转换、日期范围 begin/end 参数按全部导出覆盖；Date 格式化使用时间能力。',
  'cache 的 JSON 与普通值存取保持 session/local 隔离；copyText 的成功/失败提示、剪贴板回退和事件解绑可验证。',
  'resetForm 适配 React 表单引用；debounce 的 immediate/尾调用与滚动动画结束回调保持旧行为。'],deps=['build','time'])
g('time','时区、日期输入与提交序列化','基础',
  'src/utils/time.js|src/components/BusinessDateTimePicker/index.vue|tests/time/time.test.js',[
  'auto 优先设备时区，设备无法识别时回退业务时区；自定义时区覆盖显示、筛选、导出；App focus/visibility 更新的接线在入口集成验收。',
  '秒与毫秒入口分别处理；RFC3339 带偏移的真实时刻按显示时区格式化，无偏移墙上时间、无效日历日期不能被浏览器 Date 自动修正。',
  'DST gap 返回不存在时间错误；DST fold 保留所有候选偏移并让用户选择，取消选择时不提交。选择器分别保存日期和时间字符串，清空发出 null。',
  'prepareTimeFields 保存原始值和原时区；未修改字段提交保持原瞬时值，修改字段按选定时区转 RFC3339；日期范围上下界保持旧规则。',
  '源 tests/time/time.test.js 的外部 contract.mjs 当前缺失。实施时需恢复可信原契约，或从旧源码建立明确输入输出用例并记录替代依据；不得宣称原测试已经运行通过。'],deps=['build'],
  notes='整个 time.js 的状态、协作函数、选择偏移弹窗与日期控件同组；不拆成 29 个函数轮。缺失原测试是验证输入缺口，不排除该测试。')
g('crypto','传输加密策略与请求响应协议','基础',
  'src/utils/transportCrypto.js|src/utils/transportCryptoPolicy.js',[
  '策略并发加载去重、有效期缓存、强制失效与 60 秒失败重试保持旧行为；无历史策略加载失败时回退 off，有历史策略沿用历史策略并重试。',
  'excludePaths 优先，enabledPaths 非空时限制范围；encrypt/encryptResponse/encryptQuery=false、multipart/binary、固定下载路径按源码豁免。',
  'RSA-OAEP 包装 AES-256-GCM 会话密钥；请求/响应 AAD 的 method/path/direction、kid/version/alg、nonce、base64url、表单和查询信封与后端契约逐字段核对。',
  '无 WebCrypto、无效公钥/信封/过期版本/认证失败不能当作正常 JSON；加密查询 URL 超过 maxEncryptedGetUrlLength 按源码错误路径处理，不泄露明文。',
  '密钥缓存刷新和并发复用、原始请求快照/reset、错误响应解密、旧密钥一次重试与防重复提交豁免联动在 HTTP 集成重放。'],deps=['build'])
g('http','HTTP 请求、会话提示与导出','基础',
  'src/utils/request.js|src/utils/auth.js|src/utils/errorCode.js|src/plugins/modal.js',[
  '请求默认 10 秒超时，携带 Bearer Token 与 X-Timezone；isToken=false、repeatSubmit=false、interval 覆盖保留。POST/PUT 同 URL/数据/时区在默认 1000ms 内拒绝重复；5MB 以上按原分支处理。',
  '参数拼接前完成传输加密；GET 查询编码后清空 params；blob/arraybuffer 直接返回二进制，普通 code 缺省按 200，500/601/其他错误提示类型与拒绝结果对应旧版。',
  '401 只弹一个重新登录确认，取消可继续停留；确认调用会话注销再跳转 /index。通过注入 session-expired handler 消除 request 对 userStore 的反向依赖。',
  '422 将 loc 去掉首段映射 fieldErrors，skipErrorMessage 阻止统一弹出；429 是 warning，网络/超时/HTTP 错误文本按源码区分；Axios 取消不弹错误。',
  '旧密钥错误只重试一次，用原始明文快照重新加密，防重复提交豁免生效。通用 POST 导出使用 form-urlencoded、二进制和 encrypt=false，成功保存，JSON 错误展示后关闭 loading。',
  '共享 getConfigKey 单独落在 config-read.ts，供密码规则和其他页面使用；不要求先完成参数管理页面。'],deps=['data','crypto','time'])
g('password','密码规则与记住密码适配','基础',
  'src/utils/passwordRule.js|src/utils/jsencrypt.js',[
  '按服务端 pwrChrtype 选择全部密码字符规则，长度 6–20；普通表单 validator 和 prompt validator 的错误结果保持对应。',
  '登录记住密码使用原 JSEncrypt 格式加解密；已有 cookie 可读取，失败结果按原版记录，不把密码或源码密钥写入计划/日志。',
  '修改配置后再读取规则，不把规则静态固定；注册、重置密码、个人中心分别验证真实表单接线。'],deps=['http'])
g('dict','字典获取、缓存与标签展示','公共',
  'src/utils/dict.js|src/store/modules/dict.js|src/components/DictTag/index.vue',[
  '首次 dictType 返回空列表后异步填充 label/value/listClass/cssClass；已有缓存不重复请求；移除/清空缓存后页面重新获取。',
  '数值、字符串、数组、按 separator 分割的值按旧宽松值匹配；未匹配项和 showValue、默认 span/彩色 tag 与间距对应旧展示。',
  '空值、空 options、多个字典类型、接口失败均登记实际行为；Vue 模板过滤器写法适配为 React 明确渲染，比较 Vue 当前渲染结果以区分旧缺陷与迁移差异。'],deps=['http'])
g('icons','SVG 图标与图标选择器','公共',
  'src/assets/icons/svg/*|src/components/SvgIcon/*|src/components/IconSelect/*',[
  '96 个 SVG 逐文件复用且哈希一致，生成 #icon-<名称> 精灵或等价组件；图标名、颜色 currentColor、尺寸/className 和异常空名渲染逐项核对。',
  '图标选择器按名称过滤，选择后发出同名结果，reset 清空筛选；原 glob 包含全部文件，不能仅复制当前路由引用的图标。',
  '菜单图标、AI 图标、工具栏图标在浅/深主题展示，Vue/Element 图标注册改为 React 显式映射。'],deps=['build'])
g('theme','系统主题与布局偏好','公共',
  'src/assets/styles/*|src/assets/images/dark.svg|src/assets/images/light.svg|src/settings.js|src/store/modules/settings.js|src/utils/theme.js|src/utils/dynamicTitle.js|src/layout/components/Settings/index.vue',[
  '深/浅主题、primary 颜色的明暗派生、navType 三种布局、侧边栏主题使用源默认设置；Element 样式选择器适配到 Ant Design 后按视觉基线核对。',
  'tagsView/tagsViewPersist/tagsIcon/card或chrome/fixedHeader/sidebarLogo/dynamicTitle/footerVisible 设置和本地保存、重置保持旧结果。',
  '动态标题开关影响 document.title；刷新恢复偏好，关闭标签持久化清除缓存通过注入标签服务接线，不使主题组反向依赖标签实现。',
  'settings 抽屉 openSetting 和事件接口完整提供；全局、过渡、按钮、菜单、mixin 与变量模块全部覆盖，不能只保留首页样式。'],deps=['build'])
g('session','会话、权限与路由策略','入口',
  'src/api/login.js|src/api/menu.js|src/store/modules/user.js|src/store/modules/permission.js|src/store/modules/lock.js|src/plugins/auth.js|src/utils/permission.js|src/directive/permission/*|src/permission.js|src/router/index.js|src/utils/pluginViewResolver.js|tests/plugins/*|src/assets/images/profile.jpg',[
  '登录仅 trim username，成功保存 Token 并解除屏幕锁；getInfo 处理头像空值/相对地址/外链、角色缺省 ROLE_DEFAULT、权限、业务/账号时区及密码修改/过期提示的优先级。',
  '无 token 仅 /login 与 /register 放行；已登录访问 /login 回首页；锁定会话跳 /lock，解锁状态访问 /lock 返回首页，记录并恢复原 lockPath。',
  'roles 未加载时获取 getInfo/getRouters 并注册路由后 replace 重进；权限 OR/角色 OR、超级管理员与 *:*:*、按钮权限按源规则判断。',
  'Layout/ParentView/InnerLink 的服务端组件标记、children 路径扁平化、外链处理、query/meta/hidden/noCache/activeMenu、6 类隐藏业务入口和兜底路由均保持可解析。',
  'builtin 与 plugins glob 注册全部视图；plugin/ai/... 标识不改变。插件路径拒绝非法 pluginId/段与目录穿越，缺失插件视图回 404；原插件测试的输入逐个保留，目标索引改为 .tsx。',
  '注销 API 成功才清理旧状态的行为、getRouters 失败时原 Promise 无 reject、原 redirect 查询串拼接的歧义均列为基线差异观察点；不得通过永久挂起或静默忽略错误伪装完成。'],deps=['http','theme','password'],
  notes='用户、权限、锁状态与守卫有直接协作，合为同组。页面组件使用注入的视图注册表解析；策略可单独验证，真实入口和全部路由接线在 J002/J010 验收。')
g('download','普通与分段文件下载','公共',
  'src/plugins/download.js',[
  'name/resource/file/zip/saveAs 四种下载入口与 encoded 文件名、delete 参数、Bearer Header、错误 JSON 提示保持源码语义。',
  'Range 块大小 8MB；网络/5xx 最多额外重试两次，4xx 不重试。首块 416 回退完整下载，中途 416 报错。',
  '206 Content-Range 必须连续、大小一致且 total>end；组装最终 Blob，200 返回整文件；resource 使用响应文件名，file 缺失文件名回退路径尾段，zip loading 成败都关闭。'],deps=['http'])
g('table','分页与列表工具栏','公共',
  'src/components/Pagination/index.vue|src/components/RightToolbar/index.vue',[
  'page/limit 受控绑定，改变 pageSize 使当前页超总数时回 1，再发送含 page/limit 的 pagination 回调；autoScroll 控制滚动。',
  '搜索显示/隐藏与过渡、queryTable 刷新、列显示/全选/清除同时可用；columns 数组/对象两类输入和 storageKey 持久化按原处理。',
  '相邻不同页面的分页、列配置与搜索状态互不污染；无 storageKey 不写缓存，卸载清理动画/定时器。'],deps=['data','theme'])
g('tree','树面板查询、选择与调整','公共',
  'src/components/TreePanel/index.vue',[
  '过滤、刷新、展开/收起、节点点击/勾选、当前节点与 checkedKeys 暴露方法可调用；自定义 filterMethod 优先。',
  '鼠标/触摸拖宽限制 minWidth/maxWidth，RAF 合并移动与宽度保存；折叠不覆盖原宽度，非法缓存宽度忽略，enableStorage=false 不写入。',
  'disabled/showCheckbox/搜索空值/无树数据/宽度重置按 props 执行；卸载结束监听、RAF、延时保存并恢复 user-select。'],deps=['theme'])
g('cron','Cron 编辑与运行时间预览','公共',
  'src/components/Crontab/*',[
  '秒/分/时/日/月/周/年全部编辑方式及 *,?,/,L,W,# 范围和互斥规则按源 resolveExp/tabCheck/updateCrontabValue 执行。',
  '表达式反解恢复面板，确定填充完整表达式、重置与取消不同；hideComponent 隐藏字段保持其原表达式规则。',
  '最近 5 次运行时间来自任务 preview API 与时区/任务设置，不用前端猜测。无结果显示没有未来时间，请求中 loading 与失败显示保持源码。'],deps=['time','http'],notes='九个内部 Vue 文件同组；预览 API 适配随本组迁，不依赖整个任务页面。')
g('editor','富文本编辑与图片粘贴','公共',
  'src/components/Editor/index.vue',[
  'HTML modelValue、内容变化、readonly/height/minHeight 与工具栏配置保持旧编辑行为；Quill 实例和事件卸载清理。',
  '粘贴剪贴板图片和按钮上传都先按图片类型、默认 5MB 限制校验，成功在当前光标插入 baseAPI+路径；业务失败/网络失败关闭 loading 并提示。',
  '输入空内容与外部更新分别验证，光标位置与图片预览按原 UI 核对，不能用普通 textarea 替代。'],deps=['http','theme'])
g('json','JSON 编辑器校验与主题','公共',
  'src/components/JsonEditor/index.vue',[
  '异步 Monaco 加载期间展示 loading；modelValue 更新触发表单值/校验状态，非法 JSON 显示错误位置，revealError 可定位。',
  '仅有效 JSON 可格式化；外部值变更不形成循环，编辑器高度、禁用和暴露方法与调用方相容。',
  '深浅主题随 DOM 主题改变，卸载销毁 editor/model/listeners，Monaco worker 构建后可加载。'],deps=['build','theme'])
g('excel','Excel 导入弹窗','公共',
  'src/components/ExcelImportDialog/index.vue',[
  'open 重置覆盖更新开关和文件队列，仅一个 xls/xlsx 可提交；无文件或后缀不符提示且不发送。',
  'action 拼接 baseAPI，updateSupport 是 0/1，携带 Token；上传中禁用操作，成功关闭清理并展示 response.msg 后触发 success。',
  'templateAction 未给不显示模板入口，给定时下载对应前缀命名 xlsx；关闭重新打开状态清空，上传失败按原表现登记并对照。'],deps=['http'])
g('fileupload','通用文件附件上传','公共',
  'src/components/FileUpload/index.vue',[
  '默认数量 5、大小 5MB、doc/docx/xls/xlsx/ppt/pptx/txt/pdf 类型；逗号文件名拒绝，多文件上传聚合完成才写 modelValue。',
  '字符串/数组输入归一化、baseAPI 路径回显、删除、拖动排序后按旧逗号格式输出；禁用与 drag/tip props 保留。',
  '业务 code 失败与网络失败撤销正在上传计数并关闭提示；/common/files/ 资源使用认证下载，其他地址走原下载入口。'],deps=['download','http','theme'])
g('businessupload','业务文件上传、进度与重试','公共',
  'src/components/BusinessFileUpload/index.vue',[
  '模型只接收含 fileId 的对象数组；输出 fileId/name/url 与 getFileIds 保持，不能降为逗号 URL 字符串。',
  '文件数含正在上传数量，扩展名/大小/逗号名校验；uploadData 的数组逐值 append，忽略 null/undefined，进度依 event.total 更新。',
  '成功必须含 fileId 与 downloadUrl；失败文件独立显示可重试/删除，重试保留文件与上传参数；禁用/排序/清空和所有请求结束后的状态一致。'],deps=['download','http','theme'])
g('images','图片上传与预览','公共',
  'src/components/ImageUpload/index.vue|src/components/ImagePreview/index.vue',[
  '默认数量5、5MB、png/jpg/jpeg，类型/MIME/扩展名与逗号名称规则按源实现；本地 blob URL 不写回最终字符串。',
  '旧字符串/数组/绝对相对 URL 回显，上传并发成功计数聚合、排序/删除/禁用/预览弹窗与 modelValue 相互一致。',
  'ImagePreview 单图/多图、宽高、失败占位、预览列表与 baseAPI 前缀不重加；错误路径释放 loading 并按原版提示。'],deps=['http','theme'])
g('tabs','多标签、页面缓存与刷新','入口',
  'src/store/modules/tagsView.js|src/plugins/tab.js|src/layout/components/TagsView/*|src/views/redirect/index.vue',[
  'visited/cached/iframeViews 分别管理，路由 path 去重、affix 保留、noCache 排除；标签持久化受设置控制，刷新恢复次序。',
  '关闭当前/左/右/其他/全部及刷新后打开正确目标，保留 affix；最后页面兜底首页，iframe 刷新/移除不同于普通组件。',
  '滚轮/左右按钮/当前标签滚入视野、上下文菜单、card/chrome 两种样式、全屏操作按旧事件处理；卸载清理监听。',
  'React 必须提供可验证的缓存保活机制以替代 KeepAlive，页面保留与退出清理需要真页面集成；不只复制标签 DOM。'],deps=['session','theme'])
g('headernotice','顶部公告阅读与详情','入口',
  'src/layout/components/HeaderNotice/*',[
  'listTop 回显 unreadCount；预览未读公告才 markRead 并更新计数，全部已读使用实际 ids，空列表不请求。',
  'DetailView.open 支持对象预载和 id 查询，通知/公告/消息标签、HTML 内容、空数据及关闭清理保留。',
  '悬浮通知弹层、进入/离开计时与监听不累加；读取/全部读取请求失败按源状态和统一提示重放。'],deps=['http','theme'])
g('shell','应用入口与响应式导航布局','入口',
  'src/App.vue|src/main.js|src/plugins/index.js|src/directive/index.js|src/store/index.js|src/store/modules/app.js|src/layout/index.vue|src/layout/components/index.js|src/layout/components/AppMain.vue|src/layout/components/Copyright/*|src/layout/components/Navbar.vue|src/layout/components/Sidebar/*|src/layout/components/TopBar/*|src/layout/components/TopNav/*|src/components/Breadcrumb/*|src/components/Hamburger/*|src/components/HeaderSearch/*|src/components/Screenfull/*|src/components/SizeSelect/*|src/components/ParentView/*|src/components/RuoYi/*|src/assets/logo/*',[
  'main 所有全局组件/helpers/plugins/directives 逐项改显式 React 导入与 Context，入口 mount/日期时区焦点监听/主题初始化及卸载清理完整。',
  '横向、混合、侧边导航的菜单过滤、单子节点折叠、alwaysShow/hidden/query/external/activeMenu 与面包屑 noRedirect 保持；小屏遮罩、侧边栏 Cookie、控件 size 保留。',
  'HeaderSearch Fuse 按标题/路径检索，↑↓/Enter/Esc、无结果、匹配高亮、路由 query 与外链打开均验收；监听主题和尺寸更新。',
  'Navbar 个人中心、设置抽屉、锁屏、退出与主题切换都接真实能力；文档/Git快捷入口的链接与打开方式保留；所有全局表单/上传/列表组件注册引用有效，版权与 Logo 可见。',
  'AppMain 普通页面缓存和 iframeViews 接真实标签/内嵌服务；focus/visibilitychange 刷新设备时区，不遗留重复 listener。'],deps=['session','tabs','headernotice','icons','dict','table','tree','cron','editor','json','excel','fileupload','businessupload','images','embed'],
  notes='主入口接线集中在此组；业务页面由注册表懒加载，尚未迁的业务不能标通过，最终全部页面接入由 J010 验收。')
g('login','登录页面完整流程','入口','src/views/login.vue|src/assets/images/login-background.jpg',[
  'captchaEnabled 缺省 true、registerEnabled 缺省 false；验证码图/uuid 加载、点击刷新、启停校验与注册链接匹配原版。',
  '表单验证失败不请求；成功 Token 入会话后返回 redirect 并保留其余 query，缺省首页；失败解除 loading 并在验证码启用时重取。',
  '勾选记住密码设置 username/加密 password/rememberMe 30 天 cookie，取消删除；初始 Cookie 回填与 source 默认值保持。',
  '浅/深色背景、400px 登录卡、验证码与 footer 在参考尺寸截图对比；已有的重定向边界问题记录事实再处理。'],deps=['session','password','icons','theme'])
g('register','账号注册页面','入口','src/views/register.vue',[
  '用户名2–20字符、密码6–20和字符规则、确认密码一致与条件验证码校验保持；不合法输入不提交。',
  '成功弹出旧注册成功反馈再跳登录；失败解除 loading，验证码分支按照实际条件重放；接口关闭注册时不伪造成功。',
  '注册页背景和登录链接、图标、浅深主题与原版对照；验证码获取共用 getCodeImg。'],deps=['login','password'])
g('lock','锁屏页面与解锁','入口','src/views/lock.vue',[
  '锁定显示真实账号头像/姓名与按显示时区更新的时钟；空密码不调用 unlockscreen，失败清空/聚焦/错误状态按源执行。',
  '解锁成功恢复原 lockPath 后清除锁记录；退出账号解除锁并注销后跳登录；刷新仍按锁记录拦截。',
  '粒子背景 resize/RAF 与时钟 interval 在卸载清理；头像失败回退和移动屏幕布局有原版截图依据。'],deps=['session','time','theme'])
g('dashboard','首页工作台','业务','src/views/dashboard/*',[
  '项目数/团队排名/访问统计、项目网格、动态、快捷链接、团队与雷达图使用当前源码数据与导航，不能添加假后端接口替换静态内容。',
  'G2Plot Radar 挂载渲染、主题与容器尺寸适配、卸载 destroy；Ant Design 卡片/统计/列表布局与源图表对照。',
  'editable-link-group 中快捷链接与编辑/更多入口按原版实际存在行为保留。'],deps=['shell','theme'])
g('errors','401 与 404 错误页面','入口','src/views/error/*|src/assets/401_images/*|src/assets/404_images/*',[
  '401 返回在 noGoBack 条件下回首页，否则浏览器后退；404 返回首页链接与错误插图/动画完整。',
  '无权限入口与不存在 URL 实际到正确错误页面，直接刷新仍可访问；GIF/云图片逐文件复用。',
  '浅深主题、图片布局、文案和浏览器返回边界按原页面对照。'],deps=['session','theme'])
g('embed','内嵌页面与接口/数据源控制台','公共',
  'src/components/iFrame/*|src/layout/components/InnerLink/*|src/layout/components/IframeToggle/*|src/views/monitor/druid/*|src/views/tool/swagger/*',[
  'iframe src/height/scroll/loading 按旧 props 渲染；InnerLink 使用 route.meta.link，IframeToggle 序列化 query 后在新窗口打开。',
  'Swagger 通过 baseAPI+/proxy-docs 打开实际文档。Druid 当前模板只显示“我是数据监控”，iframe 被注释，保留这项原行为；不擅自启用 /druid/login.html。',
  '同路由 iframe 缓存和关闭由注入标签服务协作；Swagger 的后台登录/跨源/代理失败需真实环境证据，不能靠 mock 冒充文档已接通。'],deps=['build','theme','data'],notes='内嵌载体和两个简单入口按同一内嵌/文档展示能力交付；保留 Druid 的原文字页。标签状态由 tabs 提供接口，避免互相静态导入。')
g('users','用户管理页面','业务','src/views/system/user/index.vue|src/views/system/user/view.vue|src/api/system/user.js',[
  '部门树过滤禁用节点、搜索/时间范围/分页/列设置/选择/详情、完整新增编辑删除和导出均接入真实 API。',
  '用户名2–20、昵称必填、邮箱/手机号和密码规则按源表单；新增加载可选岗位/角色，编辑回填已分配值。',
  '状态开关取消或失败回滚，重置密码 prompt 使用动态规则；用户导入开关、模板与成功刷新接 Excel 弹窗。',
  '角色授权导航保留 userId 与 activeMenu；权限按钮与管理员特殊操作边界按模板原条件。'],deps=['shell','password','excel','tree'])
g('userroles','按用户分配角色','业务','src/views/system/user/authRole.vue',[
  '按路由 userId 读取当前用户和已分配角色，rowKey=roleId，禁用角色不可选择，点击行只切换可选角色。',
  '保存 roleIds 逗号串用 PUT params 提交，成功关闭并回正确原页；请求失败不展示成功。',
  '直接 URL、刷新、取消/关闭与权限隐藏入口接真实路由。'],deps=['shell'])
g('profile','个人中心资料、头像、密码与时区','业务',
  'src/views/system/user/profile/*',[
  '按 activeTab 展示资料/密码/时区，加载账号信息后同步账号时区；资料表单昵称/手机/邮箱规则与关闭页签保持。',
  '旧/新/确认密码校验，新密码用动态规则；保存失败保持输入与反馈，成功按原状态提示。',
  '头像仅图片可上传，裁剪旋转/缩放/预览和 FormData 提交后同步用户头像，关闭销毁 cropper。',
  'auto/custom 时区选择和预览、列表加载失败的当前时区回退/重试、保存中去重与保存后全局同步；设备时区无法识别显示业务时区提示。'],deps=['shell','password','time'])
g('roles','角色与菜单/数据权限管理','业务','src/views/system/role/index.vue|src/api/system/role.js',[
  '角色 CRUD、筛选/分页/导出、状态取消失败回滚与动态按钮权限完整。',
  '菜单树勾选含半选节点，回填已选与父子联动/全选/展开的差异保留；提交权限字符、顺序和菜单 IDs。',
  '数据范围非自定义清空部门，勾选部门同样包含半选；修改提交 dataScope，不混同菜单授权。',
  '分配用户导航 roleId 与返回页保持；角色名/权限字符/顺序必填，无选中项按钮状态按原模板。'],deps=['shell'])
g('roleusers','按角色分配与取消用户','业务','src/views/system/role/authUser.vue|src/views/system/role/selectUser.vue',[
  '路由 roleId 下已授权用户分页查询，单个与批量取消确认后刷新，取消不发送。',
  '选择弹窗分页加载未授权用户、点击行切换勾选，无选择提示；选择多个 userIds 逗号串提交后发成功事件刷新父页。',
  '手机/用户名筛选、回退标签页、权限与请求错误反馈全部接线。'],deps=['shell'])
g('depts','部门树管理','业务','src/views/system/dept/*|src/api/system/dept.js',[
  '树列表查询、展开收起、父部门新增/编辑，编辑父候选排除当前子树；数据用源 handleTree 规则。',
  '递归记录原顺序，只提交有变化的 deptIds/orderNums 逗号串；无变化提示不请求，成功刷新基线。',
  '名称/排序/负责人/手机/邮箱/状态校验与确认删除、取消、错误反馈保留。'],deps=['shell'])
g('menus','菜单树、路由信息与排序','业务','src/views/system/menu/*|src/api/system/menu.js',[
  '目录/菜单/按钮三种类型显示不同字段，父树、图标筛选、路由 path/component/query/权限/外链/缓存/可见性按源模板可编辑。',
  '树展开收起、CRUD 与递归只保存变化的排序，空变化不请求；禁用/隐藏项回显不丢失。',
  'roleMenuTreeselect/treeselect 公共接口归只读 menu-read.ts，角色页不依赖先完成菜单编辑页面；新增菜单后登录/重新加载路由能找到目标页面。'],deps=['shell','icons'])
g('posts','岗位管理页面','业务','src/views/system/post/*|src/api/system/post.js',[
  '编码/名称/状态筛选和分页，完整新增修改删除、批量选择与 Excel 导出按原 endpoint/method 发送。',
  '编码/名称/岗位顺序必填，新增清空、编辑回填、取消不提交；错误时加载/表单反馈与源码对照。',
  '操作权限、状态标签、排序与时间显示按旧页面视觉验证。'],deps=['shell'])
g('dictadmin','字典类型与数据管理','业务','src/views/system/dict/*|src/api/system/dict/type.js|src/api/system/dict/data.js',[
  '字典类型 CRUD/搜索/分页/导出与详情前100条、进入类型数据页完整；route dictId 查类型后设置 dictType。',
  '字典数据标签/键值/排序必填，样式属性、回显样式、状态、默认值与导出保留。',
  '数据新增修改删除后使对应缓存失效，类型刷新缓存清空全局字典；返回关闭打开正确标签，不留下旧类型数据。'],deps=['shell','dict'],notes='类型与数据页面共同组成字典维护闭环，detail 直接读数据、data 读类型，合组保留真实依赖而非拆函数消除循环。')
g('config','系统参数管理页面','业务','src/views/system/config/*|src/api/system/config.js',[
  '参数名称/键名/系统内置/时间筛选与分页、CRUD、选中行、Excel 导出、刷新缓存完整。',
  '名称、键名、键值必填；新增与编辑不同 endpoint method，取消不发送；错误不伪造刷新成功。',
  'getConfigKey 读配置公共能力已由 http 提供，新增或修改后其他调用方看到正确配置与缓存变化。'],deps=['shell'])
g('notices','公告管理、富文本与阅读人','业务','src/views/system/notice/*|src/api/system/notice.js',[
  '公告标题/创建人/类型查询、分页、新增编辑删除；标题和类型校验，内容编辑支持 HTML 与业务文件附件。',
  '详情复用 HeaderNotice DetailView，阅读用户弹窗按 noticeId 分页/筛选/关闭清理；批量删除取消不请求。',
  '新增通知后顶部未读/阅读/全部已读与管理页阅读人保持一致；类型标签/状态与权限全部接真实后端。'],deps=['shell','editor','businessupload','headernotice'])
g('files','文件资产管理完整闭环','业务','src/views/system/file/*|src/views/system/file/components/*|src/api/system/file.js',[
  '搜索/分页/统计/详情/下载，正常/回收站/清理中/过期状态、单批选择和真实 downloadUrl；被业务引用的文件不得移入回收站。',
  'ACL 单文件与批量只处理 private 文件，用户/角色/部门主体搜索异步过期响应不覆盖，deny/包含子部门/有效期 DST 提交与来源显示。转移所有者/部门/上传人权限后刷新。',
  '访问审计查询/时间范围/详情与业务引用抽屉正确按 fileId；移入回收站、恢复、永久清理均确认并保留原因/错误反馈。',
  '保留策略仅影响后续引用：新增编辑删除/停用按源码表单；提醒扫描、标已读、延期必须序列化时区，到期处置理由必填且≤500字，全部引用到期才可处置。',
  '对账任务列表、异常过滤、checkHash 开关、运行时轮询、忽略/隔离/修复/登记孤立文件按 action 发送，register_orphan 必填原文件名；抽屉关闭或卸载停止轮询。',
  'FileTable 发出的全部10类业务事件与11个配套组件接线可实际操作，所有抽屉及页面样式按原版对照。'],deps=['shell','download','time'],
  notes='保留为一组：所有文件抽屉共用列表选择、统计刷新、权限与文件生命周期，整组交付才称文件管理完成。可按“列表→ACL/转移→审计→保留→对账”续做，内部5步骤不增加执行组或提前标通过。')
g('plugins','插件生命周期、配置、诊断与审计','业务',
  'src/views/system/plugin/*|src/views/system/plugin/components/*|src/api/system/plugin.js|src/utils/pluginPlanFormatter.js',[
  '列表筛选、批量选择、启停开关、orphan 状态和 capability.blockedOperations 决定可操作性；取消启停恢复，失败通过真实错误结构展示。',
  '安装/升级/卸载/purge 先 dryRun 计划，ok 且 capability 允许才可确认执行；显示步骤/菜单冲突/迁移脚本/错误与修复建议，不跳过预演。',
  '依赖检查、安装预演和 policy.allowed=false 阻断；批量 plan 的依赖顺序/executablePluginIds、continueOnError、成功失败跳过计数完整。',
  '配置按类型归一化，secret 留空保留规则、必填/数值/正则/JSON 校验与提交 values；详情含前后端交付/菜单/权限/migrations，running或failed 可人工标成功，running 可标失败的边界按源条件。',
  '操作审计查询/排序日期范围/详情/导出exportLimit=5000；保留天数读取配置，dryRun 与真正清理分开确认，0天提示特殊语义；secret 配置变化显示不能泄露。',
  '完整5个业务弹窗和主页面结果弹窗都接原请求；normalizePlan/Batch/Action/Log 的缺省、兼容结构和错误兜底不会把失败转为成功。'],deps=['shell','json','time'],
  notes='主页面共享 pendingAction/计划结果/批量选择/刷新和详情状态，整组迁移，不再拆82组；实施可分生命周期、配置、依赖/诊断、审计4个步骤续做，全部验收后才通过。')
g('cache','Redis 缓存概览与键维护','业务','src/views/monitor/cache/*|src/api/monitor/cache.js',[
  '概览加载 Redis 信息/命令统计/内存 ECharts 图表，resize 与卸载销毁；无数据/失败不能伪造指标。',
  '名称→键→值联动，名称/键显示格式去旧前缀；刷新、清除某名称/键/全部的请求路径与当前选择状态保持。',
  '概览与维护两个入口共用完整缓存 API；权限、loading/空态、图表配色与页面布局按原版。'],deps=['shell'])
g('jobs','定时任务配置、运行与同步','业务','src/views/monitor/job/index.vue|src/views/monitor/job/detail.vue|src/views/monitor/job/runtime.vue|src/api/monitor/job.js|src/utils/job.js|tests/job/*',[
  '任务 CRUD/状态/立即执行/导出与 Cron 生成器真实接入；jobArgs 必须 JSON 数组，jobKwargs 非null非数组对象，拒绝非有限数字；最大并发/允许延迟等规则不丢失。',
  '变更结果 failed→warning、pending→普通消息、其他→success，失败同步可打开 runtime 检查并 retrySync；runningIds/changingIds/submitting 防重入，取消状态回滚。',
  '列表 pending/failed 同步状态自动轮询，版本号与 AbortController 防旧响应覆盖；页面不可见/卸载停止，恢复可见重查。',
  'runtime 在 execution/sync 两类记录间切换，jobId/executionId 定位与显示全部，有限状态刷新、重试、隐藏/卸载终止请求；详情job/log两种模式复用。',
  '原 job-form.test.js 全部断言与 payload 保留；跳日志页携 jobId/executionId，真实执行日志联调后验收。'],deps=['shell','cron','time'],notes='任务配置与运行、同步共用变更状态与刷新，同组；日志查询是独立入口，可另组交付。previewJob API 已在 cron 组，不能重复迁。')
g('joblogs','调度日志查询与清理','业务','src/views/monitor/job/log.vue|src/api/monitor/jobLog.js',[
  'route.params.jobId=0 代表所有任务，query.executionId 可定位执行；切换参数清旧任务名/分页，日期范围按显示时区。',
  '分页查询、详情复用 job detail 的 log 模式、批量删除/全部清理/导出；取消不请求，成功刷新。',
  '关闭日志标签返回正确页面，时区变化下已有范围重查，loading finally 恢复。'],deps=['shell','jobs'])
g('loginlogs','登录日志与账号解锁','业务','src/views/monitor/logininfor/*|src/api/monitor/logininfor.js',[
  '登录地址/用户名/状态/时间范围、分页与排序参数，登录状态标签及设备信息展示。',
  '选中删除、清空、选中用户名解锁各自确认，取消不发送；导出包含当前查询，按钮权限按模板。',
  '时间范围、日期排序、空结果和接口错误按旧版可验证。'],deps=['shell'])
g('online','在线会话与强退','业务','src/views/monitor/online/*|src/api/monitor/online.js',[
  '按IP和用户查询在线会话，行序号/部门/浏览器/登录时间显示，返回的数据切片/total规则按原列表逻辑。',
  '强退针对 tokenId，确认后删除并刷新，取消不请求；当前用户与其他用户真实会话联调。',
  '空状态与无强退权限隐藏按钮，网络失败保留原列表并按统一错误反馈。'],deps=['shell'])
g('operlogs','操作日志与请求详情','业务','src/views/monitor/operlog/*|src/api/monitor/operlog.js',[
  '模块/人员/IP/类型/状态/时间范围筛选、分页/排序/导出、选中删除和全部清空。',
  '详情含请求参数/返回值/异常信息/耗时，JSON 合法格式化、非法保留原文，复制用剪贴板或 textarea 回退。',
  '关闭详情、取消删除、空数据和失败loading按源码；操作权限与时间字段真实渲染。'],deps=['shell'])
g('server','服务与主机监控','业务','src/views/monitor/server/*|src/api/monitor/server.js',[
  '真实 getServer 数据中的 CPU/内存/服务器/磁盘字段依模板呈现，百分比和容量单位与源码一致。',
  '加载时遮罩，完成/失败关闭；无服务器数据不以静态数值冒充。',
  '磁盘长路径、空数组、各单位精度与旧页面截图对照。'],deps=['shell'])
g('cryptomonitor','传输加密监控与联动图表','业务','src/views/monitor/transportCrypto/*|src/api/monitor/transportCrypto.js',[
  '加载真实监控策略、密钥kid/支持版本、启用/强制/排除路径、统计范围与近期失败；缺省数组防止图表崩溃。',
  '失败原因和kid柱图点击与表格行选择相互联动、二次点击取消；零分母率显示不为 Infinity/NaN，数字格式按源码。',
  '自动刷新开关重置timer；主题/resize 更新图表，卸载清除interval与ECharts实例，错误关闭loading。'],deps=['shell','crypto'])
g('formbuilder','表单设计、属性编辑与代码导出','业务',
  'src/views/tool/build/*|src/utils/generator/*',[
  '全部 input/select/layout 组件配置、拖拽添加/嵌套/排序/复制/删除、唯一formId/renderKey、当前选择与清空确认保持。',
  'RightPanel 字段/表单属性、选项树/数字布尔默认值、时间范围、正则、上传/图标/校验/评分/联动等所有类型配置与画布同步，不用缺省演示控件替代。',
  'generate file/dialog 两种 Vue 产品格式，默认 .vue 文件名、html/js/css 生成、格式化/复制/下载保持当前业务输出；迁移的是设计器运行界面，源代码生成产品不会擅自改成 React。',
  'schema 中旧 el-* tag 作为产品数据保留，运行画布采用 React 控件映射；字段切换按相同类型复用属性，嵌套 children 递归更新。',
  'TreeNode/Icons/CodeType 内部弹窗同组，ClipboardJS 改等价剪贴板并保留成功/失败提示、卸载清理；同一schema导出与旧生成器逐字/规范化比对。'],deps=['shell','icons','images','fileupload','editor'],
  notes='画布、RightPanel 和生成器共享 schema，完整组件配置和导出一起验收；组内续做，不拆属性、函数或选择器为新组。')
g('gen','代码生成表管理、导入与预览','业务',
  'src/views/tool/gen/index.vue|src/views/tool/gen/importTable.vue|src/views/tool/gen/createTable.vue|src/api/tool/gen.js',[
  '数据源选项按默认源选择，表查询/时间范围/分页、导入已存在数据库表与创建SQL弹窗都携带 dataSourceName。',
  '生成批次必须同一数据源，genType=1 调接口生成到自定义路径，其他下载zip；表名URL编码、空选择/多源拒绝和数据库同步确认保留。',
  '预览多个文件语法高亮和复制、删除/修改入口/返回刷新 query 保留；生成仍保持 Vue2/Vue3 产品能力，前端运行框架迁移不修改后端模板。'],deps=['shell','download'])
g('genedit','代码生成字段与模板配置','业务',
  'src/views/tool/gen/editTable.vue|src/views/tool/gen/basicInfoForm.vue|src/views/tool/gen/genInfoForm.vue',[
  '按 tableId 加载基本/字段/生成信息，多表单 validate 都通过才提交 columns；拖字段排序同步 sort。',
  'Python 类型、属性、insert/edit/list/query/查询比较符、必填/唯一、字典和 date/time/datetime 分类全部保持。',
  '单/树/主子表模板、子表关联列、包/模块/业务名、菜单树、Vue2 Element/Vue3 ElementPlus 模板与表单列数保持；view 修改后时间 query 刷新返回。',
  'Sortable 生命周期在 React 重建并清理，未通过基本或生成表单时不保存；不能因为 React UI 删除旧模板选项。'],deps=['shell','gen'])
g('aimodels','AI 模型管理','业务','plugins/ai/api/model.js|plugins/ai/views/model/index.vue|plugins/ai/README.md',[
  '模型 CRUD/筛选/分页/选择，provider字典、模型编码/名称/状态必填，推理/图片支持、温度/最大输出、BaseURL/APIKey等字段完整。',
  '凭证由后端管理，报告/测试日志脱敏；新增与编辑分别 POST/PUT，取消删除不调用。',
  'all接口供聊天模型选择，plugin/ai/model/index 标识与后端 ai:model:* 权限不改变；README 改为 React 目录与验证命令。'],deps=['shell','dict'])
g('aichat','AI 会话、图片输入与流式回答','业务','plugins/ai/api/chat.js|plugins/ai/views/chat/*|plugins/ai/views/chat/components/*',[
  '读取已启用模型并选择首项，切换温度；会话按 createdAt 排序、加载当前会话去重、删除当前后清空，用户配置编辑复制后保存并重读。',
  '发送文本/图片前校验模型，用户与助手消息状态、sessionId/runId、content/reasoning/meta/run_info/metrics/error 逐行JSON流按源处理；这是NDJSON，不改成SSE。跨块残余buffer保留，原done时未消费最后无换行数据的边界列为观察点，错误结束解除loading。',
  '停止生成向后端 cancelChatRun 并终止 AbortController；不要只停止前端显示而让服务端继续运行。',
  '图片最多10张与用户配置MB限制、认证 /common/upload、多张合并与失败提示；visionEnabled与模型图片能力分支按实际源码类型判断，配置字符串/Boolean基线需核对。',
  'Markdown/推理折叠、代码高亮/复制、数学/图表能力采用真实 React 渲染替换 markstream-vue，保持消息内容与插件菜单契约；选型不改变后端npm检查声明，兼容性差异在集成登记。',
  '用户向上滚动距离>100暂停自动滚动，接近底部<20恢复；流式更新的RAF/timeout/resize与页面离开清理、图片URL回显和token指标完整。'],deps=['shell','aimodels','download'],
  notes='会话状态、图片和流处理共同组成聊天页闭环，AiMessage 随页迁；可多次会话续做，不能将单个流事件变成迁移组。后端仍声明 Vue 渲染依赖，React替换包与插件依赖检查的兼容验证需单独记录。')

# Export-level ownership prevents unrelated UI from being a prerequisite merely
# because endpoints share a source JS file. These are content mappings, not groups.
API_OVERRIDES = {
 'src/api/system/config.js': {'getConfigKey':'http'},
 'src/api/system/dict/data.js': {'getDicts':'dict'},
 'src/api/monitor/job.js': {'previewJob':'cron'},
 'src/api/system/user.js': {
   **{n:'profile' for n in ['getUserProfile','getTimezoneOptions','updateUserTimezone','updateUserProfile','updateUserPwd','uploadAvatar']},
   **{n:'userroles' for n in ['getAuthRole','updateAuthRole']},
 },
 'src/api/system/role.js': {n:'roleusers' for n in ['allocatedUserList','unallocatedUserList','authUserCancel','authUserCancelAll','authUserSelectAll']},
 'src/api/system/menu.js': {n:'session' for n in ['treeselect','roleMenuTreeselect']},
 'src/api/system/notice.js': {n:'headernotice' for n in ['getNotice','listNoticeTop','markNoticeRead','markNoticeReadAll']},
 'src/api/tool/gen.js': {n:'genedit' for n in ['getGenTable','updateGenTable']},
}

INTEGRATIONS = [
 ('J001','工程、公共协议与资源', ['基础','公共'], [
  '四环境构建、Nginx深链接、真实代理、全部静态资源引用、Monaco worker/图标注册可加载。',
  '同一请求链重放时间字段、加密/解密、Token、去重、422、401、二进制/分段下载；工具单测不能代替真实请求。',
  '通用组件 props/表单/事件/主题在消费页面实际生效，所有原测试迁移并登记缺失时间契约的解决证据。']),
 ('J002','登录、锁屏、权限与导航', ['入口'], [
  '真实登录/注册/验证码/记住密码/重定向/退出/401取消重登、刷新恢复与锁屏解锁链路。',
  '不同角色加载菜单、静态隐藏授权路由和插件路由；外链/iframe/query/未知视图/401/404均可达。',
  '三种布局/搜索/主题/标签保活、持久化、关闭返回、公告阅读与设备时区更新；截图、事件解绑和请求记录同时保存。']),
 ('J003','组织与权限维护', ['users','userroles','profile','roles','roleusers','depts','menus','posts'], [
  '用户→分配角色、角色→分配用户/数据范围→重新登录菜单权限；普通/管理员权限回归。',
  '部门与菜单排序/父子关系、用户导入导出、头像裁剪、密码与账号时区保存后跨页面反映。']),
 ('J004','字典、参数与公告', ['dictadmin','config','notices','headernotice','dict'], [
  '字典维护后缓存失效，所有消费页标签/表单显示新数据；修改参数/密码规则并刷新生效。',
  '公告含富文本和业务附件，顶部未读→详情已读→管理页阅读人→全部已读；附件权限下载一致。']),
 ('J005','文件资产生命周期', ['files','businessupload','fileupload','images','download'], [
  '上传/业务引用→private ACL→转移→认证分段下载→访问审计；引用阻止删除。',
  '策略→提醒扫描→时区延期/全部到期处置→回收站→恢复/清理；存储对账异常修复、关闭停止轮询。']),
 ('J006','插件与AI完整流程', ['plugins','aimodels','aichat','json','session'], [
  '真实后端插件清单菜单可加载React页面，依赖检查/安装预演/capability阻断/实际生命周期与迁移历史。',
  '配置校验与secret保留、批量计划执行、操作审计导出和保留清理在测试环境安全重放。',
  '模型创建→聊天模型选择→历史/配置/图片→多块流式事件/停止服务端run→重新进入；React渲染替换与后端Vue依赖声明的兼容问题必须有结论。']),
 ('J007','任务与系统监控', ['cache','jobs','joblogs','loginlogs','online','operlogs','server','cryptomonitor','cron','embed'], [
  'Cron按任务时区预览→创建任务→同步失败重试/成功→执行→executionId日志，页面隐藏和离开不继续轮询。',
  'Redis概览/键清理、在线强退/登录日志解锁、操作详情、主机与加密统计来自真实接口；图表点击联动与主题/resize回归。',
  'Swagger通过部署代理可访问，登录或跨源限制有真实诊断；Druid保留原版文字页与注释的iframe行为。']),
 ('J008','设计器与代码生成', ['formbuilder','gen','genedit'], [
  '全部schema组件拖拽/复制/配置/嵌套，导出file/dialog与原Vue生成产品对照；不得擅改生成模板。',
  '多数据源导入/创建SQL→字段配置→预览→同源批量zip/路径生成→同步结构，Vue2/Vue3产品模板保留。']),
 ('J009','全站视觉与首页', ['dashboard','theme','shell','icons','errors'], [
  '当前首页静态数据、快捷入口和Radar真实呈现。所有路由按同视口/账号/数据截原版和目标；覆盖浅深主题、小屏、表单、抽屉、编辑器、图表、空态和长文案。',
  '逐页面记录视觉差异；Ant Design替换Element的默认外观不视为自动等价，迁移后样式应以原版为基线。']),
 ('J010','全项目收尾与遗漏回归', 'ALL', [
  '全部339源文件的去向真实存在，所有55能力组与J001–J009的有效证据齐全；源/目标/合同快照一致。',
  '注册表包含全部builtin/plugin视图，不以新占位组件/假接口/待接按钮冒充迁移完成；原Druid文字页等源码既有占位行为明确保留并登记。真实深链刷新、菜单和隐藏入口全量遍历。',
  '运行目标类型检查、相关测试、完整构建和最终 check --final；无未解决失败/阻塞/缺失验证。任何不能取得的原版或后端证据明确阻塞相应验收而非标passed。']),
]
