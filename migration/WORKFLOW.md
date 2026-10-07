# 四步迁移流程

适用于按模块将 Vue 迁移到 React。源/目标目录在范围访谈中确定，写入本次 PRD。

| 阶段 | Skill | 输出 |
| --- | --- | --- |
| 确认范围 | `$grill-me-with-migration-scope` | 一个模块的边界与真实确认 |
| 需求 PRD | `$to-prd-migration` | 场景、源码证据、验收条件和短任务清单 |
| 实施迁移 | `$implements-migration` | React 代码、原版基线和实施进度 |
| 迁移验证 | `$validation-migration` | 行为覆盖、运行检查、截图对比和人工验收 |

前三个分别基于 qoderharness 的 grill-me/grilling、to-prd、implement 改写；第四个按本次迁移验证要求新增。原版 [grilling](../.agents/skills/grilling/SKILL.md) 已完整复制进本项目，作为公共访谈技能，由 grill-me-with-migration-scope 读取并复用；以后本项目的其他技能也可以直接引用它。

四个迁移阶段加一个公共 grilling 技能，所需技能和技术文档均在本项目内，不依赖 qoderharness 的安装或目录。实现技能已包含所需测试步骤，无需外部 `/tdd`；这些技能不会自动发布需求或提交代码。

技能正文在 `.agents/skills/`，`.qoder/skills/` 提供同名入口。请在此项目新会话中使用；客户端未发现 skill 时，可让 agent 直接读取对应 SKILL.md。

## 一个模块保留的资料

```text
.qoder/prd/<module-id>.md                     # 需求、证据、验收、短任务清单
.qoder/migration/<module-id>/progress.md      # 实施进度、自检、下一步
.qoder/migration/<module-id>/validation.md    # 独立验证与人工验收反馈
.qoder/migration/<module-id>/screenshots/    # 原版和目标真实截图
```

访谈摘要进入 PRD，后续统一读取 PRD 中的范围、路径和决定。执行时按需生成资料，不预填确认或通过状态。

前端转换细节统一放在 [vue-react-convert.md](vue-react-convert.md)。PRD 定义“迁哪些行为、凭什么验收”，技术文档指导“Vue 到 React 如何实现”，验证重新读取真实源码和结果。

## 开始与续跑

```text
使用 $grill-me-with-migration-scope，确认我要迁移的 Vue 模块范围。
先确认范围，一次问一个关键问题，事实从代码查。
```

范围确认后生成 PRD，PRD 确认后实施。新 coding agent 读取同一份 PRD 和 progress.md，接着做下一个任务；不需要专门的 next skill。正式 validation 使用另一个新会话/agent。遇到未决需求、缺环境或重复修复无进展就写明阻塞，不无限重启。

这四个 skills 定义流程；实际连续启动新 agent 由用户或外层执行器负责。复用到其他项目时，一起携带五个 skill 目录和 migration/vue-react-convert.md，保留相对目录关系。

之前十阶段方案移至 `migration/archive/2026-10-07-ten-stage/`，退出技能发现目录，不再参与当前流程。该目录仅留历史备份。
