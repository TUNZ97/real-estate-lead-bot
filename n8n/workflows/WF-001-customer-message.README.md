# WF-001 — Customer Message Processing (n8n setup)

This is the webhook your FastAPI backend calls on every chat message.

## Webhook URL

In n8n, create a **Webhook** node (POST) and set path to something like:

```text
customer-message
```

Full local URL example:

```text
http://localhost:5678/webhook/customer-message
```

Put that value in the repo root `.env` as:

```text
N8N_WEBHOOK_URL=http://localhost:5678/webhook/customer-message
```

> Use **Production** webhook URL when workflow is **Active**. Test URL only works while you click “Listen for test event”.

## Incoming payload (from FastAPI)

```json
{
  "message": "Hi, I'm looking for a 3-bedroom apartment around Lekki. Budget around N80 million.",
  "conversation_id": "uuid-or-null",
  "customer_id": null,
  "request_id": "uuid",
  "idempotency_key": "uuid",
  "source": "web_chat",
  "channel": "web"
}
```

Headers (optional):

- `X-Request-ID`
- `Idempotency-Key`
- `X-Webhook-Secret` (if you set `N8N_WEBHOOK_SECRET` in `.env`)

## Required response (back to FastAPI)

Your workflow **Respond to Webhook** node must return JSON:

```json
{
  "conversation_id": "same-or-new-uuid",
  "lead_id": "optional-uuid",
  "response": "Natural language reply shown to the customer",
  "processing_status": "SUCCESS"
}
```

`response` is **required**. Without it, the API returns `WORKFLOW_ERROR`.

## Minimal test workflow (no AI yet)

1. **Webhook** (POST) → path `customer-message` → Respond: “Using Respond to Webhook node”
2. **Set** / **Code** node — build reply, e.g.:

```javascript
const msg = $json.body?.message || $json.message || '';
return [{
  json: {
    conversation_id: $json.body?.conversation_id || $json.conversation_id || crypto.randomUUID(),
    lead_id: null,
    response: `Thanks for your message: "${msg.slice(0, 120)}". A PrimeHomes advisor will assist you shortly. What is your preferred location and budget?`,
    processing_status: 'SUCCESS',
  },
}];
```

3. **Respond to Webhook** — respond with JSON from the previous node.

Activate the workflow, then send a message from the React chat.

## Full WF-001 flow (from docs)

```text
Webhook → Validate → Idempotency → Load conversation → AI → Validate AI
→ Normalize → Upsert customer/lead/requirement/message → Qualify
→ Generate response → Store bot message → Respond
```

You can grow the minimal test workflow into this full path over time.

## Troubleshooting

| Symptom | Check |
|---------|--------|
| Frontend shows fallback reply | n8n not running, wrong URL, or workflow inactive |
| `WORKFLOW_ERROR` / 502 | Response missing `response` field or non-JSON |
| CORS / network error | FastAPI must be running; Vite proxies `/api` → `:8000` |
| Timeout | Increase AI node timeout or FastAPI client timeout |
