// 源：ruoyi-fastapi-frontend/src/utils/time.js（44-70 行）
// getFormatter：共享格式化器缓存，通过 time.context 注入的 timezoneFormatters 保留模块级缓存语义。
// 其他 time.parts 函数组通过本导出复用同一缓存。
import { timezoneFormatters } from '../time.context.ts'

/**
 * 获取并缓存指定时区的日期时间格式化器。
 *
 * @param timezoneName IANA 时区名称
 * @returns 格式化器实例
 */
export function getFormatter(timezoneName: string): Intl.DateTimeFormat {
  if (typeof timezoneName !== 'string' || !timezoneName.trim() || /^[+-]/.test(timezoneName)) {
    throw new Error(`无效的 IANA 时区: ${timezoneName}`)
  }

  const name = timezoneName.trim()
  if (!timezoneFormatters.has(name)) {
    try {
      const formatter = new Intl.DateTimeFormat('en', {
        timeZone: name,
        calendar: 'gregory',
        numberingSystem: 'latn',
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hourCycle: 'h23'
      })
      timezoneFormatters.set(name, formatter)
    } catch {
      throw new Error(`无效的 IANA 时区: ${timezoneName}`)
    }
  }
  return timezoneFormatters.get(name)!
}
