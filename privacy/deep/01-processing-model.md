---
id: privacy/deep/01-processing-model
title: Privacy Processing Model
shape: stage
stage: 1
inputs:
  - TM_CONTEXT
outputs:
  - TM_SYSTEM_MODEL
last_reviewed: 2026-11-07
sources: []
---
# Privacy Processing Model

Required input: `00-context.json`. Output: `TM_SYSTEM_MODEL` with `analysis_depth: deep`.

## Required instructions

Read the [runbook](../../runbook.md), the entire [system model pattern](../../reference/system-model-pattern.md), the [privacy analysis pattern](../../reference/privacy-analysis-pattern.md), and the selected profiles using the [profile pattern](../../reference/privacy-profile-pattern.md). The shared stage pattern supplies the complete embedded JSON contract and all evidence, lineage, preservation, refusal, and completion rules. Use its prescribed input type and fallback for missing, malformed, or wrong-depth predecessors. This wrapper supplies stage-specific privacy work without adding schema properties.

For `REVIEW_SCOPE: privacy`, run this privacy stage with the shared pattern. For `security-and-privacy`, also read the matching architecture stage and apply both scopes to one cumulative envelope. Keep actual architecture identities and one owner per boundary; privacy is not an architecture. Only perform this stage's work.

## Work

Reconstruct the personal-data lifecycle supported by the context. Represent affected people and recipients as appropriate actors; processing services and stores as assets; personal, sensitive, inferred, and derived information as data; and actual movements as directed flows. Reuse existing system identities. Do not invent a separate processing-record collection or encode privacy as an architecture.

For each processing activity, connect the data and affected people to its purpose, collection source, transformation or inference, recipients, storage, retention, and disposal using the privacy pattern's existing fields and relationships. Distinguish organization roles supported by evidence from assumed roles. Record unknown endpoints and retention/deletion paths as topology or evidence gaps.

Follow supported copies into logs, analytics, caches, backups, exports, third-party SDKs, training data, embeddings, or RAG stores. Do not infer all of these exist. Model consent withdrawal, preference changes, rights requests, and deletion propagation as states or flows only when evidence supports them. Identify the access, purpose, organizational, and geographic boundaries that matter for people, with one real architecture owner per boundary or a named ownership gap.

This stage establishes the processing model and coverage; it does not run threat discovery or certify a legal basis. After this artifact is written, the runbook schedules selected methods against it. Their separate fragments are inputs to stage 02, not edits to this predecessor.

## Handoff

Write `01-system-model.json` and `01-system-model.md` in the run folder. Preserve predecessor records and safe attachments under the shared pattern's lineage rules; never overwrite a prior stage. The readable report must agree with the JSON about inspected evidence, privacy coverage, method execution, unknowns, and unperformed work. Use the privacy pattern's completion criteria as well as the shared stage's requirements. No meaningful input yields a partial artifact with targeted gaps and no fabricated findings.
