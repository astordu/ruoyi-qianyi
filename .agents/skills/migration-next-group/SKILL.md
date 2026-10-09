---
name: migration-next-group
description: 从完整迁移计划中按依赖和固定优先级自动选择本轮唯一小组，生成可恢复的本轮任务。用于每轮开始、续跑或阻塞后的重新选择。
---

# 自动选择下一组

读 [状态协议](../migration-plan/references/state-protocol.md)，默认 `migration/state/`。本 skill 选任务，不实施代码，也不让用户每轮选模块。

1. 运行 `python3 .agents/skills/migration-plan/scripts/migration_state.py next --state migration/state --claim`，作为唯一选组入口；不跳过检查或手工挑容易的小组。
2. 脚本检查源快照、全文件审阅、内容登记、依赖和已有验证。文件新增/删除/修改、链接变化或计划不完整时，报告需要调用 [migration-plan](../migration-plan/SKILL.md) 更新清单与相关合同，然后结束，不覆盖旧证据。
3. 有未结束的 `active_group` 时返回该组的续跑任务，不开第二组。`implemented` 返回待验证任务，`failed` 返回本组修复任务；已标 `blocked` 的组可让其他就绪组继续进入选择。
4. 新候选要求所有依赖的本组验证有效。排序：当前功能及其所需依赖优先 → 能解锁工程基础/主入口优先 → 下游依赖更多优先 → 内容项较少优先 → 稳定编号。待页面集成不阻止其他组使用已通过本组验证的能力。
5. 读取返回的唯一组和合同，核对范围、旧行为、目标和检查方式。脚本生成 `round.json`，记录选择理由、源/合同哈希；`plan.json` 同步记录 `active_group`。选组落盘后结束，不实施或验证代码。

结果区分 `selected / blocked / groups_complete / complete`；选组的 `mode` 区分新组、续跑和 `revalidate`。`groups_complete` 报告仍需集成与收尾验证，不能当项目完成。全部就绪组都阻塞时列原因与所需输入。
