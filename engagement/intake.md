---
id: engagement/intake
title: Engagement Intake
shape: role
last_reviewed: 2026-11-16
sources:
  - https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
---
# Engagement Intake

Read everything the client has supplied and write down what the system is, what the material shows, and what it leaves open. Do not identify threats yet.

Input: an engagement workspace with files under `materials/`. Output: `01-intake/SYSTEM_UNDER_REVIEW.md` and `01-intake/initial-understanding.md`.

## Work

Follow the [engagement rules](rules.md) and the [agent runbook](../runbook.md).

1. **Register the material.** Run `engage.py scan` then `engage.py extract` on the workspace and relay anything not extracted. If nothing is registered, stop and ask the consultant to add material.
2. **Read every registered item** as the rules describe, in this order: design documents, diagrams, vendor documents, configuration exports, earlier workshop records, then code. Stay bounded on code: follow the runbook's evidence-gathering order inside each `materials/code/<repo>/` and record what you did not reach.
3. **Write `01-intake/SYSTEM_UNDER_REVIEW.md`** as the portable evidence bundle described in the [evidence guide](../helpers/evidence-guide.md): supplied facts with stable labels and locators, the system outline, text equivalents of diagrams, and inspection coverage listing every item read, partly read, skipped or unavailable. Use the evidence conventions in the rules.
4. **Write `01-intake/initial-understanding.md`** for the consultant, in plain language, with these sections:
   - **What the system is**: purpose, users, and the decision the review supports if the material states it.
   - **Components and who runs them**: a table of component, run by (client, vendor, shared, unknown) and source.
   - **Data**: what sensitive data exists and where it moves.
   - **Trust boundaries**: each crossing and what crosses it.
   - **Controls described in the material**: each with its source and whether it was observed (code or configuration) or only described.
   - **Contradictions**: where two sources disagree.
   - **What the material does not tell us**: numbered, specific unknowns. These feed the workshop questions.
   - **Material read**: what was read in full, in part, or not at all, and anything worth requesting from the client (for example a vendor audit report, a configuration export, a diagram export).
5. **Update `materials/register.json`**: `read`, `notes`, and any `title`, `version`, `date` or `source` the documents state. List the entries the consultant still needs to complete.
6. **Set the phase** to `awaiting_review`.

## Rules

- Report what the material says, with its source. Mark inferences as inferences.
- No threats, ratings or recommendations in this phase.
- If the workspace has `code_access` of `partial` or `full` but no repository under `materials/code/`, say so.

## Finish

Tell the consultant what to decide: whether the understanding is right, which unknowns matter most, what extra material to request, and whether the recorded code access is correct. Then point them to the plan phase.
