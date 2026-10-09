# G253F018 验证报告：src/utils/time.js getFormatter

验证会话：独立于实施会话（本会话重读源/目标，未沿用实施者总结作结论；基线脚本与行为测试为实施产物，本会话全部重跑并另建独立差分检查）。

## 检查条件与结果

逐项合同 I02810 `ruoyi-fastapi-frontend/src/utils/time.js` lines 44-70 FunctionDeclaration: getFormatter，源语句 sha256=892c883e9e32bb652aaaa57618500a304dbe36256283e1ad1612a266ce291923（本会话重算一致），去向 react-front/src/utils/time.parts/getFormatter.ts。

| 条件 | 原版证据 | 新实现证据 | 结果 |
| --- | --- | --- | --- |
| 输入校验：非字符串/空/空白/`+`/`-` 开头抛 Error，消息保留原始参数（含 trim 前空格） | baseline.json cases：null/undefined/123/{}/''/'   '/'+08:00'/'-05:00' 全部 ok=false，name='Error'，消息为模板串原始参数 | getFormatter.test.mjs 第 55-75 行断言相同消息与 name；diff-check 32 例中 11 例非法输入 0 不匹配 | 通过 |
| Intl 不可解析名称抛 Error，消息保留原始参数 | baseline.json：Invalid/Zone、'  Bad/Zone  ' ok=false | 测试断言 + diff-check（Invalid/Zone、Bad/Zone、Not/A_Timezone、GMT+8）一致 | 通过 |
| 有效时区返回 Intl.DateTimeFormat，选项 en/gregory/latn/h23/numeric/2-digit 全套一致 | baseline.json：Asia/Shanghai、UTC、America/New_York、Europe/Paris resolvedOptions 全字段 | 测试第 28-34 行 deepEqual 全字段；diff-check 9 个有效时区 0 不匹配 | 通过 |
| 运行时别名规范化（Asia/Kolkata → Asia/Calcutta） | baseline.json resolved.timeZone=Asia/Calcutta | 测试第 36-39 行；diff-check 一致 | 通过 |
| 缓存：键为 trim 后名称、同键二次调用同一实例 | baseline.json cache.sameInstance 三项 true | 测试第 41-53 行引用相等断言；diff-check cache_ref_equal=true | 通过 |
| 失败路径不写缓存 | baseline.json failureNotCached：sizeBefore=sizeAfter、hasFailedKey=false | 测试第 77-84 行；diff-check failure_not_cached_equal=true | 通过 |
| 调用集保留：timezoneName.trim、RegExpLiteral.test、timezoneFormatters.has/set/get | 源 45/49/50/64/69 行 | 目标 13/17/18/32/37 行逐句对应；`get(name)!` 为 TS 非空断言，无运行时差异；新增 `export` 为跨 F 组复用决策（progress.md 已记录） | 通过 |

## 命令与结果

- 基线重放：`node migration/state/evidence/G253F018/baseline-capture.mjs`（源 16 行容器 + 44-70 行逐字求值 + 真实导入原版模块）→ 与 evidence/G253F018/baseline.json 逐字节一致（baseline_reproducible: True），退出 0。条件 Node v22.23.2、hostTimezone=Asia/Shanghai、Intl 未 polyfill。
- 独立差分（本会话新建）：`node migration/state/evidence/G253F018/diff-check.mjs` → 32 个输入（9 有效时区 + 11 非法 + trim 变体 + 别名 + 缓存/失败语义）0 不匹配，退出 0；日志 diff-check.log，脚本 diff-check.mjs 已入 evidence。
- 行为测试：`cd react-front && node --test tests/time/getFormatter.test.mjs` → 6/6 通过（log: test-getFormatter.log）；`node --test tests/time/*.test.mjs` → 13/13 通过（含 G253 复跑，log: test-time-suite.log）。
- 类型：`npm run typecheck` → 退出 0。
- 构建：`npm run build:prod` → 成功（219.77 kB js，无新增运行时依赖）。

## 截图观察

不适用（纯工具函数，无视觉状态）。

## 公共影响与待集成

- 未改动任何已验证共享文件；`check --state` 显示 invalidated_groups=[]，无需依赖复验。
- 新测试文件 react-front/tests/time/getFormatter.test.mjs 的 after 钩子清理共享缓存，与 time.context.test.mjs 初始状态断言共存通过。
- 待集成：getFormatter 调用方（setBusinessTimezone、setUserTimezone、refreshDeviceTimezone、getSupportedTimezones 等 F 组）后续迁入 time.parts 复用本导出；模块级初始化终态（initTimeContext 注入真实函数）由 G253V 装配组验证；所属 J 合同与 dependency-edges.json 运行时回调、动态 import、glob、全局注册仍待集成模式。

## 结论

全部本组条件通过；原/新同输入行为一致有原版运行证据与新实现独立差分佐证。独立性说明：基线脚本与行为测试由实施会话编写，本会话全部重跑并另行构建差分检查独立核对，未伪造独立核验。
