---
id: privacy/deep/00-scope-and-evidence
title: Privacy Scope and Evidence
shape: role
last_reviewed: 2026-11-07
sources: []
---
# Privacy Scope and Evidence

Required input: `SYSTEM_UNDER_REVIEW.md`. Output: `TM_CONTEXT` with `analysis_depth: deep`.

## Required instructions

Read the [runbook](../../runbook.md), the entire [scope and evidence pattern](../../reference/scope-and-evidence-pattern.md), the [privacy analysis pattern](../../reference/privacy-analysis-pattern.md), and the selected profiles using the [profile pattern](../../reference/privacy-profile-pattern.md). The shared stage pattern supplies the complete embedded JSON contract and all evidence, lineage, preservation, refusal, and completion rules. Use its prescribed input type and fallback for missing, malformed, or wrong-depth predecessors. This wrapper supplies stage-specific privacy work without adding schema properties.

For `REVIEW_SCOPE: privacy`, run this privacy stage with the shared pattern. For `security-and-privacy`, also read the matching architecture stage and apply both scopes to one cumulative envelope. Keep actual architecture identities and one owner per boundary; privacy is not an architecture. Only perform this stage's work.

## Work

Establish the privacy decision and processing scope before modeling. Record affected groups, sensitive-data concerns, business purposes, jurisdictions claimed by the caller, controller/processor or business/service-provider roles when supported, and the organizational decisions the repository cannot establish.

Inventory bounded evidence for collection sources, notices and user choices, processing routes, recipients and vendors, retention and deletion, rights requests, international transfers, profiling and automated decisions, and assessment/breach-response dependencies. Treat policies and contracts as supplied claims about practice unless implementation or execution observations support them. Do not copy personal data or private contract content merely to make the inventory look complete.

Record selected methods and profiles, actual source access, freshness limits, and why a profile's applicability is known or unknown. The default method selection is a request, never a performed execution. Retain source material and prior fragments as sanitized attachments; do not construct threats or fictitious system records at this stage. Missing geographical, contractual, purpose, or affected-person evidence becomes a specific evidence gap.

Preserve the review configuration and exclusions in the cumulative envelope using the privacy pattern. This includes explicit exclusions and the distinction between privacy-only and integrated scope. The next stage must recover the work from this file without earlier conversation.

## Handoff

Write `00-context.json` and `00-context.md` in the run folder. Preserve predecessor records and safe attachments under the shared pattern's lineage rules; never overwrite a prior stage. The readable report must agree with the JSON about inspected evidence, privacy coverage, method execution, unknowns, and unperformed work. Use the privacy pattern's completion criteria as well as the shared stage's requirements. No meaningful input yields a partial artifact with targeted gaps and no fabricated findings.
