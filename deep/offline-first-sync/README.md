---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# Offline-first Sync Threat Modeling

Examine local replicas and queued work against synchronization and central authority. Run the [quick role](../../quick/offline-first-sync.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder for a compact `TM_REPORT`. For deep work, run each stage under the runbook, reading its cumulative input file from the run folder. Empty input yields partial scope and useful gaps. No network access, optional method or earlier session is required; read-only project access follows the runbook.

| Stage | Input | Output |
| --- | --- | --- |
| [00 Scope and Evidence](00-scope-and-evidence.md) | `SYSTEM_UNDER_REVIEW` | `TM_CONTEXT` |
| [01 System Model](01-system-model.md) | `TM_CONTEXT` | `TM_SYSTEM_MODEL` |
| [02 Threat Analysis](02-threat-analysis.md) | `TM_SYSTEM_MODEL` | `TM_ANALYSIS` |
| [03 Challenge and Consolidation](03-challenge-and-consolidate.md) | `TM_ANALYSIS` | `TM_REVIEWED_MODEL` |
| [04 Treatment and Validation](04-treatment-and-validation.md) | `TM_REVIEWED_MODEL` | `TM_TREATMENT_PLAN` |
| [05 Report and Handoff](05-report-and-handoff.md) | `TM_TREATMENT_PLAN` | `TM_REPORT` |

Optional prior models, rubrics and separately executed fragments travel as typed attachments, never required external inputs. Only `SYSTEM_UNDER_REVIEW` enters from outside the chain. Preserve IDs, exact values, counterevidence and source snapshots. Each output declares only its immediate-parent changes; older declarations remain sanitized history. Reassemble all chunks before using a predecessor. State unperformed validation and byte-comparison limits in the run, keep partial gaps and split prose into part files at section boundaries only when a tool limit prevents writing one file.

## Evidence questions

1. Which reads and writes are permitted offline, and what distinguishes a local change, durable queue entry, delivery receipt and authoritative commit?
2. Which creator, device, replica, operation and base-revision identities survive account change? What policy applies when revocation occurs after enqueue but before adjudication?
3. What ingress can create or alter queued work, and which evidence binds each input to its origin and authority?
4. Which merge policy preserves current ownership and business invariants when two replicas disagree? What evidence separates duplicate delivery from duplicate effect?
5. Which deletion and retention decisions apply to disconnected peers, backups and restored copies? What marks a peer as too old to rejoin, if anything?
6. What happens after process termination, partial commit, lost acknowledgment or restoration, and how is rejected or deferred work recovered?

Use these as unattended evidence needs. In an optional interview ask at most five per batch and two batches unless extended; no response ends the interview with a partial bundle. Never block analysis waiting for answers.

## Boundary and lifecycle checks

This summary navigates the eight governing checks under “Offline synchronization scope and boundary rules” in each prompt, including the [quick role](../../quick/offline-first-sync.md#offline-synchronization-scope-and-boundary-rules). Apply those checks within the selected stage’s task.

Check local read authority; creator/session binding across account change; external ingress into queue creation; queue-before-revocation adjudication; concurrent merge against ownership; replay after acknowledgment loss; deletion propagation to disconnected copies; and restoration/rejoin. Keep queued, locally accepted, delivered and authoritatively committed states separate. Unknown entry points and recovery paths remain explicit topology/evidence gaps. Do not assume last-write-wins, eventual execution, deletion convergence, restored-copy safety or rejection after revocation.

With `mobile`, retain the same device, account, replica, queue entry, record/assignment and backend IDs. The mobile local-session/storage crossing and offline-sync adjudication/central-authority crossing need separate supplied ownership evidence. Do not collapse them. Retain both contributions where a shared scenario is established; selecting mobile does not mean its procedure executed.

## Verification planning

**Queued action and conflict:** under separate authorization, queue an operation while its creator is entitled, change ownership/revoke authority centrally, then deliver it with a concurrent edit and retry after a lost acknowledgment. Compare a currently authorized positive operation. Observe local acceptance, queue identity, transport, adjudication and central state separately. Pass only if the supplied policy and ownership/business invariant hold for each measured sequence; an out-of-policy commit or duplicate effect fails; missing policy, ordering or commit observations is inconclusive. Rejection is not assumed and the proposal remains not_run.

**Deletion and restored peer:** under separate authorization, disconnect a replica, apply a supplied deletion/retention decision centrally, then reconnect it and restore an older snapshot in separate trials. Observe retained copies, markers, replayed writes, rejoin decisions and authorized retained data. Pass requires the supplied policy to hold without resurrection through measured paths or unauthorized destruction of retained data; either observed violation fails. Unknown retention exceptions, restore coverage or peer acknowledgments makes the relevant conclusion inconclusive. No universal convergence or successful restoration is claimed.

The [artifact contract](../../reference/artifact-contract.md) offers optional detail; each prompt embeds its own contract. Exact APIs/settings/version rules require external resolved secure-coding packs. Without them, continue architectural outcomes and label implementation advice unverified.

Source scope: the Android reference supports storage, write, synchronization and conflict-strategy framing. Revocation, replay and deletion policies require supplied system evidence. No platform guarantee or universal policy follows from the citation.
