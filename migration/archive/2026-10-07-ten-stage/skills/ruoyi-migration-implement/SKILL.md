---
name: ruoyi-migration-implement
description: 根据已确认需求和任务计划，将一个若依 Vue 模块任务实现到 react-front。用于逐任务迁移与处理评审指出的缺陷。
---

# 实施一个迁移任务

读 [共享协议](../../../migration/CONTRACT.md)、handoff、已确认需求、证据源码、当前 task、baseline 和相关公共架构。重新检查源指纹及需求确认，不能只凭上一 agent 的摘要写代码。

1. 选择一个依赖满足的 pending 任务，或有具体失败证据的修复任务；缺输入先记录 blocked。运行前检查是否已有同任务在工作，默认串行，避免重复实现。
2. 沿原版的可观察行为实现 React 代码，严格使用 react-front/。保留后端接口、权限、状态、校验、取消、错误及副作用；组件结构可以改变，不要求 Vue 文件一对一翻译。
3. 仅修改任务允许路径，复用公共适配层。遇到未定义业务行为、额外范围或共享架构缺口，记录问题并返回相应阶段，不暗中补一个新需求。
4. 添加/运行与任务风险相称的有意义检查。不得削弱需求断言、删除失败测试或替换旧版基线截图；测试修订需写清已确认需求依据并交独立评审核对。
5. 完成后写 implementation.md：修改内容、C 映射、实际命令/工作目录/退出状态、证据文件、未运行项和风险。生成 target-manifest.json；状态只到 implemented，不能自己标整模块 verified/accepted。
6. 修复轮数写回 tasks.json；默认最多 3 次，耗尽保存失败证据并 blocked。新的 agent 不能重置计数。

目标快照：

```bash
python3 .agents/skills/ruoyi-migration-research/scripts/evidence.py snapshot --root . --tree react-front --output migration/modules/<module-id>/target-manifest.json
```

保存 state/handoff。所有实施任务交付后，下一步是不同会话/agent 的 review；当前会话自检不能替代独立验证。
