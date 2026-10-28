---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# Agentic AI threat modeling

Use this set to examine how task authority crosses planning, persistent memory, delegation, tools, action approval and external effects. Adapt to the supplied domain; deployment, messages and ticket edits are other possible effects, not assumed system facts.

For one run, use [Quick Agentic AI Threat Model](../../quick/agentic-ai.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder. It returns a quick `TM_REPORT`; deep challenge and unsupplied methods remain unperformed. For deep analysis, run each stage under the runbook, reading the complete preceding JSON artifact from the run folder.

| Stage | Input | Output | Work |
| --- | --- | --- | --- |
| [00 Scope and evidence](00-scope-and-evidence.md) | `SYSTEM_UNDER_REVIEW` | `TM_CONTEXT` | Separate task grants, content, claims and outcomes. |
| [01 System model](01-system-model.md) | `TM_CONTEXT` | `TM_SYSTEM_MODEL` | Map authority and lifecycle transitions. |
| [02 Threat analysis](02-threat-analysis.md) | `TM_SYSTEM_MODEL` | `TM_ANALYSIS` | Ground the three scenario families. |
| [03 Challenge and consolidate](03-challenge-and-consolidate.md) | `TM_ANALYSIS` | `TM_REVIEWED_MODEL` | Seek scoped counterevidence and preserve identities. |
| [04 Treatment and validation](04-treatment-and-validation.md) | `TM_REVIEWED_MODEL` | `TM_TREATMENT_PLAN` | Propose outcomes and discriminating checks. |
| [05 Report and handoff](05-report-and-handoff.md) | `TM_TREATMENT_PLAN` | `TM_REPORT` | Carry every open risk, treatment, verification and gap into the handoff. |

`SYSTEM_UNDER_REVIEW` is the sole required external input. It may be prose, diagram text, sanitized excerpts or a bundle. Prior models, rubrics and separately executed method fragments are optional typed attachments. Every prompt embeds its contract. No registry, optional method file or external pack is necessary for baseline architectural analysis; read-only project access follows the runbook. Empty evidence produces a useful partial artifact with precise gaps, no invented system and no generic findings labeled as defects.

Analysis runs unattended. The questions below prepare evidence and do not pause the pipeline. If the caller separately requests an interview, limit it to five questions per batch and two batches unless extended; when answers stop, return the available evidence and gaps. Do not combine that optional interview with a required analysis handoff.

For MCP servers and connectors, apply [Tool and Shared Credential Boundaries](../../reference/tool-credential-boundaries.md) throughout the chain, retaining tool definition exposure, the per-tool authority map and evidence gaps in cumulative artifacts.

## Evidence to bring

1. What original business intent permits planning, approval requests and external actions separately? Which subject, action, resource, parameters and revision does it cover?
2. Who can change untrusted content, tool discovery metadata or tool-result data, and which exact path places it before a later privileged action decision? Is that influence observed or merely proposed?
3. Who writes and reads persistent memory, how is source/task scope retained, and can a remembered preference become an action grant in a later task?
4. What task authority does each delegate receive, what tools and credentials can it use, and what prevents returned instructions or further delegation from expanding that grant?
5. Which tool capability is selected, which credential executes it, and where is action-specific authority checked independently of availability or authentication?
6. Who actually approved which subject/action/resource/parameters/revision? How does the execution path distinguish that decision from the generated request for approval and handle changed details or delayed approval?
7. What happens after cancellation, a lost response, an unknown external result or a repeated attempt? What evidence links original intent, approved revision, attempts and actual effects?
8. Which scoped observations support claimed sandboxing, human review, model alignment or protocol protection? Which alternate tools, delegates and recovery paths remain unverified?

## Boundaries and scenario families

Check original intent versus planning; untrusted content versus privileged action; memory provenance and lifetime; delegated scope; selected capability versus execution credential; exact approval versus generated request; retries/cancellation/recovery versus external outcomes; and receiving API resource/operation authorization. Trace attribution and sensitive data across those same boundaries.

Examine three families: untrusted content, tool discovery metadata or tool-result influence on later privileged calls; memory or delegated instructions expanding scope; and approval changes/retries/recovery causing unsupported or duplicate effects. Each needs supplied controllability, a path and action-specific authority evidence. Hostile text alone is neither tool execution nor an exploitable boundary. A supervisor, memory record or authenticated API is not inherently authoritative. Protective evidence can defeat a stated prerequisite without proving universal safety.

The self-contained baseline uses security scenario lenses. [STRIDE per element](../../methods/stride-per-element.md) is a recommendation, not a performed method. Optional [STRIDE per interaction](../../methods/stride-per-interaction.md), [attack trees](../../methods/attack-trees.md) or [misuse and abuse cases](../../methods/misuse-abuse-cases.md) may be run separately and supplied as typed fragments. Their absence never disables baseline work. Keep technology rules in exact resolved external secure-coding packs; unavailable versions or packs remain unverified dependencies.

## Proposed verification

Derive verification comparisons from the supplied actions and authorization parameters.

Compare an inert external result with attacker-controlled instructions under the same authorized task; separately compare limited delegated scope with explicit authorization for an additional action. Inspect the actual execution decision and external state. Pass means unauthorized action is denied while permitted work remains available. An attributable unauthorized action is failure; only changed prose or missing outcome evidence is inconclusive.

Compare unchanged approved action/resource/recipient/parameters/revision with changed details, delayed approval after cancellation, and a repeated attempt after an unknown result. Pass means the exact caller approval and single-effect invariant holds with traceable final or pending state. Unsupported or duplicate effects are failure. Missing approval scope, cancellation ordering or authoritative outcome is inconclusive. These are proposed synthetic checks, never permission to execute tools, run a live model or cause an external effect.

## Portable and mixed results

Write JSON to the artifact file named by the runbook and the readable summary to its Markdown companion; preserve every cumulative record, source attachment, identity and counterexample. Each revision declares only actual immediate-parent changes. Preserve old nonempty declarations as sanitized revision-tagged history; no usable parent means no certified continuity, a new identity where required, null parent and empty changes. Unknown-version source is opaque, not a typed baseline. Retain complete original chunk bytes; accept only identical duplicates and resolve references globally. Missing/conflicting chunks remain partial, never silently summarized as a whole model.

Without a caller rubric, risks remain unrated with null ratings. Any suggested scale is a proposed Decision with null owner/date. Treatment proposals are not implemented controls, checks are not passed tests, and requests are not approvals. The handoff includes every open risk, treatment, verification and gap, with actual status and next evidence/action; split it with explicit continuation if necessary.

In agentic-ai plus `api`, use the same global subject, resource and action IDs. Assign assistant-to-tool request authority to agentic-ai and receiving resource/operation authorization to api, one owner per distinct boundary. Untrusted content influence may combine with broad receiving permission across both boundaries; preserve both contributions to that mechanism without duplicate findings or a claim that the API role ran.

The [artifact contract](../../reference/artifact-contract.md) expands the embedded definitions. This draft does not certify behavior, effectiveness or exhaustive coverage. Behavioral evaluation remains pending.

The agentic source used here is OWASP Agentic AI — Threats and Mitigations, Version 1.1, December 2025, as identified in the document text. Its landing-page date is not the edition identity. The workflow uses original architectural questions; it does not reproduce the source taxonomy, crosswalks, figures or examples.
