import { useState } from 'react'
import Chat from '../../components/Chat/Chat'
import type { Message } from '../../types/chat'

const WELCOME: Message = {
  id: 'welcome',
  sender: 'bot',
  content: 'Hello! Welcome to PrimeHomes Realty. How can we help you today?',
  createdAt: new Date().toISOString(),
}

export default function ChatPage() {
  const [messages, setMessages] = useState<Message[]>([WELCOME])
  const [status, setStatus] = useState<'idle' | 'sending' | 'error'>('idle')

  async function handleSend(text: string) {
    const userMsg: Message = {
      id: crypto.randomUUID(),
      sender: 'customer',
      content: text,
      createdAt: new Date().toISOString(),
    }
    setMessages((prev) => [...prev, userMsg])
    setStatus('sending')

    // Placeholder: wire to FastAPI POST /api/v1/chat in Phase 3/4
    try {
      // const data = await sendChatMessage(text)
      await new Promise((r) => setTimeout(r, 600))
      const botMsg: Message = {
        id: crypto.randomUUID(),
        sender: 'bot',
        content:
          'Thanks for your message. Our system is being set up — a real response will appear here soon.',
        createdAt: new Date().toISOString(),
      }
      setMessages((prev) => [...prev, botMsg])
      setStatus('idle')
    } catch {
      setStatus('error')
    }
  }

  return (
    <Chat
      messages={messages}
      status={status}
      onSend={handleSend}
      onRetry={() => setStatus('idle')}
    />
  )
}
