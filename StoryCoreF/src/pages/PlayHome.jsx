import React, { useEffect, useState } from 'react'

export default function PlayHome() {
  const [stories, setStories] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    let mounted = true

    async function fetchStories() {
      try {
        const res = await fetch('http://127.0.0.1:8000/api/v1/stories/')
        if (!mounted) return

        if (!res.ok) {
          setError(`HTTP ${res.status} ${res.statusText}`)
          return
        }

        const contentType = res.headers.get('content-type') || ''
        if (contentType.includes('application/json')) {
          const json = await res.json()
          setStories(json)
        } else {
          // No JSON body
          setStories(null)
        }
      } catch (err) {
        setError(err.message)
      } finally {
        setLoading(false)
      }
    }

    fetchStories()
    return () => {
      mounted = false
    }
  }, [])

  return (
    <main style={{ padding: '2rem' }}>
      <h1>Play Home</h1>

      {loading && <p>Loading stories…</p>}
      {error && (
        <p style={{ color: 'crimson' }}>Error fetching stories: {error}</p>
      )}

      {!loading && !error && (
        <section>
          {stories === null ? (
            <p>No JSON response body from the API.</p>
          ) : Array.isArray(stories) ? (
            <ul>
              {stories.map((s, i) => (
                <li key={s.id ?? i}>{s.title ?? JSON.stringify(s)}</li>
              ))}
            </ul>
          ) : (
            <pre style={{ whiteSpace: 'pre-wrap' }}>{JSON.stringify(stories, null, 2)}</pre>
          )}
        </section>
      )}
    </main>
  )
}