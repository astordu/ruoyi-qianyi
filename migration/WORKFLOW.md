# 全项目 Vue → React 迁移

默认完整保留旧项目行为和界面，由 AI 规划依赖并自动选组，一轮只实施、验证一组。普通技术转换自行决定；仅无法查明的业务冲突或必须改变的行为需要用户介入。

| 阶段 | Skill | 职责 |
| --- | --- | --- |
| 全项目规划 | [migration-plan](../.agents/skills/migration-plan/SKILL.md) | 固定文件清单、逐项内容去向、小组、依赖和验证合同 |
| 自动选组 | [migration-next-group](../.agents/skills/migration-next-group/SKILL.md) | 按固定规则选唯一就绪组，生成 round.json |
| 本轮实施 | [migration-implement-group](../.agents/skills/migration-implement-group/SKILL.md) | 只迁当前组，更新目标映射与进度 |
| 迁移验证 | [migration-validate](../.agents/skills/migration-validate/SKILL.md) | 本组验证、页面集成、全项目收尾 |

先规划一次；之后每轮由用户分别调用 **选组 → 实施 → 验证**，验证负责记账。各 skill 完成本阶段并落盘后结束，不自动调用下一阶段。失败先修本组，确实阻塞后才选其他组。组验证通过可解锁依赖，但项目完成仍需要集成验证。

验证返回 `failed` 后，直接再次调用 `migration-implement-group`，读取本组最新失败报告修复；再调用 `migration-validate` 复验。失败修复循环始终保持同一组，不重复选组。报告、日志和截图按验证次数独立保存，通过后才选择下一组。

## 开始与续跑

在本项目新会话使用：

```text
使用 $migration-plan，完整盘点 ruoyi-fastapi-frontend 到 react-front 的迁移，保留已有行为和界面，建立全文件内容清单、小组、依赖和验证计划。先完成规划。
```

规划有效后，每轮分别调用：

```text
使用 $migration-next-group，自动选下一组并落盘。
```

```text
使用 $migration-implement-group，实施已经落盘的本轮小组并记录进度。
```

```text
使用 $migration-validate，验证本轮小组并记录证据与结果。
```

无需用户每轮选择模块，也不重复确认普通实现细节。不将所有业务塞进同一轮。技能未被客户端发现时，直接读取对应 SKILL.md；四个技能和共享脚本需一起保留。

## 外层循环脚本

规划完成后，也可用项目根目录的 [migration-loop.sh](../migration-loop.sh) 按落盘状态连续调用三个 skill。Shell 入口交给 Python 3.9+ 标准库控制循环、JSON 校验、超时和项目锁；支持 macOS/Linux，不依赖 jq 或 GNU timeout。

```sh
# 只读预检：不调用 agent，不选组落盘。
./migration-loop.sh codex 10 --dry-run

# 最多处理 10 个小组/集成轮次；每阶段启动新的 CLI 会话。
./migration-loop.sh codex 10

# 与 afk.sh 一样支持其他 CLI；省略 --model 时沿用各 CLI 配置。
./migration-loop.sh qodercli 10
./migration-loop.sh claude 10

# 调整上限：同组最多 5 次自动修复，每个 CLI 调用最多 2400 秒。
./migration-loop.sh codex 100 --max-retries 5 --timeout 2400
```

需要先安装并登录所选 CLI。CLI 的无人值守权限模式沿用 `ralph-gitlab/afk.sh`：Codex/Claude 跳过交互审批，Qoder 使用当前版本的 `bypass_permissions`。可用 `--model <模型名>` 指定模型，`--state <项目内状态目录>` 指定已有迁移状态；脚本不会自动创建或重做迁移计划，也不会启动后台定时任务。

Codex 参数已对照本机 `codex exec --help`；非交互调用和分阶段修复方式参考 [OpenAI 官方修复循环示例](https://developers.openai.com/cookbook/examples/codex/build_iterative_repair_loops_with_codex)。

新组选组后执行实施和验证；已有 `implemented` 任务直接验证。`failed` 保持同一组，读取失败报告后再实施/复验，期间不调用选组 skill。`blocked` 可让其他就绪组推进；没有可执行组则退出。所有组完成后每轮执行一项集成验证，全部有效通过后执行最终检查并生成最终报告。集成发现代码缺陷时保存阻塞报告，需将修复纳入计划。

日志、阶段 prompt、CLI 输出和结果放在 `migration/state/loop/runs/<唯一运行编号>/`，验证报告仍由 skill 独立保存。`loop/repair-counts.json` 记录自动修复次数，跨脚本重启保留，通过后清零；达到修复上限会保留失败任务并退出，可提高 `--max-retries` 后续跑。规划或源码快照变化、缺少落盘记录、CLI 错误/超时都会保存诊断并停止。Ctrl-C 会终止本次 CLI 进程组，保留当前任务；重新运行同一命令可续跑。项目锁防止两个循环脚本同时修改同一个 checkout。

退出码：`0` 全部完成；`1` CLI 失败；`2` 计划/落盘/证据需要处理；`3` 阻塞、修复上限或重复启动；`4` 达到轮次上限，仍有待处理任务；`124` 超时；`130` 中断。`4` 不是迁移完成，继续执行同一命令会读取已有进度。

控制器依据共享状态检查脚本和证据哈希判断结果，不把 CLI 退出 0 或文字宣称成功当作验证通过；记录有效仍不代替真实行为测试。测试控制器可运行 `python3 -m unittest discover -s migration/scripts -p test_migration_loop.py -v`，全部使用临时项目和模拟 CLI，不触发真实迁移。

## 资料与验证

资料放在 `migration/state/`：脚本生成 `inventory.json`，agent 维护 `plan.json`，自动选组产生 `round.json`。逐组合同、进度和验证分别放在 `groups/<group-id>/`，集成检查放在 `integration/`，旧证据进入 `history/`。见 [状态字段、命令与恢复规则](../.agents/skills/migration-plan/references/state-protocol.md)。

固定脚本不使用 .gitignore，枚举隐藏与未引用文件；排除目录及数量明确记录。脚本检查清单一致、内容登记、依赖与证据哈希，不能证明源码语义理解零遗漏。工具测输入输出，组件可单独挂载，页面走操作、请求与截图；见 [验证方法](../.agents/skills/migration-validate/references/validation-methods.md)。

本组通过、页面集成通过和人工验收分别记录。源码、目标或证据变化时旧通过记录失效。所有组通过且必要集成有效后才执行最终检查。

[Vue → React 技术约定](vue-react-convert.md) 继续作为技术参考，其中的 PRD 对应本流程的 plan.json 与当前组 contract.md。旧 `.qoder/prd/`、`.qoder/migration/` 和 archive 内容只作历史依据，不能自动继承通过状态。旧 .qoder/skills 入口不再作为本流程入口。
