// G253 行为检查：对照原版基线（migration/state/groups/G253/baseline.md）验证
// react-front/src/utils/time.context.ts 的常量、状态、错误类与初始化调用次序。
// 期望值来自原版运行结果与源语句，不从目标实现倒推。
import { test } from 'node:test'
import assert from 'node:assert/strict'
import dayjs from 'dayjs'
import * as ctx from '../../src/utils/time.context.ts'

const patternCases = (pattern, cases) => cases.map(([input]) => {
  const match = input.match(pattern)
  // 未参与捕获的组为 undefined，与基线 JSON 表示统一为 null
  return { input, matched: !!match, groups: match ? match.slice(1).map(group => group ?? null) : null }
})

test('常量字面量与基线一致', () => {
  assert.equal(String(ctx.DATE_ONLY_PATTERN), String(/^(\d{4})-(\d{2})-(\d{2})$/))
  assert.equal(String(ctx.WALL_TIME_PATTERN), String(/^(\d{4})-(\d{2})-(\d{2})[ T](\d{2}):(\d{2}):(\d{2})(?:\.(\d{1,3}))?$/))
  assert.equal(String(ctx.RFC3339_PATTERN), String(/^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})(\.\d+)?(Z|[+-](?:[01]\d|2[0-3]):[0-5]\d)$/))
  assert.deepEqual([...ctx.WEEKDAYS], ['日', '一', '二', '三', '四', '五', '六'])
  assert.equal(ctx.MILLISECONDS_PER_SECOND, 1000)
  assert.equal(ctx.MILLISECONDS_PER_MINUTE, 60000)
  assert.equal(ctx.MILLISECONDS_PER_HOUR, 3600000)
})

test('日期/时间模式与基线样例一致', () => {
  assert.deepEqual(patternCases(ctx.DATE_ONLY_PATTERN, [
    ['2024-02-29'], ['2024-2-29'], ['2024-02-29T10:00:00'], ['2024-02-29 10:00:00'], ['abcd']
  ]), [
    { input: '2024-02-29', matched: true, groups: ['2024', '02', '29'] },
    { input: '2024-2-29', matched: false, groups: null },
    { input: '2024-02-29T10:00:00', matched: false, groups: null },
    { input: '2024-02-29 10:00:00', matched: false, groups: null },
    { input: 'abcd', matched: false, groups: null }
  ])
  assert.deepEqual(patternCases(ctx.WALL_TIME_PATTERN, [
    ['2024-02-29 10:30:45'], ['2024-02-29T10:30:45.123'], ['2024-02-29T10:30:45.1'],
    ['2024-02-29'], ['2024-02-29 10:30'], [' 2024-02-29 10:30:45'], ['2024-13-29 10:30:45']
  ]), [
    { input: '2024-02-29 10:30:45', matched: true, groups: ['2024', '02', '29', '10', '30', '45', null] },
    { input: '2024-02-29T10:30:45.123', matched: true, groups: ['2024', '02', '29', '10', '30', '45', '123'] },
    { input: '2024-02-29T10:30:45.1', matched: true, groups: ['2024', '02', '29', '10', '30', '45', '1'] },
    { input: '2024-02-29', matched: false, groups: null },
    { input: '2024-02-29 10:30', matched: false, groups: null },
    { input: ' 2024-02-29 10:30:45', matched: false, groups: null },
    { input: '2024-13-29 10:30:45', matched: true, groups: ['2024', '13', '29', '10', '30', '45', null] }
  ])
  assert.deepEqual(patternCases(ctx.RFC3339_PATTERN, [
    ['2024-02-29T10:30:45Z'], ['2024-02-29T10:30:45.123Z'], ['2024-02-29T10:30:45+08:00'],
    ['2024-02-29T10:30:45+8:00'], ['2024-02-29T10:30:45'], ['2024-02-29 10:30:45Z'],
    ['2024-02-29T10:30:45-05:30']
  ]), [
    { input: '2024-02-29T10:30:45Z', matched: true, groups: ['2024-02-29T10:30:45', null, 'Z'] },
    { input: '2024-02-29T10:30:45.123Z', matched: true, groups: ['2024-02-29T10:30:45', '.123', 'Z'] },
    { input: '2024-02-29T10:30:45+08:00', matched: true, groups: ['2024-02-29T10:30:45', null, '+08:00'] },
    { input: '2024-02-29T10:30:45+8:00', matched: false, groups: null },
    { input: '2024-02-29T10:30:45', matched: false, groups: null },
    { input: '2024-02-29 10:30:45Z', matched: false, groups: null },
    { input: '2024-02-29T10:30:45-05:30', matched: true, groups: ['2024-02-29T10:30:45', null, '-05:30'] }
  ])
})

