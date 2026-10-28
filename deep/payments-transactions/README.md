---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# Payments and Transactions Threat Modeling

Analyze the actual transaction domain across intent, authorization, state, partner, ledger and reconciliation boundaries where supplied. The inputs can be a short description or a portable bundle of diagrams, requirements, sanitized excerpts, observations and prior models. Missing evidence becomes explicit gaps; no interview is required, and read-only project access follows the runbook.

For a bounded first pass, run [Quick Payments and Transactions Threat Analysis](../../quick/payments-transactions.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder. It returns `TM_REPORT` with quick scope and unperformed work disclosed. It does not claim the six-stage analysis ran.

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

## Evidence to bring

1. Who may set or change significant amount, currency, beneficiary and ownership details, and which exact intent and revision does approval cover?
2. What authorizes initiation, capture, posting, refund and reversal separately, including alternate caller and partner ingress routes?
3. Which supplied states and observations distinguish pending or unknown outcome from a known rejection, confirmed effect or later reversal?
4. What connects a notification to the actual transaction and effect? Which correlation, event, message, delivery and attempt identities are supplied, and what can each prove?
5. What happens when duplicate, reordered or conflicting notifications arrive before or after a state change? What evidence separates receipt from business posting?
6. Which balance, ownership and amount constraints apply to refunds, reversals and reconciliation, and who may resolve a difference? Which observations support that authority?
7. What is observed about protection, permitted operations and denied attempts on each route, and which source revisions disagree?

The cited transaction-authorization and authorization guidance supports questions about significant details, per-operation permission and transitions. Webhook and payment-gateway guidance supports questions about callback origin, duplicate effects and late notifications; business-logic guidance supports eliciting and testing domain invariants. Refund, reversal, balance and reconciliation constraints below are evidence-elicitation/design prompts: their actual allowed states, amounts, ownership and adjustment authority must come from the caller, not a universal financial rule. Selecting an architecture companion such as event-driven does not execute that role or select a payment provider.

## Boundary and lifecycle checks

1. **Approval to execution.** Trace the supplied significant transaction tuple (transaction and operation identity, owner, amount, currency, beneficiary, intent and revision where applicable) from entry through approval to the actual execution gate. Identify who controls each field before and after approval. Do not treat authenticated identity or event authenticity as transaction consent. A change of beneficiary, amount or currency needs analysis against the supplied approval scope, not an invented universal approval scheme.
2. **Per-operation authority.** Map the actual caller and partner entry points through initiation, capture, posting, refund and reversal where those operations exist. Compare actor, resource owner, permitted operation and significant details at each crossing. Unknown ingress or authority remains a linked topology or evidence gap; a direct-read protection cannot establish write authority.
3. **Notification to effect.** Follow publisher, distribution channel and consumer into transaction state and ledger effects. Duplicate delivery is not necessarily a duplicate business posting. Preserve supplied event/message/delivery/attempt/transaction/effect identities separately where their meanings differ; a correlation ID alone is not an authorization or deduplication guarantee.
4. **Ordering and conflict.** Compare duplicate, reordered, late and conflicting notifications with supplied allowed transitions and state revisions. Transport receipt and authenticated publisher establish neither payer intent nor permission to advance a ledger. Ask which evidence resolves a conflict rather than choosing the newest arrival as authoritative.
5. **Unknown outcome and retry.** Keep pending and unknown separate from success and failure. Retrying a known rejected operation differs from repeating an operation whose prior effect is unknown. Trace outcome queries and recovery routes to actual observations of the same intent/effect; do not infer atomicity, settlement or exactly-once behavior from a response or timeout.
6. **Refund and reversal.** Tie a proposed refund or reversal scenario to supplied original effect, owner, amount limits and allowed transitions. Partial and concurrent actions require evidence of the actual premises. Do not invent negative-balance rules, a universal accounting policy, or permission to reverse any transaction merely because it was once approved.
7. **Reconciliation.** Trace supplied comparison inputs, identities, observation times and differences to the authority allowed to change state or balances. Keep an unexplained difference distinct from an authorized adjustment. Model unknown reconciliation ingress and unresolved invariant conflicts explicitly.
8. **Shared boundaries and recovery.** In mixed event-driven scope, record supplied endpoint zone membership and give each evidenced publisher/channel/subscriber crossing its event-distribution owner and the separate transition/posting/reconciliation crossing its payments owner. Share each globally identified transaction, owner, approved tuple, event, consumer or ledger the caller actually supplied across both views; count a shared threat or control once while retaining all contributors. Leave unknown membership or ingress as linked gaps. Preserve detection/recovery uncertainty and do not claim the architecture companion role executed without a typed execution record.

## Scenario families and verification

Develop three distinct families only where supplied evidence supports them: significant details change between approval and execution; duplicate/reordered/conflicting notifications reach state or ledger effects; and reversal/reconciliation differences violate supplied balance or ownership invariants. For each, state reachable route, actor capability, approval or transition premise, relevant system/evidence IDs and what would disconfirm it. Do not equate missing evidence with an implemented defect, force findings on protected paths, or generalize a scoped protection. A design hypothesis remains conditional even when its premise is explicit in a proposed design.

Propose discriminating verification adapted to the supplied domain, never authorization to execute it. (1) Compare an allowed transaction with changes to each significant approval detail, intent/revision or resource owner between approval and execution. Observe the actual initiating identity, approved and executed tuple, route, authorization decision and persisted effect. Pass requires the intended allowed effect and rejection or renewed applicable approval of mismatches; an unauthorized effect fails; missing tuple, authority or effect observation is inconclusive. (2) With the caller's supplied transitions and invariants, compare duplicate delivery of one message, distinct messages for one business effect, reordered conflicting outcomes and a reversal or reconciliation difference after an unknown outcome. Observe state before/after, allowed transition, message versus effect identity, owner, amounts and the outcome/reversal/reconciliation route. Pass requires allowed effects and rejection or unresolved handling of disallowed transitions without violating the supplied constraints; duplicate business postings or unauthorized state/balance changes fail. Missing observations are inconclusive, not proof from silence. A known rejection must be distinguished from unknown prior effect before interpreting retries. These are not_run proposals with no result evidence; neither receipt nor an authenticated event proves the expected business result.

## Optional guided preparation

If the caller chooses an interview, collect at most five of the evidence questions per batch and at most two batches unless they extend it. If nobody answers, return the available partial evidence and precise gaps. This separate preparation never blocks the unattended prompts.

## Limits

Source selection is separate from a procedure actually performed. Selecting event-driven does not run that role. The set remains draft: finite authored artifacts are not live model or payment execution.
