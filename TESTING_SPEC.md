# Testing Strategy & QA Specification

## Goal

Test the behavior that matters without building an unnecessarily large testing program.

## Test levels

1. Unit
2. Integration
3. End-to-end
4. Manual/exploratory

## Critical end-to-end test

```text
Customer message
 ↓
React
 ↓
FastAPI
 ↓
n8n
 ↓
AI
 ↓
Database
 ↓
Qualification
 ↓
Response
 ↓
Sales notification
```

This journey must work before MVP release.

## Backend tests

Test:

- validation
- services
- status transitions
- database operations
- error responses

## API tests

Verify:

- request schema
- response schema
- status codes
- errors
- idempotency
- authentication for protected routes

## Database tests

Verify:

- relationships
- constraints
- required fields
- duplicate prevention
- migrations

## Frontend tests

Test:

- sending a message
- rendering messages
- loading state
- error state
- retry

## n8n tests

For each workflow test:

- happy path
- invalid input
- duplicate request
- AI failure
- database failure
- notification failure

## AI tests

Test:

- intent
- extraction
- missing information
- conflicting information
- unsupported claims
- prompt injection
- response quality

## Qualification tests

Test score calculation, thresholds, gates, recalculation, and manual override.

## Regression

After fixing a bug, add a test when practical.

## Performance

The expected MVP volume is modest. Keep performance testing focused on the critical API/workflow path rather than building a large load-testing program.

## Practical security testing

Verify:

- secrets are not committed
- protected endpoints reject unauthorized access
- input validation works
- customer data is not unnecessarily exposed

## Release smoke test

Before release:

- customer can send message
- lead is stored
- AI processes correctly
- response returns
- qualification exists
- sales notification is generated
- follow-up can be created
