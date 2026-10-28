---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# Desktop Threat Modeling

Follow project data and requested operations across local users, files, application processes, plugins, privileged helpers and update distribution. Start with the evidence available. A missing parser trace or helper policy becomes a question, not a confirmed defect.

Run [Desktop Quick Threat Analysis](../../quick/desktop.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder for a portable `TM_REPORT`. For deeper work, run each stage under the runbook, reading its preceding cumulative JSON file from the run folder. Only `SYSTEM_UNDER_REVIEW` is required externally; descriptions, observations, prior models, rubrics and method fragments can travel inside that bundle.

| Prompt | Input | Output |
| --- | --- | --- |
| [00 Scope and evidence](00-scope-and-evidence.md) | `SYSTEM_UNDER_REVIEW` | `TM_CONTEXT` |
| [01 System model](01-system-model.md) | `TM_CONTEXT` | `TM_SYSTEM_MODEL` |
| [02 Threat analysis](02-threat-analysis.md) | `TM_SYSTEM_MODEL` | `TM_ANALYSIS` |
| [03 Challenge and consolidate](03-challenge-and-consolidate.md) | `TM_ANALYSIS` | `TM_REVIEWED_MODEL` |
| [04 Treatment and validation](04-treatment-and-validation.md) | `TM_REVIEWED_MODEL` | `TM_TREATMENT_PLAN` |
| [05 Report and handoff](05-report-and-handoff.md) | `TM_TREATMENT_PLAN` | `TM_REPORT` |

Each prompt embeds its contract, baseline questions and runbook operating boundary. Optional methods run separately; selecting one is not executing it. Preserve source identities, counterevidence and uncertainty. Reassemble a complete chunk sequence before treating it as a predecessor. Declare only immediate-parent changes and retain older declarations as sanitized source history. Unknown-version material stays opaque with a conversion gap, never a certified baseline.

## Evidence questions

1. Which project fields can select local resources or external destinations during parse, preview and save? What trace identifies the actual reader, request authority and returned content?
2. Which capabilities belong to the local user, application, parser and each plugin? Does opening a project authorize external resolution, or is that a separate decision?
3. Which callers can reach each helper operation, directly or through forwarding? What binds the original caller to operation, resource, installation target and response recipient?
4. What changes when a plugin is updated, disabled or removed while requests are queued? Which privileges or retained data survive that transition?
5. What evidence binds a release to build and publication identities? Separately, who authorizes the product, version, channel and target that may be installed locally?
6. What happens when the artifact or destination changes after approval, installation is interrupted, or a previous release is restored? Which policy and observation cover retries and recovery?
7. Which project copies, previews, logs and temporary files remain for another local user after cleanup or restart? What is the observed access scope?

Use these as evidence needs in unattended work. For an optional interview, ask at most five questions at once and two batches unless extended by the caller. With no answer, stop questioning and return supported analysis with gaps. Only when a tool limit prevents writing one Markdown file, split tables into part files at section boundaries and say what remains.

## Boundary and lifecycle checks

- Trace acquisition, parse, preview and save; distinguish a crafted document from demonstrated parser exploitation.
- Trace external resolution to actual local reads and network recipients; project-open intent is not blanket resource permission.
- Bind local-message sender, requested operation, target and response recipient; authentication alone does not authorize every helper action.
- Follow plugin activation, queued requests, revocation and removal, including operations forwarded by the main application.
- Compare distribution provenance with local installation authority for the exact artifact, product, version, channel and target.
- Follow approval-to-use changes, interruption, retry, rollback and recovery without assuming atomicity or rollback policy.
- Check retained project copies and diagnostics across local-user changes independently of helper authorization.

A denial for one helper request does not prove every route is protected. An authentic package may still be unauthorized for a target; this is not a claim that signatures are absent or broken. Keep evidence-supported protections and conflicting policy notes visible. Three scenario families do not require three defects.

For `desktop` plus `cicd-supply-chain`, reuse global release artifact, distributor and crossing IDs. Keep distinct distribution/staging and staged-release-to-target crossings separate where supported by the supplied topology, with one evidenced owner per crossing. Preserve delivery build/publication and desktop local caller/installation contributions; derive ownership from supplied responsibility evidence, leaving unknown ownership null with an open identity gap. Two descriptions of one release remain one source, not independent corroboration.

## Verification planning

**Document resolution:** with separate authority for a synthetic exercise, open projects naming an intended resource, an unrelated local resource and an external destination. Observe parsing, local reads, outbound requests and returned data, including changed destinations where supported. Pass requires only authorized resources and recipients with the legitimate case working; an out-of-scope read or disclosure fails; missing downstream observations make the corresponding claim inconclusive. This proposal stays `not_run` without execution evidence.

**Helper and installation:** with separate authority, compare an authorized updater and a plugin without installation authority requesting installation of a provenance-valid package. Include the correct target, a different target, a target changed after approval and an interrupted-install retry. Correlate sender, helper decision, artifact identity and actual destination changes. Pass requires authorized operations to work and no forbidden effect from unauthorized requests through recovery. Unauthorized installation fails; absent helper or target evidence is inconclusive. Provenance success alone cannot pass this authority test. The proposal neither authorizes execution nor records a result.

The [artifact contract](../../reference/artifact-contract.md) provides optional expanded detail. Resolve exact technology rules through external secure-coding packs; with no tools, stack version, catalog or match, record unverified coverage and continue architecture analysis. No platform settings or API prescriptions are supplied here.
