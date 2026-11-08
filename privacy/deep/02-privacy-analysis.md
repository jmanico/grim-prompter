---
id: privacy/deep/02-privacy-analysis
title: Privacy Threat Analysis
shape: stage
stage: 2
inputs:
  - TM_SYSTEM_MODEL
outputs:
  - TM_ANALYSIS
last_reviewed: 2026-11-07
sources: []
---
# Privacy Threat Analysis

Required input: `01-system-model.json`. Output: `TM_ANALYSIS` with `analysis_depth: deep`.

## Required instructions

Read the [runbook](../../runbook.md), the entire [threat analysis pattern](../../reference/threat-analysis-pattern.md), the [privacy analysis pattern](../../reference/privacy-analysis-pattern.md), and the selected profiles using the [profile pattern](../../reference/privacy-profile-pattern.md). The shared stage pattern supplies the complete embedded JSON contract and all evidence, lineage, preservation, refusal, and completion rules. Use its prescribed input type and fallback for missing, malformed, or wrong-depth predecessors. This wrapper supplies stage-specific privacy work without adding schema properties.

For `REVIEW_SCOPE: privacy`, run this privacy stage with the shared pattern. For `security-and-privacy`, also read the matching architecture stage and apply both scopes to one cumulative envelope. Keep actual architecture identities and one owner per boundary; privacy is not an architecture. Only perform this stage's work.

## Work

For `REVIEW_SCOPE: privacy`, replace the shared pattern's mandatory security-baseline lens selection with privacy threat discovery. Keep its evidence, identity/import, scenario, confidence, and contract rules. For integrated scope, apply both sets of lenses and preserve their contributions without counting a copied scenario as independent corroboration.

Examine each in-scope processing activity for harm to people from authorized behavior, misuse, and attack. Consider collection beyond the stated need, purpose drift, unwanted linkage or identification, inference, surveillance, disclosure, coercive choices, unclear notices, inability to exercise rights, excessive retention, and failed disposal. Examine children, vulnerable groups, location/health/biometric information, profiling, automated decisions, and AI processing only where the model supports them. Distinguish confidentiality protection from appropriate recipient use.

Read the scheduled `method-<method>.json` fragments named by the runbook. Preserve and import them under the shared pattern's fragment and identity rules, including their source snapshots, actual phases, evidence, and omissions. Do not rerun a method from an attachment or mark a missing procedure completed. For a valid scheduled fragment, state that its method executed earlier in this run and was imported without re-execution at this stage; generic shared wording about carried-only imports applies to caller-supplied prior-run fragments, not these scheduled executions. Record bounded general privacy analysis separately from LINDDUN execution.

For every supported scenario, identify the affected people, processing purpose and flow, actor capability (which may be legitimate authority), prerequisites, harm, protective counterexample, and evidence that could disconfirm it. Missing documentation alone is a gap, not an evidenced weakness. Keep impact on people distinct from business consequences.

Assess each selected profile topic and additional-regime screening using the profile pattern. Separate legal applicability from implementation evidence and from threat discovery. Preserve unknown applicability, unsupported source freshness, and missing organizational evidence. Link supported obligation concerns to existing system records and scenarios without declaring violations or claiming compliance.

## Handoff

Write `02-analysis.json` and `02-analysis.md` in the run folder. Preserve predecessor records and safe attachments under the shared pattern's lineage rules; never overwrite a prior stage. The readable report must agree with the JSON about inspected evidence, privacy coverage, method execution, unknowns, and unperformed work. Use the privacy pattern's completion criteria as well as the shared stage's requirements. No meaningful input yields a partial artifact with targeted gaps and no fabricated findings.
