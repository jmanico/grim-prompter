---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# Browser Extension Threat Modeling

Follow the extension’s declared operations and data through the page, extension and any supplied local or remote contexts. Storage, account synchronization and rendering checks apply where supported by the supplied design; record unknowns or justified not-applicable dispositions otherwise. Keep page influence, browser capability, declared purpose and server authority distinct. Start with any description, sanitized observation, diagram, requirement or prior model; missing evidence becomes a specific gap.

Run [Browser Extension Quick Threat Analysis](../../quick/browser-extension.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder for a bounded `TM_REPORT`. For the deep path, run each stage under the runbook, reading the preceding cumulative JSON file from the run folder. Only `SYSTEM_UNDER_REVIEW` is external. No optional method is needed for the baseline; read-only project access follows the runbook.

| Prompt | Input | Output |
| --- | --- | --- |
| [00 Scope and evidence](00-scope-and-evidence.md) | `SYSTEM_UNDER_REVIEW` | `TM_CONTEXT` |
| [01 System model](01-system-model.md) | `TM_CONTEXT` | `TM_SYSTEM_MODEL` |
| [02 Threat analysis](02-threat-analysis.md) | `TM_SYSTEM_MODEL` | `TM_ANALYSIS` |
| [03 Challenge and consolidate](03-challenge-and-consolidate.md) | `TM_ANALYSIS` | `TM_REVIEWED_MODEL` |
| [04 Treatment and validation](04-treatment-and-validation.md) | `TM_REVIEWED_MODEL` | `TM_TREATMENT_PLAN` |
| [05 Report and handoff](05-report-and-handoff.md) | `TM_TREATMENT_PLAN` | `TM_REPORT` |

Each prompt embeds its contract, baseline, tool fallback and continuation rules. Optional prior models, rubrics and separately executed method fragments travel in typed attachments. Selection is not execution. Reassemble one complete chunk sequence before treating it as a predecessor; preserve original IDs and sanitized source history. Declare changes only against the immediate parent, never copy old deltas as new changes.

## Evidence questions

1. Which page or frame can supply action, target and recipient fields to the content script, which direct external page or extension message channels and web-exposed extension resources are evidenced as distinct entry points, and what binds the background request to a current document and the user's intended operation?
2. Which browser capabilities can the background use, and which results return to the content script or page after navigation? What trace shows the actual recipient?
3. What collection and operations does the declared purpose permit? Which sites, data categories, triggers and destinations are evidenced, including collection from a second site while the user acts on the first?
4. Where are local data, source addresses and credentials retained? What happens on sign-out, profile change, deletion or private-window use, and which of those states was actually inspected?
5. What binds a queued operation to its original account when A signs out, B signs in, or A's delayed response arrives after restart? What does the server authorize, and what is the disposition of rejected or duplicate work?
6. Who can publish a release, which installed release is evidenced, and how do permission changes, local-data migration, interrupted installation and rollback affect the original purpose and retained data?
7. How are supplied data displayed in the web application and extension views? What proves that untrusted content remains data rather than becoming an action for another viewer?

Use these as optional preparation questions or unattended evidence needs. The prompts work without an interview. If the caller separately requests a preparation interview, ask at most five at once and at most two batches unless the caller extends it. With no answer, stop asking and return supported scope, partial coverage and gaps.

## Boundary and lifecycle checks

- Trace page influence through content script to background action; sender recognition and operation authority need separate evidence.
- Follow background results back to the recipient through navigation or frame changes.
- Compare cross-site reads, retention and onward disclosure with the declared user purpose and collection trigger.
- Follow local data copies through sign-out, deletion, profile changes and recovery without assuming storage defaults.
- Keep queued creator, active account and server authorization separate during delayed responses, reconnect and retries.
- Follow publisher authority through delivery, installation and migration; distinguish known release identity from observed behavior.
- Inspect data rendering in extension and web views with each audience and context stated.
- Check repeated messages and interrupted work against resource and recovery invariants supported by the design.

The numbered checks in each prompt govern that prompt’s analysis; these summaries are navigation aids. These checks support three scenario families: page-controlled privileged actions; cross-site collection or disclosure beyond purpose; and sync/update changes that expose retained data or alter behavior. They do not require three defects. A denial of one message does not prove every action safe, and a valid release origin does not prove purpose-limited collection.

For `browser-extension` plus `web`, reuse global account, data-object and sync-service identities. Use one shared extension-to-service boundary and its supplied owner. The extension lens covers page influence and browser authority; web covers application sessions, server authorization and rendering. Preserve both contributions on a genuinely shared scenario without merging unrelated rendering and privilege failures or counting a repeated trace twice.

## Verification planning

Plan verification around the supplied extension operations, permissions and data.

**Page request and return:** with separate authority for a synthetic exercise, alter a page request's action, target and recipient, navigate before delivery, and compare a legitimate selected-excerpt save. Observe the sender context, background effect and returned data. Pass requires the authorized case to work with no forbidden operation or disclosure. An observed out-of-purpose effect fails; absent background or recipient evidence is inconclusive. A displayed error alone is insufficient. Keep the proposal `not_run` until execution evidence exists.

**Account and release transition:** with separate authority, queue A's note, switch to B, deliver A's delayed response, interrupt and restart sync, then apply an intended synthetic release and interrupt its migration. Compare local visibility, outbound account, remote acceptance, installed release, post-update collection and recovery. Pass requires no reassignment or exposure of A's note, purpose-limited collection and documented pending-work disposition. A forbidden read/write or collection fails; missing account, server or installation traces leave the corresponding claim inconclusive. This proposal neither grants test authority nor claims a pass.

The [artifact contract](../../reference/artifact-contract.md) offers expanded detail, but the prompts embed the contract and use the runbook for file handoffs. Resolve exact platform and version rules through external secure-coding packs; with no tools or matching pack, keep dependent prescriptions unverified and continue architectural outcomes. Only when a tool limit prevents writing one file, use the embedded JSON chunk protocol for the runbook's part files or split prose into part files at section boundaries, recording unfinished work explicitly.
