# G253F018 实施记录

目标：`react-front/src/utils/time.parts/getFormatter.ts`（新建）。范围仅本轮源段（time.js 44-70 行 FunctionDeclaration: getFormatter）：输入校验、Intl 格式化器构造与缓存语义；`timezoneFormatters` 容器复用 G253 已建立的 `time.context.ts` 单例，调用方（setBusinessTimezone 等）属其他 F 组，导出装配属 G253V，均未提前实现。

## 映射决策

- 源 45-47 行校验（typeof/trim/`^[+-]` 正则/Intl 构造异常四路抛出）逐分支保留，错误消息模板串使用原始参数（含 trim 前空格），与基线一致。
- 源 51-64 行 `Intl.DateTimeFormat('en', {...})` 选项逐项保留（calendar 'gregory'、numberingSystem 'latn'、hourCycle 'h23' 等）。
- 源 16 行 `timezoneFormatters` Map → `import { timezoneFormatters } from '../time.context.ts'`（G253 产物），保留模块级缓存语义；`timezoneFormatters.get(name)!` 非空断言（has/set 后必存在）。
- 源为非导出函数，目标以 `export function getFormatter` 导出供其他 time.parts 函数组复用；TS 类型 `(timezoneName: string): Intl.DateTimeFormat`。
- 无 Vue/Pinia/UI 依赖；源 Vue 与后端未改动。

## 公共影响（组外必要接入，已登记）

- 新建 `react-front/tests/time/getFormatter.test.mjs` 行为测试，`node --test` 直接运行（`test:time` 脚本接线仍属 G016）；测试 `after` 钩子清理共享缓存，与 time.context.test.mjs 的初始状态断言共存通过（目录内 13/13）。
- 未改动任何已验证共享文件：time.context.ts、package.json 等哈希不变，check 显示 invalidated_groups=[]，无需复验。

## 验证命令与结果

- 基线：`node migration/state/evidence/G253F018/baseline-capture.mjs` → evidence/G253F018/baseline.json（Node v22.23.2、Asia/Shanghai、Intl 未 polyfill；源 16 行 + 44-70 行逐字求值，真实导入佐证模块初始化成功）。原版 time.js 无对应可运行测试，已以逐字求值 + 真实导入为基线，见 baseline.md。
- 行为测试：`cd react-front && node --test tests/time/getFormatter.test.mjs` → 6/6 通过；`node --test tests/time/*.test.mjs` → 13/13 通过（含 G253 复跑）。
- 类型：`npm run typecheck` → 退出 0。
- 构建：`npm run build:prod` → 成功（219.77 kB js，无新增运行时依赖）。

## 剩余问题与下一步

- 本组自检通过不代表正式验证：验证由 migration-validate 执行 record passed 后才冻结证据；getFormatter 的调用方（setBusinessTimezone、setUserTimezone、refreshDeviceTimezone、getSupportedTimezones 等 F 组）后续迁入 time.parts 并复用本导出。
- 模块级初始化终态（initTimeContext 注入真实函数）由 G253V 装配组验证。

## 记账

- plan.json：I02810 登记 target_locator，G253F018 status=implemented；check plan_valid、invalidated_groups=[]。round.json 保持 selected 快照，未执行 record（implemented 为实施状态，passed 由验证技能生成）。
