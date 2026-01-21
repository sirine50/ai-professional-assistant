import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

import Chat from "./pages/Chat"

function App() {
  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <Chat />
    </div>
  )
}

export default App

