---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# Content and Media Delivery Threat Modeling

Analyze the supplied content lifecycle from upload through processing, storage, publication and distribution to its permitted audience. Adapt to the caller's architecture.

Run [Quick Content and Media Delivery Threat Analysis](../../quick/content-media-delivery.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder for a quick `TM_REPORT`. For deep analysis, run each stage under the runbook, reading its full cumulative JSON handoff from the run folder:

| Prompt | Input | Output |
| --- | --- | --- |
| [00 Scope and evidence](00-scope-and-evidence.md) | `SYSTEM_UNDER_REVIEW` | `TM_CONTEXT` |
| [01 System model](01-system-model.md) | `TM_CONTEXT` | `TM_SYSTEM_MODEL` |
| [02 Threat analysis](02-threat-analysis.md) | `TM_SYSTEM_MODEL` | `TM_ANALYSIS` |
| [03 Challenge and consolidate](03-challenge-and-consolidate.md) | `TM_ANALYSIS` | `TM_REVIEWED_MODEL` |
| [04 Treatment and validation](04-treatment-and-validation.md) | `TM_REVIEWED_MODEL` | `TM_TREATMENT_PLAN` |
| [05 Report and handoff](05-report-and-handoff.md) | `TM_TREATMENT_PLAN` | `TM_REPORT` |

Only `SYSTEM_UNDER_REVIEW` is external. Prior models, rubrics and separately executed method fragments are optional attachments. Missing tools, optional methods or packs do not stop the baseline; return partial work and actionable gaps without waiting for an interview. Complete original-byte chunk sequences must be reassembled before continuity is claimed; unknown or unsafe inputs follow each prompt's preservation and sanitization rules.

## Evidence questions

- Who owns submitted bytes and each version, and who may request parsing, transcoding or derivative creation?
- Which input object/version and output destination does each job invocation authorize, under which execution identity?
- Who may bind a derivative/version to a publication, and how are original retirement and late completion handled?
- Which creator, manifest and object/origin mappings select delivered content, and who can change them?
- What viewer/resource/operation and entitlement revision authorize delivery, including direct and alternate routes?
- What may the cache store, especially private or credential-bearing responses, and what evidence proves eligibility? Which request attributes select stored variants, audience and reuse time?
- Could an unintended or substituted response enter the evidenced cache and reach other viewers? Which insertion and reuse routes are known?
- What recipient, resource and lifetime constrain a reusable link?
- What changes after entitlement removal, publication replacement or expiry, and which paths and retained copies remain outside evidenced revocation?
- In a serverless subsystem, which event source may invoke the function, which role may read/write each object, and which separate authority releases the result?

## Analysis boundaries

The chain follows three families:

- Hostile uploads through processing and derivative generation, including the separation of runtime grants from job authorization.
- Entitlement changes against cached content and reusable links, with the caller's audience and lifetime rules.
- Origin or metadata substitution and attribution, including unintended cache insertion and reuse where evidenced.

Use the caller's actual lifecycle and platform evidence. Each stage applies the checks to its own task, from collecting evidence to reporting decisions. Shared upload, job, derivative and origin IDs stay global. In mixed serverless scope, encode zone membership and one owner per evidenced crossing; tag only records with an actual contribution from both lenses. Unknown event ingress stays a gap linked to the known trigger, not an invented endpoint.

1. Identify uploaded bytes and versions separately from names, type labels and claimed scans. Account for interpreter and resource effects.
2. Compare invocation admission, runtime-role ambient grants and narrower job authorization. Denied grants block storage operations; unknown grants stay inconclusive. Input-memory effects and persisted derivative writes need separate authority checks.
3. Trace derivative release and the permitted publication/course binding, including completion after original retirement.
4. Map origin, creator and object selection. Keep alternate delivery paths explicit even when direct reads are protected.
5. Compare the viewer's current entitlement with authority at link issue or cache fill; keep audience, operation and resource separate.
6. Distinguish storage eligibility from insertion and reuse. Ask about private or credential-bearing responses, stored variants and the actual availability or validation rule. Unknown substitution paths remain gaps.
7. Limit invalidation claims to evidenced locations and routes; retain limits for alternate edges and previously delivered copies.
8. Use supplied processing and delivery budgets to assess recovery and resource effects; missing limits do not demonstrate exhaustion.

Use these as coverage lenses, not mandatory findings. Keep scoped protective observations and conflicting sources. A passing comparison protects only the evidenced identity, operation, version, audience, time and full route; it does not erase unrelated gaps. Technology-specific APIs, settings, headers and version prescriptions belong only in exact resolved secure-coding packs with provenance. If unavailable, continue architecture analysis and mark dependent rules unverified.

## Verification planning

Choose a design that distinguishes an allowed operation from the adverse case on the same evidenced route. These are plans (`not_run`), not permission to execute or claims of effectiveness.

1. **Processing and publication:** compare a matching upload/job/derivative tuple with changed input version, destination, owner, release scope and one late completion after retirement. Observe selected bytes, actual runtime grants, processing effects and released mapping. Pass requires intended output without an out-of-job effect; fail requires a supported unauthorized read/write/release or harmful processing effect. Missing grants, route or observations are inconclusive. An inert marker is sufficient.
2. **Delivery and reuse:** issue a scoped link and fill the cache while entitled; compare matching reuse with a copied link, wrong audience, changed resource, expiry and revocation. Observe recipient, object, entitlement revision and time through the full path. Pass means the supplied delivery policy holds; fail means disallowed delivery. Unknown applicable eligibility, insertion path, reuse availability/validation, audience, policy or timing is inconclusive. Origin-only denial or local removal cannot establish global protection.

Each prompt embeds its own contract; absent references do not disable it. These instructions do not establish model execution, compliance or operational readiness.

See the [artifact contract](../../reference/artifact-contract.md) for the shared record definitions.
