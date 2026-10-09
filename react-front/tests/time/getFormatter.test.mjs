// G253F018 行为检查：对照原版基线（migration/state/groups/G253F018/baseline.md）验证
// react-front/src/utils/time.parts/getFormatter.ts 的校验、格式化器选项与缓存语义。
// 期望值来自原版运行结果与源语句，不从目标实现倒推。
import { test, after } from 'node:test'
import assert from 'node:assert/strict'
import { getFormatter } from '../../src/utils/time.parts/getFormatter.ts'
import { timezoneFormatters } from '../../src/utils/time.context.ts'

// 本组写入共享格式化器缓存；结束时清理，避免影响其他 time 测试文件的初始状态断言。
after(() => {
  timezoneFormatters.clear()
})

const commonOptions = {
  locale: 'en',
  calendar: 'gregory',
  numberingSystem: 'latn',
  hourCycle: 'h23',
  hour12: false,
  year: 'numeric',
  month: '2-digit',
  day: '2-digit',
  hour: '2-digit',
  minute: '2-digit',
  second: '2-digit'
}

test('有效 IANA 时区返回格式化器，选项与基线一致', () => {
  for (const name of ['Asia/Shanghai', 'UTC', 'America/New_York', 'Europe/Paris']) {
    const formatter = getFormatter(name)
    assert.ok(formatter instanceof Intl.DateTimeFormat, `${name} 应为 Intl.DateTimeFormat 实例`)
    assert.deepEqual(formatter.resolvedOptions(), { ...commonOptions, timeZone: name })
  }
})

test('运行时规范化时区别名（Asia/Kolkata -> Asia/Calcutta）', () => {
  const formatter = getFormatter('Asia/Kolkata')
  assert.equal(formatter.resolvedOptions().timeZone, 'Asia/Calcutta')
})

test('trim 后名称有效时成功，缓存键为 trim 后名称', () => {
  const direct = getFormatter('Asia/Shanghai')
  const trimmed = getFormatter('  Asia/Shanghai  ')
  assert.equal(trimmed, direct)
  assert.ok(timezoneFormatters.has('Asia/Shanghai'))
  assert.ok(!timezoneFormatters.has('  Asia/Shanghai  '))
})

test('同一时区二次调用返回同一实例', () => {
  const first = getFormatter('America/Los_Angeles')
  const second = getFormatter('America/Los_Angeles')
  assert.equal(second, first)
})

test('无效输入抛出 Error，消息保留原始参数', () => {
  const cases = [
    ['', '无效的 IANA 时区: '],
    ['   ', '无效的 IANA 时区:    '],
    [null, '无效的 IANA 时区: null'],
    [undefined, '无效的 IANA 时区: undefined'],
    [123, '无效的 IANA 时区: 123'],
    [{}, '无效的 IANA 时区: [object Object]'],
    ['+08:00', '无效的 IANA 时区: +08:00'],
    ['-05:00', '无效的 IANA 时区: -05:00'],
    ['Invalid/Zone', '无效的 IANA 时区: Invalid/Zone'],
    ['  Bad/Zone  ', '无效的 IANA 时区:   Bad/Zone  ']
  ]
  for (const [input, message] of cases) {
    assert.throws(() => getFormatter(input), (error) => {
      assert.equal(error.name, 'Error')
      assert.equal(error.message, message)
      return true
    }, `输入 ${JSON.stringify(input)} 应抛错`)
  }
})

test('校验失败不写入缓存', () => {
  const before = timezoneFormatters.size
  for (const input of ['', '+08:00', 'Invalid/Zone']) {
    assert.throws(() => getFormatter(input))
  }
  assert.equal(timezoneFormatters.size, before)
  assert.ok(!timezoneFormatters.has('Invalid/Zone'))
})
