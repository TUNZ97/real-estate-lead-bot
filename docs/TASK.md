# Current Task — PrimeHomes Realty Lead Bot

## TASK-001 — Create Repository & Base Structure

**Status:** DONE

## TASK-002 — Frontend chat UI (React)

**Status:** DONE

- [x] Chat layout (mobile-first, modern orange/yellow palette)
- [x] Message list + bubbles
- [x] Input + Send
- [x] Loading / error / retry states
- [x] API client → `POST /api/v1/chat`
- [x] Conversation ID kept in sessionStorage

## TASK-003 — Backend chat API + n8n bridge

**Status:** DONE

- [x] FastAPI app with CORS + standard error handlers
- [x] `GET /health` and `GET /api/v1/health`
- [x] `POST /api/v1/chat` (validate → call n8n → return response)
- [x] n8n HTTP client (`app/services/n8n_client.py`)
- [x] Chat service with **development fallback** if n8n is offline
- [x] Request ID + Idempotency-Key headers supported

## TASK-004 — Wire to your n8n workflow (on your machine)

**Status:** READY FOR YOU

1. Ensure WF-001 webhook path matches `N8N_WEBHOOK_URL` in `.env`
2. Activate the workflow (use **Production** webhook URL)
3. Response JSON must include `response` (see `n8n/workflows/WF-001-customer-message.README.md`)
4. Run backend + frontend and send a test enquiry from the chat UI

## Next engineering tasks

| ID | Task | Phase |
|----|------|-------|
| TASK-005 | PostgreSQL models + Alembic migrations | 1 |
| TASK-006 | Persist customers / leads / messages via FastAPI or n8n | 1–2 |
| TASK-007 | Full WF-001 AI + qualification | 5–7 |
| TASK-008 | Sales notification workflow | 8 |

## How the pieces connect

```text
React chat  →  POST /api/v1/chat (FastAPI)  →  n8n webhook (WF-001)  →  JSON response  →  chat bubble
```
