# G008 SVG 图标与图标选择器

状态：pending。源清单：`aa6d95beb22b39360d2d8e0cdb5b59ad77bafd4f2d0f2998cd4549d8aa6fe318`。仅规划，未实施/未验收。

## 可观察交付与边界

SVG 图标与图标选择器可完整使用并按原版行为验证

本组拥有的所有源内容、协作状态、函数、模板、事件、样式、API和必要接线一并完成；

依赖：G001 React 工程、环境与部署

## 正常、异常与边界检查条件

1. 96 个 SVG 逐文件复用且哈希一致，生成 #icon-<名称> 精灵或等价组件；图标名、颜色 currentColor、尺寸/className 和异常空名渲染逐项核对。
2. 图标选择器按名称过滤，选择后发出同名结果，reset 清空筛选；原 glob 包含全部文件，不能仅复制当前路由引用的图标。
3. 菜单图标、AI 图标、工具栏图标在浅/深主题展示，Vue/Element 图标注册改为 React 显式映射。

这些条件来自本轮旧源码审阅；源中存在的缺陷/占位行为记录基线，不能擅自新增业务或用缺陷掩盖迁移错误。

## 验证与证据

- 工具/协议：按上述具体输入输出与分支做适量契约测试；组件：覆盖真实 props/事件/受控更新/卸载；页面：用原版和目标同账号同数据重放完整操作、取消和失败路径。
- API 适配逐字段核对下列 url/method/params/data 及后端响应，单测 mock 仅证明本组逻辑；真实请求、路由、共享状态和页面组合另留集成证据。
- 样式/资源以原页面截图为基线，保留对照截图；纯工具不虚构点击。验证报告给出命令、实际结果与独立日志/截图，不把合同、审阅JSON或构建成功当业务等价证据。
- 大组可以组内写 progress.md 并跨会话续做；只有本组完整实现且相应验证真实通过后调用 record，后续集成仍须完成。

## 全部源内容与目标映射

