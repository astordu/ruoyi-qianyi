# G253F018 原版基线

采集条件：Node v22.23.2、主机时区 Asia/Shanghai、Intl 未 polyfill（`Intl.DateTimeFormat.polyfilled` 为 false）。`getFormatter` 为源模块非导出函数，以源 16 行 `timezoneFormatters` 声明 + 44-70 行函数体在同一 Function 体内逐字求值（共享同一闭包）；另真实导入原版 time.js 佐证模块内调用链路。用例从源语句推导，不以目标实现定义原行为。

## 输入校验与异常（源 45-47 行）

所有失败均抛出普通 `Error`（`name` 为 'Error'），消息为 `` 无效的 IANA 时区: ${原始参数} ``（保留 trim 前空格、非字符串的模板串化）：

- 非字符串：`null`→`无效的 IANA 时区: null`；`undefined`→`无效的 IANA 时区: undefined`；`123`→`无效的 IANA 时区: 123`；`{}`→`无效的 IANA 时区: [object Object]`。
- 空与空白：`''`、`'   '` 均抛错，消息保留原空白（`无效的 IANA 时区:    `）。
- 以 `+`/`-` 开头的 UTC 偏移字符串：`+08:00`、`-05:00` 抛错。
- Intl 无法解析的名称：`Invalid/Zone`、`'  Bad/Zone  '`（trim 后无效）抛错，消息保留原始参数。
- 抛错路径不写入缓存（`timezoneFormatters` 大小不变、无失败键）。

## 有效时区与格式化器选项（源 51-64 行）

- `Asia/Shanghai`、`UTC`、`America/New_York`、`Europe/Paris`、`Asia/Kolkata` 返回 `Intl.DateTimeFormat` 实例。
- `resolvedOptions()`：locale `en`、calendar `gregory`、numberingSystem `latn`、hourCycle `h23`（hour12 false）、year `numeric`、month/day/hour/minute/second `2-digit`。
- 运行时会规范化别名：`Asia/Kolkata` → `timeZone: 'Asia/Calcutta'`。

## 缓存语义（源 49-69 行）

- 缓存键为 trim 后的名称：`'  Asia/Shanghai  '` 与 `'Asia/Shanghai'` 返回同一实例，Map 键为 `Asia/Shanghai`。
- 同一时区二次调用返回同一引用（`timezoneFormatters.get(name)`）。

## 真实导入佐证

原版模块初始化（523-524 行：`setBusinessTimezone(businessTimezone.value)` → `getFormatter('Asia/Shanghai')`）成功：`getBusinessTimezone()` = 'Asia/Shanghai'、`getDeviceTimezone()` = 'Asia/Shanghai'。证明原版模块内 getFormatter 接受 `Asia/Shanghai`。

详见 `migration/state/evidence/G253F018/baseline.json` 与 `baseline-capture.mjs`。
