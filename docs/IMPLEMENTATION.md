# Implementation & Development Roadmap

## Development philosophy

Build the smallest useful vertical slice, verify it, then expand.

Local stack: **npm** (React + n8n) + **Python/FastAPI** + **MySQL on your PC**. No Docker required for development.

## Phase 0 — Project Foundation

- repository
- React
- FastAPI
- environment configuration
- local tooling

## Phase 1 — Database

- **MySQL** (local)
- migrations (Alembic + PyMySQL)
- customer
- lead
- property requirement
- conversation/message
- qualification
- sales/follow-up tables

## Phase 2 — FastAPI

- health endpoint
- customer API
- lead API
- conversation API
- message API
- requirement API
- status transitions

## Phase 3 — React

- chat layout
- message components
- API client
- loading/error handling

## Phase 4 — Basic end-to-end

Get:

```text
React → FastAPI → MySQL → React
```

working before introducing AI complexity.

## Phase 5 — n8n

- webhook
- WF-001
- validation
- error handling

## Phase 6 — AI

- intent
- extraction
- missing information
- response generation

## Phase 7 — Qualification

- deterministic score
- level
- recalculation

## Phase 8 — Sales

- notification
- assignment

## Phase 9 — Follow-up

- follow-up records
- reminders
- lead status

## Phase 10 — Testing

- automated tests
- end-to-end tests
- AI evaluation
- smoke tests

## Phase 11 — MVP release

- production configuration
- migration
- workflow configuration
- smoke test

## Recommended coding sequence

```text
Repository
→ React
→ FastAPI
→ Database (MySQL)
→ Basic API
→ Basic chat
→ n8n
→ AI
→ Qualification
→ Sales
→ Follow-up
→ Testing
→ Release
```

## Do not build yet

- predictive lead scoring
- complex recommendation engine
- multiple agents
- microservices
- Kubernetes
- large analytics dashboard
- unnecessary abstractions
