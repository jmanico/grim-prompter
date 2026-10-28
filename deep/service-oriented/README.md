---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# Service-Oriented Threat Modeling

Use this set when service consumers interact through mediation, credential or message translation, or shared orchestration. It examines who can request an effect, what the message means after transformation, who can change the process, and what each recipient authorizes. It assumes no particular industry, topology, protocol or number of services.

For a compact review, run the [quick role](../../quick/service-oriented.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder. It returns a quick `TM_REPORT` with supported hypotheses, scoped protective conclusions, proposed outcomes and tests not run. It does not claim the deep challenge ran.

For deep work, run each stage under the runbook, reading its complete input file from the run folder:

| Stage | Input | Output |
| --- | --- | --- |
| [00 Scope and evidence](00-scope-and-evidence.md) | SYSTEM_UNDER_REVIEW | TM_CONTEXT |
| [01 System model](01-system-model.md) | TM_CONTEXT | TM_SYSTEM_MODEL |
| [02 Threat analysis](02-threat-analysis.md) | TM_SYSTEM_MODEL | TM_ANALYSIS |
| [03 Challenge and consolidate](03-challenge-and-consolidate.md) | TM_ANALYSIS | TM_REVIEWED_MODEL |
| [04 Treatment and validation](04-treatment-and-validation.md) | TM_REVIEWED_MODEL | TM_TREATMENT_PLAN |
| [05 Report and handoff](05-report-and-handoff.md) | TM_TREATMENT_PLAN | TM_REPORT |

`SYSTEM_UNDER_REVIEW` is the only external input. It may include any description, diagram text, requirements, sanitized excerpts and observations, plus optional prior models, risk rubrics or separately executed method fragments. Carry optional material in typed attachments. The stages use read-only project access and run-folder files under the runbook; absent material becomes gaps without waiting for answers. Empty evidence never produces an invented defect list. Use complete reassembled artifacts, not an isolated chunk. Every subsequent revision preserves records and declares only the changes from its immediate parent.

## Evidence to prepare

These questions identify useful evidence; the unattended stages continue when an answer is absent. Optional guided preparation uses at most five questions per batch and two batches unless the caller extends it; stop with a partial bundle when nobody answers.

1. Which caller, issuer, subject, recipient and intended use are accepted at each credential boundary, and which exact mapping produces the downstream identity?
2. Which actor/resource/operation constraints does the caller have, which does the mediator possess on its own, and what business approval does the recipient require?
3. Can you supply paired original/transformed messages and their versioned meaning, including owner, resource, approval scope and action versus notification?
4. Who may author, approve, publish, execute or restore an orchestration definition, and what evidence connects each privilege to the resulting service calls?
5. Which direct, legacy, asynchronous or operator paths bypass ordinary mediation, and what authorization applies on each direction?
6. How do revocation, changed ownership and updated mappings affect queued or in-flight requests? Which freshness requirement actually applies?
7. What distinguishes denial, committed-with-lost-reply and unknown outcome, and who may replay or compensate under current authority?
8. Which records link original caller, translated identity, execution principal, definition version and target decision to the actual result without exposing secrets?

## Analysis and verification

The baseline considers impersonation, tampering, accountability, disclosure, availability and privilege crossing as coverage lenses. It does not report a separately named method as executed. Three candidate families anchor the analysis: credential translation widens authority; message transformation changes ownership or security-relevant meaning; shared orchestration privileges cross separate service boundaries. Protective evidence can defeat any candidate. Record its scoped disposition rather than requiring a threat in every family. Missing implementation evidence remains missing evidence.

### Service-oriented boundary and lifecycle checks

Apply these conditional questions to supplied system IDs. Do not assume a central mediator, insurance domain, fixed service count, federation protocol or technology. An architecture label supplies no topology or protection.

1. **Caller and credential translation:** identify the initiating caller, credential issuer/subject, credential recipient and intended use. Follow each directional acceptance and translation into a distinct translated identity. State which actor/resource/operation constraints survive, narrow or expand, and cite the mapping evidence. Authentication is not delegation or target business approval.
2. **Mediator execution authority:** distinguish the process that mediates from its execution principal and the identity it presents downstream. Trace whether it acts for the caller or on its own authority, who granted that authority, and what the receiving service actually checks. A reachable route and an accepted credential alone do not authorize the requested resource operation.
3. **Message syntax and meaning:** follow action requests separately from event notifications, replies and faults. Compare original and transformed resource owner, subject, operation, approval scope and correlation. Schema validity does not establish equivalent meaning. Name who may alter mappings and which version each participant interpreted; an absent field in a diagram is an evidence gap, not proof it is dropped.
4. **Orchestration design versus execution:** separate authority to author, approve, publish or restore a process definition from authority to execute it and from each service's business approval. Trace a concrete cross-service sequence and its actor prerequisites. A process editor is not automatically a runtime administrator; establish the path that turns a changed definition into a privileged effect.
5. **Independent and alternate paths:** examine direct service calls, legacy interfaces, asynchronous work, operator overrides and manual recovery that bypass mediation. Record directional boundary ownership and the actor/resource/operation restriction on each. An observed denial on one path does not cover another; an unknown outcome is not a denial.
6. **Change and revocation:** trace changed credential mappings, issuer trust, resource ownership, transformation definitions and revoked delegation through queued and in-flight work. Identify the caller's freshness rule and what happens if a policy or identity dependency is unavailable. Do not invent universal time limits or infer failure-open behavior from absent evidence.
7. **Partial results and recovery:** distinguish a rejected action, a committed effect with lost reply, and an unobserved outcome. Follow retry, compensation, replay and restored definitions against supplied business invariants and current authority. Identify who may recover, what state is rechecked and which results remain uncertain; availability or transport success alone proves neither completion nor authorization.
8. **Attributable results and mixed boundaries:** retain initiator, translated identity, execution principal, definition version, target resource and actual decision/effect attribution where supplied. Minimize sensitive evidence. In mixed identity-federation scope use one global ID per caller, issuer, subject, mediator and resource, with evidence for each match. Give assertion acceptance/mapping a directional identity-federation boundary and delegation/business calls their service-oriented boundaries; each has one explicit owner. Both contributions must explain prerequisites or actor conditions, not merely add a tag.

Record coverage for each check at its actual scope. The three scenario families are credential translation changing authority, transformation changing ownership or security-relevant meaning, and orchestration privileges crossing otherwise separate services. They are analysis targets, not mandatory defects. If protective evidence defeats a family's enabling conditions, record that family's scoped protective disposition rather than inventing a residual threat. Preserve existing threat IDs and explain their revised premises; resolution requires resolution evidence, and retirement of an inapplicable candidate is not a remediation claim. Incomplete evidence produces actual gaps/conflicts and partial coverage.

Use discriminating verification designs, adapted to supplied identities and caller rules. These are plans requiring separate authorization for an isolated synthetic environment, never permission to run against a real service.

1. Hold the target resource and operation fixed while varying original caller, accepted credential, translated identity and mediator execution principal. Include a permitted control request, an out-of-scope caller, revocation during queued work and a direct legacy route. Observe the recipient's decision and before/after resource state, not just a transport code. Pass requires the supplied allowed action and attributable denial with no forbidden effect for the prohibited cases; fail requires an attributable forbidden effect; missing mapping, approval rule, state observation or alternate-path coverage is inconclusive. Keep status not_run and no result evidence until separately supplied execution supports a result.
2. Compare two schema-valid messages differing only in owner/resource/approval meaning, through the exact transformation version and orchestration definition. Separately compare an authorized definition with an unapproved edited or restored definition, under the same execution principal. Inspect each downstream business decision and the final or pending state after a lost reply/recovery. Pass requires meaning preservation or rejection of the prohibited meaning and denial of unapproved definition execution, with the permitted control completing as specified. Fail requires a forbidden ownership change or privileged cross-service effect. Ambiguous correlation, unavailable target state, absent caller invariant or missing publication/recovery authority is inconclusive. Keep the two authority decisions distinct even if one trace supplies both observations; proposed tests remain not_run.

## Mixed scope and portable results

With [identity-federation](../../quick/identity-federation.md), use shared global caller, issuer, subject and resource IDs with matching evidence. Assertion acceptance/mapping has a directional federation boundary; mediation/delegation and target business approval have separate service-oriented boundaries. A cross-set scenario must depend on both contributions. A signed assertion alone grants no business operation.

Supplied control implementation, bounded observed results and planned verification are distinct. No live behavior, production readiness or exhaustive coverage is claimed. Technology prescriptions require exact resolved secure-coding packs; missing coverage stays unverified. Only when a tool limit prevents writing one file, retain the full model through checked JSON part files under the runbook or split readable sections into part files without claiming omitted work is complete.
