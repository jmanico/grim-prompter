---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# Event-driven threat modeling

Use this set to follow events from publishers through brokers and topics into subscriber actions, retained data and replay facilities.

For one run, use [Quick Event-driven Threat Model](../../quick/event-driven.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder. It returns a quick `TM_REPORT`, proposed outcomes and an action register. For deeper work, run each stage under the runbook, reading its complete input artifact from the run folder:

| Stage | Input | Output | Work |
| --- | --- | --- | --- |
| [00 Scope and evidence](00-scope-and-evidence.md) | `SYSTEM_UNDER_REVIEW` | `TM_CONTEXT` | Inventory event contracts, business invariants and evidence limits. |
| [01 System model](01-system-model.md) | `TM_CONTEXT` | `TM_SYSTEM_MODEL` | Map publish, consume, retain, replay and partial-state paths. |
| [02 Threat analysis](02-threat-analysis.md) | `TM_SYSTEM_MODEL` | `TM_ANALYSIS` | Trace publisher authority, repeated effects and payload exposure. |
| [03 Challenge and consolidate](03-challenge-and-consolidate.md) | `TM_ANALYSIS` | `TM_REVIEWED_MODEL` | Seek scoped counterevidence and reconcile current identities. |
| [04 Treatment and validation](04-treatment-and-validation.md) | `TM_REVIEWED_MODEL` | `TM_TREATMENT_PLAN` | Propose outcomes and discriminating verification cases. |
| [05 Report and handoff](05-report-and-handoff.md) | `TM_TREATMENT_PLAN` | `TM_REPORT` | Preserve the cumulative model and every open action. |

`SYSTEM_UNDER_REVIEW` may be prose, diagram text, sanitized excerpts or a bundle. Optional prior models, risk rubrics and separately executed method fragments travel as typed attachments. Each prompt contains its own contract and baseline. Work without an interview: absent information becomes gaps, and an empty input produces a partial result with no invented findings. These preparation questions do not pause the stages for answers.

## Evidence to bring

1. Which authenticated publisher may assert each event type about which business scope or object, and who owns the event's business meaning?
2. Which topic permissions admit the event, which subscribers receive it, and where does each consumer decide whether its resulting business action is authorized?
3. Which fields are publisher claims, which origin is independently verified, and what separately identifies the event, object, object version and business intent?
4. What delivery, ordering, persistence, acknowledgement and retry contracts apply to this exact path and revision? What happens after an effect commits but its acknowledgement is lost?
5. Which supplied invariants govern reservation, business action, cancellation and recovery? What should happen to a stale ready event after cancellation, or to a new event ID for an already completed intent?
6. Who can create subscriptions, inspect retained/dead-letter payloads and operate replay, and which separate permission allows a business action to be repeated?
7. Which sensitive fields reach each subscriber, diagnostic view and retained copy? What retention/deletion interval and later replay behavior is required for each copy?
8. Which observations link publish, delivery, acknowledgement and side effect? Which are different views of the same event, and which missing observation leaves the result unknown?
9. In a mixed serverless system, which responsibility record assigns trigger admission, runtime privilege and business permission, and which global IDs identify the shared event, function and boundary?

## What the analysis checks

The prompts check publisher origin and authority, subscription topology, event versus intent/version identity, delivery versus effects, stale-state and recovery behavior, replay authorization, payload lifecycle, observation provenance and mixed function authority. An event-driven label establishes no exactly-once, order, durability or retention guarantee. An authenticated publisher with topic access may still lack authority to cause a business action. A payload actor field may be untrusted; a correlation ID may describe one event without authorizing it.

The three families are publisher-induced privileged action; stale, duplicate or reordered effects against a supplied invariant; and unintended disclosure through subscribers, retention or replay. They are candidate scenarios, not required defects. Preserve counterexamples at the tested identity, route, object state and revision. A protected subscriber path does not establish every replay, repair or future subscription path is protected.

The embedded baseline uses security scenario lenses; the default recommendation is [STRIDE per element](../../methods/stride-per-element.md). Selecting it does not mean it ran. Optional methods run separately and supply typed fragments; missing method files never disable the baseline. Business-sequence and recovery questions are lenses unless evidence establishes an actual named procedure execution.

## Verification planning

For publisher authority, propose sending the same isolated test event from an origin lacking action authority and an explicitly entitled origin. Observe the subscriber decision and resulting business state. Pass means the unauthorized-origin attempt causes no forbidden business effect and the entitled attempt has the specified outcome. A forbidden business effect is failure; absent origin/permission/state evidence or test authority is inconclusive. Broker acceptance alone decides none of these outcomes.

For replay and partial completion, propose a business action effect followed by a lost acknowledgement, redelivery, cancellation at a newer object version and replay of the old ready event. Include a fresh event ID for the same intent and changed intent under an old ID. Pass means the supplied invariant holds and uncertain work has an attributable recoverable state. A duplicate business effect or forbidden stale transition is failure. Missing invariant or side-effect evidence is inconclusive.

For exposure, propose comparing an entitled business-data reader, an unentitled subscriber and replay/dead-letter readers over the supplied retention interval. Pass means only entitled readers obtain protected fields through the measured paths and retained copies meet the stated lifecycle contract. A forbidden field disclosure or contradicted lifecycle requirement is failure; unknown readers or incomplete copy/deletion evidence is inconclusive. All three verification plans are `not_run` proposals requiring separate authority to execute.

## Portable results and mixed systems

Write JSON to the artifact file named by the runbook and the readable summary and action register to its Markdown companion. Preserve every treatment, verification and open gap by ID. Without a supplied risk rubric, retain unrated risks and propose a concrete consequence scale for approval; do not assign ratings, owners or dates. Keep proposed treatments, actual controls, supplied decisions and verification execution separate. Technology rules require an exact external secure-coding pack and resolver provenance; without access, name the missing result and leave those prescriptions unverified.

Every revision declares only its immediate parent's actual addressable-record delta. Keep earlier declarations in sanitized revision-tagged history attachments with unique stable IDs. No usable baseline means `changes: []` and no certified continuity. Attachment additions are not Change targets. Repeated challenge, quick reuse and prior-fragment incorporation follow the same rule.

Keep all original numbered chunk texts. Reassemble one complete consistent sequence before using it as a baseline, resolving all references and rejecting conflicting duplicate indices. A partial chunk is not an artifact snapshot. Preserve atomic records and IDs; if a sequence or long prose is unfinished, identify what remains and keep the result partial.

For event-driven plus `serverless`, share global event, function, principal and data IDs. Preserve event ownership and one boundary owner supported by responsibility evidence, with both architecture contributions to a shared threat. Trigger identity, runtime privilege and permission to create a business action are distinct. No function label proves invocation isolation or safe repetition.

The [expanded artifact contract](../../reference/artifact-contract.md) is optional reading. These prompts are draft analysis guidance, not certification, live-tested behavior or exhaustive coverage.
