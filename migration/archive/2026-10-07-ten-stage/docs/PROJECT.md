# 项目事实与调研入口

以下是创建 skills 时从本地项目读到的事实。执行迁移时重新读取相关源码，文件路径不能代替行为证据。

| 关注点 | 源码入口 | 迁移要核实的行为 |
| --- | --- | --- |
| 构建和依赖 | `ruoyi-fastapi-frontend/package.json` | Vue 3，混用 Element Plus 与 Ant Design Vue；没有通用 E2E 脚本 |
| 静态和隐藏路由 | `src/router/index.js` | 登录、重定向、详情页、面包屑、菜单高亮、历史模式 |
| 后端动态菜单 | `src/store/modules/permission.js`、`src/api/menu.js` | `getRouters`，Layout / ParentView / InnerLink，动态 component 字符串 |
| 插件页面 | `src/utils/pluginViewResolver.js`、前端 `plugins/` | Vue 通过 glob 载入内置/插件视图；React 需要自己的组件映射 |
| 登录和权限 | `src/permission.js`、`src/store/modules/user.js`、`src/directive/`、`src/plugins/auth.js` | 路由守卫、角色/按钮权限、登录过期；隐藏按钮不等于后端授权 |
| HTTP 协议 | `src/utils/request.js`、`src/utils/auth.js`、相关加密/时区工具 | Bearer token、X-Timezone、查询编码、防重复提交、业务 code、422 字段错误、401、二进制下载、传输加密及重试 |
| 具体模块 | `src/views/system/`、`src/views/monitor/`、`src/views/tool/`、`src/api/` | 只沿本次模块和真实依赖调研，不能只读页面入口 |

表内 `src/` 均相对 `ruoyi-fastapi-frontend/`。若路径变化，搜索实际实现并更新证据。

源项目可见 `build:prod`、`test:plugin`、`test:time` 脚本；后两者并不覆盖全部模块操作。`.github/workflows/playwright.yml` 指向当前缺失的 `ruoyi-fastapi-test/`，不能沿用其成功假设。后端 `tests/` 也不能作为前端迁移等价性证据。

## 公共基础应处理的决定

React 的构建工具、JS/TS、路由、状态管理、UI 组件和测试工具尚未选定。先检查已有用户偏好/已存架构记录；没有记录时提出有理由的默认组合，优先满足旧系统行为和可验证性。影响显著的视觉差异或部署变化由用户决定。无需对普通实现细节逐项索要许可。

认证、菜单、权限、字典、分页、下载、插件注册、部署基础路径等作为共享能力显式建任务。后端返回的 Vue component 字符串需要 React 映射，不能靠把整个后台菜单写死来绕过。缺少的共享能力阻塞依赖它的模块，不得临时伪造通过。

Vue 前端和后端保持为参照；默认只修改 `react-front/` 和 `migration/`。确需调整旧项目或后端时，说明原因与影响，并在已确认任务范围内实施。
