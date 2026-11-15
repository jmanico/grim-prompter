---
id: engagement/workshop-intake
title: Workshop Intake
shape: role
last_reviewed: 2026-11-16
sources:
  - https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
---
# Workshop Intake

Take a workshop transcript or notes file, record what was said and by whom, mark which questions it answered, and update the understanding of the system. Run it once per workshop.

Input: a new file in `materials/workshops/`. Output: `04-workshops/W-<nn>.json`, updates to `03-questions/workshop-questions.json`, `01-intake/SYSTEM_UNDER_REVIEW.md` and `04-workshops/summary.md`.

## Work

Follow the [engagement rules](rules.md).

1. **Register the file** with `engage.py scan` and `engage.py extract`. Read the extracted text in full.
2. **Write `04-workshops/W-<nn>.json`**, numbering in date order:

   ```json
   {
     "id": "W-01", "date": "2026-11-04", "title": "Architecture walkthrough", "material": "M-004",
     "purpose": "What the session set out to do.",
     "attendees": [{"name": "As labelled in the transcript", "role": "Only if stated or supplied", "organisation": "Only if stated or supplied"}],
     "outcomes": ["Three to six plain statements of what was established."],
     "statements": [
       {"id": "W-01-S01", "speaker": "Name", "tag": "fact", "text": "What was said, in neutral words.", "lines": "12-14", "answers": ["Q-003"]}
     ]
   }
   ```

   Record every statement that bears on a component, flow, boundary, owner, control, data, decision or open question. Use the tags in the rules. `lines` are lines in the extracted text file. Take the date and title from the file or the consultant; never guess them.
3. **Update the questions.** For each question a statement answers, set `status` to `answered` or `partly`, and add `answer` (one or two sentences) and `answered_in` (the workshop id). Add new questions the session raised, with new ids. Render with `engage.py questions`.
4. **Update `01-intake/SYSTEM_UNDER_REVIEW.md`.** Add a dated section for this workshop with new supplied facts, each labelled, attributed and located. Do not rewrite earlier facts: where a statement corrects one, mark the earlier fact superseded and point to the new one. Record contradictions between the workshop and the documents as conflicts.
5. **Write or update `04-workshops/summary.md`**: what was learned, what was corrected, contradictions still open, which `must` questions remain open, any material the client promised, and whether there is enough to draw the threat model.
6. **Set the phase** to `awaiting_review`.

## Rules

- Record what was said, not what you think was meant. If a statement is ambiguous, tag it `open_question`.
- Everything said in a workshop is a claim, including claims about controls. Only a named person's decision is recorded as a decision.
- Small talk, scheduling and unrelated discussion are left out.
- Do not identify threats in this phase; note where a statement clearly bears on one so the model phase picks it up.

## Finish

Tell the consultant what changed in the understanding, which `must` questions are still open, and whether to hold another workshop or proceed to the base model.
