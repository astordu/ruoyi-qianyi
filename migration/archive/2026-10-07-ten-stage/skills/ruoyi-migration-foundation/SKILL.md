---
name: ruoyi-migration-foundation
description: 为若依 Vue 到 React 迁移建立 react-front 公共基础，处理架构、认证、动态菜单、权限和请求兼容。用于首个模块前的准备或共享依赖补齐。
---

# 建立 React 公共基础

读 [共享协议](../../../migration/CONTRACT.md)、[源码入口和架构决定](../../../migration/PROJECT.md)、project.json 和已确认模块需求。产物只落在 react-front/ 与 migration/foundation/。

1. 检查 react-front 是否已有代码及架构记录，不覆盖现有成果。根据已确认模块识别最小共享依赖，先给具体架构方案。库选择结合当前官方文档核实；不要凭过期版本记忆锁依赖。
2. 对会显著改变视觉、部署或业务语义的未定选择，一次问一个问题并提供推荐；沿用已有决定。普通工具和组织方式可自行决定并记录，不逐项询问许可。
3. 写 migration/foundation/architecture.md、tasks.json、environment.md。每项共享任务有旧版证据、接口边界、依赖模块和可运行验证。这里的架构确认沿用真实用户授权，不伪造 approved。
4. 实现最小可运行 React 工程及当前需要的登录/布局/路由/菜单/权限/API 适配。后端 component 字符串显式映射到 React 组件，未迁移路由显示可识别的未就绪状态，不伪造已迁移页面。
5. 查原版请求、认证、错误、时区、下载、加密及重试规则；按实际启用配置保留兼容性。不要假设只有 axios 换框架即可。可复用的纯 JS 工具先核实 Vue 依赖再使用。
6. 建测试入口和真实启动/构建命令，验证启动、登录/退出/过期、动态菜单、无权限直接访问和请求契约。mock 与真实后端证据区分；不可运行的检查标 unverified/blocked。

写实际执行日志、公共任务状态和目标清单。公共能力由独立 review 检查后才标 verified。保存下一步交接；不要顺手迁移未选择的业务模块。
