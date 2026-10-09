import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from '@/App'
import '@/styles/bootstrap.css'

const container = document.getElementById('root')
if (!container) throw new Error('缺少 React 挂载容器 #root')

createRoot(container).render(<StrictMode><App /></StrictMode>)
