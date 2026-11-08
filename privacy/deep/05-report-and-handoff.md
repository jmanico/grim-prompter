---
id: privacy/deep/05-report-and-handoff
title: Privacy Report and Handoff
shape: role
last_reviewed: 2026-11-07
sources: []
---
# Privacy Report and Handoff

Required input: `04-treatment-plan.json`. Output: `TM_REPORT` with `analysis_depth: deep`.

## Required instructions

Read the [runbook](../../runbook.md), the entire [report and handoff pattern](../../reference/report-and-handoff-pattern.md), the [privacy analysis pattern](../../reference/privacy-analysis-pattern.md), and the selected profiles using the [profile pattern](../../reference/privacy-profile-pattern.md). The shared stage pattern supplies the complete embedded JSON contract and all evidence, lineage, preservation, refusal, and completion rules. Use its prescribed input type and fallback for missing, malformed, or wrong-depth predecessors. This wrapper supplies stage-specific privacy work without adding schema properties.

For `REVIEW_SCOPE: privacy`, run this privacy stage with the shared pattern. For `security-and-privacy`, also read the matching architecture stage and apply both scopes to one cumulative envelope. Keep actual architecture identities and one owner per boundary; privacy is not an architecture. Only perform this stage's work.

## Work

Retain the full cumulative envelope, including processing records, method source fragments, profile coverage, conflicting claims, treatments, verification plans, and evidence gaps. Derive all readable views from the JSON; do not create a second incompatible privacy model.

After the required inspection-coverage summary, explain the review scope, affected people and purposes, the processing inventory and key flows, consequential privacy harms, protective evidence, and residual uncertainty. Present selected-profile applicability and per-topic coverage, with source/revision limits and further review needs. State which additional regimes were only screened and which were not assessed.

Carry the shared pattern's action register keyed to every relevant treatment, verification, and open gap. Show actual statuses, evidence needed next, and supplied decisions without inventing owners, dates, acceptance, or test results. Separate proposed verification from execution and distinguish carried method work from work performed in this run.

Summarize evidence that could support a DPIA or another privacy risk assessment and identify what is still missing. Do not certify compliance, claim a formal assessment or audit was completed, infer lawful processing from a lack of threats, or infer absence of privacy harm from supported non-applicability of a profile.

State whether this was standalone privacy review or integrated security/privacy review. Preserve incomplete methods, profile coverage, and stage work in the report's status and limitations according to the privacy pattern; formatting the report does not complete omitted analysis. Name the baseline artifact suitable for a later change review and its source revision, without claiming newer project changes were examined.

## Handoff

Write `05-report.json` and `report.md` in the run folder. Preserve predecessor records and safe attachments under the shared pattern's lineage rules; never overwrite a prior stage. The readable report must agree with the JSON about inspected evidence, privacy coverage, method execution, unknowns, and unperformed work. Use the privacy pattern's completion criteria as well as the shared stage's requirements. No meaningful input yields a partial artifact with targeted gaps and no fabricated findings.
