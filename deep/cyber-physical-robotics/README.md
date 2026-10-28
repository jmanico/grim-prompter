---
external_inputs:
  - SYSTEM_UNDER_REVIEW
---
# Cyber-Physical and Robotic Systems Threat Modeling

Use this family to trace supplied sensor and command information into possible physical effects, while keeping each causal step and its evidence distinct. The architecture label does not imply a warehouse, particular hardware, networking or an independent emergency control.

Run the [quick role](../../quick/cyber-physical-robotics.md) under the runbook with sanitized evidence as `SYSTEM_UNDER_REVIEW.md` in the run folder for a bounded `TM_REPORT`. For deep work, run each stage under the runbook, reading its preceding cumulative JSON file from the run folder. Only `SYSTEM_UNDER_REVIEW` is external; prior models, rubrics and separately executed method fragments are optional attachments.

| Prompt | Input | Output |
| --- | --- | --- |
| [00 collect physical-system evidence](00-scope-and-evidence.md) | `SYSTEM_UNDER_REVIEW` | `TM_CONTEXT` |
| [01 map sensing, authority and physical effects](01-system-model.md) | `TM_CONTEXT` | `TM_SYSTEM_MODEL` |
| [02 analyze the three causal families](02-threat-analysis.md) | `TM_SYSTEM_MODEL` | `TM_ANALYSIS` |
| [03 challenge causal links and protective scope](03-challenge-and-consolidate.md) | `TM_ANALYSIS` | `TM_REVIEWED_MODEL` |
| [04 plan physical-system outcomes and safe verification](04-treatment-and-validation.md) | `TM_REVIEWED_MODEL` | `TM_TREATMENT_PLAN` |
| [05 report physical-state and authority uncertainty](05-report-and-handoff.md) | `TM_TREATMENT_PLAN` | `TM_REPORT` |

Each prompt embeds its baseline, typed contract, uncertainty rules and runbook operating boundary. Inventory unavailable material and continue with gaps. A selected method is not an executed procedure. Reassemble complete chunk sequences before using them as a predecessor; incomplete or conflicting sequences remain partial. Current changes describe only the immediate-parent delta; preserve older declarations as sanitized source history.

## Evidence questions

1. Which physical observations enter which sensors, perception processes and planners, and what distinguishes a measured value from an inferred state?
2. Which component accepts a proposed command, for which recipient, mode and actor authority? What evidence connects acceptance to physical actuation?
3. How do remote task assignment, autonomous planning and local operator requests compete? Which precedence, cancellation, revocation and restart rules are actually supplied?
4. Where can nearby people interact with the system, which physical outcomes must be avoided, and who owns that boundary in the supplied responsibility model?
5. Which exact intervals, units, time origins and clock uncertainty constrain input age and physical response? Which evidence measures each endpoint?
6. What continues during lost connectivity, which authority or observations expire, and what triggers fallback or requires deliberate recovery?
7. What dependencies do local emergency controls share with normal processing, and what distinguishes request, acceptance, indication and physical stop?
8. What changes after restart, replacement, reconnection or restored queued work? Which current identity, mode and command revision must be rechecked?

Use these as unattended evidence needs or optional guided preparation. In an interview, ask at most five questions per batch and at most two batches unless the caller extends it. If nobody answers, stop the interview and return a partial bundle with gaps; analysis does not wait.

## Boundary and lifecycle checks

- Trace actual sensed observation, inferred perception, planner proposal, accepted command and observed physical actuation as separate milestones. Name each transformation, input origin, unit, age and applicable mode. None automatically proves the next; a displayed stopped status is not evidence of physical stop.
- Follow attacker-influenced observations through the supplied processing and control path. Identify the access needed to alter, replay, suppress or substitute an input, what perception consumes, what planning proposes, what command acceptance permits and what reaches an actuator. Missing links are topology gaps, not assumed bypasses.
- Compare remote task assignment, autonomous planning and local operator commands against the actual authority and arbitration rules. Identify allowed actions, target binding, mode, precedence, simultaneous requests, cancellation and revocation. Task assignment does not itself confer actuation authority; being nearby does not grant operator authority.
- Model nearby people and the physical interaction boundary explicitly, with supplied responsibility evidence and one architecture owner. Trace possible motion, force or other physical effect to the person or protected area, and the observation that could establish it. Do not substitute a software error or command acknowledgment for a demonstrated physical consequence.
- Keep observation time, processing time, command acceptance time and physical response time distinct. Preserve supplied budgets, units, clock assumptions and uncertainty exactly. Identify which interval is bounded and which ordering matters; a supplied time budget is not universal, and a timestamp alone does not prove freshness or a deadline.
- Follow lost connectivity and delayed inputs through the supplied fallback behavior. Determine what continues locally, what authority expires, which inputs become stale and what requires a transition. Disconnection alone is not failure; assess it against the stated mode and physical constraints, not an assumed need for continuous cloud access.
- Trace local emergency controls through their actual acceptance and physical response paths, including shared dependencies. Do not assume independence, effectiveness, immediacy or priority from the emergency label. Separate a requested stop, an accepted stop, an indicated stop and physical cessation; keep unobserved links explicit.
- Review recovery, restart, replacement and reconnection against current authority and state: queued commands, old plans, stale observations, revoked operators and reset permission. Identify who may resume, what is revalidated and what prevents unintended restart. Preserve conflicts rather than choosing the most recent description without evidence.

These are scoped questions, not universal design claims. Seek counterevidence at each enabling link. When protection defeats a path, retain that disposition; do not manufacture a residual defect. When mixing with `iot-edge`, establish the same gateway, recipient and command context from full source fragments, trace the crossing into arbitration, assign one evidenced owner per boundary and retain each view's contribution. Fleet enrollment, delivery acknowledgment and actuation permission are different facts.

## Verification planning

**Observation to physical effect:** propose document review or an explicitly authorized isolated synthetic simulation with a controlled observation and an ordinary positive case. Trace sensor output, perception, planner proposal, accepted command and simulated physical effect independently. Pass requires the supplied observation and person-separation constraints at the relevant boundaries and successful ordinary operation; a simulated trace violating a stated constraint fails; missing input origin, acceptance evidence or physical trace is inconclusive. No real sensor manipulation or movement is authorized.

**Arbitration, delay and recovery:** propose a tabletop or isolated synthetic simulation with stated modes, local stop, remote task and autonomous proposal, followed by connectivity loss, expired authority and reconnection. Correlate source, recipient, epoch, precedence, fallback transition and simulated cessation using the supplied clock and interval. Pass requires all specified acceptance, timing and deliberate-restart conditions; a violating acceptance, missed bound or unauthorized resume fails; absent authority, clock or physical-state evidence is inconclusive. A stopped display alone cannot pass. No emergency-stop action or field testing is authorized.

All new verification stays `not_run` with empty result evidence. The [artifact contract](../../reference/artifact-contract.md) is optional expanded detail; the prompts use read-only project access and run-folder files under the runbook. Resolve exact technology/version rules through external secure-coding packs when authorized and available; otherwise leave prescriptions unverified and continue architectural outcomes. Only when a tool limit prevents writing one file, split JSON into the runbook's part files using the embedded chunk protocol, or prose into part files at section boundaries, with unfinished work explicit. A report establishes neither certification nor operational permission.
