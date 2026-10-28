---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# Multi-tenant SaaS Threat Modeling

Trace who may act for which tenant through shared services, data partitions, reports, support access and tenant settings. Start with any sanitized system description or portable evidence bundle. Missing evidence becomes explicit gaps; no interview is required, and read-only project access follows the runbook.

For a bounded first pass, run [Quick Multi-tenant SaaS Threat Analysis](../../quick/multi-tenant-saas.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder. It returns JSON `TM_REPORT` with `analysis_depth: quick` and names unperformed deep work. For the deep path, run each prompt under the runbook, reading the whole named cumulative JSON handoff from the run folder:

| Prompt | Input | Output |
| --- | --- | --- |
| [00 Scope and Evidence](00-scope-and-evidence.md) | `SYSTEM_UNDER_REVIEW` | `TM_CONTEXT` |
| [01 System Model](01-system-model.md) | `TM_CONTEXT` | `TM_SYSTEM_MODEL` |
| [02 Threat Analysis](02-threat-analysis.md) | `TM_SYSTEM_MODEL` | `TM_ANALYSIS` |
| [03 Challenge and Consolidation](03-challenge-and-consolidate.md) | `TM_ANALYSIS` | `TM_REVIEWED_MODEL` |
| [04 Treatment and Validation](04-treatment-and-validation.md) | `TM_REVIEWED_MODEL` | `TM_TREATMENT_PLAN` |
| [05 Report and Handoff](05-report-and-handoff.md) | `TM_TREATMENT_PLAN` | `TM_REPORT` |

Only `SYSTEM_UNDER_REVIEW` is external. Optional prior models, caller rubrics and separately performed method fragments travel in typed portable attachments with provenance. Missing method files, decks, tools or secure-coding packs never block the embedded baseline. Named security questions are coverage lenses; method selection is not method execution. A partial chunk is not a predecessor: collect every index and check reassembly before using its records as a baseline. Preserve sanitized history and declare only the actual immediate-parent changes.

## Evidence questions

- What verifies tenant selection, current actor membership and permission for the particular record or report operation? Which target tenant owns the resource?
- Which query paths, reused execution contexts and cache recipients carry that verified identity? What changes when membership or permissions change?
- What binds a queued report job to its authorized producer, tenant and resource? What does a worker recheck after delay, retry or reuse?
- Who may request an export, generate it, retrieve it later or retain it after revocation/offboarding? What observation identifies the returned contents and owner?
- Which powers belong to tenant administrators, and which require a separate platform support grant? What constrains support impersonation, expiry and audit access?
- Which settings are tenant-specific, which intentionally affect the shared service, and which other consumers could a change reach?
- Where do queue depth, worker concurrency and costly reports contend for capacity? What limits and recovery observations exist beyond ingress rate limiting?
- What happens to current membership and retention policy when a tenant is restored from a shared backup? What evidence separates the restored tenant from others?

These are evidence needs, not a blocking interview. The prompts run unattended and disclose unavailable material.

## Boundaries and counterexamples

Check identity-to-query, query-to-cache-recipient, producer-to-worker, export-creation-to-retrieval, tenant-admin-to-support, tenant-configuration-to-shared-behavior, tenant-demand-to-worker-capacity and offboarding-to-restoration separately. Follow verified identity and resource ownership throughout. Login alone establishes neither object entitlement nor role authorization. A source design or missing enforcement trace supports a question, not an observed defect.

Keep deliberately shared data and authorized platform support operations as protective counterexamples. A synthetic passing query result covers that query and actor/resource matrix; it does not establish protection for cache hits, delayed work or exports. Conversely, a shared worker or backup does not establish leakage. Preserve conflicts until observation resolves them. In a mixed data-platform view, transformations retain source-record/tenant provenance and output entitlement; use one global ID per shared element, one owner per boundary and all contributor architecture tags. This does not imply a separate role was run.

Map enqueue, worker execution, export write, publication and retrieval to their actual endpoints and boundary sides. A downstream or upstream boundary is not crossed merely because it belongs to the same report path. Retain existing entity IDs and provenance; give a distinct handoff its own boundary when supported, and record open topology or identity gaps for unknown relationships or owners. A boundary description does not establish enforcement, permission or method execution.

## Safe verification designs

Derive an allow/deny/unknown matrix from supplied tenant memberships, resource ownership, operations and deliberately shared data. Plan isolated checks for query, cache, delayed jobs and export retrieval, including membership revocation before execution or retrieval. Observe content, persistent effects and actual path use, not HTTP status or authentication alone. Pass requires all observed allowed and denied cases to match policy; a matrix violation fails; missing ownership, membership, policy or path observations is inconclusive.

For administration, distinguish tenant administrator authority from delegated support grants. Derive allowed operations, tenant scope, expiry and revocation from supplied policy. Plan isolated checks for permitted operations, out-of-scope tenants, writes outside the grant, shared-setting changes and expired grants. Observe content, configuration consumers, effects and delegation/audit scope. Pass requires the intended allows and denies; an out-of-grant effect fails; missing grant or effect evidence is inconclusive. Do not execute privileged impersonation during modeling.

For capacity, propose only bounded isolated jobs with caller-supplied budgets and observable queue age, worker concurrency and completion. No production stress. Ingress responses do not prove worker isolation. A bare assertion that a quota is configured or proposed remains a claim about its presence, not an implementation observation. Mark a quota control implemented only with implementation observation evidence, and preserve that supported status even without a scheduling test. Its effectiveness remains unverified until actual effectiveness observation evidence and a passed Verification referring back to the control support tested status; the Verification must have execution evidence. Scheduling observations support only the exercised workload and budgets, and do not bypass these requirements. All new test designs remain `not_run` until actual authorized execution evidence is supplied.

The [expanded artifact contract](../../reference/artifact-contract.md) is optional; every prompt embeds its needed definitions. If unavailable, say local validation was not run and continue. Resolve technology-specific prescriptions through exact secure-coding packs when available; otherwise record an unverified dependency without inventing settings or pack names.
