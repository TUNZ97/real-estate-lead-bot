# PrimeHomes Realty — Real Estate Lead Bot

An AI-assisted real estate lead intake and qualification system that acts as a digital receptionist for customer enquiries.

**Customer journey:** enquiry → understand intent → extract requirements → ask missing questions → store lead → qualify → respond → notify sales → assign → follow up → track outcome.

## Architecture

```text
Customer → React Frontend → FastAPI → n8n (AI + workflows) → MySQL → Sales Team
```

| Layer | Responsibility |
|-------|----------------|
| **React** | Customer chat, forms, sales UI |
| **FastAPI** | REST API, validation, business logic, DB boundary |
| **n8n** | Workflow orchestration, AI calls, notifications, follow-ups |
| **AI** | Intent detection, extraction, response generation |
| **MySQL** | Source of truth for leads, conversations, qualifications |

Principle: *AI provides intelligence; deterministic software provides control.*

**Local development stack:** npm (frontend + n8n) + Python (FastAPI) + **MySQL on your PC**. Docker is optional and reserved for later deployment work.

## Repository structure

```text
real-estate-lead-bot/
├── frontend/              # React (Vite + TypeScript)
├── backend/               # FastAPI + Alembic
├── n8n/                   # Workflow notes / exports
├── docs/                  # Approved specifications
├── .env.example
├── .gitignore
├── AGENTS.md
└── README.md
```

## Quick start (local development)

### Prerequisites

- Git, Node.js (18+) / npm, Python 3.11+, **MySQL** on your PC, n8n via npm

### 1. Clone & configure

```bash
git clone https://github.com/TUNZ97/real-estate-lead-bot.git
cd real-estate-lead-bot
cp .env.example .env
```

Edit `.env` — set your MySQL password and n8n webhook URL:

```text
DATABASE_URL=mysql+pymysql://root:YOUR_PASSWORD@localhost:3306/primehomes_lead_bot
N8N_WEBHOOK_URL=http://localhost:5678/webhook/customer-message
```

### 2. MySQL (on your PC)

Create the database once:

```sql
CREATE DATABASE IF NOT EXISTS primehomes_lead_bot
  CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 3. Backend

```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

- Health: http://localhost:8000/health
- Docs: http://localhost:8000/docs

### 4. Frontend

```bash
cd frontend
npm install
npm run dev
```

App: http://localhost:5173

### 5. n8n

```bash
npx n8n
```

See [docs/INTEGRATION_SETUP.md](./docs/INTEGRATION_SETUP.md) and [docs/DEVELOPMENT_SETUP.md](./docs/DEVELOPMENT_SETUP.md).

## Documentation

All approved specifications live in [`docs/`](./docs/).

## Development phases (summary)

0. **Project foundation** (complete)  
1. Database & migrations (MySQL)  
2. FastAPI core APIs  
3. React chat UI  
4. Basic end-to-end (React → FastAPI → MySQL)  
5. n8n workflows  
6. AI integration  
7. Qualification  
8. Sales notifications & assignment  
9. Follow-up  
10. Testing  
11. MVP release  

## License

Proprietary — PrimeHomes Realty.
