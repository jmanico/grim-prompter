---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# Real-Time Collaboration Threat Modeling

Analyze participants, documents or rooms, persistent connections, shared state and presence data. Start with any supplied description, diagram text, policy, sanitized excerpts or observations. Missing evidence becomes gaps; no interview is required, and read-only project access follows the runbook.

Run the [quick role](../../quick/collaboration-realtime.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder for a bounded `TM_REPORT`. It discloses quick depth and unperformed deep challenge. For deeper analysis, pass each complete cumulative JSON output to the next prompt, even in separate agent sessions.

| Prompt | Input | Output |
| --- | --- | --- |
| [00 Scope and evidence](00-scope-and-evidence.md) | `SYSTEM_UNDER_REVIEW` | `TM_CONTEXT` |
| [01 System model](01-system-model.md) | `TM_CONTEXT` | `TM_SYSTEM_MODEL` |
| [02 Threat analysis](02-threat-analysis.md) | `TM_SYSTEM_MODEL` | `TM_ANALYSIS` |
| [03 Challenge and consolidate](03-challenge-and-consolidate.md) | `TM_ANALYSIS` | `TM_REVIEWED_MODEL` |
| [04 Treatment and validation](04-treatment-and-validation.md) | `TM_REVIEWED_MODEL` | `TM_TREATMENT_PLAN` |
| [05 Report and handoff](05-report-and-handoff.md) | `TM_TREATMENT_PLAN` | `TM_REPORT` |

Only `SYSTEM_UNDER_REVIEW` is required from outside the chain. Optional rubrics, prior models and separately executed method fragments travel in typed attachments. Each prompt embeds its working contract and baseline security questions; an unavailable optional method does not block analysis. A selection is not an execution. Complete all chunks before consuming a predecessor; conflicting or missing chunks yield partial work with gaps. Preserve prior changes as sanitized source history and declare exactly the current immediate-parent deltas.

## Evidence questions

- Who can invite, accept, remove or change a participant's role, for which document or room? Does ownership confer different authority from ordinary membership?
- What binds a participant to a login session and persistent connection, and where is current document permission decided for each action?
- What is the required policy for an edit queued before removal but delivered afterward? What ordering identifies enqueue, receipt, authorization and authoritative commit?
- Which edit fields can the participant choose, which may change, and what preserves current ownership and attributed history during conflicts and retries?
- Which component selects live state recipients, and what cutoff governs new delivery after removal? What happens to data already delivered?
- What distinct data goes to presence, cursor and notification audiences? Which policy selects each recipient, and can notifications leave the live channel?
- Which ingress, central commit, live fanout, local replica and offline replay crossings are evidenced? Who owns each, and where are topology or responsibility unknown?
- What happens on reconnect, account switch, crash, lost acknowledgment, restored subscriptions and notification re-drive? Which observations cover these paths?

Record unanswered questions as gaps and continue. Do not infer current permission from transport authentication, authorized edits from conflict convergence, or a universal accept/reject rule for revoked queued work. The caller's policy and its actual enforcement point determine the analysis.

## Boundary and lifecycle coverage

Follow invitation and removal separately from ordinary edits; establish session/connection ingress; compare current permission at authoritative commit; preserve ownership and history through conflict; trace live state fanout; distinguish all three metadata audiences; follow local queued replay; and examine reconnect/recovery. These are coverage checks, not defects required of every system. Include actual crossed boundaries and payload references on each flow. Unknown links and owners remain gaps.

The three scenario families are revocation across active connections and queued updates, forged edits/conflicts against ownership and history, and presence/cursor/notification disclosure across membership boundaries. A protected route may defeat a family. Any residual hypothesis needs a concrete unobserved path or conditional failed protection, not a contradiction of supplied controls. Incomplete facts require partial coverage.

For bounded `offline-first-sync` composition, use one participant/document/operation/replica identity across both views. Establish collaboration commit and offline replay owners separately. Preserve both contributions only on scenarios actually spanning their crossings; selecting the partner does not run its procedure or add independent evidence.

## Verification planning

Queue a synthetic edit before removing its member, retain the connection, and deliver the edit on each side of the supplied cutoff. Observe ingress, commit and live state delivery separately. Compare a still-permitted member's operation. Pass requires the stated policy and permitted behavior; fail requires an out-of-policy commit or new delivery. Missing ordering, membership or recipient observations are inconclusive.

Submit two permitted text edits alongside a forged actor/ownership/history mutation, then inspect authoritative state and attribution. Independently emit presence, cursor and notification payloads after removal. Pass requires permitted edits, preserved invariants and only entitled recipients; an unauthorized mutation or audience disclosure fails. Missing merge, policy or recipient evidence is inconclusive. These are proposed, not-run designs, and authorize no execution.

The [artifact contract](../../reference/artifact-contract.md) is an optional expanded reference. Technology-specific configuration, APIs and version rules belong in exact resolved external secure-coding packs. Without those tools or packs, retain an unverified dependency and continue architectural analysis.

Source scope: the cited OWASP guidance supports threat-modeling structure, per-action authorization and long-lived session checks. The collaboration lifecycle and audience questions are authored workflow guidance; audience policy, ordering and merge behavior require supplied system evidence.
