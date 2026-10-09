# G253 原版基线

采集条件：Node v22.23.2、主机时区 Asia/Shanghai、Intl 未 polyfill（`Intl.DateTimeFormat.polyfilled` 为 false）。原版 time.js 在源项目 node_modules（vue/element-plus/dayjs 1.11.23）下真实导入运行；无依赖的常量声明语句（8-16 行，合同逐语句 sha256 已冻结）从源文件逐字求值。未以目标实现定义原行为。

## 常量与容器（源 8-16 行求值）

- `DATE_ONLY_PATTERN` /^(\d{4})-(\d{2})-(\d{2})$/：`2024-02-29` 匹配；`2024-2-29`、带时间/空格前缀、非日期均不匹配。
- `WALL_TIME_PATTERN` /^(\d{4})-(\d{2})-(\d{2})[ T](\d{2}):(\d{2}):(\d{2})(?:\.(\d{1,3}))?$/：`2024-02-29 10:30:45`、`2024-02-29T10:30:45.123`、`.1` 匹配；纯日期、缺秒、前导空格不匹配；月 `13` 语法上匹配（越界校验由函数组负责）。
- `RFC3339_PATTERN` /^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})(\.\d+)?(Z|[+-](?:[01]\d|2[0-3]):[0-5]\d)$/：`Z`、`.123Z`、`+08:00`、`-05:30` 匹配；`+8:00`、无偏移、空格分隔不匹配。
- `WEEKDAYS` = ['日','一','二','三','四','五','六']；毫秒常量 1000/60000/3600000。
- `ORIGINAL_TIME_FIELDS` 为 Symbol，`String()` 为 `Symbol(originalTimeFields)`。
- `timezoneFormatters` 为 Map 实例，初始 size 0。

## 模块级状态与初始化（真实导入后）

- 初始化调用次序（源 523-524 行）：先 `setBusinessTimezone(businessTimezone.value)`，再 `refreshDeviceTimezone()`；`dayjs.extend(utc)`（第 6 行）先于二者执行。
- 运行证据：`businessTimezone` = 'Asia/Shanghai'（初始化前 ref('Asia/Shanghai')）；`userTimezone` = 'auto'；`deviceTimezone` 由 null 被初始化解析为 'Asia/Shanghai'（主机时区）；`displayTimezone` = 'Asia/Shanghai'；`getSupportedTimezones(['UTC','Europe/Paris'])` = ['Asia/Shanghai','Europe/Paris','UTC']；dayjs 单例已挂载 utc 插件。
- 模块导出 21 个名字（TimeInputError + 20 个函数，供 G253V 装配核对）。

## TimeInputError

`new TimeInputError(message, code, candidates)`：`name` 保持 'Error'（继承默认）；`message`/`code`/`candidates` 原样保留；`candidates` 缺省为 []；`instanceof Error` 为 true。

## 缺证据说明

源项目 test:time 依赖工作区外的 `ruoyi-fastapi-test/time-contract` 契约包，本环境不存在，原版测试无法运行；以真实模块导入 + 逐字常量求值作为本组基线。ElMessage/ElMessageBox 使用场景（chooseTimeOffset 等）属 F045/F046 组，本组只固定其依赖接口形态。

详见 `migration/state/evidence/G253/baseline.json` 与 `baseline-capture.mjs`。
