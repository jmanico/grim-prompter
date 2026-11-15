# Engagement plan: Northwind Health, PayStream payroll

Recommended 2026-10-30. Confirmed by Dana Okafor on 2026-10-31.

## Review mode

Design review without code. The assessment relies on design documentation, vendor documentation and workshops. Controls can be recorded as reported or designed, not as implemented, unless Northwind supplies a configuration export.

## Architecture lenses

| Lens | Role | Why |
| --- | --- | --- |
| `multi-tenant-saas` | Primary | The decision is about adopting a vendor-run multi-tenant product that will hold Northwind's payroll data. |
| `identity-federation` | Secondary | Sign-on is federated to Entra ID, and local accounts sit outside it. |
| `enterprise-integration` | Secondary | File transfer, webhook and manual payment file flows cross organisational boundaries. |

Considered and not chosen: `payments-transactions` (payments are made in the bank's systems, which are out of scope) and `api` (no Northwind-built API).

## Methods

| Method | Why |
| --- | --- |
| `stride-per-element` | Gives the client a familiar classification and checks each component systematically. |

Not chosen: ATT&CK and CAPEC enrichment (little implementation detail to map), LINDDUN (privacy was not requested; raise it with the client given the tax file numbers).

## Depth and rating

Quick analysis: the system is small and the decision is near. Risk is rated with Northwind's enterprise risk matrix v3.1 (`02-plan/risk-matrix.json`).

## Decisions for the consultant

1. Confirm the lenses and method above.
2. Decide whether to offer a privacy review as an extension.
3. Confirm the client will supply its risk matrix. Done.
