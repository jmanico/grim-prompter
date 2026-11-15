---
id: engagement/workshop-questions
title: Workshop Question Builder
shape: role
last_reviewed: 2026-11-16
sources:
  - https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
  - https://www.threatmodelingmanifesto.org/
---
# Workshop Question Builder

Turn what the material leaves open into the questions to ask the client in workshops. Run this after the consultant has reviewed the initial understanding and confirmed the plan.

Input: `01-intake/` files (with the consultant's edits), the confirmed plan in `engagement.json`, and `02-plan/plan.md`. Output: `03-questions/workshop-questions.json`, rendered to Markdown and CSV.

## Work

Follow the [engagement rules](rules.md).

1. **Collect what needs answering** from:
   - every numbered unknown and contradiction in `initial-understanding.md`;
   - every control that is only described, where its existence or reach matters;
   - every component whose owner is unknown, and every trust boundary crossing whose protection is not stated;
   - what each confirmed lens needs evidence about: read `quick/<architecture>.md` for each lens in the plan, as a list of topics to ask about, not as a role to run;
   - what each confirmed method needs as input.
2. **Write one question per unknown.** Each question:
   - is open and neutral ("How are accounts removed when someone leaves?"), never leading ("You remove accounts promptly, don't you?");
   - asks about how things work today, and separately about what is planned;
   - can be answered by the person in the room; route vendor internals to the vendor;
   - asks to be shown where showing is possible ("Can you share the configuration export?").
3. **Prioritise.** `must`: the threat model cannot be drawn without it (a boundary, an owner, an authentication path, where sensitive data goes). `should`: the answer would add, remove or change a threat or control. `could`: detail that sharpens a recommendation.
4. **Group into sessions** by theme and audience, so each workshop has the right people: for example access and identity, integration and data flows, vendor and contract, operations and monitoring. Add a session "Material to request" for documents and exports to ask for.
5. **Keep it usable.** Aim for 15 to 30 questions. Merge overlaps. Put `must` questions first in each session.
6. **Write `03-questions/workshop-questions.json`**:

   ```json
   {
     "summary": "One or two sentences on what these workshops need to establish.",
     "questions": [
       {
         "id": "Q-001",
         "session": "Access and identity",
         "audience": "Role best placed to answer",
         "priority": "must",
         "question": "The question, in client wording.",
         "why": "Why the answer matters to the threat model.",
         "listen_for": "Signs of a weak or strong answer; follow-ups.",
         "refs": ["M-003"],
         "status": "open"
       }
     ]
   }
   ```

   `refs` are register ids or evidence labels that prompted the question. Ids are stable: when you rerun, keep existing ids, add new ones, and never reuse a retired id.
7. **Render** with `engage.py questions` and set the phase to `awaiting_review`.

## Rules

- Questions are a client document: follow the client-wording rule.
- Do not ask what the material already answers; ask to confirm it only when a threat or control depends on it.
- Do not suggest answers, and do not record any answer in this phase.

## Finish

Tell the consultant how many questions there are by priority and session, who needs to attend each session, and what material to request before the workshops.
