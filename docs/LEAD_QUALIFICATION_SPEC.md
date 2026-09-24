# Lead Qualification & Scoring Specification

## Principle

AI identifies signals. Deterministic rules control qualification.

## Qualification levels

- HIGH
- MEDIUM
- LOW
- UNQUALIFIED

## Scoring factors

| Factor | Weight |
|---|---:|
| Intent clarity | 15 |
| Budget clarity | 20 |
| Location clarity | 15 |
| Property requirement completeness | 15 |
| Timeframe | 20 |
| Contactability | 10 |
| Engagement | 5 |
| **Total** | **100** |

## Score bands

| Score | Level |
|---:|---|
| 80–100 | HIGH |
| 60–79 | MEDIUM |
| 40–59 | LOW |
| 0–39 | UNQUALIFIED |

These thresholds are configurable and should be treated as MVP defaults.

## Qualification gates

A lead should not be HIGH when:

- intent is unknown
- critical information conflicts remain unresolved
- actionable property requirements are missing
- critical AI extraction is low confidence

## Example

```json
{
  "score": 85,
  "level": "HIGH",
  "factors": {
    "intent_clarity": 15,
    "budget_clarity": 20,
    "location_clarity": 15,
    "property_requirement": 15,
    "timeframe": 15,
    "contactability": 10,
    "engagement": 5
  },
  "reasons": [
    "Clear purchase intent",
    "Budget provided",
    "Specific location provided",
    "Property requirement is actionable"
  ]
}
```

## Progressive qualification

Qualification should be recalculated when new information arrives.

Example:

```text
Initial message
   ↓
LOW
   ↓
Customer gives budget
   ↓
MEDIUM
   ↓
Customer gives timeframe + contact
   ↓
HIGH
```

## Lead value vs lead quality

A high budget does not automatically mean a high-quality lead.

Track property value/budget signals separately from qualification.

## Manual override

Authorized sales users may override qualification where required.

Every override should be auditable.

## Versioning

Store the qualification rule version with the result so historical scores remain explainable.
