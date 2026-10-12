# G032 个人中心资料、头像、密码与时区

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

个人中心资料、头像、密码与时区可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G002 共用数据与表单适配, G003 时区、日期输入与提交序列化, G005 HTTP 请求、会话提示与导出, G006 密码规则与记住密码适配, G008 SVG 图标与图标选择器, G010 会话、权限与路由策略, G021 多标签、页面缓存与刷新, G023 应用入口与响应式导航布局

## 正常、异常与边界检查条件

1. 按 activeTab 展示资料/密码/时区，加载账号信息后同步账号时区；资料表单昵称/手机/邮箱规则与关闭页签保持。
2. 旧/新/确认密码校验，新密码用动态规则；保存失败保持输入与反馈，成功按原状态提示。
3. 头像仅图片可上传，裁剪旋转/缩放/预览和 FormData 提交后同步用户头像，关闭销毁 cropper。
4. auto/custom 时区选择和预览、列表加载失败的当前时区回退/重试、保存中去重与保存后全局同步；设备时区无法识别显示业务时区提示。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0117 | ruoyi-fastapi-frontend/src/api/system/user.js / L74-L79 完整导出 getUserProfile | react-front/src/api/system/user-profile.ts |
| I0118 | ruoyi-fastapi-frontend/src/api/system/user.js / L82-L84 完整导出 getTimezoneOptions | react-front/src/api/system/user-profile.ts |
| I0119 | ruoyi-fastapi-frontend/src/api/system/user.js / L87-L89 完整导出 updateUserTimezone | react-front/src/api/system/user-profile.ts |
| I0120 | ruoyi-fastapi-frontend/src/api/system/user.js / L92-L98 完整导出 updateUserProfile | react-front/src/api/system/user-profile.ts |
| I0121 | ruoyi-fastapi-frontend/src/api/system/user.js / L101-L111 完整导出 updateUserPwd | react-front/src/api/system/user-profile.ts |
| I0122 | ruoyi-fastapi-frontend/src/api/system/user.js / L114-L121 完整导出 uploadAvatar | react-front/src/api/system/user-profile.ts |
| I0677 | ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue / L68-L100 script-setup 完整内容 | react-front/src/views/system/user/profile/index.tsx |
| I0678 | ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue / L1-L66 template 完整内容 | react-front/src/views/system/user/profile/index.tsx |
| I0679 | ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/user/profile/index.tsx |
| I0680 | ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue / L19-L58 script-setup 完整内容 | react-front/src/views/system/user/profile/resetPwd.tsx |
| I0681 | ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue / L1-L17 template 完整内容 | react-front/src/views/system/user/profile/resetPwd.tsx |
| I0682 | ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/user/profile/resetPwd.tsx |
| I0683 | ruoyi-fastapi-frontend/src/views/system/user/profile/timezoneSettings.vue / L44-L125 script-setup 完整内容 | react-front/src/views/system/user/profile/timezoneSettings.tsx |
| I0684 | ruoyi-fastapi-frontend/src/views/system/user/profile/timezoneSettings.vue / L1-L42 template 完整内容 | react-front/src/views/system/user/profile/timezoneSettings.tsx |
| I0685 | ruoyi-fastapi-frontend/src/views/system/user/profile/timezoneSettings.vue / L127-L154 style-1 完整内容 | react-front/src/views/system/user/profile/timezoneSettings.tsx |
| I0686 | ruoyi-fastapi-frontend/src/views/system/user/profile/timezoneSettings.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/user/profile/timezoneSettings.tsx |
| I0687 | ruoyi-fastapi-frontend/src/views/system/user/profile/userAvatar.vue / L61-L145 script-setup 完整内容 | react-front/src/views/system/user/profile/userAvatar.tsx |
| I0688 | ruoyi-fastapi-frontend/src/views/system/user/profile/userAvatar.vue / L1-L59 template 完整内容 | react-front/src/views/system/user/profile/userAvatar.tsx |
| I0689 | ruoyi-fastapi-frontend/src/views/system/user/profile/userAvatar.vue / L147-L171 style-1 完整内容 | react-front/src/views/system/user/profile/userAvatar.tsx |
| I0690 | ruoyi-fastapi-frontend/src/views/system/user/profile/userAvatar.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/user/profile/userAvatar.tsx |
| I0691 | ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue / L25-L67 script-setup 完整内容 | react-front/src/views/system/user/profile/userInfo.tsx |
| I0692 | ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue / L1-L23 template 完整内容 | react-front/src/views/system/user/profile/userInfo.tsx |
| I0693 | ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/views/system/user/profile/userInfo.tsx |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/api/system/user.js

逻辑定位：getUserProfile@L74–79, getTimezoneOptions@L82–84, updateUserTimezone@L87–89, updateUserProfile@L92–98, updateUserPwd@L101–111, uploadAvatar@L114–121.
- URL/请求对象 L75: `'get' '/system/user/profile'`; params=`None`, data=`None`
- URL/请求对象 L83: `'get' '/system/user/profile/timezones'`; params=`None`, data=`None`
- URL/请求对象 L88: `'put' '/system/user/profile/timezone'`; params=`None`, data=`{ timeZone }`
- URL/请求对象 L93: `'put' '/system/user/profile'`; params=`None`, data=`data`
- URL/请求对象 L106: `'put' '/system/user/profile/updatePwd'`; params=`None`, data=`data`
- URL/请求对象 L115: `'post' '/system/user/profile/avatar'`; params=`None`, data=`data`

### ruoyi-fastapi-frontend/src/views/system/user/profile/index.vue

逻辑定位：getUser@L84–91.
全部模板事件/权限：saved=state.user.timeZone = $event@L59.

### ruoyi-fastapi-frontend/src/views/system/user/profile/resetPwd.vue

逻辑定位：equalToPassword@L32–38, submit@L45–53, close@L55–57.
全部模板事件/权限：click=submit@L13; click=close@L14.

### ruoyi-fastapi-frontend/src/views/system/user/profile/timezoneSettings.vue

逻辑定位：loadOptions@L86–97, save@L100–122.
全部模板事件/权限：submit=save@L2; change=fieldError = ''@L18; click=loadOptions@L26.

### ruoyi-fastapi-frontend/src/views/system/user/profile/userAvatar.vue

逻辑定位：editCropper@L87–89, modalOpened@L91–93, requestUpload@L95–95, rotateLeft@L97–99, rotateRight@L101–103, changeScale@L105–108, beforeUpload@L110–121, uploadImg@L123–135, realTime@L137–139, closeDialog@L141–144.
全部模板事件/权限：click=editCropper()@L2; opened=modalOpened@L4; close=closeDialog@L4; realTime=realTime@L16; click=changeScale(1)@L42; click=changeScale(-1)@L45; click=rotateLeft()@L48; click=rotateRight()@L51; click=uploadImg()@L54.

### ruoyi-fastapi-frontend/src/views/system/user/profile/userInfo.vue

逻辑定位：submit@L44–54, close@L57–59.
全部模板事件/权限：click=submit@L19; click=close@L20.
