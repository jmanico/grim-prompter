---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# High-assurance and isolated systems threat modeling

Use this set to examine supplied security domains, controlled imports and exports, removable media, administrators and offline maintenance. Isolation is not assurance. This analysis does not certify a system or establish that a proposed mechanism works.

## Choose an entry point

Run the [quick role](../../quick/high-assurance-isolated.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder for a bounded TM_REPORT with analysis_depth quick. For deep work, run each stage under the runbook, reading its complete preceding JSON artifact from the run folder. Only SYSTEM_UNDER_REVIEW is external; prior models, rubrics and separately executed fragments are optional bundle attachments. The prompts embed their contracts and baseline; optional methods are not prerequisites, and read-only project access follows the runbook.

| Stage | Required input | Output |
| --- | --- | --- |
| [00-scope-and-evidence](00-scope-and-evidence.md) | `SYSTEM_UNDER_REVIEW` | `TM_CONTEXT` |
| [01-system-model](01-system-model.md) | `TM_CONTEXT` | `TM_SYSTEM_MODEL` |
| [02-threat-analysis](02-threat-analysis.md) | `TM_SYSTEM_MODEL` | `TM_ANALYSIS` |
| [03-challenge-and-consolidate](03-challenge-and-consolidate.md) | `TM_ANALYSIS` | `TM_REVIEWED_MODEL` |
| [04-treatment-and-validation](04-treatment-and-validation.md) | `TM_REVIEWED_MODEL` | `TM_TREATMENT_PLAN` |
| [05-report-and-handoff](05-report-and-handoff.md) | `TM_TREATMENT_PLAN` | `TM_REPORT` |

Empty or unavailable evidence produces partial output and targeted gaps without waiting for answers. For chunked input, supply all consistent parts; one chunk is not a full model. Only when a tool limit prevents writing output as one artifact file, use the prompt's bounded continuation rules and retain every part before the next stage. Proposed tests, decisions and controls never become executed or approved merely by appearing in a report.

## Evidence worth supplying

- What security domains, sensitive research outputs and permitted directions of transfer does the supplied policy define, including physical and removable-media paths?
- Who establishes artifact provenance, who approves transfer of those exact bytes, and who validates their content before the isolated domain uses them?
- What happens between review and use: media custody, replacement, staging, parsing, quarantine, acceptance, rejection and retained evidence?
- What export authority binds the released content, recipient and purpose, including attachments, metadata, hidden fields and diagnostic output?
- Which administrators can change validation, release policy, audit records or the identities of approvers, and what separation is actually required and enforced?
- Who authorizes offline maintenance and recovery, which trusted state is restored, and what happens to pending transfers, old approvals, evidence and temporary privileges?
- Which scoped observations support assurance claims, what assumptions do they depend on, and which changes would invalidate them?

## Boundary and lifecycle checks

1. Trace the security-domain crossing from the external source through staging and removable-media custody to acceptance and use. Include supplied physical, service and intermittent maintenance paths; no network route does not mean no input path.
2. Keep artifact provenance, approved transfer and content validation separate. A known producer or signed artifact does not authorize its transfer or prove acceptable content; a scan result does not establish provenance. Bind each decision to the actual artifact, revision, destination and purpose that the supplied policy covers.
3. Examine review-to-use substitution, parsing and transformation, quarantine failure, rejected media reuse and stale validation results. Establish the reachable processing path and its privileges; do not infer perfect sanitization or an exploitable parser from missing evidence.
4. Trace exports from protected data through release review to the exact released representation and recipient. Include supplied embedded content, metadata, attachments and diagnostics. Approval of a visible summary is not necessarily approval of its hidden content; keep export authority distinct from import approval.
5. Model administrative separation against the caller's actual policy: who may propose, approve, execute, change checks and alter evidence? Different account names do not prove independent authority. Do not invent a universal two-person rule, assume collusion, or treat every shared administrator as a defect.
6. Follow offline update acceptance separately from permission to initiate installation, activate a new state, or restore an older one. Trace the provenance and applicability of the restored validation/export policy and its approval state; authenticity alone does not settle rollback authority.
7. Follow emergency maintenance and recovery through degraded operation, evidence retention, temporary access, revocation and return to normal. State what recovery may lose or reintroduce and whose authority permits each transition; restoration of service alone is not proof of restored protection.
8. Challenge assurance claims against their evidence, assumptions, system revision and covered failure paths. Isolation is not assurance. A bounded protective observation narrows a scenario only within its scope; a threat model is not certification or proof of absence of unauthorized flows.

## Mixed architecture and optional methods

For mixed cicd-supply-chain scope, trace the same update artifact from build/release provenance to offline transfer, local acceptance, installation and recovery. Keep one shared artifact ID and scoped evidence identity when the caller establishes they are the same object. Assign each boundary one owner: the supplied build/release boundary may belong to cicd-supply-chain while local transfer, export and maintenance boundaries belong to high-assurance-isolated. Unknown ownership stays null with an open identity gap. A release approval does not grant local transfer or installation authority; local export approval does not authorize publishing build artifacts. Do not merge findings with different actors, approval scopes or failure conditions. Preserve both contributors on genuine cross-set threats, original fragment namespaces and one disposition per source identity across revisions. Repeated release reports derived from one observation are not independent corroboration. Similar names do not establish identity or ownership.

The default stride-per-element identity names a separately available procedure. These prompts carry an independent STRIDE-style baseline and never claim the full procedure ran merely from selection. Optional methods run separately and contribute portable fragments. Keep technology-specific rules in exact externally resolved secure-coding packs; without access, record the unresolved dependency and continue architectural outcomes with those prescriptions unverified.

## Verification planning

- Transfer proposal: in an independently authorized synthetic environment, compare the exact approved import satisfying content-validation criteria with a changed artifact on the same media, a known-producer artifact lacking local transfer approval, and an artifact with valid provenance and local transfer approval whose content violates the supplied validation criteria. Supply provenance, transfer policy, validation criteria and acceptance observations. Pass requires the intended approved content to be accepted and changed, unapproved or content-invalid content to be denied before use under that policy; fail is observed unauthorized or content-invalid acceptance or use; missing criteria or observations is inconclusive. Keep provenance failure, approval failure and content rejection distinguishable. This proposal does not authorize connecting media to a real isolated system.
- Export proposal: with authorized synthetic test data and a supplied release policy, compare an approved report with a representation containing an unapproved embedded attachment or metadata field, and with a changed recipient. Pass requires only the approved content/recipient combination to leave the domain; fail is observed release outside that scope; absent visibility into the released bytes or authority is inconclusive. A successful sample does not prove all covert or hidden channels absent.
- Recovery proposal: with a caller-authorized rehearsal, explicit recovery authority and a supplied protected-state definition, restore a prior snapshot while a transfer is pending. Observe policy version, old approvals, audit continuity and temporary administrator revocation before normal operation resumes. Pass requires the supplied protection and recovery criteria to hold; fail is an observed unauthorized transition or lost protection contrary to those criteria; missing state, authority or observations is inconclusive. Leave the verification not_run and never conduct real recovery from this prompt.

## Limits

No live behavior, formal assurance, certification or readiness is established. Empty input produces targeted gaps, not generic defects. Only when a tool limit prevents writing one artifact file, split output into the runbook's part files using the embedded continuation contract; no single chunk is a complete predecessor.
