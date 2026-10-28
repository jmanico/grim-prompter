---
id: start-here
title: Start Here
shape: reference
last_reviewed: 2026-10-28
---
# Start here

Grim Prompter runs inside your AI coding agent. The agent reads your repository, gathers evidence with file and line citations, and writes a threat model into a `threat-model/` folder. This guide covers running it on your project and reading what comes back. If you haven't installed the skill yet, follow [Install](README.md#install).

## Run it on your project

Open your project in the agent and ask for a quick run. Name the architecture if you know it:

```text
/threat-model quick api
```

You'll get better results if you also say:

- **the decision the review supports**, such as "before we open the partner API";
- **what's in and out of scope**, such as "only `services/billing`; ignore the admin console";
- **what you already know**, such as known gaps, design documents to read first, or a prior threat model.

The agent inspects your project read-only. It reads documentation, entry points, authorization code, data stores, integrations, deployment configuration and dependency manifests, and it records every source as a `path:start-end` locator in `SYSTEM_UNDER_REVIEW.md`. It doesn't build, test, install or use the network unless you explicitly allow a specific action. Secrets it encounters are replaced with placeholders, and each redaction is recorded. The full rules are in the [agent runbook](runbook.md).

Read `SYSTEM_UNDER_REVIEW.md` first. If the agent misunderstood scope or missed an important component, correct it and run again.

## Go deep

For a decision that warrants more depth, run the six-stage chain:

```text
/threat-model deep web
```

| Stage | Prompt (web) | Reads | Writes |
| --- | --- | --- | --- |
| 00 Scope and evidence | [00-scope-and-evidence.md](deep/web/00-scope-and-evidence.md) | `SYSTEM_UNDER_REVIEW.md` | `00-context.json` |
| 01 System model | [01-system-model.md](deep/web/01-system-model.md) | `00-context.json` | `01-system-model.json` |
| 02 Threat analysis | [02-threat-analysis.md](deep/web/02-threat-analysis.md) | `01-system-model.json` | `02-analysis.json` |
| 03 Challenge and consolidate | [03-challenge-and-consolidate.md](deep/web/03-challenge-and-consolidate.md) | `02-analysis.json` | `03-reviewed-model.json` |
| 04 Treatment and validation | [04-treatment-and-validation.md](deep/web/04-treatment-and-validation.md) | `03-reviewed-model.json` | `04-treatment-plan.json` |
| 05 Report and handoff | [05-report-and-handoff.md](deep/web/05-report-and-handoff.md) | `04-treatment-plan.json` | `05-report.json`, `report.md` |

Each envelope is cumulative: it carries scope, evidence, attachments and every earlier record. Each stage reads the complete previous file, so stages can run in fresh contexts or subagents. To resume, name the run folder, for example `continue threat-model/2026-10-28-deep-web from stage 03`. Each stage also writes a readable `.md` companion.

## Other things you can ask for

