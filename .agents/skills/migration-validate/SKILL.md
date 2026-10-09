---
name: migration-validate
description: 按旧实现的检查条件验证本轮迁移小组并登记证据，或在所有组完成后执行页面集成与全项目收尾。覆盖工具、请求、组件、页面和视觉验证。
---

# 验证迁移

读 [状态协议](../migration-plan/references/state-protocol.md) 与适用的 [验证方法](references/validation-methods.md)。条件来自原版，重新读取源/目标，不把实施者总结当结论。同轮 agent 实施后检查是自检；新会话或独立 agent 才可真实注明独立性，不伪造核验，独立性不阻止自动推进本组。

## 本组模式（默认）

1. 运行 `migration_state.py check --state migration/state`，读选定组、合同和逐项映射。可显式指定已迁组回归，不顺便实施其他组。
2. 核对全部旧内容和目标。漏内容/分支补计划、标失败并回交实施。纯函数比较同输入输出/异常；逻辑查状态和副作用；组件单独挂载查 props/事件/交互；页面查操作、请求与相关截图。无需每个文件都跑页面或每个资源都写单测。
3. 按风险跑测试、必要真实集成和公共影响回归。mock 只证明受控契约，构建不证明等价，组件单测不证明页面接线。原版不可运行可用明确源码依据检查，但不能称运行等价已证实；必要证据缺失不通过。
4. 每次验证把报告写到新的 `groups/Gxxx/validation-attempts/<attempt-id>/report.md`，日志与截图也使用本次独立路径，保留旧文件；`groups/Gxxx/validation.md` 可更新为最新结果摘要。报告包含逐项条件、原/新证据、命令/结果、通过/失败/未验证、截图观察、公共影响及待集成项。失败项必须写明条件/内容项编号、原版预期、目标实际结果、复现步骤或失败命令、证据路径及受影响目标文件，供下一次 implementation 读取。原图不可覆盖；双边一致处理动态噪声，不记录凭证。
5. 全部本组条件通过后运行 `migration_state.py record --state migration/state --group Gxxx --result passed --report <本次报告路径> --evidence <本次日志或测试文件>`，可重复 `--evidence`。脚本冻结源/目标/合同/依赖和证据哈希。失败或缺条件也执行 `record`，使用 `--result failed/blocked --report <本次报告路径> --note <失败诊断与恢复条件>` 并登记已有证据，不能直接改状态解锁。同类失败连续 3 次无进展则保留证据标阻塞，原因改变后再就绪。

记账后结束本 skill。`failed` 保留当前组，后续直接调用 `migration-implement-group` 读取本次报告修复，再调用本 skill 复验；无需重新选组。通过后可另行调用 `migration-next-group`；`blocked` 时按已记录恢复条件处理。各阶段由用户或其授权的外层执行器调用，不在本 skill 内自动执行。

## 集成与收尾模式

用户要求集成/收尾，或返回 `groups_complete` 时进入，不每轮重复全项目检查。

- 按 `integration_checks` 重放组接入页面及跨页面关键流程，覆盖入口、权限、刷新、请求异常和受影响公共能力；可分轮，每轮一项集成流程。
- 写 `integration/<check-id>.md`，用 `migration_state.py record --state migration/state --integration <check-id> --result passed --report <报告> --evidence <证据>` 冻结证据。缺账号/环境保留未验证或阻塞。
- 运行 `migration_state.py check --state migration/state --final`，要求快照一致、文件全审阅、内容有合法去向、本组验证与全部集成有效。脚本不证明内容盘点零遗漏，再核对动态入口、全局注册、样式/资源和审阅记录。
- 写 `migration/state/final-report.md`：覆盖数量、去向、排除依据、真实验证与环境、未解决差异、人工可操作的验收步骤。区分机器通过与真实人工验收，不把沉默算接受，不部署或提交代码。
