# Backend — PrimeHomes Lead Bot

FastAPI application. Layering: **API → Service → Repository → Database**.

## Structure

```text
app/
├── main.py              # FastAPI entry
├── core/
│   └── config.py        # Settings from env
├── api/
│   └── v1/
│       ├── router.py
│       └── endpoints/   # Route handlers
├── schemas/             # Pydantic request/response models
├── services/            # Business logic
├── repositories/        # Data access
├── models/              # SQLAlchemy ORM (Phase 1)
└── db/                  # Engine & sessions (Phase 1)
```

## Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt

# From repo root, ensure .env exists (copy from .env.example)
uvicorn app.main:app --reload --app-dir .
```

Or from `backend/`:

```bash
uvicorn app.main:app --reload
```

- Health: http://localhost:8000/health  
- API docs: http://localhost:8000/docs  
- Chat (placeholder): `POST /api/v1/chat`

## Rules

- Validate all input.
- AI output is untrusted until validated.
- Do not put secrets in code; use environment variables.
- Keep public customer endpoints and internal/sales endpoints separate.
