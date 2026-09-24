# AGENTS.md — Guidance for AI & Coding Agents

This file helps coding agents (and humans) work correctly on the PrimeHomes Realty Lead Bot.

## Project identity

- **Product:** AI-assisted real estate lead intake & qualification system
- **Company context:** PrimeHomes Realty (Nigeria-focused examples: Lekki, Ikeja, Ibadan, NGN)
- **Stack:** React (Vite) + FastAPI + n8n + AI provider + PostgreSQL
- **Principle:** AI provides intelligence; deterministic software provides control.

## Source of truth

1. Approved specifications in `docs/` — especially PRD, SYSTEM_ARCHITECTURE, API, DATABASE, AI, LEAD_QUALIFICATION, N8N, UI_UX, IMPLEMENTATION.
2. This file and the root `README.md`.
3. Code that has already been merged and tested.

When in doubt, follow the docs over assumptions.

## Architecture boundaries (do not violate)

- React must **never** access PostgreSQL or hold secrets (DB credentials, AI keys, JWT secrets).
- FastAPI owns: validation, auth boundary, application services, repository/DB access, custom business logic.
- n8n owns: workflow orchestration, AI workflow execution, notifications, scheduled follow-ups, routing.
- AI output is **untrusted** until validated. Never let LLM output bypass DB constraints or set final lead status.
- Do **not** put all domain logic into n8n code nodes.
- Do **not** introduce microservices, Kubernetes, multiple AI agents, or complex CRM integrations for the MVP.

## Layering (backend)

```text
API → Service → Repository → Database
```

Keep these layers distinct.

## Current phase focus

See `docs/IMPLEMENTATION.md` and `docs/TASK.md`.

Build the **smallest useful vertical slice**, verify it, then expand.

Recommended sequence:

```text
Repository → React scaffold → FastAPI scaffold → Database → Basic API → Basic chat
→ n8n → AI → Qualification → Sales → Follow-up → Testing → Release
```

## Coding conventions

### General

- Prefer clarity over cleverness.
- Use UTC timestamps.
- Validate all external input.
- Return stable error codes (see API_SPECIFICATION).
- Use request IDs and idempotency keys where appropriate.
- Do not log unnecessary PII.

### Backend (FastAPI)

- Python 3.11+
- Type hints and Pydantic schemas for request/response.
- SQLAlchemy (or equivalent) models + Alembic migrations.
- Tests for validation, services, status transitions, and errors.

### Frontend (React)

- Vite + React + TypeScript preferred.
- Components under `src/components/`, pages under `src/pages/`.
- API client in `src/services/api/`.
- Clear loading / error / retry states for chat.
- Mobile-first chat UI.

### n8n

- Export workflows as JSON into `n8n/workflows/` when possible.
- Protect internal webhooks; no hardcoded secrets.
- Retry only transient failures.

## What not to build yet

- Predictive lead scoring / recommendation engines
- Multiple AI agents
- Microservices or Kubernetes
- Large analytics dashboards
- Complex enterprise identity systems
- Advanced real-time collaboration

## File placement

| Content | Location |
|---------|----------|
| Specs & docs | `docs/` |
| Frontend app | `frontend/` |
| FastAPI app | `backend/` |
| n8n workflows | `n8n/` |
| Secrets template | `.env.example` (root) |
| Agent guidance | `AGENTS.md` |

## When adding features

1. Check the relevant spec in `docs/`.
2. Prefer extending existing modules over new top-level packages.
3. Keep public customer endpoints and internal/sales endpoints clearly separated.
4. Add or update tests when practical.
5. Update `docs/TASK.md` or implementation notes if the roadmap changes.

## Success definition (MVP)

A customer can send an enquiry and the system can: receive it → understand it → extract data → store it → qualify it → respond → notify sales → support follow-up.
