// 源：ruoyi-fastapi-frontend/src/utils/time.js（1-36、523-524 行）
// 状态、输入与依赖接口：大文件函数组（time.parts/*）通过本模块显式注入共享状态与依赖。
// 生命周期启动与页面按钮接线由 G253V 装配组验证。
import dayjs from 'dayjs'
import utc from 'dayjs/plugin/utc.js'

dayjs.extend(utc)

export const DATE_ONLY_PATTERN = /^(\d{4})-(\d{2})-(\d{2})$/
export const WALL_TIME_PATTERN = /^(\d{4})-(\d{2})-(\d{2})[ T](\d{2}):(\d{2}):(\d{2})(?:\.(\d{1,3}))?$/
export const RFC3339_PATTERN = /^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})(\.\d+)?(Z|[+-](?:[01]\d|2[0-3]):[0-5]\d)$/
export const WEEKDAYS = ['日', '一', '二', '三', '四', '五', '六']
export const MILLISECONDS_PER_SECOND = 1000
export const MILLISECONDS_PER_MINUTE = 60 * MILLISECONDS_PER_SECOND
export const MILLISECONDS_PER_HOUR = 60 * MILLISECONDS_PER_MINUTE
export const ORIGINAL_TIME_FIELDS = Symbol('originalTimeFields')
export const timezoneFormatters = new Map<string, Intl.DateTimeFormat>()

// 源：`import { ref } from 'vue'`。工具层无渲染订阅者，用可变值持有器保留 .value 访问语义；
// 组件层的响应式衔接由各组件组负责，不把 Vue 依赖带入 React。
export interface MutableRef<T> {
  value: T
}

export const businessTimezone: MutableRef<string> = { value: 'Asia/Shanghai' }
export const userTimezone: MutableRef<string> = { value: 'auto' }
export const deviceTimezone: MutableRef<string | null> = { value: null }

export interface TimeInputCandidate {
  epoch: number
  offset: string
  value: string
}

/**
 * 日期时间输入校验异常，包含夏令时重复时间的候选值。
 */
export class TimeInputError extends Error {
  /** 错误类型 */
  code: string
  /** 可选的真实时刻 */
  candidates: TimeInputCandidate[]

  constructor(message: string, code: string, candidates: TimeInputCandidate[] = []) {
    super(message)
    this.code = code
    this.candidates = candidates
  }
}

// 源：`import { ElMessage, ElMessageBox } from 'element-plus'`。
// Vue 专属 UI 提示按转换约定隔离为依赖接口，由装配层注入 React 对应能力，不引入 element-plus。
export interface TimePromptDeps {
  ElMessage: {
    error: (message: string) => void
  }
  ElMessageBox: {
    prompt: (
      message: string,
      title: string,
      options: {
        inputPlaceholder: string
        inputValidator: (value: string) => string | boolean
        confirmButtonText: string
        cancelButtonText: string
      }
    ) => Promise<{ value: string }>
  }
}

// 源 523-524 行模块初始化调用：先 setBusinessTimezone(businessTimezone.value)，再 refreshDeviceTimezone()。
// 函数实现由各 F 组迁入 time.parts 后，G253V 装配在 time.ts 模块加载时调用本函数注入真实实现，保留原调用次序。
export interface TimeContextInitDeps {
  setBusinessTimezone: (timezoneName: string) => void
  refreshDeviceTimezone: () => string | null
}

export function initTimeContext(deps: TimeContextInitDeps): void {
  deps.setBusinessTimezone(businessTimezone.value)
  deps.refreshDeviceTimezone()
}

export { dayjs }
