---
name: ruoyi-migration-research
description: 针对已选择的若依模块读取 Vue 源码、还原操作场景和验收条件，并提供逐项文件证据。用于迁移前需求调研与确认。
---

# 从源码还原场景

读 [共享协议](../../../migration/CONTRACT.md)、[项目入口](../../../migration/PROJECT.md) 和当前 scope。先产出有证据的需求，不开始 React 实现。

1. 用 rg 从路由/菜单/页面入口定位，沿事件处理、API、子组件、状态、权限、字典和相关后端契约追踪。动态菜单/插件入口要查其加载机制。无需把整个仓库所有文件读一遍。
2. 建“入口 → 用户动作 → 分支 → 可观察结果”清单。核对成功、校验/服务端失败、取消、空数据、分页、刷新、权限、下载/写入副作用。每个发现映射到场景，或记录排除理由；动态依赖与未知项显式列出。
3. 写 spec.md 和 scenarios.json，按协议给稳定 S/C/E 编号。证据写真实路径、函数/模板绑定、行号、支持的行为；不拿文件名列表充当覆盖证明。
4. 每条条件写明确数据、步骤、结果、API 参数/副作用及验证方式。标注原版既有缺陷、用户要求的改善和代码无法确认之处。检查无人认领的分支及未映射证据。
5. 写 source-files.json，使用下方脚本生成源指纹；保存可审阅的场景和证据，请人确认具体需求。真实确认后写 approval.json，绑定 scope/spec/scenarios 哈希；没有反馈只能是 awaiting_human。

证据脚本用标准库，不需要项目依赖：

```bash
python3 .agents/skills/ruoyi-migration-research/scripts/evidence.py snapshot --root . --files migration/modules/<module-id>/source-files.json --output migration/modules/<module-id>/source-manifest.json
python3 .agents/skills/ruoyi-migration-research/scripts/evidence.py check --root . --manifest migration/modules/<module-id>/source-manifest.json
```

文件清单采用项目相对路径。脚本只检测文件变化；场景完整性仍需分支清单和人的确认。保存 state/handoff，已确认需求下一步通常为 foundation 或 baseline。
