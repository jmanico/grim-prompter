---
id: privacy/quick
title: Quick Privacy Threat Review
shape: role
last_reviewed: 2026-11-07
sources: []
---
# Quick privacy threat review

Required input: `SYSTEM_UNDER_REVIEW.md`. Output: `TM_REPORT` with `analysis_depth: quick`, written to `quick-report.json` and `report.md` in the run folder.

## Required instructions

Read the [runbook](../runbook.md), the entire [quick analysis pattern](../reference/quick-analysis-pattern.md), the [privacy analysis pattern](../reference/privacy-analysis-pattern.md), and the selected profiles using the [profile pattern](../reference/privacy-profile-pattern.md). The shared quick pattern supplies the complete embedded JSON contract, provenance, lineage, input, evidence, treatment, risk, verification, and completion rules. This prompt adds privacy work; it does not define a new schema.

For `REVIEW_SCOPE: privacy`, use the privacy lenses below in place of the shared pattern's mandatory security-baseline lens selection. All its other analytical and contract obligations still apply. State that security-baseline review was not performed. For `security-and-privacy`, also read the selected quick architecture prompt and apply both scopes to one model. Privacy never becomes an `architecture_ids` value.

## Work

1. Bound the processing activities and affected people from the evidence. Record the selected profiles, their applicability assumptions, and the sources actually inspected. Distinguish unknown applicability from supported non-applicability.
2. Build a compact inventory of personal and sensitive data, purposes, actors, recipients, stores, directed flows, retention, and deletion. Include logs, backups, derived data, exports, and third-party handling where supported. Missing topology stays a gap.
3. Examine privacy harms across collection, use, inference, sharing, storage, and disposal. Include authorized secondary use, loss of control, tracking or linkage, misleading choices, excessive retention, ineffective deletion, and relevant AI/profiling harms. Tie every scenario to actual or proposed system elements and affected people; preserve protective evidence and alternative explanations.
4. Import only the method fragments scheduled and actually produced under the runbook. Preserve original identities, source attachments, method omissions, and coverage. A method name or source link is not an executed method. If GO cards or other method prerequisites were unavailable, preserve that gap and describe any general privacy analysis separately.
5. Assess each selected profile topic against the available implementation and organizational evidence. Record applicability, source freshness, coverage, supporting evidence, and missing inputs through the privacy/profile patterns. Screen additional regimes. Do not turn a possible obligation into a proven violation.
6. For each open threat, retain the shared pattern's risk, treatment, proposed-decision, and verification obligations. Describe impact on people separately; keep ratings unrated without supplied criteria. Propose privacy outcomes and synthetic-data verification with pass, fail, and inconclusive criteria. Do not execute them.

## Handoff

Write the complete portable envelope using the shared quick contract, preserving all input inventories, privacy records, method fragments, coverage, gaps, and prior content. Derive the readable processing inventory and regulatory coverage matrix from those records. Explain which work was bounded or omitted, that deep challenge was not performed, and which method or profile work remains partial. A quick review is never relabeled as a completed deep workflow or compliance certification.
