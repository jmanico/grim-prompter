---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# Embedded Firmware Threat Modeling

Use the [quick role](../../quick/embedded-firmware.md) with supplied evidence for a bounded `TM_REPORT`, or run each deep stage under the runbook, reading its cumulative predecessor file from the run folder. No optional methods are required; read-only project access follows the runbook. Only `SYSTEM_UNDER_REVIEW` is external; optional prior models, rubrics and separately executed fragments travel as typed, sanitized attachments. A selected method is not an executed method.

| Stage | Input | Output |
| --- | --- | --- |
| [00-scope-and-evidence](00-scope-and-evidence.md) | `SYSTEM_UNDER_REVIEW` | `TM_CONTEXT` |
| [01-system-model](01-system-model.md) | `TM_CONTEXT` | `TM_SYSTEM_MODEL` |
| [02-threat-analysis](02-threat-analysis.md) | `TM_SYSTEM_MODEL` | `TM_ANALYSIS` |
| [03-challenge-and-consolidate](03-challenge-and-consolidate.md) | `TM_ANALYSIS` | `TM_REVIEWED_MODEL` |
| [04-treatment-and-validation](04-treatment-and-validation.md) | `TM_REVIEWED_MODEL` | `TM_TREATMENT_PLAN` |
| [05-report-and-handoff](05-report-and-handoff.md) | `TM_TREATMENT_PLAN` | `TM_REPORT` |

## Evidence questions

1. Which images can be selected at startup and recovery, and what evidence identifies the code actually executed?
2. Who supplies an authentic image, and who separately authorizes its replacement on this device?
3. Which versions and critical-data states are permitted during rollback, interruption and recovery, and who may approve exceptions?
4. What can a service or debug actor read or change in each lifecycle state, separately from stored secrets and device authority?
5. Who admits replacement peripherals, what input can they supply, and which privileged firmware decision consumes it?
6. What remains able to detect corruption and restore image, data and policy when the running firmware is unavailable?
7. If IoT/edge is included, how do current ownership, queued commands and device identity survive replacement, disconnection and recovery?

Use these as unattended evidence needs. An optional interview has at most five questions per batch and two batches unless extended. With no answer, return partial scope and gaps; do not block.

## Boundary and lifecycle checks

- Follow each executable image from acquisition through replacement, selection and startup. Separate image authenticity from owner authorization to replace it and from the code actually executed. A signed image alone proves no effective control; identify the decision, protected reference and bypass paths before crediting enforcement. Where signing trust is in scope, ask how signing-key compromise or loss of trust in the key store can be detected and recovered from.
- Compare permitted versions in normal update, rollback and recovery. Ask who can authorize an exception, which critical data accompanies an image and whether intermediate recovery states preserve the supplied policy. Neither rollback nor automatic recovery is universally required or forbidden. When applying SP 800-193’s authenticated-update requirements, distinguish the required capability to prevent unauthorized rollback to vulnerable versions (or versions that enable them) from permission for an authorized rollback.
- Trace interruption and corruption through detection and recovery. Identify what can still detect damage, obtain an acceptable image and restore critical data when active firmware or policy is unavailable. Ask about evidence lost during restoration and dependent devices needed to recover; boot completion alone is not restored authority or safety. Could the recovery policy restore the attacked version and repeat the attack/recovery cycle?
- Separate permission to service or debug from permission to read persistent secrets, change policy or act as the device. Follow each local interface through production, servicing and returned-to-service states. Physical possession is a capability premise, not proof of secret extraction or privileged access. Ask whether debug or diagnostic paths can write executable images or critical data outside the authorized update path. If local physical presence authorizes update or recovery, identify how it is distinguished from a remote or software-spoofed request.
- Follow peripheral replacement and provenance separately from the content it supplies. Identify who admits the replacement, which input it can influence and which firmware decision consumes it. A recognized peripheral does not authorize every message; an unfamiliar one is not automatically exploitable.
- Trace peripheral input into privileged behavior and critical data changes. Identify the parser or decision boundary, reachable action and required authority without inventing an API or memory flaw. Seek observations that reject invalid or unauthorized input while permitting legitimate use; distinguish denial from a hidden state change.
- Follow manufacturing or provisioning assumptions into deployment, maintenance, transfer and retirement where supplied. Track stored authority, current owner, accepted image policy and replaced peripheral identity across these transitions. Do not assume erasure, revocation propagation or safe defaults from a lifecycle label.
- For a supplied IoT/edge subsystem, follow current device ownership, intermediary delegation, delayed observations and queued commands through disconnect and reconnect. Separate submission, acceptance, delivery and execution. Recheck the same device, owner, command and firmware-policy identities after recovery or replacement; transport success establishes none of those decisions.

These questions distinguish authenticity, owner authority and version policy; servicing from secret/device privilege; and peripheral provenance from input behavior. They do not prescribe a vendor, algorithm or device setting. A protective observation defeats only the tested premise, missing evidence is not a defect, and a retired candidate is not remediated.

For `embedded-firmware` plus `iot-edge`, establish shared device, owner, image-policy and command IDs from evidence, one boundary owner and explicit dependencies. Similar names do not establish equivalence. Preserve firmware and IoT/edge contributions without duplicating one observation as corroboration.

## Verification planning

**Image and recovery policy:** with separate authorization in a synthetic setting, compare an authentic but owner-unapproved or version-disallowed image with an approved permitted image. Interrupt replacement and follow recovery. Observe authorization, image selection, active code and critical data independently. Pass requires the supplied policy and positive case at each measured step; unauthorized selection fails; missing observations are inconclusive. Signing or boot completion alone is insufficient.

**Servicing and peripheral behavior:** with separate authorization, compare permitted diagnostics with secret-read and privileged-action requests, then admitted peripheral input with a replacement peripheral requesting an unauthorized action. Observe both denial and resulting device state, including return from servicing. Pass requires the supplied restrictions and legitimate operations; unauthorized disclosure or action fails; absent state or access evidence is inconclusive. New verification remains `not_run`; neither example authorizes device operations or establishes safety.

The optional [artifact contract](../../reference/artifact-contract.md) expands definitions embedded in each prompt. Without tools or exact technology packs, continue with gaps and unverified technology dependencies. For large inputs, inventory omissions. Only when a tool limit prevents writing one artifact file, preserve all records in the runbook's part files using the embedded chunk protocol and reassemble a complete sequence before using it as a parent. Keep earlier change declarations in sanitized source history and declare only each immediate-parent delta. Only when a tool limit prevents writing one Markdown file, split prose into part files at section boundaries and state unfinished work.
