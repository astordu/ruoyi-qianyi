---
name: migration-implement-group
description: 将自动选定的一组 Vue 源内容迁移为 React，或根据本组上次验证报告修复失败项。保留旧行为并更新逐项目标映射，不用于全项目一次性改写。
---

# 实施本轮唯一小组

先读 [状态协议](../migration-plan/references/state-protocol.md)。无有效 `round.json` 或 `active_group` 时报告前置任务缺失并结束，需先调用 [migration-next-group](../migration-next-group/SKILL.md) 选组落盘，不自行选择或扩大范围。

1. 运行 `migration_state.py check --state migration/state`，读合同、源内容、已有目标和技术约定。核对本轮源/合同哈希，读取真实函数、模板分支、样式和依赖，不能只靠摘要。仅实施当前组；默认保持旧行为、沿用已定目标架构。
   - 本组 `status` 或最近 `validation.result` 为 `failed` 时，先读取 `plan.json` 中本组的 `validation.report`、`validation.note` 和 `validation.artifacts` 指向的报告与证据，再读 `progress.md`。按失败条件/内容项编号查明原版预期、目标实际结果、复现步骤和受影响代码，形成当前组的修复清单。报告或必要证据缺失时记录缺失并结束，不凭聊天记忆猜测失败原因。
   - 在已有目标上修复这些失败项及必要的关联缺陷，保留已通过的内容和原验收条件。修复期间保持当前 `active_group`，不重新选组；保留上次 `validation` 和证据供复验追溯。
2. 实施前取得所需原版输入输出、请求、组件行为或截图，固定数据、角色、语言/时区、viewport 等相关条件。原版不可运行时记录缺证据，推进不依赖它的工作，但不标通过。没有测试时只补本组需要的行为检查。
3. 按需读 [Vue → React 技术约定](../../../migration/vue-react-convert.md)。复用已通过公共能力；纯工具可兼容复用，组件/状态合理拆分。不得带入 Vue/Pinia/UI 依赖凑覆盖，也不得用空实现或业务占位页冒充迁移。
4. 将各项目标文件和函数/组件写回 `plan.json` 的 `targets/target_locator`。组外公共改动只限当前组必要接入，登记影响与回归；新增能力属于另一组时补依赖，本轮不越界。源 Vue 与后端默认只读。
5. 运行真实构建、类型和本组检查，日志写工作目录、命令、结果及未执行项。预期依据旧行为，不删断言、缩合同、换原图消除失败。写 `groups/Gxxx/progress.md`，记录映射、公共影响、剩余问题和下一步；失败修复时逐条记录上次失败项的原因、修改和自检结果，并重跑相关已通过条件的回归。
6. 本组状态设 `implemented`，实施记录落盘后结束。自检不是正式通过，不直接写 `passed` 或人工确认；已验证共享文件改变时相关哈希失效，记录受影响组的回归要求。验证由用户另行调用 [migration-validate](../migration-validate/SKILL.md)。

不因“整个项目迁完”把整站塞进一轮。可查事实直接查；无法确定的业务冲突/改变才询问，已定选择不重复确认。
