---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# Batch workflow threat modeling

Use this set to analyze supplied batch jobs and scheduled workflows, their run authority, partial completion and intermediate data lifecycle. No particular scheduler, storage product or business domain is required.

## Choose an entry point

For one unattended pass, run [Batch workflow quick threat analysis](../../quick/batch-workflows.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder. It emits TM_REPORT with analysis_depth quick, explicit omissions and proposed next verification. Optional method files, tools and a registry are not prerequisites.

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

Use these questions to select evidence you already have. Run the quick role under the runbook with your sanitized system evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder. For deeper work, run stage 00 with that file, then read each complete output file in the next stage. Missing answers become gaps; no interview is required, and read-only project access follows the runbook.

- Which scheduler identity may start which versioned job, and who may change its schedule or parameters?
- Which initiating person or operator requested this logical run, and which execution identity performs each privileged operation?
- What immutable input snapshot, job definition/version, parameters, scope and output destination does the business approver authorize? What happens if one changes afterward?
- What distinguishes a logical run from each attempt, overlapping invocation, manual rerun or resumed step?
- Which supplied state transitions and business invariants distinguish a checkpoint, partial output, completed export and downstream acknowledgment/effect?
- Who may read copied, staged, failed-run and restored intermediate data, under which caller-supplied retention and operating rules?
- Which alternate start, repair, replay and export-consumption routes are known, and what evidence establishes their authority and boundary owner?

## Boundary and lifecycle coverage

The three families—changed run intent, repeated or partial work, and intermediate-data exposure—are reasoning targets, not mandatory defects. Apply the checks to supplied paths, retain protective counterevidence, and disclose unsupported coverage.

1. Trace schedule configuration and each start route to the versioned job. An authenticated scheduler or successful start is not business approval.
2. Bind the input snapshot/version, job definition/version, parameters, run scope and output destination to the actual approval tuple. Correct parsing does not authorize the contents; changes after approval need their own evidence.
3. Follow initiating/operator identity into execution identity and each action/resource grant. A broad allowed runtime grant does not establish narrower run intent; an explicit denial blocks only its exact effect and route.
4. Separate logical run identity from attempt identity. Examine rerun and overlap before a checkpoint using supplied state and coordination rules, without assuming every retry duplicates effects or any universal exactly-once guarantee.
5. Trace partial output before the completion marker, restart, resume and recovery. Count distinct exports separately from downstream acknowledgments and business effects; neither produced nor marked-complete output proves consumption, authorization or settlement.
6. Follow sensitive intermediate data across workers, staging, failed attempts, logs and storage. Compare each reader against the supplied audience rather than treating every copy as a disclosure.
7. Compare cleanup with retained/restored copies and the caller's retention and operating rules. Identify what survives deletion, what can be restored and which readers regain access; invent no fixed duration.
8. Preserve the evidence linking run, attempt, source revision and output identity through audit and recovery. Missing routes, grants, boundary ownership or coordination/reservation points produce targeted gaps, not inferred safe or unsafe execution.

## Mixed systems and methods

When data-platform is supplied, trace the actual producer → ingestion → transformation → store → batch consumer relationship. Reuse global source, record, dataset revision, run and export IDs. Follow transform lineage into the approved input snapshot and run/export boundary; a revised transform can change that binding even when a filename stays the same. Distinguish data owner, ingestion admission and notebook runtime authority from scheduler, execution identity, business approver and export consumer authority. Give each boundary one evidence-supported architecture owner, or null with an open identity gap; missing boundary topology has an open topology gap. Flow endpoints are assets, actors or entry points; boundary sides are zones or assets, never data records. Tag a threat with both architectures only when its actual path crosses their responsibilities. A shared observation is not independent corroboration and selecting the companion does not mean its procedure ran.

The standalone STRIDE-style baseline uses coverage lenses, not a claim of completed method execution. Optional methods run separately and arrive as typed fragments.

## Verification planning

Retention, cleanup authority and restore rules must come from the caller, including who may remove or restore each copy. Missing rules or authority remain gaps; the sources do not prescribe a universal retention duration.

- Approval-binding comparison: propose an authorized synthetic comparison of the approved input/job/parameter tuple with a changed input version and a changed parameter, across every supplied start route. Pass requires the allowed tuple to reach only its intended export and the changed tuples to be rejected before that effect. Fail requires an observed mismatched tuple producing the forbidden export. Missing route, decision authority or outcome evidence is inconclusive; scheduler authentication and parse success cannot fill it.
- Recovery comparison: propose two attempts of the same logical run, an overlap before checkpoint, and a failure after partial export but before completion marking. Compare the supplied invariant with export identities and separately evidenced consumer acknowledgments/effects. Pass requires that invariant to hold on those traces; fail requires its observed violation; missing consumer evidence leaves downstream effects inconclusive even if duplicate exports are demonstrated.
- Intermediate-data comparison: propose authorized synthetic allowed and forbidden reads after failure, after cleanup and after restore. Pass requires the caller's audience/retention rules to hold on every tested copy; fail is an observed forbidden read or retained copy contrary to that rule; missing copy inventory, policy or observation is inconclusive. These proposals do not authorize execution and remain not_run.

## Limits

Reports remain bounded hypotheses and proposed verification; technology prescriptions need exact resolved packs or an unverified dependency gap.
