# Integration setup — Frontend + Backend + n8n

Follow these steps on your machine to run the full chat path.

**Stack:** npm (React + n8n) + Python (FastAPI) + MySQL on your PC (no Docker for development).

## Architecture in practice

```text
Browser (React :5173)
    → POST /api/v1/chat  (Vite proxy → FastAPI :8000)
        → POST N8N_WEBHOOK_URL  (n8n WF-001)
            ← { conversation_id, lead_id, response, processing_status }
        ← same shape wrapped as { data, meta }
    ← bot message bubble
```

## 1. Pull latest code

```bash
cd real-estate-lead-bot
git pull origin main
cp .env.example .env
```

## 2. Configure `.env`

At minimum set:

```text
DATABASE_URL=mysql+pymysql://root:YOUR_MYSQL_PASSWORD@localhost:3306/primehomes_lead_bot
N8N_WEBHOOK_URL=http://localhost:5678/webhook/customer-message
CORS_ORIGINS=http://localhost:5173
VITE_API_BASE_URL=/api/v1
APP_ENV=development
DEBUG=true
```

Use the **exact** production webhook URL from your active n8n workflow.

Create the MySQL database once (if it does not exist):

```sql
CREATE DATABASE IF NOT EXISTS primehomes_lead_bot
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

> Chat + n8n work **without** tables for now. MySQL is ready for Phase 1 migrations.

## 3. Start n8n + activate WF-001

1. Start n8n: `npx n8n`
2. Open the customer-message workflow.
3. Webhook path should match the URL above (e.g. `customer-message`).
4. **Respond to Webhook** must return JSON with a `response` string (see `n8n/workflows/WF-001-customer-message.README.md`).
5. **Activate** the workflow (toggle ON).

### Minimal response example

```json
{
  "conversation_id": "test-1",
  "lead_id": null,
  "response": "Thanks! What location and budget are you considering?",
  "processing_status": "SUCCESS"
}
```

## 4. Start backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Check: http://localhost:8000/health → `{"status":"ok",...}`  
Docs: http://localhost:8000/docs

### Quick API test (optional)

```bash
curl -s http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d "{\"message\":\"I need a 3-bed in Lekki under 80 million\"}"
```

- If n8n is active → you get the workflow’s `response`.
- If n8n is down → in development you still get a **fallback** message so the UI keeps working.

## 5. Start frontend

```bash
cd frontend
npm install
npm run dev
```

Open: http://localhost:5173

You should see the orange/yellow PrimeHomes chat UI. Send a message; the reply should come from n8n (or the fallback if n8n is offline).

## 6. Verify end-to-end

1. Type: `Hi, I'm looking for a 3-bedroom apartment around Lekki. Budget around N80 million.`
2. Click **Send**.
3. Loading dots appear, then a bot bubble with the n8n `response` text.
4. In n8n, confirm the webhook execution ran.

## Troubleshooting

| Issue | Fix |
|-------|-----|
| Chat always shows fallback | Workflow inactive, wrong `N8N_WEBHOOK_URL`, or using Test URL without listening |
| CORS error in browser | Ensure FastAPI is running and `CORS_ORIGINS` includes `http://localhost:5173` |
| Network error on send | Backend not running, or `VITE_API_BASE_URL` wrong |
| `response` missing | n8n Respond node must include JSON field `response` |
| MySQL connection (later phases) | Service running? Password correct? DB created? Port 3306? |
| Port 5678 vs production URL | After activating workflow, copy the **Production** webhook URL into `.env` |

## What’s already implemented in code

- **Frontend:** modern orange/yellow chat, API client, conversation id, loading/error/retry
- **Backend:** validation, n8n client, chat service, standard error format, CORS, PyMySQL driver
- **Docs:** this guide + `n8n/workflows/WF-001-customer-message.README.md`

## Not required yet for this chat test

- MySQL tables / migrations (Phase 1)
- Full AI extraction inside n8n (you can add AI nodes next)
- Sales UI
