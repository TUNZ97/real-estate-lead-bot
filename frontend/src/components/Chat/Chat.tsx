import MessageList from '../Message/MessageList'
import MessageInput from '../Input/MessageInput'
import Loading from '../Loading/Loading'
import type { Message, ChatStatus } from '../../types/chat'
import './Chat.css'

interface ChatProps {
  messages: Message[]
  status: ChatStatus
  onSend: (text: string) => void
  onRetry?: () => void
}

export default function Chat({ messages, status, onSend, onRetry }: ChatProps) {
  return (
    <div className="chat">
      <header className="chat__header">
        <h1>PrimeHomes Realty</h1>
        <p className="chat__subtitle">Digital receptionist</p>
      </header>

      <div className="chat__body">
        <MessageList messages={messages} />
        {status === 'sending' && <Loading label="Sending…" />}
        {status === 'error' && (
          <div className="chat__error" role="alert">
            Message could not be sent.{' '}
            {onRetry && (
              <button type="button" onClick={onRetry}>
                Try again
              </button>
            )}
          </div>
        )}
      </div>

      <MessageInput
        disabled={status === 'sending'}
        onSend={onSend}
      />
    </div>
  )
}
