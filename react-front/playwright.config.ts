import { defineConfig } from '@playwright/test'

export default defineConfig({
  testDir: './tests/foundation',
  testMatch: '*.spec.ts',
  workers: 1,
  retries: 0,
  outputDir: '../migration/state/evidence/G000/browser-artifacts',
  reporter: [
    ['list'],
    ['json', { outputFile: '../migration/state/evidence/G000/browser-results.json' }],
  ],
  use: { browserName: 'chromium', viewport: { width: 1280, height: 720 }, locale: 'zh-CN', timezoneId: 'Asia/Shanghai' },
  webServer: [
    { command: 'node tests/foundation/source-html-server.mjs', url: 'http://127.0.0.1:13581', reuseExistingServer: false },
    { command: 'node tests/foundation/target-server.mjs dev', url: 'http://127.0.0.1:12582', reuseExistingServer: false },
    { command: 'node tests/foundation/target-server.mjs preview', url: 'http://127.0.0.1:12583', reuseExistingServer: false },
  ],
})