test('共享容器与初始状态符合基线', () => {
  assert.equal(typeof ctx.ORIGINAL_TIME_FIELDS, 'symbol')
  assert.equal(String(ctx.ORIGINAL_TIME_FIELDS), 'Symbol(originalTimeFields)')
  assert.ok(ctx.timezoneFormatters instanceof Map)
  assert.equal(ctx.timezoneFormatters.size, 0)
  // 源 ref('Asia/Shanghai')/ref('auto')/ref(null) 初始值；初始化调用前不解析设备时区
  assert.equal(ctx.businessTimezone.value, 'Asia/Shanghai')
  assert.equal(ctx.userTimezone.value, 'auto')
  assert.equal(ctx.deviceTimezone.value, null)
})

test('TimeInputError 语义与基线一致', () => {
  const err = new ctx.TimeInputError('无效的日期时间: x', 'INVALID_TIME', [
    { epoch: 1, offset: '+08:00', value: 'v1' }
  ])
  assert.equal(err.name, 'Error')
  assert.equal(err.message, '无效的日期时间: x')
  assert.equal(err.code, 'INVALID_TIME')
  assert.deepEqual(err.candidates, [{ epoch: 1, offset: '+08:00', value: 'v1' }])
  assert.ok(err instanceof Error)
  const errDefault = new ctx.TimeInputError('msg', 'CODE')
  assert.deepEqual(errDefault.candidates, [])
  assert.equal(errDefault.code, 'CODE')
})

test('initTimeContext 保留源 523-524 行调用次序', () => {
  const calls = []
  const deps = {
    setBusinessTimezone: (name) => calls.push(['setBusinessTimezone', name]),
    refreshDeviceTimezone: () => { calls.push(['refreshDeviceTimezone']); return 'Asia/Shanghai' }
  }
  const result = ctx.initTimeContext(deps)
  assert.equal(result, undefined)
  // 先 setBusinessTimezone(businessTimezone.value)，再 refreshDeviceTimezone()
  assert.deepEqual(calls, [['setBusinessTimezone', 'Asia/Shanghai'], ['refreshDeviceTimezone']])
})

test('initTimeContext 注入等价行为后终态与基线一致', () => {
  // 模拟原函数可观察契约：setBusinessTimezone 写入业务时区，refreshDeviceTimezone 解析设备时区。
  // 本组不实现这些函数（属 F 组），仅验证初始化次序产生的终态与基线相同。
  const deps = {
    setBusinessTimezone: (name) => { ctx.businessTimezone.value = name.trim() },
    refreshDeviceTimezone: () => {
      ctx.deviceTimezone.value = new Intl.DateTimeFormat().resolvedOptions().timeZone
      return ctx.deviceTimezone.value
    }
  }
  ctx.initTimeContext(deps)
  assert.equal(ctx.businessTimezone.value, 'Asia/Shanghai')
  assert.equal(ctx.userTimezone.value, 'auto')
  assert.equal(ctx.deviceTimezone.value, new Intl.DateTimeFormat().resolvedOptions().timeZone)
})

test('模块加载已挂载 dayjs utc 插件', () => {
  assert.equal(typeof dayjs.utc, 'function')
})
