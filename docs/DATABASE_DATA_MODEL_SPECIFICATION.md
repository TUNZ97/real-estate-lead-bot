# Database & Data Model Specification

## Database

**Development:** MySQL (local install on the developer machine — no Docker required).

**Connection string format (SQLAlchemy + PyMySQL):**

```text
mysql+pymysql://USER:PASSWORD@HOST:PORT/DATABASE
```

Example:

```text
mysql+pymysql://root:your_password@localhost:3306/primehomes_lead_bot
```

**Character set:** `utf8mb4` (recommended for names and chat text).

**Note:** Docker is optional and reserved for later deployment experiments. Local development uses the MySQL instance already on your PC.

## Core entities

```text
customers
leads
property_requirements
conversations
messages
qualifications
sales_users
lead_assignments
follow_ups
lead_status_history
notifications
audit_events
```

## Customer

Suggested fields:

- id
- name
- email
- phone
- created_at
- updated_at

## Lead

Suggested fields:

- id
- customer_id
- intent
- source
- status
- created_at
- updated_at

## Property requirement

- id
- lead_id
- property_type
- bedrooms
- location
- budget
- currency
- transaction_type
- timeframe
- created_at
- updated_at

## Conversation

- id
- customer_id
- lead_id
- channel
- created_at
- updated_at

## Message

- id
- conversation_id
- sender_type
- content
- created_at

## Qualification

- id
- lead_id
- score
- level
- factors
- rule_version
- created_at
- updated_at

## Assignment

- id
- lead_id
- sales_user_id
- assigned_at
- unassigned_at

## Follow-up

- id
- lead_id
- assigned_to
- type
- due_at
- status
- notes
- completed_at

## Lead status history

Every meaningful status change should be recorded.

## Relationships

```text
Customer
  └── Conversations
  └── Leads
       ├── Property Requirement
       ├── Qualification
       ├── Assignments
       ├── Follow-ups
       └── Status History

Conversation
  └── Messages
```

## Constraints

- Foreign keys must be enforced (InnoDB).
- Required fields must be non-null.
- Status transitions must be controlled.
- Duplicate business records should be prevented where appropriate.
- Timestamps should use UTC.

## Indexes

At minimum consider indexes for:

- lead status
- lead created_at
- customer email
- customer phone
- lead location
- assigned sales user
- follow-up due_at

## AI data boundary

AI output must be validated before persistence.

Do not allow an LLM response to bypass database constraints.
