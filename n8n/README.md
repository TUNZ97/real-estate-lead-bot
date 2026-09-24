# n8n — Workflow orchestration

n8n owns workflow orchestration, AI workflow execution, notifications, scheduled follow-ups, and lead routing. It is **not** the entire backend.

## Workflow inventory (from spec)

| ID | Name | Purpose |
|----|------|---------|
| WF-001 | Customer Message Processing | Main intake: validate → AI → persist → qualify → respond |
| WF-002 | Lead Qualification | Deterministic score & level |
| WF-003 | Sales Notification | Notify sales when criteria met |
| WF-004 | Lead Assignment | Assign to sales user |
| WF-005 | Follow-Up Reminder | Scheduled reminders |

## Structure

```text
n8n/
├── README.md
└── workflows/          # Export workflow JSON here when ready
    └── .gitkeep
```

## Local development

```bash
n8n
# or: npx n8n
```

Default UI: http://localhost:5678

Configure webhook URL in root `.env` as `N8N_WEBHOOK_URL`.

Use ngrok when FastAPI needs to reach n8n from outside (or vice versa):

```bash
ngrok http 5678
```

Do not hardcode temporary ngrok hostnames in source.

## Rules

- Credentials live in n8n credentials / environment — never in committed files.
- Protect internal webhooks.
- Retry only transient failures.
- Prefer visual nodes; use code nodes only when necessary for calculation or awkward transforms.
- Export important workflows as JSON into `workflows/` for version control.
