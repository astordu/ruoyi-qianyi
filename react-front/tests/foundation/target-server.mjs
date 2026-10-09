import { createServer, preview } from 'vite'

if (process.argv[2] === 'dev') {
  const server = await createServer({ server: { host: '127.0.0.1', port: 12582, strictPort: true, open: false } })
  await server.listen()
} else {
  await preview({ preview: { host: '127.0.0.1', port: 12583, strictPort: true, open: false } })
}
