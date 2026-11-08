---
id: privacy/deep/04-treatment-and-validation
title: Privacy Treatment and Validation Planning
shape: stage
stage: 4
inputs:
  - TM_REVIEWED_MODEL
outputs:
  - TM_TREATMENT_PLAN
last_reviewed: 2026-11-07
sources: []
---
# Privacy Treatment and Validation Planning

Required input: `03-reviewed-model.json`. Output: `TM_TREATMENT_PLAN` with `analysis_depth: deep`.

## Required instructions

Read the [runbook](../../runbook.md), the entire [treatment and validation pattern](../../reference/treatment-and-validation-pattern.md), the [privacy analysis pattern](../../reference/privacy-analysis-pattern.md), and the selected profiles using the [profile pattern](../../reference/privacy-profile-pattern.md). The shared stage pattern supplies the complete embedded JSON contract and all evidence, lineage, preservation, refusal, and completion rules. Use its prescribed input type and fallback for missing, malformed, or wrong-depth predecessors. This wrapper supplies stage-specific privacy work without adding schema properties.

For `REVIEW_SCOPE: privacy`, run this privacy stage with the shared pattern. For `security-and-privacy`, also read the matching architecture stage and apply both scopes to one cumulative envelope. Keep actual architecture identities and one owner per boundary; privacy is not an architecture. Only perform this stage's work.

## Work

For every open privacy threat, propose outcomes that reduce harm to people: collect less, narrow purposes or audiences, avoid unnecessary inference, shorten retention, separate identities, improve meaningful choice, enforce rights, constrain third-party propagation, or remove the processing activity. Explain tradeoffs, dependencies, alternatives, and residual uncertainty. Do not assume consent cures an unnecessary or inappropriate activity.

Retain the shared pattern's risk obligations. Use caller-supplied privacy criteria when available and distinguish impact on people from organizational impact. Without supported criteria and inputs, keep ratings unrated and null; proposed criteria are not an approved rubric. Prioritization may describe evidence-backed urgency and dependencies without inventing numeric scores.

Plan verification for the actual scenarios and controls, including applicable access/correction/deletion requests, consent withdrawal, preference signals, retention expiry, backup restoration, derived data, and recipient propagation. Use synthetic subjects and data by default. State prerequisites and separate pass, fail, and inconclusive criteria. A proposed check is `not_run` with no result evidence; do not perform requests, contact recipients, or re-identify people.

Identify missing contracts, organizational decisions, source interpretation, formal assessment, and operational evidence as dependencies with clear next evidence needs. Support DPIA and other privacy-risk-assessment work without claiming a required assessment or audit was completed. Owners, dates, risk acceptance, approvals, and executed results require supplied evidence under the contract.

Carry privacy profile and method coverage forward, including non-applicability and partial work. A mitigation proposal cannot close a threat or gap, upgrade a control to tested, or establish legal compliance.

## Handoff

Write `04-treatment-plan.json` and `04-treatment-plan.md` in the run folder. Preserve predecessor records and safe attachments under the shared pattern's lineage rules; never overwrite a prior stage. The readable report must agree with the JSON about inspected evidence, privacy coverage, method execution, unknowns, and unperformed work. Use the privacy pattern's completion criteria as well as the shared stage's requirements. No meaningful input yields a partial artifact with targeted gaps and no fabricated findings.
