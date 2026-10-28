---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# Data-platform threat modeling

Use this set to follow data from its producers through ingestion, transformations, analytical stores, notebooks and consumers. It examines who can supply a value, what happens to sensitive fields, who can read an output, and which execution identity or consumer can act on it.

Run [Quick Data Platform Threat Model](../../quick/data-platform.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder for a quick `TM_REPORT`. It provides supported hypotheses, protective evidence, proposed outcomes and verification designs. For deeper analysis, run each stage under the runbook, reading the complete preceding artifact file from the run folder:

| Stage | Input | Output | Work |
| --- | --- | --- | --- |
| [00 Scope and evidence](00-scope-and-evidence.md) | `SYSTEM_UNDER_REVIEW` | `TM_CONTEXT` | Inventory data purposes, audiences, authority and missing evidence. |
| [01 System model](01-system-model.md) | `TM_CONTEXT` | `TM_SYSTEM_MODEL` | Separate producers, processing, stores, execution identities and consumers. |
| [02 Threat analysis](02-threat-analysis.md) | `TM_SYSTEM_MODEL` | `TM_ANALYSIS` | Trace field survival, source influence and notebook authority. |
| [03 Challenge and consolidate](03-challenge-and-consolidate.md) | `TM_ANALYSIS` | `TM_REVIEWED_MODEL` | Test enabling premises against protective evidence and reconcile identities. |
| [04 Treatment and validation](04-treatment-and-validation.md) | `TM_REVIEWED_MODEL` | `TM_TREATMENT_PLAN` | Propose boundary outcomes and falsifiable checks. |
| [05 Report and handoff](05-report-and-handoff.md) | `TM_TREATMENT_PLAN` | `TM_REPORT` | Preserve the cumulative model and account for open work. |

Only `SYSTEM_UNDER_REVIEW` is external. It can be prose, diagram text, sanitized excerpts, or any subset of available evidence. Prior models, rubrics and separately executed method fragments are optional attachments. Each prompt embeds its contract and runs unattended under the agent runbook, without an interview. Missing evidence yields gaps and partial output; an empty input does not produce invented platform components or threats. A path alone does not establish access. If tools or exact secure-coding packs are unavailable, identify the needed evidence and leave dependent technology prescriptions unverified while continuing architectural analysis.

## Evidence to bring

1. Which producer supplied each dataset, under what purpose, event time, schema and units? Who can correct or replace a record, and how is the source revision preserved?
2. Which passenger fields survive each projection, join, aggregation and export? Supply the join keys, input/output revisions and intermediate copies rather than a label such as anonymized.
3. What policy defines each output's permitted fields, row scope, audience and use? Which datasets are public, and which broader outputs are explicitly authorized?
4. What rule consumes an operations value, and what decision can change if that value is late, corrupted or deliberately altered? Supply the actual rule and expected outcome, not an inferred threshold.
5. Which identity runs interactive notebook cells and scheduled jobs? What read, write, export or delegation rights does it have, and how do those compare with the analyst's intended project scope?
6. How do rejected records, late corrections, backfills and failed publications affect existing outputs and prior consumer decisions? Which version does a consumer actually use?
7. What happens to derived datasets, exports and notebook results when a purpose, permission or retention rule changes, or a copy is restored?
8. Which observations establish a control's implementation or effectiveness for the exact fields, principal, operation, execution mode and revision? Which routes remain untested?
9. If an AI consumer is supplied, what exact dataset/feature boundary and serving identity are shared? Is there evidence of training or of a prediction controlling a decision, or are those still unknown?

These questions prepare evidence; they do not stop a stage for answers. Optional guided preparation is separate: ask at most five questions per batch and two batches unless the caller extends it. If nobody answers, return the available bundle and gaps. Never invent interview answers, participants or approval.

## What changes the analysis

The prompts check producer admission separately from content validity; raw-to-derived field lineage; publication and audience policy; analyst-to-runtime authority; data-to-consumer decision causality; correction/replay/recovery; retention and governance changes; and a supplied feature/dataset boundary shared with `ai-ml`. Each check gets coverage tied to actual system records. Missing lineage, policy or execution evidence remains a gap.

The three scenario families are targets for reasoning, not required defects. Public timetable data, an authorized broad output, removal of a prohibited field, rejection before a decision, or denial under a scoped runtime can defeat a specific claim. A protection observed on one path does not establish effectiveness on every export, scheduled run or restored copy. Multiple views of one event are not independent observations.

The embedded baseline uses security scenario lenses. [STRIDE per element](../../methods/stride-per-element.md) is a recommended method identity; selecting it does not mean its separate procedure executed. Optional supplied fragments preserve their actual work and omissions. Privacy, integrity and recovery lenses are not claims that a branded method ran.

In a mixed `data-platform`/`ai-ml` system, preserve the supplied consumer even if its architecture role is still a candidate. Model the shared feature/dataset boundary once with one owning architecture and global identities. Keep source integrity, downstream decisions and model execution/serving authority distinct. A feature or prediction label alone proves neither training, poisoning nor a decision effect.

## Verification designs

For field publication, first obtain source/output revisions, field lineage, audience policy and observable query/export results. In separately authorized isolated synthetic copies, compare a marked restricted field and an allowed public field as the named reader. Pass means the allowed output is available and prohibited fields or explicitly prohibited derivations are absent on every tested route. A prohibited value returned is failure. Missing policy, lineage, observation or test authority is inconclusive. This bounded design cannot establish anonymization against unknown joins.

For source influence, first obtain provenance, admission rules, transformation revision, the exact consumer rule and decision/correction state. In an authorized isolated non-operational consumer, compare a baseline, one altered record and its correction. Pass means rejection before use or the caller's explicitly permitted outcome and correction behavior. An attributable forbidden decision is failure. Missing causal linkage, rules, observations or authority is inconclusive.

For notebook authority, first obtain intended analyst scope, runtime mapping, permissions and observable allow/deny results. In an authorized synthetic project, compare an allowed dataset and a forbidden dataset through interactive and scheduled execution where those routes are supplied. Pass requires the allowed read and denial without data return for the forbidden read. Prohibited data returned is failure. Missing mapping, route evidence or authority is inconclusive. All new designs remain `not_run`.

The deep chain preserves each usable immediate parent, original stable IDs, exact current changes and sanitized prior history. Preserve original chunk bytes: only identical duplicates can be deduplicated. Missing or conflicting chunks cannot become a completed predecessor. Without a usable baseline, use a new model identity, null parent, empty changes and explicit gaps. A baseline that only needs further sanitization keeps its safe identities under a new revision with a null parent; continuity to the unsafe content stays uncertified.

No rubric means unrated risks; any proposed scale awaits a caller decision with null owner/date. Proposed treatments are not implemented controls. A report does not establish security, compliance, operational readiness or evaluated behavior.
