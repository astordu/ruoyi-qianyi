// G253 目标侧比对：对照原版 baseline.json 检查 react-front/src/utils/time.context.ts。
// 输出差异清单，全部一致时退出 0。
import { readFileSync } from 'node:fs'
import dayjs from '../../../../react-front/node_modules/dayjs/dayjs.min.js'
import * as ctx from '../../../../react-front/src/utils/time.context.ts'

const baseline = JSON.parse(readFileSync(new URL('./baseline.json', import.meta.url), 'utf8'))
const diffs = []

const patternCases = (pattern, cases) => cases.map(({ input }) => {
  const match = input.match(pattern)
  return { input, matched: !!match, groups: match ? match.slice(1).map(group => group ?? null) : null }
})

const compare = (label, actual, expected) => {
  if (JSON.stringify(actual) !== JSON.stringify(expected)) {
    diffs.push({ label, actual, expected })
  }
}

const conditions = {
  node: process.version,
  hostTimezone: new Intl.DateTimeFormat().resolvedOptions().timeZone,
  intlPolyfilled: !!Intl.DateTimeFormat.polyfilled
}

for (const name of ['DATE_ONLY_PATTERN', 'WALL_TIME_PATTERN', 'RFC3339_PATTERN']) {
  compare(`constants.${name}.source`, String(ctx[name]), baseline.constants[name].source)
  compare(`constants.${name}.flags`, ctx[name].flags, baseline.constants[name].flags)
  compare(`constants.${name}.cases`, patternCases(ctx[name], baseline.constants[name].cases), baseline.constants[name].cases)
}
compare('constants.WEEKDAYS', [...ctx.WEEKDAYS], baseline.constants.WEEKDAYS)
compare('constants.MILLISECONDS_PER_SECOND', ctx.MILLISECONDS_PER_SECOND, baseline.constants.MILLISECONDS_PER_SECOND)
compare('constants.MILLISECONDS_PER_MINUTE', ctx.MILLISECONDS_PER_MINUTE, baseline.constants.MILLISECONDS_PER_MINUTE)
compare('constants.MILLISECONDS_PER_HOUR', ctx.MILLISECONDS_PER_HOUR, baseline.constants.MILLISECONDS_PER_HOUR)
compare('constants.ORIGINAL_TIME_FIELDS', { type: typeof ctx.ORIGINAL_TIME_FIELDS, string: String(ctx.ORIGINAL_TIME_FIELDS) }, baseline.constants.ORIGINAL_TIME_FIELDS)
compare('constants.timezoneFormatters', { isMap: ctx.timezoneFormatters instanceof Map, initialSize: ctx.timezoneFormatters.size }, baseline.constants.timezoneFormatters)

// 初始状态：business/user 与源 ref 初始值一致；device 初始化前为 null（源在模块加载末尾解析）
compare('state.businessTimezone', ctx.businessTimezone.value, baseline.runtime.businessTimezone)
compare('state.userTimezone', ctx.userTimezone.value, baseline.runtime.userTimezone)

// TimeInputError
const err = new ctx.TimeInputError('无效的日期时间: x', 'INVALID_TIME', [
  { epoch: 1, offset: '+08:00', value: 'v1' }
])
const errDefault = new ctx.TimeInputError('msg', 'CODE')
compare('timeInputError', {
  name: err.name, message: err.message, code: err.code, candidates: err.candidates,
  instanceofError: err instanceof Error, defaultCandidates: errDefault.candidates, defaultCode: errDefault.code
}, baseline.runtime.timeInputError)

// dayjs utc 插件副作用
compare('dayjsUtcPluginEnabled', typeof dayjs.utc === 'function', baseline.runtime.dayjsUtcPluginEnabled)

// 初始化调用次序：setBusinessTimezone(businessTimezone.value) → refreshDeviceTimezone()
const calls = []
ctx.initTimeContext({
  setBusinessTimezone: (name) => calls.push(['setBusinessTimezone', name]),
  refreshDeviceTimezone: () => { calls.push(['refreshDeviceTimezone']); return null }
})
compare('initCalls', calls, [['setBusinessTimezone', ctx.businessTimezone.value], ['refreshDeviceTimezone']])

const out = {
  conditions,
  baselineConditions: baseline.conditions,
  comparisons: Object.keys({
    ...baseline.constants, state: true, timeInputError: true, dayjsUtcPluginEnabled: true, initCalls: true
  }).length,
  diffs,
  passed: diffs.length === 0
}
console.log(JSON.stringify(out, null, 2))
process.exit(diffs.length === 0 ? 0 : 1)
