# 迁移文件协议

项目根目录固定为 `/Users/dulei/Documents/projects/ruoyi-qianyi`，React 产物固定为 `react-front/`。所有 skill 先读 `project.json`，再读本协议及本阶段需要的模块资料。模块 ID 用稳定的英文小写短横线形式，如 `system-user`。

## 人与 agent 的边界

人定义范围、确认还原出的需求、接受最终成果。agent 查事实、提出遗漏问题、实施、验证并报告证据。既有授权继续有效；不要重复确认已决定的事项。仅在缺少真实范围决策、需求确认或最终验收反馈时等待人。

`grill-me` 的参考价值是一次问一个问题、给推荐答案、事实先自行调查。不要为了完成访谈问完固定问题清单。未决项可以保存草稿；不得把未回答的问题填成用户选择。

人工确认必须来自实际用户反馈：记录时间、原意、确认对象和需求文件的 SHA-256。草稿、示例、其他 agent 的报告不是人工确认。确认范围与完整需求是不同记录；用户一次反馈明确覆盖两者即可，不必再询问。最终验收还要绑定目标指纹。需求修改后重新确认变化部分；旧记录保留，不改写历史。

## 一个模块的文件

按阶段创建文件，不创建假通过报告。所有 JSON 使用 UTF-8，根对象含 `schema_version: 1` 和 `module_id`。

| 文件 | 内容 |
| --- | --- |
| `scope.md` | 模块入口、纳入/排除功能、用户决定、未决项、关联模块 |
| `spec.md` | 人能读懂的场景、验收条件、证据、依赖、差异决策 |
| `scenarios.json` | 下述结构化场景和证据索引 |
| `approval.json` | 真实反馈、`scope_sha256`、`spec_sha256`、`scenarios_sha256`；未确认时不写 approved |
| `source-files.json` | 已调研的项目相对文件路径数组，用于源证据指纹 |
| `source-manifest.json` | 该清单文件的 SHA-256；调研后发现依赖应加入并重新确认影响 |
| `baseline.json` | 原版运行环境、数据复位办法、场景结果、截图路径、未覆盖项、源/需求指纹 |
| `tasks.json` | 依赖图、状态、修改边界、验收映射、修复次数 |
| `implementation.md` | 已改内容、真实执行命令/结果、遗留问题 |
| `target-manifest.json` | React 整棵有效代码树的指纹；在实现/修复后生成 |
| `review.json` | 独立覆盖矩阵、行为/API/集成验证结果、源/需求/目标指纹、缺陷 |
| `visual.json` | 截图逐状态对比及差异、源/需求/目标指纹 |
| `acceptance.md` | 人工操作步骤、结果、实际用户验收反馈及绑定版本 |
| `state.json` | 阶段、阻塞原因、当前任务、阶段修复次数；用于续跑定位，不代替证据 |
| `handoff.md` | 当前结论、下一步 skill/任务、必读文件、命令、阻塞、禁止改动资料 |

公共架构、环境说明和公共基础任务放在 `migration/foundation/`，模块不得各自复制一套认证/菜单规则。

## 场景和证据格式

`scenarios.json` 的关键字段如下；这是格式示意，创建真实模块时必须填实际内容，不复制空数组来声称完整：

```json
{
  "schema_version": 1,
  "module_id": "system-user",
  "evidence": [
    {
      "id": "E001",
      "path": "ruoyi-fastapi-frontend/src/views/system/user/index.vue",
      "symbol": "实际函数/模板绑定名",
      "lines": "实际起止行",
      "finding": "该片段实际支持的行为"
    }
  ],
  "scenarios": [
    {
      "id": "S001",
      "name": "明确的用户操作场景",
      "route": "从路由核实的入口",
      "roles": ["经确认的测试角色"],
      "preconditions": ["确定的数据及权限状态"],
      "steps": ["可重放的用户操作"],
      "criteria": [
        {
          "id": "S001-C01",
          "expected": "可观察、可判定的结果",
          "evidence_ids": ["E001"],
          "verification": ["e2e", "api"],
          "required": true
        }
      ],
      "visual_states": ["需要对比的列表/弹窗/错误状态"],
      "dependencies": ["相关共享能力或模块"],
      "open_questions": []
    }
  ],
  "excluded": [{"item": "明确排除内容", "reason": "用户决定或边界依据"}],
  "unmapped_findings": []
}
```

证据需覆盖页面、被调用 API、权限/状态/组件及相关后端契约；不是要求全项目逐文件阅读。记录实际读到的分支：成功、失败、校验、取消、空数据、加载、分页、刷新、权限和副作用。每个分支映射到场景或有依据的排除项。扫描不到的动态行为/服务端开关注明未知，不能用“所有文件读完”证明完整性。

验收条件以行为为单位，例如“点击取消不发更新请求”“提交后列表刷新且保留查询条件”“无权限角色不显示入口，直接访问仍被拒绝”。写清数据、动作、输出、API 参数/副作用和检查方式；不能只写“和原来一样”。需求来源或约定改善与原版实际行为分开记录。

