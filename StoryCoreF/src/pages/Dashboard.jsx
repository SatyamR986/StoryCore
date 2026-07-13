import React from 'react'

export default function Dashboard() {
  return (
    <main style={{padding: '2rem'}}>
        <button onClick={() => window.location.href = '/play'}>Play</button>
        <button onClick={() => window.location.href = '/create'}>Create</button>
    </main>
  )
}
