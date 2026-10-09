// G253 原版基线采集：在 Node 中真实导入原版 time.js，并对无依赖的常量声明语句逐字求值。
// 固定条件：Node v22.23.2、主机时区（见输出 hostTimezone）、Intl 未 polyfill。
import { readFileSync } from 'node:fs'
// 与原版 time.js 同一 dayjs 单例（源项目 node_modules），用于检查 utc 插件是否已挂载。
import dayjs from '../../../../ruoyi-fastapi-frontend/node_modules/dayjs/dayjs.min.js'

const srcPath = new URL('../../../../ruoyi-fastapi-frontend/src/utils/time.js', import.meta.url)
const src = readFileSync(srcPath, 'utf8')
const lines = src.split('\n')

// 源 8-16 行为无依赖的常量/容器声明（合同逐语句 sha256 已冻结），逐字求值。
const declBlock = lines.slice(7, 16).join('\n')
const literals = new Function(`${declBlock}
return { DATE_ONLY_PATTERN, WALL_TIME_PATTERN, RFC3339_PATTERN, WEEKDAYS, MILLISECONDS_PER_SECOND, MILLISECONDS_PER_MINUTE, MILLISECONDS_PER_HOUR, ORIGINAL_TIME_FIELDS, timezoneFormatters }`)()

const patternCases = (pattern, cases) => cases.map(([input]) => {
  const match = input.match(pattern)
  return { input, matched: !!match, groups: match ? match.slice(1) : null }
})

const out = {
  conditions: {
    node: process.version,
    hostTimezone: new Intl.DateTimeFormat().resolvedOptions().timeZone,
    intlPolyfilled: !!Intl.DateTimeFormat.polyfilled
  },
  constants: {
    DATE_ONLY_PATTERN: {
      source: String(literals.DATE_ONLY_PATTERN),
      flags: literals.DATE_ONLY_PATTERN.flags,
      cases: patternCases(literals.DATE_ONLY_PATTERN, [
        ['2024-02-29'], ['2024-2-29'], ['2024-02-29T10:00:00'], ['2024-02-29 10:00:00'], ['abcd']
      ])
    },
    WALL_TIME_PATTERN: {
      source: String(literals.WALL_TIME_PATTERN),
      flags: literals.WALL_TIME_PATTERN.flags,
      cases: patternCases(literals.WALL_TIME_PATTERN, [
        ['2024-02-29 10:30:45'], ['2024-02-29T10:30:45.123'], ['2024-02-29T10:30:45.1'],
        ['2024-02-29'], ['2024-02-29 10:30'], [' 2024-02-29 10:30:45'], ['2024-13-29 10:30:45']
      ])
    },
    RFC3339_PATTERN: {
      source: String(literals.RFC3339_PATTERN),
      flags: literals.RFC3339_PATTERN.flags,
      cases: patternCases(literals.RFC3339_PATTERN, [
        ['2024-02-29T10:30:45Z'], ['2024-02-29T10:30:45.123Z'], ['2024-02-29T10:30:45+08:00'],
        ['2024-02-29T10:30:45+8:00'], ['2024-02-29T10:30:45'], ['2024-02-29 10:30:45Z'],
        ['2024-02-29T10:30:45-05:30']
      ])
    },
    WEEKDAYS: [...literals.WEEKDAYS],
    MILLISECONDS_PER_SECOND: literals.MILLISECONDS_PER_SECOND,
    MILLISECONDS_PER_MINUTE: literals.MILLISECONDS_PER_MINUTE,
    MILLISECONDS_PER_HOUR: literals.MILLISECONDS_PER_HOUR,
    ORIGINAL_TIME_FIELDS: {
      type: typeof literals.ORIGINAL_TIME_FIELDS,
      string: String(literals.ORIGINAL_TIME_FIELDS)
    },
    timezoneFormatters: {
      isMap: literals.timezoneFormatters instanceof Map,
      initialSize: literals.timezoneFormatters.size
    }
  }
}

// 真实导入原版模块，捕获模块级状态与初始化效果。
const time = await import('../../../../ruoyi-fastapi-frontend/src/utils/time.js')
const err = new time.TimeInputError('无效的日期时间: x', 'INVALID_TIME', [
  { epoch: 1, offset: '+08:00', value: 'v1' }
])
const errDefault = new time.TimeInputError('msg', 'CODE')
out.runtime = {
  moduleExports: Object.keys(time).sort(),
  businessTimezone: time.getBusinessTimezone(),
  userTimezone: time.getUserTimezone(),
  deviceTimezone: time.getDeviceTimezone(),
  displayTimezone: time.getDisplayTimezone(),
  supportedTimezonesSample: time.getSupportedTimezones(['UTC', 'Europe/Paris']),
  timeInputError: {
    name: err.name,
    message: err.message,
    code: err.code,
    candidates: err.candidates,
    instanceofError: err instanceof Error,
    defaultCandidates: errDefault.candidates,
    defaultCode: errDefault.code
  },
  dayjsUtcPluginEnabled: typeof dayjs.utc === 'function'
}

console.log(JSON.stringify(out, null, 2))
