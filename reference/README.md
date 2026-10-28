# Threat Modeling reference files

The stage and quick-analysis patterns are runnable instructions with their own input and output contracts; run them under the [agent runbook](../runbook.md). The artifact contract and method catalog are supporting references.

**Quick start:** Run [Quick Threat Analysis](quick-analysis-pattern.md) under the runbook with the available system material as `SYSTEM_UNDER_REVIEW.md` in the run folder for a quick TM_REPORT. To review an existing model, use the [Threat Model Challenger](../helpers/model-challenger.md).

**Deep sequence:** Run each pattern under the runbook, reading the preceding JSON envelope file from the run folder: [00 Scope and evidence](scope-and-evidence-pattern.md) takes SYSTEM_UNDER_REVIEW and emits TM_CONTEXT; [01 System model](system-model-pattern.md) emits TM_SYSTEM_MODEL; [02 Threat analysis](threat-analysis-pattern.md) emits TM_ANALYSIS; [03 Challenge and consolidation](challenge-and-consolidation-pattern.md) emits TM_REVIEWED_MODEL; [04 Treatment and validation](treatment-and-validation-pattern.md) emits TM_TREATMENT_PLAN; [05 Report and handoff](report-and-handoff-pattern.md) emits TM_REPORT.

**Existing models:** Start a re-review of a versioned envelope with the quick pattern or challenger to preserve its model identity. Stage 00 starts a new deep model and carries prior models as source attachments.

**Access limits:** Each pattern works from supplied material without an interview. Missing optional references stay unverified and do not block baseline analysis. Method roles run separately and supply typed fragments; a catalog candidate is not a completed execution.

## Available references

| File | What it is | Reviewed |
| --- | --- | --- |
| [`artifact-contract.md`](artifact-contract.md) | Portable Threat Model Artifact Contract | 2026-10-28 |
| [`challenge-and-consolidation-pattern.md`](challenge-and-consolidation-pattern.md) | Challenge and Consolidation Pattern | 2026-10-28 |
| [`composition-guide.md`](composition-guide.md) | Mixed Architecture Composition and Change Review | 2026-10-28 |
| [`quick-analysis-pattern.md`](quick-analysis-pattern.md) | Quick Threat Analysis Pattern | 2026-10-28 |
| [`report-and-handoff-pattern.md`](report-and-handoff-pattern.md) | Report and Handoff Pattern | 2026-10-28 |
| [`scope-and-evidence-pattern.md`](scope-and-evidence-pattern.md) | Scope and Evidence Pattern | 2026-10-28 |
| [`system-model-pattern.md`](system-model-pattern.md) | System Model Pattern | 2026-10-28 |
| [`threat-analysis-pattern.md`](threat-analysis-pattern.md) | Threat Analysis Pattern | 2026-10-28 |
| [`tool-credential-boundaries.md`](tool-credential-boundaries.md) | Supporting checklist for MCP tools, tool description poisoning and shared service identities | 2026-10-28 |
| [`treatment-and-validation-pattern.md`](treatment-and-validation-pattern.md) | Treatment and Validation Pattern | 2026-10-28 |
