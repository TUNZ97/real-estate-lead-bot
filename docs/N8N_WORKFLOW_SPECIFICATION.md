# n8n Workflow Specification

## Role

n8n is the workflow orchestration layer.

## Workflow inventory

- WF-001 Customer Message Processing
- WF-002 Lead Qualification
- WF-003 Sales Notification
- WF-004 Lead Assignment
- WF-005 Follow-Up Reminder

## WF-001 Customer Message Processing

```text
Webhook
 ↓
Validate
 ↓
Idempotency check
 ↓
Load conversation
 ↓
AI processing
 ↓
Validate AI output
 ↓
Normalize
 ↓
Upsert customer
 ↓
Upsert lead
 ↓
Store requirement
 ↓
Store customer message
 ↓
Qualification
 ↓
Generate response
 ↓
Store bot message
 ↓
Return response
```

## WF-002 Qualification

- receive lead
- collect deterministic factors
- calculate score
- determine level
- persist qualification
- update lead status where allowed

## WF-003 Sales Notification

Triggered when a lead meets notification criteria.

Notification should include:

- lead ID
- intent
- customer information available
- property requirement
- qualification
- score/reasons
- recommended next action

Prevent duplicate notifications.

## WF-004 Assignment

- identify eligible sales users
- apply configured assignment rule
- persist assignment
- preserve assignment history
- notify assignee

## WF-005 Follow-Up Reminder

Scheduled workflow:

```text
Schedule Trigger
 ↓
Find due follow-ups
 ↓
Check status
 ↓
Prevent duplicate reminder
 ↓
Send reminder
 ↓
Record notification
```

## Error handling

Classify:

- validation
- AI
- database
- external integration
- workflow

Retry transient errors only.

## n8n code-node rule

Use code nodes for:

- custom calculations
- data transformation that is awkward visually
- special validation
- custom business logic that genuinely belongs in code

Do not use code nodes for everything.

## Security

- credentials stored in n8n credentials/environment configuration
- do not hardcode secrets
- protect internal webhooks
- minimize PII in logs

## Testing

Each workflow should have:

- happy path
- invalid input
- duplicate input
- AI failure
- database failure
- notification failure
- retry behavior
