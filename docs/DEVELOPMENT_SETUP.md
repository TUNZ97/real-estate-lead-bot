# Development Setup

Local development uses **npm** (frontend + n8n), **Python/FastAPI** (backend), and **MySQL on your PC**. Docker is **not** required for day-to-day development.

## Prerequisites

Install:

- Git
- Node.js (18+) / npm
- Python 3.11+
- **MySQL** (already installed on your machine)
- n8n (via npm: `npx n8n` or global install)
- ngrok (only when external webhooks are needed)

## Repository

```bash
git clone https://github.com/TUNZ97/real-estate-lead-bot.git
cd real-estate-lead-bot
cp .env.example .env
```

Edit `.env` and set your real MySQL password and n8n webhook URL.

## MySQL (local — no Docker)

1. Start the MySQL service on your PC (Windows Services, or MySQL Workbench, or `mysql.server start` on macOS).

2. Create the database (once):

```sql
CREATE DATABASE IF NOT EXISTS primehomes_lead_bot
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
```

You can run that in MySQL Workbench, phpMyAdmin, or the CLI:

```bash
mysql -u root -p -e "CREATE DATABASE IF NOT EXISTS primehomes_lead_bot CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
```

3. Set `DATABASE_URL` in `.env`:

```text
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/primehomes_lead_bot
```

Replace `root` / `YOUR_PASSWORD` if you use another user.

> Tables/migrations are Phase 1. Chat + n8n work **without** tables for now.

## Frontend (npm)

```bash
cd frontend
npm install
npm run dev
```

App: http://localhost:5173

## Backend (Python)

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
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- Health: http://localhost:8000/health
- API docs: http://localhost:8000/docs

## n8n (npm)

```bash
npx n8n
# or, if installed globally: n8n
```

UI: http://localhost:5678

## ngrok (optional)

```bash
ngrok http 5678
```

Do not hardcode a temporary ngrok hostname into source code.

## Environment variables

Keep secrets in `.env` at the repo root. See `.env.example`.

Important keys:

```text
DATABASE_URL          # mysql+pymysql://...
N8N_WEBHOOK_URL
CORS_ORIGINS
VITE_API_BASE_URL     # prefer /api/v1 with Vite proxy
```

## Local workflow (order)

1. MySQL running on your PC
2. n8n (`npx n8n`) — activate WF-001 webhook
3. FastAPI (`uvicorn ...`)
4. React (`npm run dev`)
5. ngrok only when required

## Troubleshooting

### MySQL connection fails

- Is the MySQL service running?
- Is the password in `DATABASE_URL` correct? (URL-encode special characters, e.g. `@` → `%40`)
- Does the database `primehomes_lead_bot` exist?
- Default port is `3306`

### CORS

Verify `CORS_ORIGINS` includes `http://localhost:5173`.

### n8n webhook unavailable

Check n8n is running, workflow is **Active**, and `N8N_WEBHOOK_URL` matches the **Production** webhook URL.

### AI request fails

Check provider credentials, model, payload, and rate limits inside n8n.
