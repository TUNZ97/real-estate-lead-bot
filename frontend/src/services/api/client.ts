const API_BASE =
  import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:8000/api/v1'

export interface ChatRequest {
  message: string
  conversation_id?: string
  customer_id?: string
  idempotency_key?: string
}

export interface ChatResponse {
  data: {
    conversation_id: string
    lead_id?: string
    response: string
    processing_status: string
  }
  meta?: Record<string, unknown>
}

export interface ApiError {
  error: {
    code: string
    message: string
    details?: unknown[]
    request_id?: string
  }
}

function requestId(): string {
  return crypto.randomUUID()
}

export async function sendChatMessage(
  payload: ChatRequest,
): Promise<ChatResponse> {
  const res = await fetch(`${API_BASE}/chat`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-Request-ID': requestId(),
      ...(payload.idempotency_key
        ? { 'Idempotency-Key': payload.idempotency_key }
        : {}),
    },
    body: JSON.stringify({
      message: payload.message,
      conversation_id: payload.conversation_id,
      customer_id: payload.customer_id,
    }),
  })

  const body = await res.json()

  if (!res.ok) {
    const err = body as ApiError
    throw new Error(err?.error?.message ?? `Request failed (${res.status})`)
  }

  return body as ChatResponse
}
