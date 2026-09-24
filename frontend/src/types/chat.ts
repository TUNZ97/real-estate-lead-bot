export type SenderType = 'customer' | 'bot' | 'system'

export interface Message {
  id: string
  sender: SenderType
  content: string
  createdAt: string
}

export type ChatStatus = 'idle' | 'sending' | 'receiving' | 'error' | 'retrying'