| 项 | 原文件/定位 | 目标 |
| --- | --- | --- |
| I0142 | ruoyi-fastapi-frontend/src/assets/icons/svg/404.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/404.svg |
| I0143 | ruoyi-fastapi-frontend/src/assets/icons/svg/ai-chat.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/ai-chat.svg |
| I0144 | ruoyi-fastapi-frontend/src/assets/icons/svg/ai-manage.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/ai-manage.svg |
| I0145 | ruoyi-fastapi-frontend/src/assets/icons/svg/ai-model.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/ai-model.svg |
| I0146 | ruoyi-fastapi-frontend/src/assets/icons/svg/bell.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/bell.svg |
| I0147 | ruoyi-fastapi-frontend/src/assets/icons/svg/bug.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/bug.svg |
| I0148 | ruoyi-fastapi-frontend/src/assets/icons/svg/build.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/build.svg |
| I0149 | ruoyi-fastapi-frontend/src/assets/icons/svg/button.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/button.svg |
| I0150 | ruoyi-fastapi-frontend/src/assets/icons/svg/cascader.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/cascader.svg |
| I0151 | ruoyi-fastapi-frontend/src/assets/icons/svg/chart.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/chart.svg |
| I0152 | ruoyi-fastapi-frontend/src/assets/icons/svg/checkbox.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/checkbox.svg |
| I0153 | ruoyi-fastapi-frontend/src/assets/icons/svg/clipboard.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/clipboard.svg |
| I0154 | ruoyi-fastapi-frontend/src/assets/icons/svg/code.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/code.svg |
| I0155 | ruoyi-fastapi-frontend/src/assets/icons/svg/color.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/color.svg |
| I0156 | ruoyi-fastapi-frontend/src/assets/icons/svg/component.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/component.svg |
| I0157 | ruoyi-fastapi-frontend/src/assets/icons/svg/dashboard.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/dashboard.svg |
| I0158 | ruoyi-fastapi-frontend/src/assets/icons/svg/date-range.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/date-range.svg |
| I0159 | ruoyi-fastapi-frontend/src/assets/icons/svg/date.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/date.svg |
| I0160 | ruoyi-fastapi-frontend/src/assets/icons/svg/deepthink.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/deepthink.svg |
| I0161 | ruoyi-fastapi-frontend/src/assets/icons/svg/dict.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/dict.svg |
| I0162 | ruoyi-fastapi-frontend/src/assets/icons/svg/documentation.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/documentation.svg |
| I0163 | ruoyi-fastapi-frontend/src/assets/icons/svg/download.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/download.svg |
| I0164 | ruoyi-fastapi-frontend/src/assets/icons/svg/drag.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/drag.svg |
| I0165 | ruoyi-fastapi-frontend/src/assets/icons/svg/druid.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/druid.svg |
| I0166 | ruoyi-fastapi-frontend/src/assets/icons/svg/edit.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/edit.svg |
| I0167 | ruoyi-fastapi-frontend/src/assets/icons/svg/education.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/education.svg |
| I0168 | ruoyi-fastapi-frontend/src/assets/icons/svg/email.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/email.svg |
| I0169 | ruoyi-fastapi-frontend/src/assets/icons/svg/enter.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/enter.svg |
| I0170 | ruoyi-fastapi-frontend/src/assets/icons/svg/example.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/example.svg |
| I0171 | ruoyi-fastapi-frontend/src/assets/icons/svg/excel.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/excel.svg |
| I0172 | ruoyi-fastapi-frontend/src/assets/icons/svg/exit-fullscreen.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/exit-fullscreen.svg |
| I0173 | ruoyi-fastapi-frontend/src/assets/icons/svg/eye-open.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/eye-open.svg |
| I0174 | ruoyi-fastapi-frontend/src/assets/icons/svg/eye.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/eye.svg |
| I0175 | ruoyi-fastapi-frontend/src/assets/icons/svg/form.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/form.svg |
| I0176 | ruoyi-fastapi-frontend/src/assets/icons/svg/fullscreen.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/fullscreen.svg |
| I0177 | ruoyi-fastapi-frontend/src/assets/icons/svg/github.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/github.svg |
| I0178 | ruoyi-fastapi-frontend/src/assets/icons/svg/guide.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/guide.svg |
| I0179 | ruoyi-fastapi-frontend/src/assets/icons/svg/icon.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/icon.svg |
| I0180 | ruoyi-fastapi-frontend/src/assets/icons/svg/input.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/input.svg |
| I0181 | ruoyi-fastapi-frontend/src/assets/icons/svg/international.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/international.svg |
| I0182 | ruoyi-fastapi-frontend/src/assets/icons/svg/job.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/job.svg |
| I0183 | ruoyi-fastapi-frontend/src/assets/icons/svg/language.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/language.svg |
| I0184 | ruoyi-fastapi-frontend/src/assets/icons/svg/link.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/link.svg |
| I0185 | ruoyi-fastapi-frontend/src/assets/icons/svg/list.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/list.svg |
| I0186 | ruoyi-fastapi-frontend/src/assets/icons/svg/lock.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/lock.svg |
| I0187 | ruoyi-fastapi-frontend/src/assets/icons/svg/log.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/log.svg |
| I0188 | ruoyi-fastapi-frontend/src/assets/icons/svg/logininfor.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/logininfor.svg |
| I0189 | ruoyi-fastapi-frontend/src/assets/icons/svg/message.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/message.svg |
| I0190 | ruoyi-fastapi-frontend/src/assets/icons/svg/money.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/money.svg |
| I0191 | ruoyi-fastapi-frontend/src/assets/icons/svg/monitor.svg / L1-L2 asset 完整内容 | react-front/src/assets/icons/svg/monitor.svg |
| I0192 | ruoyi-fastapi-frontend/src/assets/icons/svg/moon.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/moon.svg |
| I0193 | ruoyi-fastapi-frontend/src/assets/icons/svg/more-up.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/more-up.svg |
| I0194 | ruoyi-fastapi-frontend/src/assets/icons/svg/nested.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/nested.svg |
| I0195 | ruoyi-fastapi-frontend/src/assets/icons/svg/number.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/number.svg |
| I0196 | ruoyi-fastapi-frontend/src/assets/icons/svg/online.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/online.svg |
| I0197 | ruoyi-fastapi-frontend/src/assets/icons/svg/password.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/password.svg |
| I0198 | ruoyi-fastapi-frontend/src/assets/icons/svg/pdf.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/pdf.svg |
| I0199 | ruoyi-fastapi-frontend/src/assets/icons/svg/people.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/people.svg |
| I0200 | ruoyi-fastapi-frontend/src/assets/icons/svg/peoples.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/peoples.svg |
| I0201 | ruoyi-fastapi-frontend/src/assets/icons/svg/phone.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/phone.svg |
| I0202 | ruoyi-fastapi-frontend/src/assets/icons/svg/post.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/post.svg |
| I0203 | ruoyi-fastapi-frontend/src/assets/icons/svg/qq.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/qq.svg |
| I0204 | ruoyi-fastapi-frontend/src/assets/icons/svg/question.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/question.svg |
| I0205 | ruoyi-fastapi-frontend/src/assets/icons/svg/radio.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/radio.svg |
| I0206 | ruoyi-fastapi-frontend/src/assets/icons/svg/rate.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/rate.svg |
| I0207 | ruoyi-fastapi-frontend/src/assets/icons/svg/redis-list.svg / L1-L2 asset 完整内容 | react-front/src/assets/icons/svg/redis-list.svg |
| I0208 | ruoyi-fastapi-frontend/src/assets/icons/svg/redis.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/redis.svg |
| I0209 | ruoyi-fastapi-frontend/src/assets/icons/svg/row.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/row.svg |
| I0210 | ruoyi-fastapi-frontend/src/assets/icons/svg/search.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/search.svg |
| I0211 | ruoyi-fastapi-frontend/src/assets/icons/svg/select.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/select.svg |
| I0212 | ruoyi-fastapi-frontend/src/assets/icons/svg/server.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/server.svg |
| I0213 | ruoyi-fastapi-frontend/src/assets/icons/svg/shopping.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/shopping.svg |
| I0214 | ruoyi-fastapi-frontend/src/assets/icons/svg/size.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/size.svg |
| I0215 | ruoyi-fastapi-frontend/src/assets/icons/svg/skill.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/skill.svg |
| I0216 | ruoyi-fastapi-frontend/src/assets/icons/svg/slider.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/slider.svg |
| I0217 | ruoyi-fastapi-frontend/src/assets/icons/svg/star.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/star.svg |
| I0218 | ruoyi-fastapi-frontend/src/assets/icons/svg/sunny.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/sunny.svg |
| I0219 | ruoyi-fastapi-frontend/src/assets/icons/svg/swagger.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/swagger.svg |
| I0220 | ruoyi-fastapi-frontend/src/assets/icons/svg/switch.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/switch.svg |
| I0221 | ruoyi-fastapi-frontend/src/assets/icons/svg/system.svg / L1-L2 asset 完整内容 | react-front/src/assets/icons/svg/system.svg |
| I0222 | ruoyi-fastapi-frontend/src/assets/icons/svg/tab.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/tab.svg |
| I0223 | ruoyi-fastapi-frontend/src/assets/icons/svg/table.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/table.svg |
| I0224 | ruoyi-fastapi-frontend/src/assets/icons/svg/textarea.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/textarea.svg |
| I0225 | ruoyi-fastapi-frontend/src/assets/icons/svg/theme.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/theme.svg |
| I0226 | ruoyi-fastapi-frontend/src/assets/icons/svg/time-range.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/time-range.svg |
| I0227 | ruoyi-fastapi-frontend/src/assets/icons/svg/time.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/time.svg |
| I0228 | ruoyi-fastapi-frontend/src/assets/icons/svg/tool.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/tool.svg |
| I0229 | ruoyi-fastapi-frontend/src/assets/icons/svg/tree-table.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/tree-table.svg |
| I0230 | ruoyi-fastapi-frontend/src/assets/icons/svg/tree.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/tree.svg |
| I0231 | ruoyi-fastapi-frontend/src/assets/icons/svg/upload.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/upload.svg |
| I0232 | ruoyi-fastapi-frontend/src/assets/icons/svg/user.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/user.svg |
| I0233 | ruoyi-fastapi-frontend/src/assets/icons/svg/validCode.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/validCode.svg |
| I0234 | ruoyi-fastapi-frontend/src/assets/icons/svg/wechat.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/wechat.svg |
| I0235 | ruoyi-fastapi-frontend/src/assets/icons/svg/zip.svg / L1-L1 asset 完整内容 | react-front/src/assets/icons/svg/zip.svg |
| I0320 | ruoyi-fastapi-frontend/src/components/IconSelect/index.vue / L26-L59 script-setup 完整内容 | react-front/src/components/IconSelect/index.tsx |
| I0321 | ruoyi-fastapi-frontend/src/components/IconSelect/index.vue / L1-L24 template 完整内容 | react-front/src/components/IconSelect/index.tsx |
| I0322 | ruoyi-fastapi-frontend/src/components/IconSelect/index.vue / L61-L111 style-1 完整内容 | react-front/src/components/IconSelect/index.tsx |
| I0323 | ruoyi-fastapi-frontend/src/components/IconSelect/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/IconSelect/index.tsx |
| I0324 | ruoyi-fastapi-frontend/src/components/IconSelect/requireIcons.js / L1-L8 module 完整内容 | react-front/src/components/IconSelect/requireIcons.ts |
| I0361 | ruoyi-fastapi-frontend/src/components/SvgIcon/index.vue / L7-L35 script 完整内容 | react-front/src/components/SvgIcon/index.tsx |
| I0362 | ruoyi-fastapi-frontend/src/components/SvgIcon/index.vue / L1-L5 template 完整内容 | react-front/src/components/SvgIcon/index.tsx |
| I0363 | ruoyi-fastapi-frontend/src/components/SvgIcon/index.vue / L37-L53 style-1 完整内容 | react-front/src/components/SvgIcon/index.tsx |
| I0364 | ruoyi-fastapi-frontend/src/components/SvgIcon/index.vue / SFC 外壳、块属性与全部块间注释 | react-front/src/components/SvgIcon/index.tsx |
| I0365 | ruoyi-fastapi-frontend/src/components/SvgIcon/svgicon.js / L1-L11 module 完整内容 | react-front/src/components/SvgIcon/svgicon.ts |

