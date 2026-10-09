import assert from 'node:assert/strict'
import { test } from 'node:test'
import { readFile, readdir } from 'node:fs/promises'
import { createServer as createHttpServer } from 'node:http'
import { resolve } from 'node:path'
import { createServer, loadEnv, resolveConfig } from 'vite'
import postcss from 'postcss'

const original = resolve('../ruoyi-fastapi-frontend')
const read = (path) => readFile(path, 'utf8')
const baseline = JSON.parse(await read('../migration/state/groups/G000/baseline.json'))
const config = await resolveConfig({ configFile: resolve('vite.config.ts') }, 'build')

test('environment keys/values retain the source contract in all four modes', () => {
  for (const mode of ['development', 'production', 'staging', 'docker']) {
    assert.deepEqual(loadEnv(mode, process.cwd()), baseline.modes[mode])
    assert.deepEqual(loadEnv(mode, original), baseline.modes[mode])
  }
})

test('configuration retains the original deployment/proxy/output contracts', () => {
  assert.equal(config.base, '/')
  assert.equal(config.server.port, 12580)
  assert.equal(config.server.host, true)
  assert.equal(config.server.open, true)
  const proxy = config.server.proxy['/dev-api']
  assert.equal(proxy.target, baseline.proxy.target)
  assert.equal(proxy.changeOrigin, true)
  assert.equal(proxy.rewrite('/dev-api/items?x=1'), '/items?x=1')
  assert.equal(proxy.rewrite('/dev-api'), '')
  for (const [name, target] of [['@', resolve('src')], ['~', process.cwd()+'/']]) {
    const alias = config.resolve.alias.find(a => a.find === name)
    assert.equal(alias.replacement.replace(/\/$/, ''), target.replace(/\/$/, ''))
  }
  assert.equal(config.build.outDir, 'dist')
  assert.equal(config.build.assetsDir, 'assets')
  assert.equal(config.build.chunkSizeWarningLimit, 2000)
  assert.equal(config.build.sourcemap, false)
  const output = config.build.rolldownOptions.output
  assert.equal(output.entryFileNames, 'static/js/[name]-[hash].js')
  assert.equal(output.chunkFileNames, 'static/js/[name]-[hash].js')
  assert.equal(output.assetFileNames, 'static/[ext]/[name]-[hash].[ext]')
})

test('HTML retains the whole original loading markup and CSS, with only React entry substitutions', async () => {
  const source = await read(original+'/index.html')
  const expected = source.replaceAll('#app', '#root').replace('id="app"', 'id="root"').replace('/src/main.js', '/src/main.tsx')
  assert.equal(await read('index.html'), expected)
  assert.deepEqual(await readFile('public/favicon.ico'), await readFile(original+'/public/favicon.ico'))
  assert.deepEqual(await readFile('public/html/ie.html'), await readFile(original+'/html/ie.html'))
})

test('all three emitted builds retain title/assets and contain no production source maps', async () => {
  for (const mode of ['production', 'staging', 'docker']) {
    const root = resolve('../migration/state/evidence/G000/builds', mode)
    const html = await read(root+'/index.html')
    assert.match(html, new RegExp(`<title>${baseline.modes[mode].VITE_APP_TITLE}</title>`))
    assert.match(html, /src="\/static\/js\/[^" ]+\.js"/)
    assert.match(html, /href="\/static\/css\/[^" ]+\.css"/)
    const jsfiles = await readdir(root+'/static/js')
    assert.ok(jsfiles.some(f => f.endsWith('.js')))
    assert.ok(jsfiles.every(f => !f.endsWith('.map')))
    for (const f of jsfiles.filter(f => f.endsWith('.js'))) {
      assert.doesNotMatch(await read(root+'/static/js/'+f), /sourceMappingURL=/)
    }
    assert.deepEqual(await readFile(root+'/favicon.ico'), await readFile(original+'/public/favicon.ico'))
    assert.deepEqual(await readFile(root+'/html/ie.html'), await readFile(original+'/html/ie.html'))
  }
})

test('real dev proxy forwards path/query and rewrites Host using a read-only probe', async () => {
  const probe = createHttpServer((req, res) => {
    res.setHeader('Content-Type', 'application/json')
    res.end(JSON.stringify({ method: req.method, url: req.url, host: req.headers.host }))
  })
  await new Promise(resolve => probe.listen(0, '127.0.0.1', resolve))
  const probePort = probe.address().port
  let server
  try {
    server = await createServer({
      configFile: resolve('vite.config.ts'),
      server: { host: '127.0.0.1', port: 12681, strictPort: true, open: false,
        proxy: { '/dev-api': { ...config.server.proxy['/dev-api'], target: `http://127.0.0.1:${probePort}` } } },
    })
    await server.listen()
    const response = await fetch('http://127.0.0.1:12681/dev-api/__migration_probe?echo=hello%20world')
    assert.equal(response.status, 200)
    assert.deepEqual(await response.json(), { method: 'GET', url: '/__migration_probe?echo=hello%20world', host: `127.0.0.1:${probePort}` })
    const module = await fetch('http://127.0.0.1:12681/src/main.tsx')
    assert.equal(module.status, 200)
    assert.match(await module.text(), /src\/App\.tsx/)
  } finally {
    if (server) await server.close()
    await new Promise(resolve => probe.close(resolve))
  }
})

test('CSS processing removes charset while preserving declarations', async () => {
  const result = await postcss(config.css.postcss.plugins).process('@charset "UTF-8"; .fixture { color: red; }', { from: undefined })
  assert.doesNotMatch(result.css, /@charset/)
  assert.match(result.css, /\.fixture\s*\{\s*color:\s*red;/)
})

test('target dependency graph contains no Vue/Pinia/ElementPlus runtime', async () => {
  const lock = JSON.parse(await read('package-lock.json'))
  for (const name of Object.keys(lock.packages)) {
    assert.doesNotMatch(name, /node_modules\/(vue|pinia|element-plus|ant-design-vue|@vue)(\/|$)/)
  }
})
