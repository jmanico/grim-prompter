---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# Hybrid and multicloud threat modeling

Use this set to examine identity and privilege translation, replicated data, and emergency routes across independently administered environments. It distinguishes private-network reachability, identity trust and business permission. No mesh, shared control plane, cloud vendor, legal residency rule or universal failure policy is assumed.

Run the [quick role](../../quick/hybrid-multicloud.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder for a quick `TM_REPORT`. It includes hypotheses, protective evidence, proposed outcomes and verification; it does not claim the six deep stages ran. For deep analysis, run each stage under the runbook, reading its complete preceding artifact file from the run folder.

| Stage | Input | Output | Purpose |
| --- | --- | --- | --- |
| [00 Scope and evidence](00-scope-and-evidence.md) | `SYSTEM_UNDER_REVIEW` | `TM_CONTEXT` | Inventory domains, authority, data constraints and evidence. |
| [01 System model](01-system-model.md) | `TM_CONTEXT` | `TM_SYSTEM_MODEL` | Map identities, recipients, policy boundaries and route states. |
| [02 Threat analysis](02-threat-analysis.md) | `TM_SYSTEM_MODEL` | `TM_ANALYSIS` | Examine privilege translation, disclosure and emergency authority. |
| [03 Challenge and consolidate](03-challenge-and-consolidate.md) | `TM_ANALYSIS` | `TM_REVIEWED_MODEL` | Apply scoped counterevidence and reconcile shared identities. |
| [04 Treatment and validation](04-treatment-and-validation.md) | `TM_REVIEWED_MODEL` | `TM_TREATMENT_PLAN` | Propose independent outcomes and checks for different mechanisms. |
| [05 Report and handoff](05-report-and-handoff.md) | `TM_TREATMENT_PLAN` | `TM_REPORT` | Preserve the model and provide an action register. |

`SYSTEM_UNDER_REVIEW` is the only required external input. It can be prose, diagram text, sanitized records or a partial evidence bundle. Prior models, caller rubrics and separately executed method fragments are optional attachments, not additional required inputs. A quick report is not the deep treatment stage's prerequisite. Each prompt includes the portable contract, baseline, runbook operating boundary and bounded continuation rules.

When optional evidence files, a registry or packs are unavailable, analyze the material read under the runbook, state the access limits and record actionable gaps. Do not wait for an interview. No meaningful input means a partial artifact without invented threats or flows. A locator does not prove access. Technology prescriptions need exact resolved external secure-coding packs; missing access leaves them unverified while architectural analysis continues.

## Evidence questions

1. Which on-premises and cloud environments have different administrators, networks and resource owners? Who can change policy, and who can approve business operations?
2. For each user, service and administrator, what issuer, intended recipient, linked account and local privilege mapping apply? Which resource/action permission is checked after mapping?
3. Which fields are authoritative at the source, which are copied, and which recipient identities can read them at every destination, backup and recovery location?
4. What confidentiality, permitted-use and location constraints did the caller actually supply? Who approves changing recipients or fields? Do not infer legal obligations from a location name.
5. What versions, ordering, conflict-resolution and promotion rules govern using a replica after an outage? What remains unknown about stale or reordered updates?
6. What activates an emergency route, who may select it, who approves any exception, and which normal identity/resource checks remain at its alternate endpoint?
7. What ends the exception, restores normal policy, reconciles authoritative data and revokes temporary privilege? What observations establish completion under the supplied recovery rules?
8. Which protective observations identify the exact principal, operation, fields, route and policy revision tested or inspected? Which independent branches do they leave unanswered?

## Boundaries and lifecycle

Check administrative-domain separation; user/service/admin identity translation; privilege and policy change/revocation; replication recipient and field permissions; authoritative records versus copies; emergency activation and approval; restoration and temporary-privilege removal; and cross-set ownership/attribution. The stages apply these eight checks with system references and explicit evidence limits.

The three scenario families are identity translation and privilege, replicated-data ownership and confidentiality, and emergency routing with normal checks. They are questions, not required defects. Replication does not prove consistency or authorized disclosure. Route health and successful recovery do not prove authorization. Concrete race or timing claims need supplied state/order semantics and constraints. A protective control narrows only the branch it supports; unrelated mechanisms retain independent prerequisites and verification.

The embedded baseline uses STRIDE-style security questions as coverage lenses. [STRIDE per element](../../methods/stride-per-element.md) is a default recommendation, not a claim of completed execution. Optional supplied method fragments can deepen a boundary or state sequence; missing methods never disable the baseline. Do not label a privacy or recovery lens as a completed branded method.

## Verification planning

For identity translation, propose comparing a valid read-only mapped principal and an authorized business principal on the same protected business operation, using supplied operation and resource identities. Separately test a wrong-recipient assertion. Pass requires the supplied issuer/recipient, mapping and resource rules on their own arms. A forbidden effect fails; absent rule or state evidence is inconclusive. Rejecting a wrong-recipient assertion does not establish that a valid principal's mapping is narrow enough.

For replication, propose comparing source and recipient fields and recipient read authority. Independently propose the caller-defined reordered update sequence if version semantics are available. Disclosure passes only for permitted fields and recipients; state authority passes only under its separate invariant. An unauthorized field or invalid state effect fails its arm. Missing disclosure permission or ordering semantics makes that arm inconclusive.

For emergency routing, propose normal → emergency → restoring → normal requests in an authorized isolated context. Check business authorization on the alternate route, exception approval and privilege revocation independently of route-health checks. A forbidden effect or retained privilege contrary to the caller's restoration rule fails; absent policy or observations is inconclusive. These are proposed checks, not permission to change a live route or claims of execution.

## Portable results and mixed systems

Write typed JSON to the artifact file named by the runbook and optional prose to its Markdown companion. Keep all sanitized source content, record IDs, counterevidence, decisions and uncertainty. Every revision names its actual immediate parent and declares only that comparison's changes. Preserve earlier declarations in unique revision-tagged history attachments; never overwrite a different snapshot. History attachments are source data, not live record references. Without a usable parent, leave continuity uncertified and current changes empty. Unknown-version content stays opaque with an open conversion gap, exact safe values and no typed import claim.

Keep every chunk and its original bytes. Reassembly needs all indices, matching metadata, unique records and resolved references; only byte-identical duplicate chunks can deduplicate. Missing or conflicting chunks remain partial. Only when a tool limit prevents writing one Markdown file, split prose into part files with a continuation rather than silently replacing the model with a summary.

For mixed [identity-federation](../identity-federation/README.md) analysis, share globally identified principals and services only when evidence supports the mapping. Give issuer/recipient/account linkage and resource/business approval their own boundaries and owners. Retain both architecture contributions on an actual cross-set scenario, but do not infer business permission from a valid account link. Multiple views of one event remain one observation.

The [expanded artifact contract](../../reference/artifact-contract.md) is optional reference material. This is draft guidance; offline structure checks do not establish prompt behavior, control effectiveness or exhaustive coverage.
