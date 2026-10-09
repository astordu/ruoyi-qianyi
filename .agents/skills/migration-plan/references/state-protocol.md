# 状态、覆盖和命令

四个 skills 一起使用，共用 `migration-plan/scripts/migration_state.py`，只依赖 Python 3 标准库。命令路径相对项目根；状态路径可通过 `--state` 修改。迁移过程不能只复制其中一个 skill 而丢掉共享脚本和参考。

本项目状态默认 `migration/state/`，不放被 Git 忽略的 `.qoder/`。这次安装仅创建技能，不初始化真实迁移状态；运行规划后才生成以下文件。

```text
migration/state/
  inventory.json             # 脚本生成；完整源文件、哈希、排除规则
  plan.json                  # agent 维护审阅、内容映射、小组、依赖、集成计划
  round.json                 # 自动选组输出；本轮唯一组与快照
  groups/G001/contract.md    # 旧行为、本轮边界与检查条件
  groups/G001/progress.md
  groups/G001/validation.md
  groups/G001/validation-attempts/A001/report.md  # 每次报告独立保存，validation.report 指向最新一次
  evidence/                  # 脱敏日志、原/新截图、自动检查结果
  integration/J001.md        # 集成合同或结果，合同和报告可分开
  history/                   # 重盘点、换轮、重验证保留旧记录
  final-report.md
```

## 命令

```sh
# 不读取 .gitignore；--source 可重复。显式排除的是目录名，不排除单个文件。
python3 .agents/skills/migration-plan/scripts/migration_state.py inventory --root . --source ruoyi-fastapi-frontend --target react-front --state migration/state

# 规划后的结构/覆盖/快照检查；不证明业务等价。
python3 .agents/skills/migration-plan/scripts/migration_state.py check --state migration/state

# 查看下一组（只读）；实际开轮加 --claim，写 round.json 与 active_group。
python3 .agents/skills/migration-plan/scripts/migration_state.py next --state migration/state --claim

# 实际运行验证后记账，--evidence 可重复，至少一个证据不能是报告本身。
python3 .agents/skills/migration-plan/scripts/migration_state.py record --state migration/state --group G001 --result passed --report migration/state/groups/G001/validation.md --evidence migration/state/evidence/G001-tests.json

# 阻塞需报告、诊断和恢复条件，标记后可以选择其他组。
python3 .agents/skills/migration-plan/scripts/migration_state.py record --state migration/state --group G001 --result blocked --report migration/state/groups/G001/validation.md --note '原版环境不可用；恢复后重放指定场景'

# 单项集成完成后记账；最终收尾检查返回非零即未完成。
python3 .agents/skills/migration-plan/scripts/migration_state.py record --state migration/state --integration J001 --result passed --report migration/state/integration/J001-result.md --evidence migration/state/evidence/J001-browser.json
python3 .agents/skills/migration-plan/scripts/migration_state.py check --state migration/state --final
```

成功退出 0；结构、快照或最终覆盖不满足退出 2，并打印 JSON 诊断。`next` 返回 `blocked/groups_complete` 可退出 0，执行器必须检查 JSON 的 `status`，不能只看退出码。

## plan.json 字段

以下是字段形状示例，路径/编号/行为必须替换为实际调查结果，不把示例当已完成任务。文件清单由 inventory 命令生成，不照例子手写全清单。

```json
{
  "schema_version": 1,
  "inventory_digest": "inventory.json 中的真实 digest",
  "files": {
    "ruoyi-fastapi-frontend/src/utils/query.js": {
      "sha256": "该文件的真实 sha256",
      "reviewed": true,
      "review_evidence": "已逐段阅读导出、空值与编码分支；内容对应 I001"
    }
  },
  "items": [
    {
      "id": "I001",
      "source": "ruoyi-fastapi-frontend/src/utils/query.js",
      "locator": "encodeQuery 导出函数及其边界分支",
      "basis": "原函数的参数编码、空值与数组规则；原版测试/源码定位",
      "disposition": "migrate",
      "group": "G001",
      "target_locator": "encodeQuery 导出函数",
      "targets": ["react-front/src/utils/query.ts"]
    }
  ],
  "groups": [
    {
      "id": "G001",
      "title": "查询参数编码",
      "feature": "shared",
      "entry_priority": 2,
      "depends_on": [],
      "contract": "migration/state/groups/G001/contract.md",
      "targets": [],
      "status": "pending"
    }
  ],
  "integration_checks": [
    {
      "id": "J001",
      "groups": ["G001"],
      "contract": "migration/state/integration/J001-contract.md",
      "status": "pending"
    }
  ],
  "active_group": null,
  "active_feature": null
}
```

