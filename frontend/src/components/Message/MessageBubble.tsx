import type { Message } from '../../types/chat'
import './Message.css'

interface MessageBubbleProps {
  message: Message
}

export default function MessageBubble({ message }: MessageBubbleProps) {
  const isCustomer = message.sender === 'customer'

  return (
    <div
      className={`message ${isCustomer ? 'message--customer' : 'message--bot'}`}
    >
      <div className="message__bubble">{message.content}</div>
    </div>
  )
}
