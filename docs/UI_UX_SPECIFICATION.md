# UI/UX & Frontend Specification

## 1. Goal

Provide a simple, responsive interface for customer enquiries and the minimum internal views required for sales follow-up.

## 2. MVP principle

Do not build a large CRM dashboard first.

Build the critical user journey first.

## 3. Customer chat

Primary screen:

```text
┌──────────────────────────────┐
│ PrimeHomes Realty            │
├──────────────────────────────┤
│                              │
│ Bot: How can we help?        │
│                              │
│ Customer: I need a 3-bed...  │
│                              │
│ Bot: What's your budget?     │
│                              │
├──────────────────────────────┤
│ Type your message...   Send  │
└──────────────────────────────┘
```

## 4. Chat states

- idle
- sending
- receiving
- error
- retrying
- completed

## 5. Components

Suggested:

```text
src/
├── components/
│   ├── Chat/
│   ├── Message/
│   ├── Input/
│   └── Loading/
├── pages/
│   ├── Chat/
│   └── Leads/
├── services/
│   └── api/
├── hooks/
├── types/
└── utils/
```

## 6. API integration

Frontend communicates with FastAPI.

Do not expose database credentials or AI provider keys to React.

## 7. Sales view

MVP sales view should support:

- lead list
- lead details
- qualification
- status
- assignment
- follow-up

Avoid advanced analytics initially.

## 8. Lead details

Display:

- customer information
- intent
- property requirement
- budget
- timeframe
- qualification
- conversation history
- assigned sales user
- follow-ups
- status history where useful

## 9. Accessibility

- keyboard usable
- readable text
- visible focus state
- useful labels
- clear error messages
- responsive layout

## 10. Error handling

Never leave the user wondering whether a message was sent.

Use clear states such as:

> “Message could not be sent. Try again.”

## 11. Responsive behavior

The customer chat must work on mobile first, while remaining usable on desktop.

## 12. Definition of done

- chat works
- API integration works
- loading/error states work
- responsive layout works
- lead information can be displayed
- no secrets are exposed
