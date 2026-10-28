---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# Identity and Federation Threat Modeling

Analyze assertion authority, account linking/recovery and trust changes across human sign-in services. Supply any available sanitized description, diagram, policy or observation; missing information becomes gaps without an interview pause. This is architectural analysis, not a compliance assessment or a protocol configuration guide.

Run [Quick Identity and Federation Threat Analysis](../../quick/identity-federation.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder for a bounded `TM_REPORT`. It discloses omitted deep work. For the deep path, run each stage under the runbook, reading its cumulative input file from the run folder and preserving the full JSON and attachments.

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

- Which issuer-qualified subject, recipient, initiating session and intended use does each assertion represent, and what observed acceptance checks bind them?
- Which local account is resolved, and what establishes control before linking another identity? Can attributes collide or be reassigned across internal and external issuers or after an affiliation change?
- Who can start recovery, and who can authorize the final replacement/link? What happens on retries, concurrent requests, cancellation and link removal?
- Who can change trust, registration or key sources? Which configuration revision has each connected relying service actually adopted?
- What does the caller's policy require of existing sessions after signout, trust withdrawal, key change or loss of affiliation? What evidence exists per connected service?
- Which tenant/resource operation follows authentication, and where is its current permission decided independently of assertion validity?
- Which attributes and linkage records reach external or partner applications, for which use, with what retention or correlation limits?
- What detection, dispute and recovery evidence distinguishes an authorized correction from account takeover?

## Identity and federation scope and boundary checks

Include architecture identity `identity-federation` as this requested lens, preserving caller-selected and carried architectures. A selected lens is not a performed method. Identify human subscribers, issuers, relying services and identity administrators from evidence; do not infer a protocol, product, assurance level or trust relationship from a sign-in label. NIST federation guidance informs human digital identity questions here; it does not establish workload authorization, a universal compliance obligation or application permission policy.

Apply these checks to the supplied scope; preserve unknowns and protective alternatives.

1. Trace assertion issuance and reception separately. Identify the issuer-qualified subject, intended relying service, initiating session and intended use. Ask what binds those values at acceptance, including freshness and repeat presentation. A valid signature alone does not establish that this recipient or transaction is authorized to use the assertion.
2. Follow the accepted identity into each protected operation. Distinguish authentication/assertion validity from per-operation tenant/resource authorization, including data exports and administrative actions. Attribute values and affiliation labels are evidence inputs, not automatic grants; identify their authority, currency and local policy.
3. Map account resolution separately from linking: an identifier match locates a candidate account but does not prove control of that account. Check collisions across issuers, reassigned attributes and affiliation or role changes without merging identities by display name or email alone. Ask what evidence establishes the intended account relationship and its permitted consequences.
4. Separate initiating recovery from permission to replace or link an identity. Follow the requester, target account, existing and new identity, approval scope and final mutation; include cancellation, concurrent attempts, fallback and removal of a link. Do not infer takeover merely because a recovery path exists.
5. Trace who may add or remove an issuer, change a relying-service registration or alter the trusted key source. Separate authorized trust administration from ordinary account management. Identify each connected service's accepted configuration revision, propagation evidence, failed updates and rollback authority; a published change does not prove every consumer adopted it. Distinguish planned key overlap from emergency withdrawal; an explicitly authorized overlap window is not itself a defect.
6. Follow key transition and trust withdrawal through both new assertions and existing relying-service sessions. Keep assertion validity, issuer session, local account state and downstream session lifetime distinct. Ask what the caller's intended revocation policy requires and what each service actually does, including a disconnected or externally operated service; do not assume key replacement or IdP signout terminates every session.
7. Track identity attributes and linkage records to their recipients and uses. Distinguish necessary resolution data from unrelated disclosure or correlation across user populations and external partner contexts. A shared person does not imply permission to share every attribute or resource.
8. Examine disputed linking, rejected assertions, trust-change detection and recovery from an incorrect link or stale grant. Preserve attribution and safe recovery evidence without repeating assertions, secrets or unnecessary personal information. Ask what distinguishes an authorized correction from another unauthorized replacement and what remains usable during an outage.

Use these as evidence and coverage checks, not a required defect list. Record protective alternatives and unresolved evidence. Keep exact protocol settings, APIs, versions and cryptographic prescriptions in resolved secure-coding packs; missing tools or packs leave those rules unverified while architectural analysis continues.

For mixed `multi-tenant-saas` scope, reuse global subject, relying-service, tenant and resource IDs. Keep the issuer-to-relying-service federation boundary separate from the relying-service-to-tenant-resource authorization boundary: one evidenced owner per crossing, with null ownership and an open identity gap when unknown. Preserve both contributions on shared threats and controls; do not invent execution of the partner role. For a previously mapped source model, namespace and source ID, keep its one existing identity disposition across newer source revisions. Preserve mapping ID and original source revision/provenance; add corroboration, not another per-revision alias. New source snapshots get separate sanitized attachments without overwriting prior history.

## Verification planning

Three verification designs are available only as proposed `not_run` work, adapted to the supplied scenario and requiring separate execution authorization. First, compare a valid intended sign-in with an assertion for another recipient, another initiating session, a repeated presentation and the same subject string from a different issuer. Observe issuance context, acceptance decision, local account and resulting session; then separately observe a permitted resource operation and a forbidden operation on another tenant's or user's resource. Pass requires the intended cases to work and each unauthorized case to be rejected at its relevant boundary. Wrong-context acceptance or an unauthorized resource effect fails. Missing assertion context, decision, session or resource observations are inconclusive; a denied resource operation alone does not prove assertion rejection.

Second, compare an authorized account link/recovery completion with a request that merely knows the target identifier or can initiate recovery. Observe who controls the existing and new identity, who authorizes the final mutation, concurrent/retried completions, resulting links and later access through removed links. Pass requires the intended authorized change and rejection of unauthorized replacement or residual access under the supplied policy. An unauthorized link, replacement or forbidden subsequent access fails. Missing control, final-link or access evidence is inconclusive. A notification or accepted recovery request alone does not establish permission to replace the identity.

Third, for trust withdrawal or key transition, propose observing each connected service before and after an authorized change, testing new assertion acceptance separately from existing sessions against the caller's revocation policy. Pass needs observed adoption and session behavior meeting that policy; a forbidden acceptance or retained authority fails; unknown policy, consumer revision or session behavior is inconclusive. Do not invent a universal session cutoff or claim any example ran.

The [artifact contract](../../reference/artifact-contract.md) is an optional expanded reference, not another required input. Each prompt includes its own contract and tool fallback. Only when a tool limit prevents writing one file, split JSON into the runbook's part files using its chunk protocol or prose into part files at section boundaries; keep a continuation record and disclose undelivered work.
