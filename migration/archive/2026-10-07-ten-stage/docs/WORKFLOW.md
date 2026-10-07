# 若依 Vue → React 分模块迁移

源前端：`ruoyi-fastapi-frontend/`。目标前端：`react-front/`。
这些 skills 已定义工作流程；当前尚未选择模块、批准架构或实施迁移。

skills 正文位于 `.agents/skills/`，`.qoder/skills/` 提供同名链接。请在此项目中打开新会话；若客户端尚未发现 skill，可直接让 agent 读取对应的 `SKILL.md`。文件中的命令是使用示例，不会自行启动 agent。

## 使用顺序

| 阶段 | Skill | 产物 / 结束条件 |
| --- | --- | --- |
| 1. 人工选择范围 | `$ruoyi-migration-scope` | 模块边界、纳入/排除功能、未决问题 |
| 2. 读代码还原场景 | `$ruoyi-migration-research` | 场景、验收条件、源文件证据及指纹；人工确认需求 |
| 3. React 公共基础 | `$ruoyi-migration-foundation` | 有依据的架构选择及登录、请求、菜单、权限等共享能力 |
| 4. 锁定原版基线 | `$ruoyi-migration-baseline` | 旧系统行为记录、测试数据、原版截图、可执行检查 |
| 5. 拆任务 | `$ruoyi-migration-plan` | 带依赖、修改范围、验收条件的任务列表 |
| 6. 实施一个任务 | `$ruoyi-migration-implement` | React 实现、检查日志、交接；不自行宣布验收通过 |
| 7. 独立覆盖与行为验证 | `$ruoyi-migration-review` | 从原需求逐项映射实现和运行证据 |
| 8. 截图验证 | `$ruoyi-migration-visual` | 同一场景/数据/环境的原版与 React 对比 |
| 9. 人工验收 | `$ruoyi-migration-accept` | 可供人操作的验收清单，记录实际反馈 |
| 10. 新上下文续跑 | `$ruoyi-migration-next` | 下一步动作与最小交接包；每次只执行一个可运行步骤 |

第 3 阶段通常全项目做一次；各模块若暴露新的共享能力，先作为依赖任务补齐。原版基线可在公共基础准备之前收集，但必须在模块实现前完成。第 7、8 阶段均通过，才进入人工验收。

推荐首次输入：

```text
使用 $ruoyi-migration-scope，从系统管理的用户管理开始。
先收集迁移范围，一次问一个关键问题，事实从代码中查。
```

确认需求后输入：

```text
使用 $ruoyi-migration-next，推进模块 system-user 的下一步。
按 migration/modules/system-user/ 的已确认资料执行。
```

新会话也可用相同输入。外层循环每轮启动新 coding agent，先读公共约定和模块 `handoff.md`，再调用 `next`。agent 返回 `awaiting_human`、`blocked`、`accepted` 或重试耗尽时，外层循环应停止该模块；不得用无限重启绕过阻塞。实现会话之后，评审必须使用另一个干净会话/agent。

## 交接与检查

共享文件协议见 [CONTRACT.md](CONTRACT.md)，项目事实和源码入口见 [PROJECT.md](PROJECT.md)。每个模块的资料保存到 `migration/modules/<module-id>/`；不要依靠会话记忆判断完成。

源文件证据和目标代码使用 `ruoyi-migration-research/scripts/evidence.py` 固定版本。脚本只证明文件是否变化，无法证明业务完整性；业务覆盖由逐条验收矩阵、运行检查和人工复核共同确认。

初次试运行建议只选一个小模块。先跑完整闭环，再扩大范围；不要在没有已确认需求和原版基线时批量生成 React 页面。

范围访谈参考了 `qoderharness` 中的 [grill-me](../../qoderharness/.qoder/skills/grill-me/SKILL.md) 及其实际调用的 [grilling](../../qoderharness/.qoder/skills/grilling/SKILL.md)，采用“一次一个关键问题、事实自行调查、决策等待人反馈”。这里的 skills 独立实现，不需要调用外部 `/grilling` 命令。

本次创建后的格式、链接及脚本验证结果见 [VALIDATION.md](VALIDATION.md)。这些检查验证的是流程文件与辅助脚本，不代表业务迁移已经通过。
