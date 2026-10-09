# G253 实施记录

目标：`react-front/src/utils/time.context.ts`（新建）。范围仅本轮 20 个源段（time.js 1-36、523-524 行）：导入、dayjs 装配、常量、状态、TimeInputError 与初始化调用次序；函数实现属 F 组、导出装配属 G253V，均未提前实现。

## 映射决策

- `import { ElMessage, ElMessageBox } from 'element-plus'` → `TimePromptDeps` 依赖接口。按转换约定隔离 Vue 专属 UI 提示，由装配层注入 React 对应能力，不引入 element-plus。使用场景（chooseTimeOffset、serializeTimeFieldsForSubmit）属 F045/F046。
- `import { ref } from 'vue'` → `MutableRef<T>` 可变值持有器，保留 `.value` 语义；工具层无渲染订阅者，组件层响应式衔接由各组件组负责。
- dayjs/utc 导入与 `dayjs.extend(utc)` 保持模块级副作用，`dayjs` 单例 re-export 供 parts 使用。
- 源 523-524 行模块初始化 → `initTimeContext(deps)`：保留"先 setBusinessTimezone(businessTimezone.value)，再 refreshDeviceTimezone()"的调用次序与参数，函数实现由 F 组迁入后由 G253V 在 time.ts 模块加载时调用注入。未使用占位函数。

## 公共影响（组外必要接入，已登记）

- `react-front/package.json` 增加 `dayjs@1.11.23`（与源版本一致，npm install 完成）。原因：time.context.ts 必须真实导入 dayjs。影响：G016（package.json 内容项）实施时需核对本接入；G000 验证因 package.json 哈希变化而失效（check 输出 invalidated_groups: [G000]），下一轮按协议以 revalidate 模式复验，本轮不处理。
- 新增 `react-front/tests/time/time.context.test.mjs` 行为测试；`test:time` 脚本接线属 G016，本轮用 `node --test` 直接运行。
- 源 Vue 与后端未改动。

## 验证命令与结果

- 基线：`node migration/state/evidence/G253/baseline-capture.mjs` → evidence/G253/baseline.json（Node v22.23.2、Asia/Shanghai、Intl 未 polyfill）。原版 test:time 依赖工作区外 contract 包，无法运行，已记录缺证据。
- 行为测试：`cd react-front && node --test tests/time/time.context.test.mjs` → 7/7 通过。
- 类型：`npm run typecheck` → 退出 0。
- 构建：`npm run build:prod` → 成功（219.77 kB js）。

## 剩余问题与下一步

- deviceTimezone 初始化解析、格式器缓存等运行时终态已用注入等价行为验证；真实函数注入后的完整初始化效果由 G253V 验证。
- 依赖 G000 的 revalidate 与 F018 起的函数组由后续轮次处理。

## 记账

- G000 复验（本组 package.json 接入 dayjs 导致的失效）：重跑三套构建、test:foundation 7/7、playwright 3/3、锁文件无 Vue 系依赖，验证报告追加复验章节，record passed 已重新冻结快照。
- G253 record passed 完成：check 显示 2/773 小组通过、invalidated_groups=[]。本轮结束，未选第二组。
