import './App.css'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Dashboard from './pages/Dashboard'
import PlayHome from './pages/PlayHome'
import CreateHome from './pages/CreateHome'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/play" element={<PlayHome />} />
        <Route path="/create" element={<CreateHome />} />
      </Routes>
    </BrowserRouter>
  )
}

export default App
