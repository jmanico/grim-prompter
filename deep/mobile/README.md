---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# Mobile Threat Modeling

Follow account-bound data and actions across a device, the app, operating-system services, other apps and backend authority. Start with the material you have: a description, sanitized observations, a diagram, lifecycle requirements or a prior model. A missing storage policy or sync trace becomes a specific evidence need, not a finding.

Run [Mobile Quick Threat Analysis](../../quick/mobile.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder for a bounded `TM_REPORT`. It preserves a portable model and proposes next verification without claiming the deep workflow ran. For deeper work, run each stage under the runbook, reading the preceding cumulative JSON artifact from the run folder. Only `SYSTEM_UNDER_REVIEW` is an external requirement.

| Prompt | Input | Output |
| --- | --- | --- |
| [00 Scope and evidence](00-scope-and-evidence.md) | `SYSTEM_UNDER_REVIEW` | `TM_CONTEXT` |
| [01 System model](01-system-model.md) | `TM_CONTEXT` | `TM_SYSTEM_MODEL` |
| [02 Threat analysis](02-threat-analysis.md) | `TM_SYSTEM_MODEL` | `TM_ANALYSIS` |
| [03 Challenge and consolidate](03-challenge-and-consolidate.md) | `TM_ANALYSIS` | `TM_REVIEWED_MODEL` |
| [04 Treatment and validation](04-treatment-and-validation.md) | `TM_REVIEWED_MODEL` | `TM_TREATMENT_PLAN` |
| [05 Report and handoff](05-report-and-handoff.md) | `TM_TREATMENT_PLAN` | `TM_REPORT` |

Each prompt embeds its definitions, security questions and tool fallback. Optional risk rubrics, prior models and separately executed method fragments travel inside the bundle with provenance. No optional method is needed to run the baseline. Security questions are named lenses; selecting a procedure does not mean it ran. Preserve every cumulative record, attachment and revision identity. Reassemble all chunks of one sequence before using it as a predecessor; missing or conflicting chunks remain partial. Current changes describe only the immediate-parent delta, while earlier declarations remain sanitized source history.

## Evidence questions

1. Which resources, original attachments, thumbnails and exports remain locally, and who can read each after device loss, sign-out, account switch or restoration? What observation covers the device state in question?
2. How are a local record and a pending completion bound to their creator account and current resource entitlement? What happens if an attachment write or cleanup is interrupted while accounts change?
3. Which fields from app links, shared items and notifications influence local lookup, navigation or backend actions? What checks bind the requested resource and operation to the current account?
4. When a refresh begins for A and completes after B becomes active, who can consume the result? How do disconnection, server revocation and later reconnect affect queued work?
5. What happens when two devices edit the same resource, the server accepts a completion but its acknowledgment is lost, or an old replica is restored? Which revisions and operation identities are compared?
6. What resource details or attachments enter notifications, another app, a backup, a screenshot or logs? What evidence identifies the recipient and limits of later removal?

Use these as preparation questions or unattended evidence needs. If using them as an interview, ask at most five at once and at most two batches unless the caller extends it. With no answer, stop the interview and return the supported scope and explicit gaps; analysis does not wait for every answer.

## Boundary and lifecycle checks

- Separate possession of a lost device from access to its local data and from backend permission; name the locked/unlocked and account state actually evidenced.
- Follow account-specific data through sign-out, switch, interrupted cleanup and restoration, including original attachments and derived copies.
- Trace links and shared content from external producer to candidate object and action, checking authority separately from successful routing.
- Separate notification delivery and display from a later tap under a possibly different account or assignment.
- Trace queue ownership, base revision and operation identity through offline creation, reconnect, acknowledgment loss and retry.
- Follow refresh completion, revocation and refresh failure across account/connectivity transitions without reassigning pending work by assumption.
- Include transfers into other apps and operating-system facilities with recipient and retention scope; missing evidence is not a bypass.
- Compare recovery after restart or partial upload with the same confidentiality and resource invariants as the ordinary path.

A passing backend read observation does not prove local preview or attachment-sharing protection, and an in-app account check does not decide whether the backend accepts an operation. A screen lock label does not prove device-loss confidentiality. Preserve counterevidence and competing policy descriptions; do not force the three scenario families into three defects.

For `mobile` plus `offline-first-sync`, reuse global account, resource, queue and boundary IDs. Mobile contributes device exposure and entry handling; synchronization contributes stale-write, replay and central-authority analysis. Name one owner for the client-to-sync boundary from supplied responsibility evidence. Keep both contributions on shared threats and controls. Two views of one reconnect trace remain one observation.

## Verification planning

**Account switch and reconnect:** with separate authority for a synthetic exercise, select test accounts and resources from supplied policy, retain one account's content, queue an offline operation, switch accounts, complete a delayed refresh for the original account and reconnect. Repeat around a lost acknowledgment. Observe local visibility, outgoing identity, remote acceptance and recovery separately. A pass requires the supplied invariant: the active account cannot read another account's private material or adopt its pending operations, and rejected work has an explicit disposition. A measured unauthorized read/write fails; missing device, identity or server evidence makes the corresponding claim inconclusive. The proposal remains `not_run` until execution evidence exists.

**Untrusted entry:** under separate authority, present an app link and shared item naming A's work while B is active, and tap an old A notification after restart. Include a B-owned positive case. Observe preview, fetched data, queued actions and remote changes as well as the visible response. Pass requires no out-of-scope content or state change and a working authorized case; an unintended read/write fails; an unobserved effect is inconclusive. This is a proposed check, not permission to operate a device or evidence that it passed.

The [artifact contract](../../reference/artifact-contract.md) supplies optional expanded detail; each prompt works without that file. Keep platform settings and APIs in exact externally resolved secure-coding packs. With no tools, catalog or matching pack, record the unresolved technology dependency and continue architectural analysis. Only when a tool limit prevents writing one file, split JSON into the runbook's part files using the embedded chunk protocol, or prose into part files at section boundaries, with unfinished work explicit.
