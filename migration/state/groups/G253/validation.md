# G253 验证报告

验证对象：`react-front/src/utils/time.context.ts`（新建），对照合同 20 项源段与原版基线（`groups/G253/baseline.md`、`evidence/G253/baseline.json`）。重新读取源 time.js（1-36、523-524 行）与目标文件全文核对，未沿用实施者结论。检查为同轮自检，独立性不宣称；条件来自原版运行结果与源语句，未从目标实现倒推。

固定条件：Node v22.23.2、主机时区 Asia/Shanghai、Intl 未 polyfill；原/新两侧一致。

## 逐项结果

| 项 | 源段 | 检查方式 | 结果 |
| --- | --- | --- | --- |
| I02792 | element-plus 导入 | 目标以 TimePromptDeps 依赖接口隔离 Vue UI 提示，未引入 element-plus（转换约定）；使用方属 F045/F046 | 通过 |
| I02793 | vue ref 导入 | MutableRef<T> 可变值持有器，`.value` 语义保留；三个状态持有器初始值经比对 | 通过 |
| I02794/I02795/I02796 | dayjs/utc 导入与 extend | 目标保持模块级 `dayjs.extend(utc)`；运行检查 dayjs 单例已挂载 utc 插件（与基线同为 true） | 通过 |
| I02797-I02799 | 三个正则常量 | 字面量与基线逐字符一致；三组共 17 个样例（匹配/不匹配/分组）与原版逐项一致（evidence/target-capture.json，diffs=[]） | 通过 |
| I02800-I02803 | WEEKDAYS/毫秒常量 | 值逐一比对：['日','一','二','三','四','五','六']、1000/60000/3600000 | 通过 |
| I02804 | ORIGINAL_TIME_FIELDS | typeof symbol、String() 为 Symbol(originalTimeFields)，与基线一致 | 通过 |
| I02805 | timezoneFormatters | Map 实例、初始 size 0，与基线一致 | 通过 |
| I02806-I02808 | 三个状态 ref | 初始值 business='Asia/Shanghai'、user='auto'、device=null（初始化前），与源 ref 初始值一致 | 通过 |
| I02809 | TimeInputError | name='Error'、message/code/candidates 原样保留、candidates 缺省 []、instanceof Error，与原版运行结果一致 | 通过 |
| I02835/I02836 | 模块初始化两调用 | initTimeContext 以 spy 验证：先 setBusinessTimezone(businessTimezone.value)，再 refreshDeviceTimezone()；注入等价行为后终态 business='Asia/Shanghai'、device=主机时区，与基线一致 | 通过 |

## 证据

- 原版基线：`evidence/G253/baseline-capture.mjs` → `baseline.json`（原版真实导入运行 + 源常量逐字求值）。
- 目标比对：`evidence/G253/target-capture.mjs` → `target-capture.json`，13 组比较全部通过，diffs=[]，exit 0。
- 行为测试：`react-front/tests/time/time.context.test.mjs`，`node --test` 7/7 通过（`evidence/G253/test-time.context.log`）。
- 类型检查：`npm run typecheck` exit 0（`evidence/G253/typecheck.log`）。
- 构建：`npm run build:prod` exit 0（`evidence/G253/build-prod.log`）。

## 公共影响与待集成

- 公共改动：react-front/package.json 增加 dayjs@1.11.23（本组必要接入）。导致 G000 验证失效（check: invalidated_groups=[G000]），按协议下一轮 revalidate 复验；G016 实施 package.json 内容项时需核对本接入。新增 tests/time 测试文件；test:time 脚本接线属 G016。
- 待集成：ElMessage/ElMessageBox 真实 UI 注入、真实函数装配与模块加载初始化由 G253V 及 F045/F046 验证；本组通过仅证明本组条件。
- 未验证：原版 test:time（依赖工作区外 contract 包不存在）无法运行，已以真实模块导入替代，baseline.md 中已记录。

## 结论

本组 20 项条件全部通过，未发现缺内容或失败分支。
