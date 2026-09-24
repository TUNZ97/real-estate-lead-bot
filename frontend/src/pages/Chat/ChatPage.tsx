import { useState, useRef, useEffect } from 'react'
import Chat from '../../components/Chat/Chat'
import type { Message, ChatStatus } from '../../types/chat'
import { sendChatMessage } from '../../services/api/client'

const WELCOME: Message = {
  id: 'welcome',
  sender: 'bot',
  content:
    "Hello! Welcome to PrimeHomes Realty. Looking for a home, land, or rental? Tell me what you need — location, budget, or bedrooms — and I'll help get you started.",
  createdAt: new Date().toISOString(),
}

const CONVERSATION_KEY = 'ph_conversation_id'

export default function ChatPage() {
  const [messages, setMessages] = useState<Message[]>([WELCOME])
  const [status, setStatus] = useState<ChatStatus>('idle')
  const [errorMessage, setErrorMessage] = useState<string | null>(null)
  const conversationIdRef = useRef<string | null>(
    typeof window !== 'undefined'
      ? sessionStorage.getItem(CONVERSATION_KEY)
      : null,
  )
  const lastFailedText = useRef<string | null>(null)

  useEffect(() => {
    // ensure scroll container can be used by Chat if needed later
  }, [messages])

  async function handleSend(text: string) {
    const userMsg: Message = {
      id: crypto.randomUUID(),
      sender: 'customer',
      content: text,
      createdAt: new Date().toISOString(),
    }
    setMessages((prev) => [...prev, userMsg])
    setStatus('sending')
    setErrorMessage(null)
    lastFailedText.current = text

    try {
      const data = await sendChatMessage({
        message: text,
        conversation_id: conversationIdRef.current ?? undefined,
        idempotency_key: crypto.randomUUID(),
      })

      if (data.data.conversation_id) {
        conversationIdRef.current = data.data.conversation_id
        sessionStorage.setItem(CONVERSATION_KEY, data.data.conversation_id)
      }

      const botMsg: Message = {
        id: crypto.randomUUID(),
        sender: 'bot',
        content: data.data.response,
        createdAt: new Date().toISOString(),
      }
      setMessages((prev) => [...prev, botMsg])
      setStatus('idle')
      lastFailedText.current = null
    } catch (err) {
      const msg =
        err instanceof Error ? err.message : 'Message could not be sent.'
      setErrorMessage(msg)
      setStatus('error')
    }
  }

  function handleRetry() {
    setStatus('idle')
    setErrorMessage(null)
    const text = lastFailedText.current
    if (text) {
      void handleSend(text)
    }
  }

  return (
    <Chat
      messages={messages}
      status={status}
      errorMessage={errorMessage}
      onSend={handleSend}
      onRetry={handleRetry}
    />
  )
}
