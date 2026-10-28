---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# Monolithic application threat modeling

Use this set for a supplied application whose business functions share a deployment/process boundary. It examines internal authorization and shared data/resource effects without treating every module as a separately isolated service. It does not certify security or prove that a design concern is implemented.

## Choose an entry point

For one unattended pass, run [Monolith quick threat analysis](../../quick/monolith.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder. It emits TM_REPORT with analysis_depth quick, explicit omissions and proposed next verification. Optional method files, tools and a registry are not prerequisites.

For deeper work, run the next stage under the runbook, reading the preceding complete JSON artifact from the run folder. Only SYSTEM_UNDER_REVIEW is required from outside the chain. It may contain an optional prior model, risk rubric or separately executed method fragment as typed attachments; an instruction prompt is not execution evidence. The chain preserves the entire cumulative model and current-parent change declarations, not hidden session state.

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

- Which external caller or operator can enter each public and administrative route, and what operation is each allowed to request?
- Which internal calls can reach privileged business functions, including imports, reports and notification callbacks that bypass the ordinary route?
- Which shared credentials or execution identities can read or change each business function's data, and where is narrower caller authority enforced?
- What actor, tenant, object and authorization context survives a background handoff, retry or resumed task?
- Which costly functions share workers, database capacity or other finite resources with critical workflows, and what evidence defines acceptable degradation?
- Which cross-function business invariants must survive partial completion, recovery and operator intervention?
- Who can change shared configuration or operational actions, and which evidence distinguishes their authority from ordinary application callers?

## Boundary and lifecycle coverage

1. Trace external caller authority through the route to the final privileged function. Authentication or reaching an internal call is not proof of authorization for its action and object. Include alternate internal, import and operator paths that the supplied evidence identifies.
2. Examine internal privilege transitions across business functions. Model a module boundary as a logical responsibility or authority boundary when justified, not automatically as process or network isolation. Identify the enforcing operation and counterevidence rather than treating a shared process as a defect.
3. Follow shared credentials and data authority across otherwise unrelated functions. Distinguish what the process identity can access from what a caller can cause it to access; establish the reachable path, resource and intended restriction before stating a hypothesis.
4. Trace background work from submission through execution, retries and cancellation. Preserve actor, tenant and object context when supplied; missing attribution is a gap, while a supplied proposed context-loss condition can ground a hypothesis. Keep actual separate workers distinct from in-process tasks.
5. Follow costly work into shared finite resources and the critical workflow that depends on them. Use supplied demand, capacity and recovery evidence; do not invent thresholds or infer denial of service solely from co-location. Include admission, bounded work, degradation and recovery as candidate outcomes where relevant.
6. Check cross-function transaction and recovery invariants. Distinguish a failed request from committed side effects; consider supplied partial-completion, repeated-import and resumed-report behavior without assuming every retry duplicates effects.
7. Trace shared configuration, administrative controls and emergency actions. Keep operator permissions, deployment authority, business-data authority and recovery authority distinct, and preserve any observed constraints on their scope.

## Optional methods and mixed architecture

The default registered method is stride-per-element. The copied baseline provides evidence-linked STRIDE-style questions independently; it does not claim the registered method's full procedure ran. For that procedure, run the separate method role and attach its versioned fragment. Keep privacy, abuse or operational considerations as explicit lenses unless a separate procedure was actually performed.

When a separate batch-workflows subsystem is supplied, keep monolith as the owner of its shared-process/function boundaries and use the caller's declared owner for each scheduler, job or shared-data boundary. If ownership is unknown, use null with an open identity gap. Reuse the same member, tenant, data and boundary IDs across both views; do not clone one object or observation merely because two architecture lenses discuss it. Trace job parameters, execution identity, intermediate outputs, reruns and recovery only where supplied, without pretending the batch-workflows role or its full procedure ran. Keep a cross-set threat's actual architecture contributions and distinguish job authority from the monolith's internal call authority. A separate worker is not implied by the word background.

## Verification planning

- Privileged-operation proposal: with caller-authorized synthetic ordinary and operator identities, compare the same protected operation through its ordinary route and a supplied alternate internal/import path. Pass means the supplied operation/object policy holds on every tested path; fail means a disallowed actor produces the protected effect; inconclusive means the path, observation or execution authority is missing. Do not run this proposal.
- Resource/recovery proposal: with explicit authority, a bounded synthetic workload and caller-supplied capacity/latency/recovery criteria, exercise the costly feature while observing the critical workflow and its recovery after work stops. Pass means those supplied criteria hold; fail means an observed violation attributable to the tested shared resource; inconclusive means missing criteria, attribution or observations. Never invent numeric limits or claim an experiment ran.

## Limits

Keep technology-specific implementation rules in exact resolved secure-coding packs; absent pack access leaves those prescriptions unverified while architectural analysis continues.
