# Deployment Specification

## Deployment principle

Keep the MVP deployment simple. Do not introduce Kubernetes or microservices.

## Components

- React frontend
- FastAPI backend
- PostgreSQL database
- n8n
- AI provider

## Environments

### Development

Local machine, optionally using ngrok for webhook access.

### Staging

Environment for integration testing before production.

### Production

Real customer traffic and production data.

## Configuration

Secrets must come from environment/secret configuration.

Never commit:

- API keys
- database passwords
- JWT secrets
- webhook secrets
- provider credentials

## Database deployment

Before release:

1. backup existing production data when applicable
2. run migrations
3. verify schema
4. run smoke tests

## n8n deployment

- import/version workflows
- configure credentials
- configure environment-specific webhook URLs
- test workflows
- verify retry/error behavior

## Backend deployment

Verify:

- health endpoint
- database connection
- migrations
- environment configuration
- API routes
- logging

## Frontend deployment

Verify:

- production API URL
- no secret keys bundled into frontend
- customer chat
- error handling
- responsive UI

## Release smoke test

Send a realistic enquiry:

> “Hi, I'm looking for a 3-bedroom apartment around Lekki. My budget is around N80 million.”

Verify:

1. request received
2. lead created/updated
3. property requirement stored
4. response returned
5. qualification calculated
6. sales notification generated
7. conversation persisted

## Rollback

If a release causes critical failure:

- stop new rollout
- restore previous application version
- preserve database integrity
- investigate failed migration before retrying

## MVP principle

Prefer a simple, repeatable deployment process over a highly complex platform.
