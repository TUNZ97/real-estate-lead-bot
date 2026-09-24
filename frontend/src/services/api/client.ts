const API_BASE =
  import.meta.env.VITE_API_BASE_URL ?? '/api/v1'

export interface ChatRequest {
  message: string
  conversation_id?: string
  customer_id?: string
  idempotency_key?: string
}

export interface ChatResponse {
  data: {
    conversation_id: string
    lead_id?: string | null
    response: string
    processing_status: string
  }
  meta?: Record<string, unknown>
}

export interface ApiErrorBody {
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

  let body: unknown
  try {
    body = await res.json()
  } catch {
    throw new Error(`Request failed (${res.status})`)
  }

  if (!res.ok) {
    const err = body as ApiErrorBody
    throw new Error(
      err?.error?.message ?? `Request failed (${res.status})`,
    )
  }

  return body as ChatResponse
}
