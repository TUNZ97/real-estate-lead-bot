# System Architecture Document

## PrimeHomes Realty — Real Estate Lead Bot

## 1. Architecture principle

> AI provides intelligence; deterministic software provides control.

## 2. High-level architecture

```text
Customer
   ↓
React Frontend
   ↓
FastAPI
   ↓
n8n
   ├── AI Processing
   ├── Lead Qualification
   ├── Notifications
   └── Follow-up Automation
   ↓
PostgreSQL
   ↓
Sales Team
```

## 3. Component responsibilities

### React

Owns:

- customer chat
- forms
- loading/error states
- customer-facing interactions
- sales UI when implemented

React must not access PostgreSQL directly.

### FastAPI

Owns:

- REST API
- request validation
- authentication/authorization boundary
- application services
- database boundary
- custom business logic
- API error handling

Suggested layering:

```text
API → Service → Repository → Database
```

### n8n

Owns:

- workflow orchestration
- AI workflow execution
- notifications
- integrations
- scheduled follow-ups
- lead routing

n8n is not the entire backend.

### AI

Owns:

- intent detection
- structured extraction
- missing-information detection
- natural-language response generation
- conversation summaries

AI output is untrusted until validated.

### PostgreSQL

Production source of truth for:

- customers
- leads
- requirements
- conversations
- messages
- qualification
- assignments
- follow-ups
- notifications
- history/audit records

## 4. Lead lifecycle

```text
NEW
 ↓
QUALIFYING
 ↓
QUALIFIED
 ↓
CONTACTED
 ↓
FOLLOW_UP
 ↓
CONVERTED
```

Alternative outcomes:

- DISQUALIFIED
- UNRESPONSIVE
- LOST

## 5. Core message flow

1. Customer sends message.
2. React sends request to FastAPI.
3. FastAPI validates request.
4. FastAPI sends workflow request to n8n.
5. n8n loads relevant conversation context.
6. AI extracts structured information.
7. Structured output is validated.
8. Customer/lead/requirement/message data is persisted.
9. Qualification is calculated.
10. Response is generated.
11. Response is returned to customer.
12. Relevant sales notifications are sent.

## 6. Security principles

- HTTPS in deployed environments.
- Secrets in environment variables.
- Validate external input.
- Protect internal endpoints.
- Restrict database access.
- Avoid logging unnecessary PII.
- Rate-limit public endpoints where appropriate.

## 7. Reliability

Use:

- request IDs
- idempotency keys
- retryable workflow steps
- explicit failure handling
- consistent API errors
- database constraints

## 8. Observability

Track:

- request ID
- workflow execution ID
- lead ID
- AI processing failures
- API errors
- notification failures
- follow-up failures

## 9. Architecture boundaries

Do not:

- put database credentials in React
- let AI directly control lead status
- put all domain logic into n8n code nodes
- duplicate business rules across frontend/backend/n8n
- introduce microservices for the MVP
