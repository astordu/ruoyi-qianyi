// G253F018 原版基线采集：从源文件逐字求值 getFormatter（44-70 行）与 timezoneFormatters 容器（16 行），
// 并以源项目 node_modules 真实导入原版 time.js 验证模块内调用链路（初始化成功即证明 getFormatter('Asia/Shanghai') 通过）。
// 固定条件：Node v22.23.2、主机时区（见输出 hostTimezone）、Intl 未 polyfill。
import { readFileSync } from 'node:fs'

const srcPath = new URL('../../../../ruoyi-fastapi-frontend/src/utils/time.js', import.meta.url)
const src = readFileSync(srcPath, 'utf8')
const lines = src.split('\n')

// 源第 16 行容器声明 + 44-70 行 getFormatter，同一 Function 体内逐字求值，共享同一 timezoneFormatters 闭包。
const decl = lines[15]
const fnBlock = lines.slice(43, 70).join('\n')
const factory = new Function(`${decl}\n${fnBlock}\nreturn { getFormatter, timezoneFormatters }`)
const { getFormatter, timezoneFormatters } = factory()

const call = (input) => {
  try {
    const formatter = getFormatter(input)
    return {
      input,
      ok: true,
      isIntlDateTimeFormat: formatter instanceof Intl.DateTimeFormat,
      resolved: formatter.resolvedOptions()
    }
  } catch (error) {
    return { input, ok: false, error: { name: error.name, message: error.message } }
  }
}

const out = {
  conditions: {
    node: process.version,
    hostTimezone: new Intl.DateTimeFormat().resolvedOptions().timeZone,
    intlPolyfilled: !!Intl.DateTimeFormat.polyfilled
  },
  cases: [
    call('Asia/Shanghai'),
    call('  Asia/Shanghai  '),
    call('UTC'),
    call('America/New_York'),
    call('Europe/Paris'),
    call('Asia/Kolkata'),
    call(''),
    call('   '),
    call(null),
    call(undefined),
    call(123),
    call({}),
    call('+08:00'),
    call('-05:00'),
    call('Invalid/Zone'),
    call('  Bad/Zone  ')
  ],
  cache: {
    // 同一时区二次调用返回同一实例（引用相等），且缓存键为 trim 后的名称。
    sameInstance: (() => {
      const first = getFormatter('America/Los_Angeles')
      const second = getFormatter('America/Los_Angeles')
      const trimmed = getFormatter('  America/Los_Angeles  ')
      return {
        repeatedSameReference: first === second,
        trimmedSameReference: first === trimmed,
        hasTrimmedKey: timezoneFormatters.has('America/Los_Angeles')
      }
    })(),
    // 校验失败不写入缓存。
    failureNotCached: (() => {
      const before = timezoneFormatters.size
      try {
        getFormatter('Not/A_Timezone')
      } catch {
        /* 预期抛错 */
      }
      return { sizeBefore: before, sizeAfter: timezoneFormatters.size, hasFailedKey: timezoneFormatters.has('Not/A_Timezone') }
    })()
  }
}

// 真实导入原版模块：模块初始化（523-524 行）会调用 setBusinessTimezone -> getFormatter('Asia/Shanghai')，
// 成功初始化即证明原版模块内 getFormatter 接受 'Asia/Shanghai'。函数本身不导出，逐字求值部分为行为基线。
const time = await import('../../../../ruoyi-fastapi-frontend/src/utils/time.js')
out.runtimeImport = {
  moduleLoaded: true,
  businessTimezone: time.getBusinessTimezone(),
  deviceTimezone: time.getDeviceTimezone()
}

console.log(JSON.stringify(out, null, 2))
