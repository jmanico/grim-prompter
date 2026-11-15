---
id: engagement/validation-outcomes
title: Validation Outcomes
shape: role
last_reviewed: 2026-11-16
sources:
  - https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
---
# Validation Outcomes

Record what the client confirmed, corrected, rejected or added in the validation call, and update the threat model to match, keeping every record's identity.

Input: the validation call transcript or the consultant's notes in `materials/workshops/`, and the base model envelope. Output: a workshop record, `06-validation/validation.json`, and a change review run under `threat-model/`.

## Work

Follow the [engagement rules](rules.md).

1. **Record the session** as the [workshop intake](workshop-intake.md) describes: register and extract the file, write `04-workshops/W-<nn>.json`, update the questions and the evidence bundle.
2. **Write `06-validation/validation.json`**:

   ```json
   {
     "sessions": [{"date": "2026-11-13", "title": "Threat model validation", "material": "M-005", "attendees": [{"name": "", "role": "", "organisation": ""}]}],
     "items": [{"ref": "T-002", "outcome": "corrected", "note": "What the client said, in one sentence."}]
   }
   ```

   One item for each record the call discussed: components, flows, boundaries, assumptions' threats, controls and threats. Outcomes:
   - `confirmed`: the client agreed it is right as drafted;
   - `corrected`: right in substance, with a detail changed;
   - `rejected`: the client said it does not apply, with their reason;
   - `added`: raised by the client and not in the draft;
   - `deferred`: the client needs to check and come back;
   - `not_discussed`: on the agenda but not reached.
   Do not mark anything confirmed because nobody objected. Silence is `not_discussed`.
3. **Update the model.** Run the [change reviewer](../helpers/change-reviewer.md) under the runbook's `change` mode with the base model envelope as the baseline and the validation record and any new material as the change evidence. It writes `change-review.json` in a new run folder. In that run:
   - a correction changes the record and cites the client's statement; the earlier evidence stays, marked as superseded in its limitations;
   - a rejected threat is retired with the client's reason, not deleted; if you think the rejection is unsafe, keep the threat open, record the disagreement as a conflict and tell the consultant;
   - an added threat gets a new id and the same treatment as any other: affected components, controls, recommendation, verification;
   - a control the client confirmed in words stays `claimed`. It becomes `implemented` only if they supplied a configuration export or code;
   - ratings agreed on the call are recorded with the supplied matrix as the rubric and the agreed likelihood and consequence as inputs, citing the statement;
   - a decision by a named client person is recorded as a decision with that statement as evidence. Owners and dates are recorded only if stated.
4. **Update `07-final/narrative.json`** for changed or added records: titles, impacts and responsibilities.
5. **Set the validation phase** to `awaiting_review`.

## Finish

Tell the consultant: the counts by outcome, each correction and addition, anything deferred with who owes the answer, any threat left unrated and why, and the path of the updated envelope. Then point to the report phase.
