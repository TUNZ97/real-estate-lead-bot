import { BrowserRouter, Routes, Route } from 'react-router-dom'
import ChatPage from './pages/Chat/ChatPage'

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<ChatPage />} />
        {/* Future: /leads for sales view */}
      </Routes>
    </BrowserRouter>
  )
}

export default App