完整原版结构证据：`migration/state/source-audit.json` 对应 files/sections，包括全部声明、函数条件/返回、template 指令/事件、样式选择器。这些是定位补充，不替代上面的实际行为检查。

## 原版行为定位与请求清单

### ruoyi-fastapi-frontend/src/assets/icons/svg/404.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/ai-chat.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/ai-manage.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/ai-model.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/bell.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/bug.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/build.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/button.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/cascader.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/chart.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/checkbox.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/clipboard.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/code.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/color.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/component.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/dashboard.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/date-range.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/date.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/deepthink.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/dict.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/documentation.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/download.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/drag.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/druid.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/edit.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/education.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/email.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/enter.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/example.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/excel.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/exit-fullscreen.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/eye-open.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/eye.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/form.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/fullscreen.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/github.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/guide.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/icon.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/input.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/international.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/job.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/language.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/link.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/list.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/lock.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/log.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/logininfor.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/message.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/money.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/monitor.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/moon.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/more-up.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/nested.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/number.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/online.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/password.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/pdf.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/people.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/peoples.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/phone.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/post.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/qq.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/question.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/radio.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/rate.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/redis-list.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/redis.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/row.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/search.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/select.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/server.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/shopping.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/size.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/skill.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/slider.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/star.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/sunny.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/swagger.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/switch.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/system.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/tab.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/table.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/textarea.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/theme.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/time-range.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/time.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/tool.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/tree-table.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/tree.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/upload.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/user.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/validCode.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/wechat.svg


### ruoyi-fastapi-frontend/src/assets/icons/svg/zip.svg


### ruoyi-fastapi-frontend/src/components/IconSelect/index.vue

逻辑定位：filterIcons@L39–44, selectedIcon@L46–49, reset@L51–54.
全部模板事件/权限：clear=filterIcons@L8; input=filterIcons@L9; click=selectedIcon(item)@L15.

### ruoyi-fastapi-frontend/src/components/IconSelect/requireIcons.js


### ruoyi-fastapi-frontend/src/components/SvgIcon/index.vue

逻辑定位：setup@L23–33.
全部模板事件/权限：.

### ruoyi-fastapi-frontend/src/components/SvgIcon/svgicon.js

逻辑定位：install@L4–9.
