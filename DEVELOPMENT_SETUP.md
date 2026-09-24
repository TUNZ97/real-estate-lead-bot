# Development Setup

## Prerequisites

Install:

- Git
- Node.js
- Python
- PostgreSQL
- n8n
- ngrok

## Repository

```bash
git clone <repository-url>
cd primehomes-lead-bot
```

## Frontend

```bash
cd frontend
npm install
npm run dev
```

## Backend

Create and activate a virtual environment, then install dependencies.

Example:

```bash
cd backend
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install project dependencies from the backend requirements file.

Start FastAPI with the project's configured command, commonly:

```bash
uvicorn app.main:app --reload
```

## n8n

The project uses npm-based local n8n development.

Example:

```bash
n8n
```

## ngrok

When FastAPI/n8n needs to be reachable externally during local development:

```bash
ngrok http 5678
```

Do not hardcode a temporary ngrok hostname into source code.

## Environment variables

Keep secrets in `.env`.

Provide `.env.example` with names only.

Typical configuration categories:

```text
DATABASE_URL
API_BASE_URL
N8N_BASE_URL
N8N_WEBHOOK_URL
AI_API_KEY
JWT_SECRET
```

Use placeholder values in `.env.example`.

## Local workflow

Run:

1. PostgreSQL
2. FastAPI
3. React
4. n8n
5. ngrok only when required

## Troubleshooting

### CORS

Verify frontend origin is allowed by FastAPI.

### n8n webhook unavailable

Check n8n is running and the webhook URL is correct.

### AI request fails

Check provider credentials, model configuration, request payload, and rate limits.

### Database connection fails

Check PostgreSQL is running and `DATABASE_URL` is correct.
