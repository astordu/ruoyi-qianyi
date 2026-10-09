// Temporary engineering diagnostic. No business page is counted as migrated.
// Later application-registration groups replace this with the actual route tree.
export default function App() {
  return (
    <main className="bootstrap-status" data-testid="bootstrap-status">
      <h1>{import.meta.env.VITE_APP_TITLE}</h1>
      <p>React 工程已启动</p>
    </main>
  )
}
