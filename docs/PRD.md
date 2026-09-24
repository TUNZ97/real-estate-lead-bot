# Product Requirements Document (PRD)

## PrimeHomes Realty — Real Estate Lead Bot

**Version:** 0.1  
**Status:** MVP specification

## 1. Product overview

PrimeHomes Realty needs a system that can receive potential customer enquiries, understand what the customer wants, capture the relevant information, qualify the lead, respond to the customer, notify the sales team, and support follow-up.

The product acts as a digital receptionist for real-estate enquiries.

## 2. Problem

Manual processing becomes slow and inconsistent as enquiry volume grows. Important information can be missed and sales representatives may not receive qualified leads quickly enough.

## 3. Goals

- Receive customer enquiries.
- Understand intent.
- Extract customer and property requirements.
- Ask for missing high-value information.
- Store leads and conversation history.
- Qualify leads consistently.
- Respond clearly.
- Notify and route leads to sales.
- Track follow-up and lead status.

## 4. Non-goals for MVP

- Predictive property recommendations.
- Complex CRM integrations.
- Multiple AI agents.
- Microservices.
- Kubernetes.
- Large analytics platform.
- Complex enterprise identity systems.
- Advanced real-time collaboration.

## 5. Users

### Customer
Wants a property or has a property-related enquiry.

### Sales representative
Receives, contacts, and follows up with leads.

### Sales manager
Monitors leads, assignment, and follow-up.

### Admin
Manages system configuration and users.

## 6. Example enquiries

> “Hi, I'm looking for a 3-bedroom apartment around Lekki. My budget is around N80 million.”

> “Do you have any 2-bedroom apartments in Ikeja?”

> “I need land around Ibadan, preferably below N20 million.”

> “Hello, I want to buy a house.”

## 7. Functional requirements

| ID | Requirement |
|---|---|
| FR-001 | Receive customer messages |
| FR-002 | Understand customer intent |
| FR-003 | Extract customer information |
| FR-004 | Extract property requirements |
| FR-005 | Identify missing information |
| FR-006 | Store leads |
| FR-007 | Store conversation history |
| FR-008 | Qualify leads |
| FR-009 | Respond to customers |
| FR-010 | Notify sales |
| FR-011 | Assign leads |
| FR-012 | Support follow-up |
| FR-013 | Track lead status |
| FR-014 | Search/retrieve leads |

## 8. Customer data

- name
- email
- phone

## 9. Property data

- property type
- bedrooms
- location
- budget
- currency
- buy/rent/sell
- timeframe

## 10. Intent types

- BUY_PROPERTY
- RENT_PROPERTY
- SELL_PROPERTY
- BUY_LAND
- PROPERTY_ENQUIRY
- GENERAL_ENQUIRY
- UNKNOWN

## 11. Timeframes

- IMMEDIATE
- WITHIN_1_MONTH
- WITHIN_3_MONTHS
- RESEARCHING
- UNKNOWN

## 12. Non-functional requirements

- Reasonable response time.
- Reliable processing.
- Clear error handling.
- Maintainable architecture.
- **MySQL** as the database source of truth for development (local install; Docker optional later for deployment).
- Practical security.
- Testable components.

## 13. Success criteria

A customer can send an enquiry and the system can:

1. receive it
2. understand it
3. extract relevant data
4. store it
5. qualify it
6. respond
7. notify sales
8. support follow-up

## 14. Definition of done

The MVP is done when the critical customer-to-sales journey works end-to-end and passes the release test suite.
