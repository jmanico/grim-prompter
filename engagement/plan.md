---
id: engagement/plan
title: Engagement Plan
shape: role
last_reviewed: 2026-11-16
sources:
  - https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
---
# Engagement Plan

Recommend how to run the threat model: which architecture lenses, which methods, what depth, and how risk will be rated. The consultant decides.

Input: `01-intake/SYSTEM_UNDER_REVIEW.md` and `01-intake/initial-understanding.md`, including any edits the consultant made. Output: `02-plan/plan.md`.

## Work

Follow the [engagement rules](rules.md).

1. **Select architecture lenses.** Run the [architecture selector](../helpers/architecture-selector.md) on the evidence bundle under the runbook's `select` mode. Take its primary architecture and bounded secondary scopes. Architecture ids are the basenames in `quick/`.
2. **Select methods.** Run the [method selector](../helpers/method-selector.md) the same way. Method ids are the basenames in `methods/`. Weigh what the evidence can support:
   - Classification and enumeration methods that work from a design, such as STRIDE per element or per interaction, suit reviews without code.
   - Enrichment methods such as ATT&CK, CAPEC or ATLAS need behaviour specific enough to map. With documents only, expect partial coverage and say so.
   - Attack trees or attack graphs suit one or two high-consequence goals, not the whole system.
   - Privacy methods (LINDDUN) apply only when a privacy review is in scope.
   - Rating methods (CVSS, DREAD) are not a substitute for the client's risk matrix.
3. **Recommend depth.** Quick suits a small system, a near decision or a first pass. Deep suits many components or boundaries, high consequence, or a client who expects a challenged model. Deep runs six stages and takes correspondingly longer.
4. **Check the review scope.** Security by default. If the system holds personal, health or financial data about people and privacy was not requested, recommend raising a privacy review with the client; do not add it yourself.
5. **Check risk rating.** Threats are rated only with a client-supplied matrix and client-agreed likelihood and consequence. If no matrix is in the workspace, say what to ask the client for and that threats will otherwise be reported unrated.
6. **Write `02-plan/plan.md`**: review mode (with or without code, and what that limits), lenses with the reason for each and lenses considered but not chosen, methods with reasons and expected coverage, depth, scope, rating approach, and the decisions the consultant must make.
7. **Give the confirmation command**, filled in, for the consultant to run or change:

   ```text
   python3 -I -S -B LIBRARY_ROOT/engagement/tools/engage.py plan WORKSPACE --architectures <primary>,<secondary> --methods <ids> --depth quick|deep --risk-matrix 02-plan/<file>.json --by "<consultant>"
   ```

8. **Set the phase** to `awaiting_review`. The `plan` command sets it to complete.

## Rules

- Recommend; do not record the plan yourself. Only the consultant runs `engage.py plan`.
- Keep the selection small: one primary lens, at most two secondary, and only methods whose output the client will use.
- If the evidence is too thin to choose a lens, say which workshop answers would settle it and recommend a provisional lens for drafting questions.
