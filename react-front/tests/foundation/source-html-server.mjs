// Runs only the unchanged original HTML pre-mount state, not the Vue business app.
import { createServer } from 'node:http'
import { readFile } from 'node:fs/promises'
import { resolve } from 'node:path'

const source = resolve('../ruoyi-fastapi-frontend')
const baseline = JSON.parse(await readFile('../migration/state/groups/G000/baseline.json', 'utf8'))
const html = (await readFile(source+'/index.html', 'utf8')).replace('%VITE_APP_TITLE%', baseline.modes.development.VITE_APP_TITLE)
createServer(async (req, res) => {
  if (req.url === '/favicon.ico') {
    res.setHeader('Content-Type', 'image/x-icon')
    res.end(await readFile(source+'/public/favicon.ico'))
  } else {
    res.setHeader('Content-Type', 'text/html; charset=utf-8')
    res.end(html)
  }
}).listen(13581, '127.0.0.1')
