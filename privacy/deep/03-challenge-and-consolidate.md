---
id: privacy/deep/03-challenge-and-consolidate
title: Privacy Challenge and Consolidation
shape: stage
stage: 3
inputs:
  - TM_ANALYSIS
outputs:
  - TM_REVIEWED_MODEL
last_reviewed: 2026-11-07
sources: []
---
# Privacy Challenge and Consolidation

Required input: `02-analysis.json`. Output: `TM_REVIEWED_MODEL` with `analysis_depth: deep`.

## Required instructions

Read the [runbook](../../runbook.md), the entire [challenge and consolidation pattern](../../reference/challenge-and-consolidation-pattern.md), the [privacy analysis pattern](../../reference/privacy-analysis-pattern.md), and the selected profiles using the [profile pattern](../../reference/privacy-profile-pattern.md). The shared stage pattern supplies the complete embedded JSON contract and all evidence, lineage, preservation, refusal, and completion rules. Use its prescribed input type and fallback for missing, malformed, or wrong-depth predecessors. This wrapper supplies stage-specific privacy work without adding schema properties.

For `REVIEW_SCOPE: privacy`, run this privacy stage with the shared pattern. For `security-and-privacy`, also read the matching architecture stage and apply both scopes to one cumulative envelope. Keep actual architecture identities and one owner per boundary; privacy is not an architecture. Only perform this stage's work.

## Work

Challenge every privacy scenario's system connection, affected population, processing purpose, prerequisites, and plausible harm. Seek protective evidence and competing explanations; absence of a privacy policy in the inspected files does not establish absent notice, absent consent, or unlawful processing. Authorized processing can still create a supported privacy harm.

Check whether minimization, aggregation, pseudonymization, encryption, isolation, or deletion claims cover the actual endpoints and copies in scope. Do not treat pseudonymization as proof of anonymity, safe transit as proof of safe use, or a deletion interface as proof of downstream erasure. Keep re-identification concerns as hypotheses unless actual observations justify stronger claims; never attempt real-person linkage as part of review.

Challenge profile applicability and source revisions independently of technical findings. Review claimed exemptions, geographical assumptions, sensitive-data classifications, role assignments, compliance dates, and statements that a missing document proves a violation. Preserve unresolved interpretations as gaps for privacy/legal review.

Reconcile duplicate security/privacy scenarios only when scoped identities and mechanisms agree. Preserve all method contributions, privacy impacts, evidence, existing IDs, and source attachments. Complementary harms with different affected people or purposes may need linked findings rather than one merged threat. A fragment's partial method status must survive consolidation.

Check processing and profile coverage for recipients, retained copies, lifecycle transitions, and topics omitted by the earlier analysis. Record omitted work honestly rather than filling the model with generic threats. Retain explicit non-applicable dispositions and their rationale; do not silently drop the topic.

## Handoff

Write `03-reviewed-model.json` and `03-reviewed-model.md` in the run folder. Preserve predecessor records and safe attachments under the shared pattern's lineage rules; never overwrite a prior stage. The readable report must agree with the JSON about inspected evidence, privacy coverage, method execution, unknowns, and unperformed work. Use the privacy pattern's completion criteria as well as the shared stage's requirements. No meaningful input yields a partial artifact with targeted gaps and no fabricated findings.
