---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# Web Threat Modeling

Analyze a web application from its browser, application origin, session, server, external-content and sensitive-data boundaries. The inputs can be a short description or a portable bundle of diagrams, requirements, sanitized excerpts, observations and prior models. Missing evidence becomes explicit gaps; no interview is required, and read-only project access follows the runbook.

For a bounded first pass, run [Quick Web Threat Analysis](../../quick/web.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder. It returns `TM_REPORT` with quick scope and unperformed work disclosed. It does not claim the six-stage analysis ran.

For the deep path, run each prompt under the runbook, reading its named cumulative JSON input from the run folder. Keep the whole model, including evidence, attachments and prior record identities, between stages.

| Prompt | Input | Output |
| --- | --- | --- |
| [00 Scope and evidence](00-scope-and-evidence.md) | `SYSTEM_UNDER_REVIEW` | `TM_CONTEXT` |
| [01 System model](01-system-model.md) | `TM_CONTEXT` | `TM_SYSTEM_MODEL` |
| [02 Threat analysis](02-threat-analysis.md) | `TM_SYSTEM_MODEL` | `TM_ANALYSIS` |
| [03 Challenge and consolidate](03-challenge-and-consolidate.md) | `TM_ANALYSIS` | `TM_REVIEWED_MODEL` |
| [04 Treatment and validation](04-treatment-and-validation.md) | `TM_REVIEWED_MODEL` | `TM_TREATMENT_PLAN` |
| [05 Report and handoff](05-report-and-handoff.md) | `TM_TREATMENT_PLAN` | `TM_REPORT` |

A complete chunk sequence must be reassembled before it becomes a predecessor. Incomplete or conflicting input stays partial and cannot establish revision continuity. Each prompt includes the portable contract and handles unavailable tools. Optional risk rubrics, prior models and separately executed method fragments travel inside the bundle, never as extra required inputs. The baseline uses named security questions without claiming a specialist method ran. If you want the separate STRIDE per element procedure, supply its actual fragment; its absence does not block this analysis.

## Evidence questions

- Which browser requests change application state, and what establishes that the intended user authorized that request?
- Where does the server bind session identity, tenant, object and operation? Do export, background and staff routes use the same authority?
- Which customer-controlled notes, links or uploads reach another user's view, in which rendering context and with what observed protection?
- Which private responses enter a shared cache or remain in browser storage, and what distinguishes their permitted recipients before reuse?
- Which third-party code or resources can read or receive sensitive page context, and who can change that code after review? What data actually crosses that boundary?
- What changes on signout, expiry, tenant/account switch, privilege change and recovery? What happens to old authority and retained content?
- Which component owns each boundary, and which description or observation supports it? Where do sources conflict or lack a revision?

## Analysis boundaries

Trace intended request authority separately from recognized session and object ownership. Follow content from its user-controlled source into another user's rendering context. Review private response reuse separately from third-party data transmission, and ask whether attacker-influenced content can be stored in a shared cache for other users. Include upload preview/download ownership, authority transitions and delegated asynchronous routes. These are checks to apply to supplied evidence, not a list of defects every application must have.

Keep a passing test scoped to its operation and observation. A protected note view does not prove the upload preview safe; a direct read check does not prove export ownership; a known session does not prove intended request authority. Conversely, missing settings or an external resource alone do not prove a vulnerability. Preserve protective observations, contradictory descriptions and unresolved assumptions.

When combining with `multi-tenant-saas`, keep global resource and tenant identities. Give each boundary one evidenced owner and preserve both architecture contributors on shared threats and controls. Do not count repeated descriptions of the same scenario as independent evidence.

## Verification planning

For a resource update, propose an authorized synthetic comparison using customer A/B sessions and known object ownership. Record the intended allowed operation, unintended-request and cross-owner cases, observable state changes, and separate pass/fail/inconclusive conditions. Missing state or request-authority evidence is inconclusive.

For private response reuse, propose warming a synthetic response and requesting the relevant resource as a non-entitled user in the same tenant, a different tenant and a signed-out client through the same path. Observe recipient ownership and response content as well as whether the cache was used. Unauthorized private content is a failure; an unobserved path cannot establish a pass. Neither example authorizes execution or implies a test ran.

The [artifact contract](../../reference/artifact-contract.md) is an optional expanded reference. If it or a technology pack is unavailable, each prompt still works from its embedded definitions and records the missing checks. Keep technology APIs and configuration recipes in exact resolved secure-coding packs; never guess a pack identity.
