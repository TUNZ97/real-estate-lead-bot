# Frontend — PrimeHomes Lead Bot

React (Vite + TypeScript) customer chat and future sales views.

## Structure

```text
src/
├── components/
│   ├── Chat/
│   ├── Message/
│   ├── Input/
│   └── Loading/
├── pages/
│   ├── Chat/
│   └── Leads/          # future
├── services/
│   └── api/
├── hooks/              # future
├── types/
└── utils/              # future
```

## Setup

```bash
npm install
npm run dev
```

App runs at http://localhost:5173

Set `VITE_API_BASE_URL` in the root `.env` (or frontend `.env`) to point at FastAPI.

## Rules

- Never put database credentials or AI provider keys in the frontend.
- All data access goes through FastAPI.
- Prefer clear loading and error states for every network action.