| Ask | What happens |
| --- | --- |
| `/threat-model evidence` | Runs the [evidence guide](helpers/evidence-guide.md) and writes only `SYSTEM_UNDER_REVIEW.md`. Ask for guided questions if you want the agent to ask you about gaps: at most five per batch and two batches unless you ask for more. |
| `/threat-model STRIDE per element` | Runs one [method](#choose-a-method-for-a-question) and writes `method-stride-per-element.json`. |
| `/threat-model challenge threat-model/<run>/05-report.json` | The [model challenger](helpers/model-challenger.md) looks for unsupported assumptions, counterexamples and missing evidence. |
| `/threat-model change main...feature` | The [change reviewer](helpers/change-reviewer.md) compares an existing model with the code changes in that range. |

## Read the results honestly

Each JSON envelope is the authoritative model, and its `.md` companion is a readable view of the same records. Keep these distinctions when you share a result:

- **Observed, claimed or hypothesized.** Code the agent read is an implementation observation; a design document is a claim; a scenario without implementation evidence is a design hypothesis.
- **Proposed, not done.** Treatments are proposals and verification is a plan with pass, fail and inconclusive criteria. Nothing was implemented or tested unless the envelope cites real execution evidence.
- **Unrated without your rubric.** Risks stay unrated until you supply a rating rubric; the agent proposes criteria for you to approve.
- **No invented decisions.** Owners, dates, approvals and accepted risk appear only when you supplied them.

Readiness labels describe evidence about the prompts themselves:

| Label | What it establishes | What it does not establish |
| --- | --- | --- |
| Authored (`draft`) | Instructions and contracts exist for use and review | Observed successful execution or new-user completion |
| Content-reviewed (`reviewed`) | Identified content was checked against its scope and sources at a recorded revision | Live behavior, complete method execution or deployed control effectiveness |
| Behavior-evaluated (`evaluated`) | Retained actual runs and assessments support specified cases at specified revisions | Exhaustive coverage or a guarantee for another system or version |

All 36 architecture sets and 29 method prompts are currently `draft`.

This is the library-wide readiness declaration; individual prompts do not carry separate readiness fields. A `last_reviewed` date records editorial review, including scoped corrections, and does not by itself promote a prompt to `reviewed` or `evaluated`.

Technology-specific rules, such as framework settings and version guidance, stay out of these prompts. If you have an exact, already resolved secure-coding pack for your stack, put it in the run folder with its identity, source and version. Otherwise the agent records the dependency as a gap and continues with architectural outcomes.

## Choose architecture by boundaries

Choose one primary set for the decision in scope, then only useful secondary sets for distinct bounded subsystems. A web portal is not automatically a microservice system; a product or language name does not establish its boundaries. For example, keep web primary for browser/session behavior and add multi-tenant SaaS only for an evidenced tenant boundary. State exactly which tenant flows the secondary scope adds.

Use the [composition guide](reference/composition-guide.md) for mixed systems: preserve a global identity map, assign one architecture owner per boundary, retain all contributors and reconcile shared threats/controls once. Do not treat overlapping reports as independent evidence. The [architecture selector](helpers/architecture-selector.md) can explain fit; selection is not execution.

All 36 sets are below. Each quick link opens its quick prompt; each deep link opens its six-stage chain. “Available” means the prompts exist, not that they have passed behavior evaluation.

| Set | Match these actual boundaries | Quick | Deep |
| --- | --- | --- | --- |
| Web application | browser, application origin, session, server, external content, sensitive data | [Quick](quick/web.md) | [Deep](deep/web/README.md) |
| API | API caller, identity, resource ownership, gateway, backend, external callbacks | [Quick](quick/api.md) | [Deep](deep/api/README.md) |
| Monolith | external caller, shared process, privileged functions, common data store, background work | [Quick](quick/monolith.md) | [Deep](deep/monolith/README.md) |
| Modular monolith | module contracts, shared process, module-owned data, internal events, deployment privileges | [Quick](quick/modular-monolith.md) | [Deep](deep/modular-monolith/README.md) |
| Microservices | workload identities, service interfaces, network segments, distributed state, operators | [Quick](quick/microservices.md) | [Deep](deep/microservices/README.md) |
| Service-oriented architecture | service consumers, shared mediation, orchestration, legacy services, transformed identity | [Quick](quick/service-oriented.md) | [Deep](deep/service-oriented/README.md) |
| Event-driven | publishers, brokers, topics, subscribers, event ownership, replay facilities | [Quick](quick/event-driven.md) | [Deep](deep/event-driven/README.md) |
| Batch workflows | scheduler, job definitions, input files, execution identity, intermediate data, outputs | [Quick](quick/batch-workflows.md) | [Deep](deep/batch-workflows/README.md) |
| Serverless | event sources, short-lived functions, execution roles, managed storage, configuration | [Quick](quick/serverless.md) | [Deep](deep/serverless/README.md) |
| Container platform | workloads, hosts, scheduling authority, images, tenant partitions, platform operators | [Quick](quick/container-platform.md) | [Deep](deep/container-platform/README.md) |
| Cloud control plane | administrative identities, resource ownership, delegated roles, automation, audit records | [Quick](quick/cloud-control-plane.md) | [Deep](deep/cloud-control-plane/README.md) |
| Hybrid and multicloud | provider domains, private networks, federated identities, replicated data, failover paths | [Quick](quick/hybrid-multicloud.md) | [Deep](deep/hybrid-multicloud/README.md) |
| Multi-tenant SaaS | tenant identity, shared services, data partitions, support access, tenant configuration | [Quick](quick/multi-tenant-saas.md) | [Deep](deep/multi-tenant-saas/README.md) |
| Data platform | data producers, ingestion, transformation, analytical stores, notebooks, consumers | [Quick](quick/data-platform.md) | [Deep](deep/data-platform/README.md) |
| Real-time streaming | stream producers, partitions, processors, time windows, checkpoints, live decisions | [Quick](quick/real-time-streaming.md) | [Deep](deep/real-time-streaming/README.md) |
| AI and machine learning | data collection, labeling, training, model artifacts, evaluation, inference, feedback | [Quick](quick/ai-ml.md) | [Deep](deep/ai-ml/README.md) |
| Retrieval-augmented generation | document ingestion, source permissions, retrieval, model context, citations, output | [Quick](quick/rag.md) | [Deep](deep/rag/README.md) |
| Agentic AI | user intent, planning, persistent memory, delegated agents, tools, external side effects | [Quick](quick/agentic-ai.md) | [Deep](deep/agentic-ai/README.md) |
| Mobile application | device owner, application storage, operating-system services, other applications, backend | [Quick](quick/mobile.md) | [Deep](deep/mobile/README.md) |
| Desktop application | local user, files, application process, privileged helpers, plugins, update distribution | [Quick](quick/desktop.md) | [Deep](deep/desktop/README.md) |
| Browser extension | web pages, content scripts, extension background work, browser privileges, user accounts | [Quick](quick/browser-extension.md) | [Deep](deep/browser-extension/README.md) |
| CLI and developer tools | local workspace, configuration, environment, tool process, plugins, remote services | [Quick](quick/cli-developer-tools.md) | [Deep](deep/cli-developer-tools/README.md) |
| IoT and edge | devices, local gateways, physical access, fleet identity, cloud services, update authority | [Quick](quick/iot-edge.md) | [Deep](deep/iot-edge/README.md) |
| Embedded firmware | boot chain, firmware images, debug interfaces, persistent secrets, peripherals, servicing | [Quick](quick/embedded-firmware.md) | [Deep](deep/embedded-firmware/README.md) |
| Operational technology and industrial control systems | business networks, engineering workstations, controllers, operator stations, physical process | [Quick](quick/ot-ics.md) | [Deep](deep/ot-ics/README.md) |
| Cyber-physical and robotics | sensors, perception, planning, actuators, operator authority, nearby people | [Quick](quick/cyber-physical-robotics.md) | [Deep](deep/cyber-physical-robotics/README.md) |
| Peer-to-peer | peer identities, discovery, routing, shared state, local trust, network partitions | [Quick](quick/peer-to-peer.md) | [Deep](deep/peer-to-peer/README.md) |
| Blockchain and smart contracts | transaction submitters, contract state, administrators, external price data, off-chain services | [Quick](quick/blockchain-smart-contracts.md) | [Deep](deep/blockchain-smart-contracts/README.md) |
| Identity federation | identity providers, relying services, account linkage, trust configuration, recovery | [Quick](quick/identity-federation.md) | [Deep](deep/identity-federation/README.md) |
| Payments and transactions | customer intent, authorization, transaction state, ledger, payment partners, reconciliation | [Quick](quick/payments-transactions.md) | [Deep](deep/payments-transactions/README.md) |
| Real-time collaboration | participants, rooms or documents, persistent connections, shared state, presence data | [Quick](quick/collaboration-realtime.md) | [Deep](deep/collaboration-realtime/README.md) |
| Content and media delivery | uploaders, processing workers, content storage, distribution caches, entitlement, viewers | [Quick](quick/content-media-delivery.md) | [Deep](deep/content-media-delivery/README.md) |
| CI/CD and software supply chain | contributors, source changes, build workers, dependencies, artifact storage, signing, deployment | [Quick](quick/cicd-supply-chain.md) | [Deep](deep/cicd-supply-chain/README.md) |
| Enterprise integration | partner organizations, connectors, mapped accounts, business records, integration operators | [Quick](quick/enterprise-integration.md) | [Deep](deep/enterprise-integration/README.md) |
| Offline-first sync | local replicas, offline identity, synchronization service, conflict resolution, central authority | [Quick](quick/offline-first-sync.md) | [Deep](deep/offline-first-sync/README.md) |
| High-assurance isolated environment | security domains, controlled transfer, removable media, administrators, offline maintenance | [Quick](quick/high-assurance-isolated.md) | [Deep](deep/high-assurance-isolated/README.md) |

## Choose a method for a question

Start with the architecture role's own baseline. Add a method only when it answers a distinct question and you can supply its inputs. The [method selector](helpers/method-selector.md) produces recommendations, not execution. Run a chosen method with `/threat-model <method>` or `$threat-model <method>`. The agent writes `method-<id>.json` to the run folder; carry that `THREAT_MODEL_FRAGMENT` into a deep run as attributed evidence. A copied method prompt or selection does not prove that procedure ran. Do not force different methods into one score.

Name the actual result file in the next request, for example `/threat-model deep web using threat-model/2026-10-28-method/method-stride-per-element.json as a prior method fragment`. The agent sanitizes a copy into the new run's `inputs/` folder, records it in `SYSTEM_UNDER_REVIEW.md`, and carries its content into stage 00's attachments. Use the path your method run actually returned; the folder may have a numeric suffix. This carries the previous execution as evidence without claiming it ran again.

The following 29 links are runnable roles with bounded scope. Effort means a suggested unit of work, not a measured duration or a promise that one run completes the procedure. Inputs and source prerequisites remain mandatory for claims that depend on them. Missing prerequisites leave that work partial or unperformed while the architectural baseline continues. Each linked role carries its own boundaries. If a role or a required lawful source excerpt is unavailable, record the gap; do not reconstruct a specialist procedure from its name.

| Method and purpose | Inputs and source prerequisites | Suggested effort and limit |
| --- | --- | --- |
| [Four-question workflow](methods/four-question-workflow.md) — Frame scope, problems, responses and review | System, stakeholders, objectives and available evidence | One scoped pass; general workflow, not a full methodology |
| [STRIDE per element](methods/stride-per-element.md) — Enumerate security scenarios by element | Elements, flows, functions, boundaries and protections | Per-element applicability pass; interactions still matter |
| [STRIDE per interaction](methods/stride-per-interaction.md) — Examine directional interactions | Source/target types, flow data, boundaries and properties | Per-interaction pass; keep category exclusions, do not assume a boundary crossing or exact tool equivalence |
| [LINDDUN GO](methods/linddun-go.md) — Elicit privacy concerns in a workshop | System hotspots, lawful deck access and actual participant contributions | Bounded card discussion; disclose unreviewed cards |
| [LINDDUN PRO](methods/linddun-pro.md) — Analyze privacy across data interactions | DFD, sender/transfer/recipient context and source mapping guidance | Systematic interaction pass; missing mappings limit completeness |
| [PASTA](methods/pasta.md) — Connect application threats to business risk | Objectives, decomposition, threat/weakness evidence, attack-validation results and risk inputs | Seven phases; missing validation stays unperformed |
| [Attack trees](methods/attack-trees.md) — Decompose an adversary goal | Goal, subgoals, prerequisites and constraints | One bounded goal; AND needs all children |
| [Attack graphs](methods/attack-graphs.md) — Explore prerequisite/state transitions | Initial/goal states, action preconditions/effects, evidence and traversal limits | Bounded state exploration; pinned cyclic profile, disclose cutoffs |
| [Misuse and abuse cases](methods/misuse-abuse-cases.md) — Explore adverse workflow goals | Normal use cases, assets, loss concerns and actor assumptions | One normal workflow and its adverse sequences with protective requirements; no invented actors or required exploit |
| [Security use cases](methods/security-use-cases.md) — Specify protective interactions | Threats or misuse cases, assets/services and desired outcomes | Success/failure alternatives per interaction; no effectiveness claim |
| [NIST data-centric modeling](methods/nist-data-centric.md) — Trace data exposure | Data, authorized locations/movement, objectives, attacks and controls | Scoped data lifecycle pass; source remains Initial Public Draft |
| [OCTAVE Allegro](methods/octave-allegro.md) — Analyze organizational information-asset risk | Impact criteria, asset ownership/use, containers and scenarios | Eight-step asset review; original instructions, no copied worksheets |
| [Trike](methods/trike.md) — Compare allowed actions with implementation | Actor/asset/action rules, implementation flows, stakeholder-supplied asset values and justified ordinal factors | Bounded experimental v1 pass; ordinal ranks are not probabilities |
| [Hybrid Threat Modeling Method (hTMM)](methods/htmm.md) — Combine elicitation with formal risk work | Requirements/system artifacts, lawful Security Cards, real stakeholder-group responses, caller-supplied impact ratings and named risk process | Multi-step workshop plus risk work; disclose skipped steps |
| [Persona non Grata](methods/persona-non-grata.md) — Explore hypothetical attacker archetypes | System goals, plausible capabilities, roles and access assumptions | Bounded personas and misuse cases; no invented empirical motives |
| [Security Cards](methods/security-cards.md) — Broaden discussion across threat dimensions | Lawful caller-accessible deck, system description and real responses | One scoped cross-dimension discussion; disclose partial-deck coverage, no reproduced deck or simulated consensus |
| [Elevation of Privilege](methods/elevation-of-privilege.md) — Facilitate card-to-system scenarios | Shared model, lawful deck and actual players/contributions | One bounded recorded round of card-to-system discussion; no invented play, scoring or full-game completion |
| [STPA-Sec](methods/stpa-sec.md) — Explore insecure control actions and losses | Losses, operational context, control/feedback structure and process models | Bounded 2018 application pass; disclose application inconsistencies, no originating-method or assurance claim |
| [STPA](methods/stpa.md) — Analyze unsafe control actions | Stakeholder losses, hazards, constraints, conditions and feedback structure | One basic chapter 2 analysis pass; no safety assurance or certification |
| [FMEA and FMECA](methods/fmea-fmeca.md) — Analyze failures and effects | Functions, dependencies, failure evidence and ground rules; criticality needs justified criteria/likelihood | Scoped failure analysis; no fabricated rates or universal thresholds |
| [CORAS](methods/coras.md) — Structure risk scenarios and treatment | Target/assets, stakeholder criteria, threat evidence and estimation basis | Pinned eight-step edition; no invented stakeholder approvals |
| [Bow-tie analysis](methods/bow-tie.md) — Connect causes, top event and consequences | Hazard, causes, consequences, barriers and effectiveness evidence | Eight-step barrier pass; distinguish prevention from recovery |
| [CSA MAESTRO for agentic AI](methods/csa-maestro.md) — Examine agentic AI layers and interactions | Goals, tools, autonomy, data, interactions and caller risk rubric | Seven-layer article scope; implementation/monitoring need evidence |
| [MITRE ATT&CK](methods/attack-enrichment.md) — Map grounded behavior to ATT&CK | Supported behavior, chosen domain and item-level source/version access | One evidenced behavior mapping pass; verify selected IDs/version, taxonomy is not attack evidence |
| [CAPEC](methods/capec-enrichment.md) — Map scenario mechanics to attack patterns | Mechanics, prerequisites, weaknesses and item-level source access | One scenario-mechanics mapping pass; verify selected IDs, no guessed catalog matches |
| [MITRE ATLAS](methods/atlas-enrichment.md) — Map AI adversary scenarios | Grounded AI scenario and item-level source access with exact revision | One grounded AI-scenario mapping pass; verify AML IDs/revision, source cases are not system observations |
| [Cyber Kill Chain](methods/cyber-kill-chain.md) — View a fitting intrusion by stage | Intrusion scenario and stage evidence | One bounded mapping; unknown/not-applicable stages stay explicit |
| [DREAD](methods/dread.md) — Apply a supplied ordinal rubric | Caller-approved anchors and evidence for all five criteria | One justified scoring pass or unrated; not empirical probability |
| [CVSS](methods/cvss.md) — Describe technical vulnerability severity | Supported vulnerability/metrics; numeric score needs verified official calculator or lookup implementation | Vector first; score uncalculated without dependencies, not business risk |

## Suggest a method or architecture

Open an issue in this repository with a short, sanitized proposal: the boundary or question current choices miss, why an existing choice is insufficient, primary procedure sources you know, and required inputs and any access or reuse limits. Leave out private system material.
