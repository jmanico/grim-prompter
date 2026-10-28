---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# IoT and Edge Threat Modeling

Follow device identity, ownership and authority through physical access, enrollment, configuration, disconnected work and recovery. Use only the caller's actual topology. A gateway, fleet or cloud boundary belongs in the model when the supplied evidence establishes it.

Run [IoT and Edge Quick Threat Analysis](../../quick/iot-edge.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder for a bounded `TM_REPORT`. For deep analysis, run each stage under the runbook, reading its cumulative predecessor file from the run folder. Read-only project access follows the runbook; no optional method is required, and only `SYSTEM_UNDER_REVIEW` enters from outside.

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

1. Which physical and logical identifiers identify each device, and what separate record establishes its current owner and enrollment scope? Who may replace, transfer or retire it?
2. What can a person with physical access actually read or change through local interfaces, storage or recovery? Which device states were observed?
3. Where an intermediary exists, which target devices and actions may it authorize, and what independent device/upstream decisions constrain a compromised intermediary?
4. Who may administer ownership, change configuration, deploy software and initiate updates? Which explicit delegation connects those roles, and who owns each crossing?
5. What identifies a queued command and its target, owner, configuration revision and expiry? What observations separately establish submission, acceptance, delivery and execution?
6. Which timestamp describes measurement versus receipt, how is age evaluated at a decision, and what caller-supplied operating constraint applies when observation or clock evidence is missing?
7. What happens to old identities, queued commands and observations after replacement, revocation, interrupted update, restoration and reconnect? What evidence shows recovery rather than only reconnection?

Use these as unattended evidence needs. For an optional interview, ask at most five questions per batch and two batches unless extended; with no answer, stop the interview and return supported scope and explicit gaps.

## Boundary and lifecycle checks

- Identify physical access, exposed local interfaces, storage and recovery entry points. Separate possession from the capability to read data, change identity or configuration, initiate an update, or affect another device. Do not infer extraction or bypass from physical access alone.
- Trace enrollment and replacement from device identity to current owner and intended scope. Ask who approves transfer, what happens to the replaced identity and pending work, and how revocation reaches disconnected components. An identifier match alone does not prove ownership.
- Follow intermediary authority at each device-facing and upstream decision. For a compromised gateway where one exists, identify reachable targets, delegated actions and independent checks before predicting cross-device propagation. Transport reachability and authenticated gateway identity are not a device-specific grant.
- Separate configuration submission, acceptance, delivery and execution, including the intended device, owner, configuration revision and command identity. Keep acknowledgments scoped to their actual milestone. Ask how duplicates, stale commands and changed authority are handled if the caller design includes queued work.
- Keep observation time, receipt time, provenance and age at a decision distinct. Compare delayed or reordered data with caller-supplied operating constraints. Fresh transport delivery does not establish a current observation. Missing timing or clock evidence remains a gap; do not supply operating limits or treat assumed timing premises as safety guarantees.
- Follow disconnected operation, reconnect, replacement, revocation and recovery against the same identity and authority invariants as normal operation. Ask which queued work is revalidated, rejected, retained or reconciled and what independent evidence shows the resulting state. Do not assume eventual delivery or execution.
- Separate software authenticity, permission to initiate an update, deployment scope and recovery authority. Ask about interrupted update, restoration and rollback only as applicable to the supplied device; neither rollback nor automatic updates are universally required or forbidden. A restored device still needs its current ownership/configuration context.
- Follow stored and transmitted data protection and cybersecurity-state reporting separately from operational measurements. Identify authorized readers and modifiers, recipients, evidence retention and recovery visibility. A device health indication is not proof of current measurements or a successful authorized command.

These are tailored analysis questions. The device baseline is a starting point, not a universal mandatory checklist. Do not infer a defect from an absent capability or a missing observation. Keep identity, configuration, interfaces, updates, data protection and cybersecurity-state reporting separate. Reconnect policies and operational timing are caller design premises, never safety guarantees.

For `iot-edge` plus `cloud-control-plane`, use the same device, fleet, configuration and command IDs at gateway and cloud decisions. Model directional flows and one evidenced owner per crossing. Keep cloud resource/delegation authority distinct from device enforcement and preserve both architecture contributions. Two summaries of one observation do not corroborate each other.

## Verification planning

**Replacement and intermediary authority:** with separate authorization in a synthetic or approved isolated setting, replace a device within one ownership scope, revoke its old identity, then attempt old-device enrollment and a compromised-gateway action against a separately owned device. Include a valid replacement and correctly scoped action. Pass requires the supplied ownership invariant and independent target checks to hold at each measured decision; an unauthorized binding or cross-device effect fails; missing identity, enforcement or resulting-state evidence is inconclusive. New verification remains `not_run`; this design authorizes no real device operation.

**Delayed observations and reconnect:** with separate authorization, delay a measurement beyond the caller-supplied freshness limit, queue a configuration command, change ownership/configuration, and reconnect around a lost acknowledgment. Observe submission, acceptance, delivery, execution and measurement age independently, with a fresh authorized positive case. Pass requires stale data to remain labeled and excluded from decisions requiring freshness, obsolete work to have the specified disposition and no duplicate effect. An unsupported current-state assertion or unauthorized/duplicate execution fails; absent clocks or execution evidence is inconclusive. A passing synthetic check neither sets an operating limit nor establishes safe actuation.

The optional [artifact contract](../../reference/artifact-contract.md) expands definitions already embedded in every prompt. Resolve exact technology packs only if a stack is supplied; otherwise retain an unverified technology gap. Only when a tool limit prevents writing one file, use the embedded chunk protocol for JSON part files under the runbook or split prose into part files at section boundaries, with unfinished work explicit.
