# PrimeHomes Realty — Real Estate Lead Bot

An AI-assisted real estate lead intake and qualification system that acts as a digital receptionist for customer enquiries.

**Customer journey:** enquiry → understand intent → extract requirements → ask missing questions → store lead → qualify → respond → notify sales → assign → follow up → track outcome.

## Architecture

```text
Customer → React Frontend → FastAPI → n8n (AI + workflows) → PostgreSQL → Sales Team
```

| Layer | Responsibility |
|-------|----------------|
| **React** | Customer chat, forms, sales UI |
| **FastAPI** | REST API, validation, business logic, DB boundary |
| **n8n** | Workflow orchestration, AI calls, notifications, follow-ups |
| **AI** | Intent detection, extraction, response generation |
| **PostgreSQL** | Source of truth for leads, conversations, qualifications |

Principle: *AI provides intelligence; deterministic software provides control.*

## Repository structure

```text
real-estate-lead-bot/
├── frontend/          # React (Vite) customer chat & sales views
├── backend/           # FastAPI application
├── n8n/               # n8n workflow exports & notes
├── docs/              # Approved specifications (PRD, architecture, etc.)
├── .env.example       # Environment variable template
├── AGENTS.md          # Guidance for AI/coding agents
└── README.md
```

## Quick start (local development)

### Prerequisites

- Git, Node.js (18+), Python 3.11+, PostgreSQL, n8n, ngrok (optional)

### 1. Clone

```bash
git clone https://github.com/TUNZ97/real-estate-lead-bot.git
cd real-estate-lead-bot
cp .env.example .env   # then fill in values
```

### 2. Backend

```bash
cd backend
python -m venv .venv
# Windows: .venv\Scripts\Activate.ps1
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### 3. Frontend

```bash
cd frontend
npm install
npm run dev
```

### 4. n8n

```bash
n8n
# or: npx n8n
```

### 5. PostgreSQL

Ensure PostgreSQL is running and `DATABASE_URL` in `.env` is correct.

## Documentation

All approved specifications live in [`docs/`](./docs/):

| Document | Description |
|----------|-------------|
| [PRD.md](./docs/PRD.md) | Product requirements |
| [SYSTEM_ARCHITECTURE.md](./docs/SYSTEM_ARCHITECTURE.md) | Architecture & boundaries |
| [API_SPECIFICATION.md](./docs/API_SPECIFICATION.md) | REST API contract |
| [DATABASE_DATA_MODEL_SPECIFICATION.md](./docs/DATABASE_DATA_MODEL_SPECIFICATION.md) | Data model |
| [AI_SPECIFICATION.md](./docs/AI_SPECIFICATION.md) | AI behaviour |
| [N8N_WORKFLOW_SPECIFICATION.md](./docs/N8N_WORKFLOW_SPECIFICATION.md) | Workflow inventory |
| [LEAD_QUALIFICATION_SPEC.md](./docs/LEAD_QUALIFICATION_SPEC.md) | Scoring rules |
| [UI_UX_SPECIFICATION.md](./docs/UI_UX_SPECIFICATION.md) | Frontend UX |
| [IMPLEMENTATION.md](./docs/IMPLEMENTATION.md) | Development roadmap |
| [DEVELOPMENT_SETUP.md](./docs/DEVELOPMENT_SETUP.md) | Local setup details |
| [DEPLOYMENT_SPEC.md](./docs/DEPLOYMENT_SPEC.md) | Deployment |
| [TESTING_SPEC.md](./docs/TESTING_SPEC.md) | Testing strategy |
| [TASK.md](./docs/TASK.md) | Current task / structure |

## Development phases (summary)

See [docs/IMPLEMENTATION.md](./docs/IMPLEMENTATION.md) for the full roadmap.

0. Project foundation (this scaffolding)  
1. Database & migrations  
2. FastAPI core APIs  
3. React chat UI  
4. Basic end-to-end (React → FastAPI → PostgreSQL)  
5. n8n workflows  
6. AI integration  
7. Qualification  
8. Sales notifications & assignment  
9. Follow-up  
10. Testing  
11. MVP release  

## License

Proprietary — PrimeHomes Realty.