- `files` 必须与 inventory 完全一致，每文件审阅有依据，哈希对应当前原版；每文件至少一项。脚本能发现漏登记文件，不能判断函数/模板分支是否真的读全。
- `items.id` 稳定唯一；`source` 为项目相对路径；`locator/basis` 非空。`migrate/reuse` 必须关联组，验证通过前各项 `targets` 非空且文件存在于目标目录，`target_locator` 明确对应函数、组件或完整资源；`reuse` 指实际落到目标工程的兼容复用，不用源路径假装目标。`exclude` 无 group，需 `reason`，仍占清单位置并接受内容审核。
- 多个组可以分别迁同一文件的不同内容；源哈希按整个文件冻结。`groups.targets` 放没有单独源项的工程产物，以及由本组修改的公共文件；不能遗漏这些文件来逃避回归。
- `status` 为 `pending/implementing/implemented/failed/blocked/passed`。agent 可登记前几个执行状态；`passed` 只用 record 命令生成验证记录。脚本仅冻结已执行证据，不能替 agent 判断报告真假。
- `groups.depends_on` 是组编号，不是文件路径；依赖未知或循环时不能随便删边。`entry_priority` 越小越优先，实际调度还考虑当前功能、下游数量、内容数量、编号。
- `integration_checks` 非空且涵盖全部组，指明页面接入/跨页及最终运行检查。纯工具不需虚构页面点击，可在相关调用链或最终装配检查中说明其验证适用范围。
- 合同必须是真实非空行为清单，不能是“功能一致”。脚本检查文件存在，内容质量由读取/验证负责。
- `record` 自动写 `validation`：报告和证据哈希、源/目标/合同/依赖快照、时间。旧记录进入 history。验证通过后释放 active_group；失败保留它供修复，阻塞释放它供其他组推进。解除阻塞需原因改变，写明事实后改为 pending，再由 next 选组。
- 验证失败后直接调用 implementation：读取当前组的 `validation.report/note/artifacts` 和进度，修复同一组，再调用 validation 复验。无需调用 next。旧 `validation` 在修复阶段保留；新验证记账时才替换。每次报告、日志、截图使用独立路径，脚本只归档旧记录元数据，不自动备份被覆盖的文件；`validation.md` 若作为最新摘要，不作为历史证据文件复用。

## 修改、失效与续跑

源变化后重跑相同参数的 inventory，旧计划不会被覆盖；逐项对照新增/删除/变化内容，更新 `files/items/groups/合同` 和 `inventory_digest`。删除的源项去向保留在 history/审阅报告，不能静默缩小功能。

源、目标、合同、依赖验证或证据变化会使通过记录失效。`next` 优先选可重新验证的最前依赖，返回 `mode: revalidate`；必要时暂存原 active_group，依赖验证完成后恢复。重新验证一轮仍只处理一个组，先查是否真有缺陷，需要时修复再重新 record。单纯共享文件变化也必须记录复验，而非假定其他模块不受影响。

`round.json` 保存选组快照。实施时核对组、源 digest 和合同哈希；本轮合同有变化先重新明确边界，不能沿旧 round 施工。所有源均读取，目标文件/真实证据均落盘，所需集成有效时 `--final` 才成功。机器状态不代表人工验收。

## 自动化边界

规划、选组、实施、验证四个技能可由已授权执行器按顺序调用。一个执行轮次只处理一个选定组，写完状态交接；下一轮重新读取清单，不凭长对话记忆。用户仅请求安装技能时，不自动开始业务迁移。此脚本没有 agent 调用、定时、提交或部署能力。
