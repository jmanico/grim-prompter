---
id: privacy/deep/00-scope-and-evidence
title: Privacy Scope and Evidence
shape: stage
stage: 0
inputs:
  - SYSTEM_UNDER_REVIEW
outputs:
  - TM_CONTEXT
last_reviewed: 2026-11-08
sources: []
---
# Privacy Scope and Evidence

Required input: `SYSTEM_UNDER_REVIEW.md`. Output: `TM_CONTEXT` with `analysis_depth: deep`.

## Required instructions

Read the [runbook](../../runbook.md), the entire [scope and evidence pattern](../../reference/scope-and-evidence-pattern.md), the [privacy analysis pattern](../../reference/privacy-analysis-pattern.md), and the selected profiles using the [profile pattern](../../reference/privacy-profile-pattern.md). The shared stage pattern supplies the complete embedded JSON contract and all evidence, lineage, preservation, refusal, and completion rules. Use its prescribed input type and fallback for missing, malformed, or wrong-depth predecessors. This wrapper supplies stage-specific privacy work without adding schema properties.

For `REVIEW_SCOPE: privacy`, run this privacy stage with the shared pattern. For `security-and-privacy`, also read the matching architecture stage and apply both scopes to one cumulative envelope. Keep actual architecture identities and one owner per boundary; privacy is not an architecture. Only perform this stage's work.

## Work

Establish the privacy decision and processing scope before modeling. Record affected groups, sensitive-data concerns, business purposes, jurisdictions claimed by the caller, controller/processor or business/service-provider roles when supported, and the organizational decisions the repository cannot establish.

Consume the [bounded code evidence pass](../../reference/privacy-evidence-pattern.md) and inspection ledger collected before this stage; carry its sanitized observations and read limits into the context. This stage does not silently reread sources or expand scope. Inventory bounded evidence for collection sources, notices and user choices, processing routes, recipients and vendors, retention and deletion, rights requests, international transfers, profiling and automated decisions, and assessment/breach-response dependencies. Treat policies and contracts as supplied claims about practice unless implementation or execution observations support them. Do not copy personal data or private contract content merely to make the inventory look complete.

Record selected methods and profiles, actual source access, freshness limits, and why a profile's applicability is known or unknown. Populate `selected_methods` with resolved `METHODS` under the runbook (explicit requests for a new run, saved selections on continuation), including selections whose prompts are unavailable. Both `METHODS` and `PRIVACY_PROFILES` default to empty lists; selections are requests, never performed executions. Retain source material and prior fragments as sanitized attachments; do not construct threats or fictitious system records at this stage. Missing purpose or affected-person evidence becomes a scoped processing gap. Geographical or contractual gaps are needed only where they limit an in-scope engineering question or an explicitly selected profile, never solely because a legal profile was not requested.

Preserve the review configuration and exclusions in the cumulative envelope using the privacy pattern. This includes explicit exclusions and the distinction between privacy-only and integrated scope. The next stage must recover the work from this file without earlier conversation.

## Handoff

Write `00-context.json` and `00-context.md` in the run folder. Preserve predecessor records and safe attachments under the shared pattern's lineage rules; never overwrite a prior stage. The readable report must agree with the JSON about inspected evidence, privacy coverage, method execution, unknowns, and unperformed work. Use the privacy pattern's completion criteria as well as the shared stage's requirements. No meaningful input yields a partial artifact with targeted gaps and no fabricated findings.
