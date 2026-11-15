---
id: engagement/validation-pack
title: Validation Pack
shape: role
last_reviewed: 2026-11-16
sources:
  - https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
---
# Validation Pack

Build the short pack the consultant walks through with the client to confirm or correct the draft threat model, and an agenda for the call.

Input: the base model envelope the consultant has reviewed, and `07-final/narrative.json`. Output: `06-validation/validation-pack.html` and `06-validation/agenda.md`.

## Work

Follow the [engagement rules](rules.md).

1. **Confirm the envelope.** Use the one the consultant names, or the latest final envelope under `threat-model/`. Say which you used.
2. **Check the annotations** in `07-final/narrative.json`: every threat, control and component in the envelope has a title, each threat an impact, each component a responsibility. Add any that are missing under the base-model rules.
3. **Build the pack**:

   ```text
   python3 -I -S -B LIBRARY_ROOT/engagement/tools/engage.py build WORKSPACE <envelope> WORKSPACE/06-validation/validation-pack.html --pack
   ```

   The pack shows the system as understood, components and who runs them, assumptions, the controls believed to be in place, the draft threats and the open questions, each with a column for the client to confirm. It carries no ratings, recommendations or verification plans. If the name is taken, add a suffix such as `-2`. Relay any wording warnings and fix them in the narrative file.
4. **Write `06-validation/agenda.md`** for a 60 to 90 minute call:
   - the order: architecture diagram, components and owners, assumptions, controls, threats, open questions, then risk rating if a matrix is set;
   - the five to ten items that most need the client's answer, with the record id and what a "no" would change;
   - the claimed controls a configuration export or screenshot could turn into observed ones, to ask for on the call;
   - the threats to rate and the matrix levels to choose from;
   - a reminder to record the call and save the transcript or notes in `materials/workshops/`.

## Rules

- The pack is a client document and a draft. It must not read as a finding of fact.
- Do not change the envelope in this phase.

## Finish

Give the consultant the two files and who should attend the call.
