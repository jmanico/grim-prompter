---
id: privacy/examples
title: Fictional Privacy Workflow Walkthroughs
shape: reference
last_reviewed: 2026-11-07
sources: []
---
# Fictional privacy workflow walkthroughs

These are author-written, fictional walkthroughs of expected reasoning and file handoffs, not records of an executed assessment or passing tests. The labels, evidence, system facts, and findings below belong only to these examples. A real run must gather its own evidence and use the complete contract in the required shared patterns. Example artifact filenames describe files the workflow would create inside its chosen run folder; no example run artifacts are supplied here.

## Standalone deep privacy review with missing evidence

Request:

```text
$threat-model deep privacy using LINDDUN PRO and GDPR and CCPA/CPRA profiles
Review the account export and deletion lifecycle in this project.
```

Fictional input: a caller describes a small subscription service, provides a diagram with application/database/analytics flows, and supplies a deletion-handler excerpt. The excerpt schedules deletion from the primary store but says nothing about analytics or backup restoration. Customer geography, contractual roles, retention policy, and LINDDUN PRO mapping/tree guidance are unavailable.

The runbook chooses an actual architecture from the supplied system, for example `web`, and records why. The scope stays privacy-only; selecting `web` does not imply a security review. Default profiles are not assertions that either law applies.

| Handoff | Expected work and honest limits |
| --- | --- |
| `SYSTEM_UNDER_REVIEW.md` | Inventory the supplied materials and their read extent. Separate the caller's design claims from the inspected handler. List unavailable geography, contracts, retention policy, and method guidance. |
| `00-context.json` | Record the privacy objective, configuration, source provenance, bounded scope, and specific evidence needs. Do not create threat findings yet. |
| `01-system-model.json` | Model account data, affected people, deletion request, primary store, and analytics path only as supported. Model unavailable downstream deletion and restore behavior as gaps. |
| `method-linddun-pro.json` | Preserve the model and record only phases actually possible. Without mapping/tree material, do not claim interaction elicitation ran or that PRO completed. Record its omissions. |
| `02-analysis.json` | Import the partial fragment. Separately develop a general privacy hypothesis: retained analytics or restored copies could keep an account link after a deletion request. Tie it to the modeled copies and unknown deletion paths. Do not label an uninspected downstream implementation defective. Record profile applicability as unknown. |
| `03-reviewed-model.json` | Consider the counterexample that analytics records are irreversibly aggregated or removed by an independent process. Retain the gap that would distinguish these cases. Missing policy evidence alone is not a violation. |
| `04-treatment-plan.json` | Propose accountable deletion propagation and restore handling, with synthetic-data verification. Keep execution `not_run`, result evidence empty, risk unrated without supplied criteria, and owners/dates unknown. |
| `05-report.json` and `report.md` | Preserve partial PRO execution, unknown profile applicability, the affected-person harm, proposed outcome, and remaining evidence needs. Do not certify GDPR/CCPA compliance or completion of a DPIA. |

A relevant proposed verification would create synthetic linked records only in a separately authorized test environment, request deletion, inspect the declared downstream copies, and exercise a bounded restore scenario. Pass would require the specified deletion outcome across all declared copies; a retained usable link would fail that criterion; inaccessible recipients or restore paths would make the result inconclusive. None of those actions occurs merely because the plan was written.

The final report remains partial where the selected method and requested topic assessment could not be completed. A valid JSON handoff does not erase those limitations.

## Integrated web review: intended processing can cause harm

Request:

```text
$threat-model deep web with privacy using LINDDUN PRO and GDPR profiles
Review profile visibility, personalization, and account deletion.
```

Fictional input: implementation excerpts show that a signed-in user can view their own profile, an authorization check restricts exports to that user, and a personalization job legitimately joins activity history with profile attributes. A supplied product decision authorizes the join. A separate inspected deletion path removes the profile row but leaves a person-linked personalization record. No synthetic test has been executed.

The run loads each `deep/web/` stage and its matching `privacy/deep/` stage. Stage 01 creates one set of actors, stores, data, flows, and boundaries. Stage 02 imports the separately executed method fragment, then examines security and privacy in one `02-analysis.json`.

The authorization check is protective evidence for one disclosure scenario, with its actual scope. It does not settle whether the intended join infers sensitive characteristics or uses data beyond the stated purpose. A privacy hypothesis can name that authorized processing and its possible harm without inventing an attacker or labeling the observed product authorization as a legal decision.

The inspected deletion path supports a bounded implementation concern about the retained personalization record if the supplied evidence establishes that no deletion step handles it. If that conclusion depends on uninspected services, keep it a hypothesis with the precise gap instead. The report must distinguish this from an observed test failure: there is no execution result.

Keep both findings linked to the same system records rather than cloning the database or user. Preserve their distinct harms and supporting evidence; one combined report may retain a security scenario, an authorized-use privacy scenario, and a deletion scenario without counting shared evidence three times.

If supplied scope and source evidence establish that this specific processing activity has no international transfer, the relevant GDPR transfer topic may be `not_applicable` with a scoped rationale. That does not exempt the whole service from GDPR or make the privacy scenarios disappear. If the evidence only says the primary database is local, recipients and remote access remain unknown, so non-applicability is unsupported.

Additional-regime screening still runs. A jurisdiction or sector outside the implemented profiles creates a further-review need; screening is not a complete assessment of that regime. Explicitly unselected CCPA/CPRA assessment stays outside this run's scope rather than being silently marked assessed.

## Quick review with no optional method

Request:

```text
$threat-model quick privacy with no optional method and GDPR profiles
Review the supplied registration flow and analytics notice.
```

The explicit method choice overrides default GO selection. The run still inventories processing, examines grounded privacy harms, assesses selected profile topics and other-regime screening, and proposes outcomes/verification using [quick privacy](quick.md). It writes `quick-report.json` and `report.md`; it does not fabricate a method fragment or advertise LINDDUN completion. The report states that the deep modeling/challenge sequence was not performed. A missing analytics recipient remains a gap even when the visible notice describes a purpose.

## Continue or review a change

For a paused deep run that already has `02-analysis.json`, name the existing run folder and ask to continue from stage 03. Recover the original review configuration and source provenance from the artifacts. Read the complete predecessor; do not recreate missing earlier evidence from conversation. If stage 03 JSON exists but its Markdown companion is missing, derive that companion without rerunning the stage. Use a new run for refreshed evidence, changed profiles, or a different library revision.

For a later change review, name the previous `05-report.json` and the exact branch/commit range. A range alone is insufficient. Suppose the fictional change adds a new analytics recipient: preserve the prior model's privacy IDs and historical coverage, map the new flow from diff evidence, and identify which purpose, recipient, retention, deletion, transfer, and profile assessments need reconsideration. Do not carry earlier assessed coverage forward as fresh assurance for the new recipient. The change review produces its own `change-review.json` and `.md`; it does not overwrite the baseline or pretend the complete six-stage privacy workflow reran.

## Manual review checks

These checks guide review of the prompts and an actual generated run; they are not assertions that a run passed them.

- Trace one processing record and one threat from stage 01 or 02 to the final report without losing IDs, evidence, method omissions, or privacy profile coverage.
- Check that unknown applicability and supported non-applicability remain different dispositions with reasons.
- Confirm that an authorized-use harm can survive a successful authorization-control observation.
- Confirm that proposed deletion verification is `not_run` until actual authorized execution evidence exists.
- Confirm that an integrated run produces one cumulative artifact at each stage and that privacy-only scope does not claim a security-baseline review.
- Confirm that continuation preserves the run configuration and a change review identifies coverage affected by changed processing.
