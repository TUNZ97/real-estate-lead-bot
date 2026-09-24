import MessageList from '../Message/MessageList'
import MessageInput from '../Input/MessageInput'
import Loading from '../Loading/Loading'
import type { Message, ChatStatus } from '../../types/chat'
import './Chat.css'

interface ChatProps {
  messages: Message[]
  status: ChatStatus
  errorMessage?: string | null
  onSend: (text: string) => void
  onRetry?: () => void
}

export default function Chat({
  messages,
  status,
  errorMessage,
  onSend,
  onRetry,
}: ChatProps) {
  return (
    <div className="chat">
      <header className="chat__header">
        <h1>PrimeHomes Realty</h1>
        <p className="chat__subtitle">Your digital property assistant</p>
      </header>

      <div className="chat__body">
        <MessageList messages={messages} />
        {(status === 'sending' || status === 'receiving') && (
          <Loading label="Thinking…" />
        )}
        {status === 'error' && (
          <div className="chat__error" role="alert">
            {errorMessage || 'Message could not be sent.'}{' '}
            {onRetry && (
              <button type="button" onClick={onRetry}>
                Try again
              </button>
            )}
          </div>
        )}
      </div>

      <MessageInput
        disabled={status === 'sending' || status === 'receiving'}
        onSend={onSend}
      />
    </div>
  )
}
