import { useState, FormEvent, KeyboardEvent } from 'react'
import './MessageInput.css'

interface MessageInputProps {
  disabled?: boolean
  onSend: (text: string) => void
}

export default function MessageInput({ disabled, onSend }: MessageInputProps) {
  const [value, setValue] = useState('')

  function submit() {
    const text = value.trim()
    if (!text || disabled) return
    onSend(text)
    setValue('')
  }

  function handleSubmit(e: FormEvent) {
    e.preventDefault()
    submit()
  }

  function handleKeyDown(e: KeyboardEvent<HTMLTextAreaElement>) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      submit()
    }
  }

  return (
    <form className="message-input" onSubmit={handleSubmit}>
      <label htmlFor="chat-input" className="sr-only">
        Type your message
      </label>
      <textarea
        id="chat-input"
        rows={1}
        placeholder="Type your message…"
        value={value}
        disabled={disabled}
        onChange={(e) => setValue(e.target.value)}
        onKeyDown={handleKeyDown}
        aria-label="Type your message"
      />
      <button type="submit" disabled={disabled || !value.trim()}>
        Send
      </button>
    </form>
  )
}
