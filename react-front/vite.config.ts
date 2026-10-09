import { fileURLToPath, URL } from 'node:url'
import react from '@vitejs/plugin-react'
import { defineConfig } from 'vite'

export default defineConfig(({ command }) => ({
  base: '/',
  plugins: [react()],
  resolve: {
    alias: {
      '~': fileURLToPath(new URL('.', import.meta.url)),
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
    extensions: ['.mjs', '.js', '.ts', '.jsx', '.tsx', '.json'],
  },
  build: {
    sourcemap: command === 'build' ? false : 'inline',
    outDir: 'dist',
    assetsDir: 'assets',
    chunkSizeWarningLimit: 2000,
    rolldownOptions: {
      output: {
        chunkFileNames: 'static/js/[name]-[hash].js',
        entryFileNames: 'static/js/[name]-[hash].js',
        assetFileNames: 'static/[ext]/[name]-[hash].[ext]',
      },
    },
  },
  server: {
    port: 12580,
    host: true,
    open: true,
    proxy: {
      '/dev-api': {
        target: 'http://127.0.0.1:19099',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/dev-api/, ''),
      },
    },
  },
  css: {
    postcss: {
      plugins: [{
        postcssPlugin: 'internal:charset-removal',
        AtRule: {
          charset: (rule) => { rule.remove() },
        },
      }],
    },
  },
}))
