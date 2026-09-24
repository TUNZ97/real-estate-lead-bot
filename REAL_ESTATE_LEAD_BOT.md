# PrimeHomes Realty — Real Estate Lead Bot

## Product summary

An AI-assisted real estate lead intake and qualification system.

## Customer journey

```text
Customer enquiry
    ↓
Understand intent
    ↓
Extract requirements
    ↓
Ask missing questions
    ↓
Store lead
    ↓
Qualify
    ↓
Respond
    ↓
Notify sales
    ↓
Assign
    ↓
Follow up
    ↓
Track outcome
```

## Example

Customer:

> I need land around Ibadan below N20 million.

System should understand:

```json
{
  "intent": "BUY_LAND",
  "location": "Ibadan",
  "budget": 20000000,
  "currency": "NGN"
}
```

It should not invent the customer's name, phone, email, exact location, or property availability.

## Architecture

React + FastAPI + n8n + AI + PostgreSQL.

## MVP objective

Build the smallest reliable system that moves a customer enquiry into a usable sales lead.
