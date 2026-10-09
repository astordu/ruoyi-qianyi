// 独立差分：原版逐字求值 vs 目标实现，同输入比较结果
import { readFileSync } from 'node:fs'
import { createRequire } from 'node:module'
const require = createRequire(import.meta.url)

const src = readFileSync('/Users/dulei/Documents/projects/ruoyi-qianyi/ruoyi-fastapi-frontend/src/utils/time.js', 'utf8').split('\n')
const decl = src[15]
const fnBlock = src.slice(43, 70).join('\n')
const orig = new Function(`${decl}\n${fnBlock}\nreturn { getFormatter, timezoneFormatters }`)()

// 目标：TS 通过 strip 加载（Node 22 原生支持 type stripping）
const { getFormatter: newGet, ...rest } = await import('/Users/dulei/Documents/projects/ruoyi-qianyi/react-front/src/utils/time.parts/getFormatter.ts')
const { timezoneFormatters: newMap } = await import('/Users/dulei/Documents/projects/ruoyi-qianyi/react-front/src/utils/time.context.ts')

const inputs = [
  'Asia/Shanghai', 'UTC', 'America/New_York', 'Europe/Paris', 'Asia/Kolkata',
  'Asia/Tokyo', 'Australia/Sydney', 'Africa/Cairo', 'America/Sao_Paulo',
  '  Asia/Shanghai  ', '  UTC', 'UTC  ',
  '', '   ', ' ', null, undefined, 123, {}, [], true,
  '+08:00', '-05:00', '+5:30', '-3',
  'Invalid/Zone', '  Bad/Zone  ', 'Not/A_Timezone', 'GMT+8', 'Etc/GMT-5',
  'America/Los_Angeles', 'America/Los_Angeles'
]
const capture = (fn) => (input) => {
  try {
    const f = fn(input)
    return { ok: true, instance: f instanceof Intl.DateTimeFormat, resolved: f.resolvedOptions() }
  } catch (e) {
    return { ok: false, name: e.name, message: e.message }
  }
}
const origCall = capture(orig.getFormatter)
const newCall = capture(newGet)

let failures = 0
for (const input of inputs) {
  const o = origCall(input)
  const n = newCall(input)
  if (JSON.stringify(o) !== JSON.stringify(n)) {
    failures++
    console.log('MISMATCH', JSON.stringify(input))
    console.log('  orig:', JSON.stringify(o))
    console.log('  new :', JSON.stringify(n))
  }
}
// 缓存引用语义：trim 键一致、失败不写缓存（两实现独立 Map，只比相对行为）
const origRef = (() => { const a = orig.getFormatter('Europe/London'); return orig.getFormatter('  Europe/London  ') === a })()
const newRef = (() => { const a = newGet('Europe/London'); return newGet('  Europe/London  ') === a })()
const origNoCache = (() => { const s = orig.timezoneFormatters.size; try { orig.getFormatter('Xxx/Yyy') } catch {} return { same: orig.timezoneFormatters.size === s, has: orig.timezoneFormatters.has('Xxx/Yyy') } })()
const newNoCache = (() => { const s = newMap.size; try { newGet('Xxx/Yyy') } catch {} return { same: newMap.size === s, has: newMap.has('Xxx/Yyy') } })()
console.log('cache_ref_equal:', origRef === newRef, origRef)
console.log('failure_not_cached_equal:', JSON.stringify(origNoCache) === JSON.stringify(newNoCache), newNoCache)
console.log('cases:', inputs.length, 'mismatches:', failures)
process.exit(failures === 0 ? 0 : 1)
