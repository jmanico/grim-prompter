---
id: privacy/README
title: Privacy Threat Modeling
shape: reference
last_reviewed: 2026-11-07
sources: []
---
# Privacy threat modeling

Review how a system's processing can harm people, including intended and authorized processing. Combine this workflow with an architecture review, or run a standalone privacy review. Both use the [runbook](../runbook.md), read-only project inspection, evidence cited as `path:start-end`, and cumulative JSON files in the run folder.

Privacy is a review scope, not an architecture. `quick` and `deep` still select depth; real architecture identities still describe the system and own its boundaries. Standalone privacy review uses `REVIEW_SCOPE: privacy`; architecture review with privacy uses `REVIEW_SCOPE: security-and-privacy`. When an architecture is not named, the runbook selects one from the evidence without turning it into a claim that security analysis ran.

## Run

| Request | Claude Code | Codex |
| --- | --- | --- |
| Quick standalone privacy review | `/threat-model quick privacy` | `$threat-model quick privacy` |
| Full standalone privacy review | `/threat-model deep privacy` | `$threat-model deep privacy` |
| Full web review including privacy | `/threat-model deep web with privacy` | `$threat-model deep web with privacy` |
| Choose the method and profiles | `/threat-model deep web with privacy using LINDDUN PRO and GDPR and CCPA/CPRA profiles` | `$threat-model deep web with privacy using LINDDUN PRO and GDPR and CCPA/CPRA profiles` |

These are natural-language skill requests, not a separate command-line parser. Supply the decision the review supports, relevant directories, and explicit exclusions. To run without a skill, ask the coding agent to follow the runbook with the same depth, review scope, architecture, method, and profile choices.

For privacy requests without explicit method selection, quick selects [LINDDUN GO](../methods/linddun-go.md) and deep selects [LINDDUN PRO](../methods/linddun-pro.md). Explicit method choices, including no optional method, override that default. Selection does not prove execution: absent source material or incomplete method work remains a named gap with partial or unassessed coverage. General privacy scenarios can still be examined without claiming a LINDDUN procedure ran.

The default profiles are [GDPR](profiles/gdpr.md) and [CCPA/CPRA](profiles/ccpa-cpra.md). Profile selection requests assessment; it does not establish legal applicability. An explicit profile list replaces these defaults. Always include [other-regime screening](profiles/other-regimes-screening.md), which identifies additional review needs without pretending those profiles are implemented. An explicit exclusion remains visible in scope and coverage.

## Workflow and artifacts

| Depth or stage | Privacy prompt | Run-folder output |
| --- | --- | --- |
| Quick | [Bounded privacy review](quick.md) | `quick-report.json`, `report.md` |
| Deep 00 | [Scope and evidence](deep/00-scope-and-evidence.md) | `00-context.json`, `00-context.md` |
| Deep 01 | [Processing model](deep/01-processing-model.md) | `01-system-model.json`, `01-system-model.md` |
| Deep 02 | [Privacy analysis](deep/02-privacy-analysis.md) | `02-analysis.json`, `02-analysis.md` |
| Deep 03 | [Challenge and consolidation](deep/03-challenge-and-consolidate.md) | `03-reviewed-model.json`, `03-reviewed-model.md` |
| Deep 04 | [Treatment and validation](deep/04-treatment-and-validation.md) | `04-treatment-plan.json`, `04-treatment-plan.md` |
| Deep 05 | [Report and handoff](deep/05-report-and-handoff.md) | `05-report.json`, `report.md` |

The run starts with `SYSTEM_UNDER_REVIEW.md`. Each deep stage reads the complete predecessor file. Selected methods run after stage 01 and before stage 02; quick methods read the evidence bundle before quick analysis. Their `method-<method>.json` and `.md` files are separate source fragments, imported by the consuming analysis under the runbook's identity and provenance rules.

Integrated runs load the matching architecture prompt and privacy prompt, then write one cumulative artifact per stage. They do not run two competing pipelines or overwrite one report with another. The shared [privacy analysis pattern](../reference/privacy-analysis-pattern.md) defines the record representation and preservation rules; the [profile pattern](../reference/privacy-profile-pattern.md) defines regulatory coverage.

## Review the result

Check the inspection ledger, processing inventory, affected people, privacy scenarios, profile applicability and topic coverage, proposed treatments, residual uncertainty, and the action register. Review privacy impact on people separately from organizational impact. A privacy risk may exist even when processing is authorized or a particular legal regime does not apply.

Repository inspection cannot establish actual contracts, organizational practice, external recipients' behavior, legal decisions, or control effectiveness without corresponding evidence. Reports support DPIA and privacy-risk-assessment work; they do not certify compliance or replace a required formal assessment. No test runs, live requests, real-person re-identification, or publication of run artifacts are authorized by these prompts.

For concrete handoffs and partial-analysis cases, see the [fictional walkthroughs](examples.md). Continue a run by naming its run folder and next missing stage. A changed scope, new profile selection, refreshed evidence, or different library revision requires a new run with the old model explicitly named as prior input. Change review uses the named baseline and revision range, preserving its privacy records and identifying coverage made stale by the change.
