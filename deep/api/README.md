---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# API Threat Modeling

Follow authority through API callers, identity, resource ownership, gateway admission, backend operations and external callbacks. Start with whatever sanitized system evidence exists. Missing evidence becomes a gap; no interview, shell or optional method file is required.

For a bounded first pass, run [Quick API Threat Analysis](../../quick/api.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder. It returns JSON `TM_REPORT` with `analysis_depth: quick`, proposed outcomes, tests not run and explicit limits. It does not claim a deep challenge ran.

For deep analysis, run each stage under the runbook, reading its cumulative input file from the run folder. Keep the entire JSON artifact, including attachments, evidence, source identities, counterevidence and uncertainty.

| Prompt | Input | Output |
| --- | --- | --- |
| [00 Scope and evidence](00-scope-and-evidence.md) | `SYSTEM_UNDER_REVIEW` | `TM_CONTEXT` |
| [01 System model](01-system-model.md) | `TM_CONTEXT` | `TM_SYSTEM_MODEL` |
| [02 Threat analysis](02-threat-analysis.md) | `TM_SYSTEM_MODEL` | `TM_ANALYSIS` |
| [03 Challenge and consolidate](03-challenge-and-consolidate.md) | `TM_ANALYSIS` | `TM_REVIEWED_MODEL` |
| [04 Treatment and validation](04-treatment-and-validation.md) | `TM_REVIEWED_MODEL` | `TM_TREATMENT_PLAN` |
| [05 Report and handoff](05-report-and-handoff.md) | `TM_TREATMENT_PLAN` | `TM_REPORT` |

Only `SYSTEM_UNDER_REVIEW` enters from outside the chain. Optional prior models, risk rubrics and separately executed method fragments travel in typed portable attachments. Selecting a method does not execute it. The built-in security scenario questions are named lenses; missing procedure text or a workshop deck does not block them. Each prompt embeds its contract. The expanded [artifact contract](../../reference/artifact-contract.md) is optional.

Each revision compares against its supplied immediate parent. Prior change declarations become sanitized history attachments; the current `changes` list describes only current record deltas. No usable parent means null parent and empty changes. A single incoming chunk is not a whole predecessor: reassembly needs all indices, consistent metadata and resolved references. Missing or conflicting chunks yield explicit partial coverage. Only when a tool limit prevents writing one file, split prose into part files at section boundaries or JSON into the runbook's part files using the embedded continuation contract.

## Evidence questions

- Who can call each operation, and what identity, issuer and intended resource audience reaches the backend after gateway admission?
- Which customer owns each resource, and where are object, function and read/write property permissions decided? Which evidence covers changing an identifier?
- How do bulk selection, export execution and result retrieval carry the requesting principal? What happens after revocation, ownership change or job delay?
- Which competing state transitions and business effects are permitted? What is the commitment point, and what should retry, duplicate or concurrent requests do after an unknown outcome?
- Who can register or change a callback destination? Which destination and redirect transitions are permitted, and what can the outbound worker reach?
- Which resource properties leave in notification payloads? Which external response fields reach downstream processing, and can any change business state?
- Is there a separate external status channel? What authenticates its source and correlates it with a resource, without giving caller notification acknowledgments the same authority?
- What scopes do the actual observations cover? Which revisions disagree, and which worker, response, recovery or identity paths have no observation?

## Analysis boundaries

Keep gateway admission separate from backend object authority, and object permission separate from function and property permission. Follow each resource through normal calls, bulk lists, delayed export work and download. Compare replay, duplicates and concurrent operations with the supplied invariant rather than an assumed exactly-once guarantee. Follow destination changes and redirects through the outbound worker, then trace outbound data and returned fields separately. Include cancellation, revocation, retained outputs and recovery where evidence supports them.

Three scenario families guide the analysis: cross-owner object selection; privileged-operation replay or sequencing; and callback destination/response trust. They are not three required defects. A design can support a conditional hypothesis. A scoped protective observation can defeat it on that path. One passed GET test cannot establish export or callback protection, and a configurable callback alone cannot establish SSRF or data exposure.

When adding `identity-federation`, keep one global principal and resource identity, preserve each source namespace, and give each boundary one owner. Shared threats and controls retain API and federation tags. Do not claim the optional identity role ran just because both identities appear in the model.

## Verification planning

In an authorized isolated setup, use test accounts and resources with known ownership. First write the expected allowed, denied or unknown outcome for each actor, resource, action and property from the supplied policy, including an ordinary principal attempting any operation reserved for a privileged role. Signing in as a test account proves no entitlement, and an unknown expectation makes that path inconclusive. Compare allowed access, a changed object identifier, a mixed-owner bulk export, delayed execution after a supplied revocation event and retrieval by the wrong principal. Observe both returned fields and worker/result behavior. A pass is scoped to each observed path; missing worker evidence is inconclusive.

Use inert callback receivers under the test owner's control with synthetic payloads. Every permitted or disallowed destination and redirect target must be an inert receiver controlled by the test owner. Compare allowed and disallowed destinations and redirects; inspect the transmitted fields and the state affected by returned acknowledgment fields. Test any legitimate external status update on its separate authorized channel. A forbidden transmission or unauthorized business-state change is a failure; absent outbound or downstream traces are inconclusive. Do not probe internal, third-party or production destinations.

For a supplied competing state-transition invariant, propose replay and concurrent requests against an isolated downstream test sink. Compare actual committed effects and final state with that invariant, including retry after an unknown outcome. A transport response alone is insufficient. All these checks are plans, not execution authority or test results.

Technology recipes remain in exact resolved secure-coding packs that the caller supplies. Without those tools or a matching pack, disclose the dependency, identify the resolver result needed and continue with architectural outcomes. Never invent a pack identity.