每条 required 条件至少有适配它的验证证据。函数变换可用单元测试；浏览器行为用 E2E/可重放的人工步骤；请求用 mock 契约检查及必要的真实后端集成；视觉用截图。mock 通过不能证明真实后端兼容，截图相似不能证明按钮功能；单元测试不是所有场景的统一答案。

## 基线和任务

基线逐条件记录 `pass | fail | unverified`、命令/步骤、环境、证据路径及失败原因。记录旧版已有缺陷；迁移预期是否修复由需求决定。固定浏览器、viewport、语言、时区、字体、账号权限和数据；隐藏时间戳等动态区域必须两边采用同一规则并记录。测试修改应有需求依据，不能删断言或更新原版快照来让迁移通过。

`tasks.json` 根对象含 `tasks` 数组。每项必填：`id`、`title`、`scenario_ids`、`criterion_ids`、`depends_on`、`allowed_paths`、`checks`、`status`、`repair_attempts`。`checks` 为命令或手工步骤对象，含工作目录和预期结果。不要填写不存在的测试命令。状态为 `pending | running | implemented | verified | blocked`；implemented 只代表已交付代码，verified 必须来自实际验证。

所有 required 条件都有实现任务和验证归属；独立公共任务可用空 scenario_ids，但需写明依赖模块。任务大小以能一次实施和验证一个有意义行为为准，不按文件数切分。每个任务先满足依赖，默认串行，避免两个 agent 同改共享文件。

## 验证、版本与结束条件

`review.json` 根对象含 `status`、`reviewer_session`、`bindings`、`criteria`、`defects`。criteria 每行含 `criterion_id`、`implementation_evidence`、`checks`、`status`。status 用 `pass | fail | unverified`；checks 必须给真实命令/步骤、退出状态或观察结果和日志路径。reviewer_session 来自实际独立会话/agent 的可用标识；无法获得独立环境时明确说明，不伪造 ID 或独立性。

`visual.json` 含 `status`、`bindings`、`comparisons`；每条 comparison 关联 scenario_id 和状态，记录原版/目标/差异图或并排图路径、环境、观察结论、未解决差异。视觉容差在比较前按需求明确；不能拿任意百分比当全项目标准。接受视觉差异需要真实用户决定并关联当前版本。

报告 bindings 包含 `spec_sha256`、`scenarios_sha256`、`source_manifest_sha256`、`target_manifest_sha256` 和相关基线文件哈希。先检查 manifest 对应实际文件仍一致，再检查 bindings。报告缺文件、没执行、依赖假数据而尚缺真实集成证据或版本不一致，都不能给总体 pass。清单只对已列源文件有效；新发现的依赖要补入。

指纹脚本 `hash <file>...` 可计算上述文件哈希；`snapshot --tree` 检查整个有效目标树的新增、删除和变化。脚本排除 node_modules、构建/覆盖率/测试报告缓存、.git、.venv、.DS_Store 和非示例 .env 文件，拒绝越界路径及符号链接。环境变化由不含凭据的 environment/baseline 记录绑定，不能因为 .env 被排除而忽略运行配置差异。指纹不包含任何测试通过或人工确认推断。

人工验收前的门槛：需求已确认；所需公共基础完成；原版相关基线已建立；每条 required 条件已核对且通过；行为/真实后端契约与影响到的共享功能回归通过；所有要求的视觉状态完成对比，差异已解决或被明确接受；无未解决阻塞。人工可以决定调整需求，但 agent 不得把失败项擅自降级。

React 共享代码变化会使其他模块目标指纹失效：据依赖判断影响，重新运行相关检查；无影响结论也要由独立评审记录并绑定新版本，不能直接复用旧 pass。原版变化先更新需求/基线。需求、原版和目标指纹变化均使旧版最终验收不能直接套用。

## 新上下文循环

state 阶段可为 `scoping | researching | awaiting_human | foundation | baseline | planning | implementing | reviewing | visual | ready_for_acceptance | accepted | blocked`。每轮读取真实文件和指纹，核对 state，执行一个已具备输入的阶段/任务，再保存交接。

缺需求确认返回 awaiting_human；缺账号/运行服务/测试数据返回具体 blocked；可修复代码缺陷转回 implementing。默认每个任务最多修复 3 次，无法归到任务的阶段问题也最多 3 次；达到上限保存失败证据并停止，不能靠新会话重置计数。可跳到无依赖的其他已确认任务，但不能忽略阻塞直接验收。

外层调度器负责真正启动干净上下文、等待完成、限制次数/时间和防重复运行。仅有 skill 文件不等于自动化调度已安装。独立评审与实现会话分开；若没有可用 agent/会话工具，只写交接包并交由新会话执行，不假称已启动。外层循环遇到人工确认节点停止派发该模块，等真实回复后续跑。
