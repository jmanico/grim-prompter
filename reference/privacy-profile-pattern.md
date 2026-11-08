---
id: reference/privacy-profile-pattern
title: Privacy Regulatory Profile Pattern
shape: reference
last_reviewed: 2026-11-07
sources:
  - https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng
  - https://www.cppa.ca.gov/regulations/
---
# Privacy Regulatory Profile Pattern

Use a profile within the [privacy analysis pattern](privacy-analysis-pattern.md) and [runbook](../runbook.md). Profiles supply bounded assessment questions, not legal determinations or method executions. They do not replace LINDDUN or establish that a formal DPIA, audit, or organizational approval occurred.

## Selection and source evidence

Select profiles from the caller's request and supported processing context. A profile selection is not a finding that the law applies. Record the people, geography, entity roles, processing purposes, exemptions and temporal scope needed to decide applicability. Do not infer residency from a hosting region, legal role from a variable name, or an exemption from a sector label.

Use only source access authorized by the runbook. A profile's source list and `last_reviewed` are library provenance, not proof the agent consulted those sources during this run. With no current primary source or supplied lawful source snapshot, continue engineering analysis, identify the unavailable authority and keep dependent legal conclusions unverified. Do not fetch sources merely because they are linked. Record the actual source title, URL or supplied locator, provision, version/publication date, access date, read extent and access limitations as Evidence. Record applicability evidence separately from evidence of implementation.

Distinguish an enactment or effective date, a phased compliance date, a submission date and the processing period assessed. A future deadline does not mean the underlying privacy harm is absent. When sources or interpretations conflict, preserve the alternatives and request a specific legal determination through an open gap; never resolve the conflict from a headline or outdated draft.

## Coverage representation

Use the existing version 1.0 contract. Each declared topic gets a Coverage record with lens `privacy:<profile>:<topic>`, a system `target_ref` for the processing scope when available (otherwise null), and `method_ref: null`. Keep separate rows when processing activities have different applicability or findings. Profiles are not Methods; do not create method executions or add arbitrary JSON fields for profile results.

Write the Coverage `reason` using these labels:

- **Applicability:** applicable, not applicable, or unknown, scoped to this processing activity and provision.
- **Basis:** the evidence IDs and reasoning supporting that disposition; distinguish caller claims and observations.
- **Source:** the authoritative provision and Evidence ID, revision and actual access limitations.
- **Timing:** assessed date/period, operative rule and relevant deadline or an explicit timing gap.
- **Assessment:** protective evidence, supported concern, or unassessed questions; cite related threat, control and requirement IDs in prose where useful.
- **Follow-up:** the gap, proposed treatment/verification, or legal/organizational evidence needed.

These are text conventions within `reason`, not new schema keys or typed reference fields. Retain typed relationships in the appropriate records. Express a proposed engineering requirement in Requirement `statement`, with `origin`, system `affected_refs`, `evidence_refs` and `status: proposed`. Use `supplied` only for an evidenced supplied requirement, never because this library suggests one. Threats require supported scenarios; a profile checklist failure or missing document alone does not prove a violation.

Use `assessed` only for a bounded question with adequate evidence and a reasoned disposition, not as a synonym for compliant. Use `partial` for unresolved applicability, sources or assessment; `not_assessed` for skipped work; and `not_applicable` only with affirmative scoped support. Any missing material needed for a conclusion remains a linked open gap. Preserve existing IDs and carry these records through every subsequent stage. Derive the readable obligation matrix from this cumulative model.

## Adding a profile

A new profile is a Markdown reference with a path-matching frontmatter ID, source list, review date, explicit jurisdiction/version boundary and stable topic IDs. For each topic include applicability questions, evidence needs, potential harms or control objectives, proposed verification, and authoritative provision pointers. Document excluded subjects and any screening-only coverage. Updating a rule must identify changed topics and implications for prior assessments; never silently reinterpret a saved baseline. Keep the catalog, entry points and routing in step. Use original instructions rather than copied legal tables or method material.
