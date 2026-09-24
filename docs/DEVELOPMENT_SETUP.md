# Development Setup

## Prerequisites

Install:

- Git
- Node.js (18+)
- Python 3.11+
- Docker (optional, for PostgreSQL via docker-compose)
- PostgreSQL (or use Docker)
- n8n
- ngrok (only when external webhooks are needed)

## Repository

```bash
git clone https://github.com/TUNZ97/real-estate-lead-bot.git
cd real-estate-lead-bot
cp .env.example .env
```

## PostgreSQL (Docker — recommended for local)

```bash
docker compose up -d
```

This starts PostgreSQL on port `5432` with credentials matching `.env.example`:

- user: `primehomes`
- password: `primehomes`
- database: `primehomes_lead_bot`

Stop with: `docker compose down`

## Frontend

```bash
cd frontend
npm install
npm run dev
```

App: http://localhost:5173

## Backend

Create and activate a virtual environment, then install dependencies.

```bash
cd backend
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Linux / macOS:

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

- Health: http://localhost:8000/health
- API docs: http://localhost:8000/docs

## n8n

```bash
n8n
# or: npx n8n
```

UI: http://localhost:5678

## ngrok

When FastAPI/n8n needs to be reachable externally during local development:

```bash
ngrok http 5678
```

Do not hardcode a temporary ngrok hostname into source code.

## Environment variables

Keep secrets in `.env` at the repo root.

`.env.example` lists names and safe placeholders only.

Typical categories:

```text
DATABASE_URL
API_BASE_URL
N8N_BASE_URL
N8N_WEBHOOK_URL
AI_API_KEY
JWT_SECRET
```

## Local workflow

Run in this order:

1. PostgreSQL (`docker compose up -d`)
2. FastAPI (`uvicorn app.main:app --reload` from `backend/`)
3. React (`npm run dev` from `frontend/`)
4. n8n
5. ngrok only when required

## Troubleshooting

### CORS

Verify frontend origin is allowed by FastAPI (`CORS_ORIGINS` in `.env`).

### n8n webhook unavailable

Check n8n is running and `N8N_WEBHOOK_URL` is correct.

### AI request fails

Check provider credentials, model configuration, request payload, and rate limits.

### Database connection fails

Check PostgreSQL is running (`docker compose ps`) and `DATABASE_URL` matches.
