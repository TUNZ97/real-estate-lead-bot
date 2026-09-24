# API Specification

## Base

```text
/api/v1
```

JSON is the default representation.

## Headers

- `X-Request-ID`
- `Idempotency-Key` where applicable
- `Authorization: Bearer <token>` for protected endpoints

## Standard success

```json
{
  "data": {},
  "meta": {}
}
```

## Standard error

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid request.",
    "details": [],
    "request_id": "..."
  }
}
```

## Important error codes

- VALIDATION_ERROR
- AUTHENTICATION_REQUIRED
- INVALID_TOKEN
- FORBIDDEN
- NOT_FOUND
- CONFLICT
- DUPLICATE_RESOURCE
- INVALID_STATUS_TRANSITION
- RATE_LIMITED
- AI_PROCESSING_ERROR
- WORKFLOW_ERROR
- DATABASE_ERROR
- INTERNAL_ERROR
- SERVICE_UNAVAILABLE

## Core endpoints

### Chat

`POST /chat`

Receives a customer message and returns the customer-facing response.

### Customers

- `POST /customers`
- `GET /customers/{customer_id}`
- `PATCH /customers/{customer_id}`

### Leads

- `POST /leads`
- `GET /leads`
- `GET /leads/{lead_id}`
- `PATCH /leads/{lead_id}`

### Property requirement

`POST /leads/{lead_id}/property-requirement`

### Conversations

- `POST /conversations`
- `GET /conversations/{conversation_id}`

### Messages

- `POST /conversations/{conversation_id}/messages`
- `GET /conversations/{conversation_id}/messages`

### Qualification

- `GET /leads/{lead_id}/qualification`
- `POST /leads/{lead_id}/qualification/recalculate`

### Assignment

`POST /leads/{lead_id}/assignment`

### Follow-ups

- `POST /leads/{lead_id}/follow-ups`
- `GET /leads/{lead_id}/follow-ups`
- `PATCH /follow-ups/{follow_up_id}`

### Notifications

- `GET /notifications`
- `PATCH /notifications/{notification_id}`

## n8n internal contract

FastAPI sends a validated message payload to the n8n webhook.

n8n returns:

```json
{
  "conversation_id": "...",
  "lead_id": "...",
  "response": "...",
  "processing_status": "SUCCESS"
}
```

## API rules

- Validate all input.
- Use UTC timestamps.
- Never expose secrets.
- Return stable error codes.
- Use pagination for collection endpoints.
- Keep public and internal endpoints separate.
