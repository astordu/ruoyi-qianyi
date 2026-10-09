import { readFile, writeFile, mkdir } from 'node:fs/promises'
import { resolve } from 'node:path'
import { test, expect } from '@playwright/test'

const evidence = resolve('../migration/state/evidence/G000')
const title = 'vfadmin管理系统'

test('original and React HTML have pixel-identical pre-mount loading screens', async ({ browser }) => {
  await mkdir(evidence, { recursive: true })
  const images: Buffer[] = []
  for (const [name, port, entry] of [['original', 13581, 'main.js'], ['react', 12582, 'main.tsx']] as const) {
    const page = await browser.newPage({ viewport: { width: 1280, height: 720 }, locale: 'zh-CN', timezoneId: 'Asia/Shanghai' })
    await page.route(`**/src/${entry}`, route => route.abort())
    await page.goto(`http://127.0.0.1:${port}/`)
    await expect(page).toHaveTitle(title)
    await expect(page.locator('.load_title')).toHaveText('正在加载系统资源，请耐心等待')
    await expect(page.locator('.loader-section').first()).toHaveCSS('background-color', 'rgb(113, 113, 198)')
    // Freeze both versions, including pseudo-elements, before visual comparison.
    await page.addStyleTag({ content: '*, *::before, *::after { animation: none !important; transition: none !important; }' })
    images.push(await page.screenshot({ path: `${evidence}/${name}-loading.png` }))
    await page.close()
  }
  expect(images[1].equals(images[0])).toBe(true)
  await writeFile(evidence+'/loading-comparison.json', JSON.stringify({ comparison: 'exact PNG bytes', equal: images[1].equals(images[0]), animationHandling: 'disabled on both original and React', scope: 'pre-mount HTML only' }, null, 2))
})

for (const [name, port] of [['dev', 12582], ['production-preview', 12583]] as const) {
  test(`${name}: mounts at root and preserves deep URL on reload`, async ({ page, request }) => {
    const errors: string[] = []
    const apiRequests: string[] = []
    page.on('pageerror', error => errors.push(error.message))
    page.on('request', req => { if (/\/(dev|prod|stage|docker)-api\//.test(req.url())) apiRequests.push(req.url()) })
    await page.goto(`http://127.0.0.1:${port}/`)
    await expect(page).toHaveTitle(title)
    await expect(page.getByTestId('bootstrap-status')).toContainText('React 工程已启动')
    await expect(page.locator('#loader-wrapper')).toHaveCount(0)
    const deep = `http://127.0.0.1:${port}/system/user/profile?tab=security#details`
    await page.goto(deep)
    await expect(page.getByTestId('bootstrap-status')).toBeVisible()
    await expect(page).toHaveURL(deep)
    await page.reload()
    await expect(page.getByTestId('bootstrap-status')).toBeVisible()
    await expect(page).toHaveURL(deep)
    expect(errors).toEqual([])
    expect(apiRequests).toEqual([])
    const favicon = await request.get(`http://127.0.0.1:${port}/favicon.ico`)
    expect(favicon.status()).toBe(200)
    expect((await favicon.body()).equals(await readFile(resolve('../ruoyi-fastapi-frontend/public/favicon.ico')))).toBe(true)
    const fallback = await request.get(`http://127.0.0.1:${port}/html/ie.html`)
    expect(fallback.status()).toBe(200)
    expect((await fallback.body()).equals(await readFile(resolve('../ruoyi-fastapi-frontend/html/ie.html')))).toBe(true)
    await page.screenshot({ path: `${evidence}/${name}-mounted.png` })
  })
}
