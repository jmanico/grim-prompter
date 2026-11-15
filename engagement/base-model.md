---
id: engagement/base-model
title: Base Threat Model
shape: role
last_reviewed: 2026-11-16
sources:
  - https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
---
# Base Threat Model

Produce the first complete threat model from the evidence gathered so far, using the confirmed plan. It is a draft for the consultant to review and then validate with the client.

Input: `01-intake/SYSTEM_UNDER_REVIEW.md`, the workshop records, and the plan in `engagement.json`. Output: a library run folder under `threat-model/`, and draft annotations in `07-final/narrative.json`.

## Before you start

Follow the [engagement rules](rules.md).

- The plan must be confirmed (`engage.py status` shows who confirmed it). If not, stop and point to the plan phase.
- List any `must` questions still open in `03-questions/workshop-questions.json`. Modelling can proceed, but each becomes a gap and limits the threats that depend on it. Ask the consultant whether to proceed or wait, unless they have already said to proceed.

## Work

1. **Run the library** exactly as the [agent runbook](../runbook.md) describes, with these inputs:
   - `PROJECT_ROOT`: the engagement workspace.
   - `MODE`: the plan's depth, `quick` or `deep`.
   - `ARCHITECTURE`: the plan's first lens as primary and the rest as bounded secondaries.
   - `METHODS`: the plan's methods. `REVIEW_SCOPE`: the plan's scope.
   - The caller-supplied `SYSTEM_UNDER_REVIEW` file: `01-intake/SYSTEM_UNDER_REVIEW.md`. Gather more evidence only from registered material, and only where the bundle points to something not yet read.
   - The rating rubric: the plan's risk matrix file, if set. Rate a threat only when the client has agreed its likelihood and consequence in a recorded workshop statement. Otherwise leave it unrated; ratings are normally agreed in the validation call.
2. **Apply the engagement rules throughout the run**: the evidence conventions, the limits on `implemented` controls and `evidenced_weakness` findings when code or configuration was not seen, and the handling of vendor-run components. Record in scope limitations what kind of material the model rests on.
3. **Write verification that fits the evidence.** For each threat and each claimed control, plan the activity that would settle it: a test in an isolated environment where code or a test system exists; otherwise a configuration review, a process walkthrough, a design review, or a vendor assurance request. Give every one pass, fail and inconclusive criteria that a reviewer can apply.
4. **For a quick run, challenge the result.** Run the [model challenger](../helpers/model-challenger.md) on the quick report and carry its output forward as the base model. A deep run already includes a challenge stage.
5. **Write draft annotations** to `07-final/narrative.json` so the validation pack reads well. Include only:
   - `records`: a short `title` for every threat, control, recommendation and verification; an `impact` sentence for every threat; `responsibility` (`client`, `vendor`, `shared`, `unknown`) for every component and entry point, from the evidence;
   - `executive_summary.system_overview`: one or two paragraphs on what the system is and does.
   Follow the annotation rules in the [report builder](../helpers/report-builder.md). Leave owners, dates, responses and target ratings out.
6. **Set the phase** to `awaiting_review`.

## Finish

Give the consultant the path of the final envelope in the run folder (`quick-report.json`, `challenge.json` or `05-report.json`) and a review list:

- threats that rest on a single statement or an inference;
- controls recorded as claimed that a configuration export could confirm;
- components whose owner is unknown;
- gaps that block a rating;
- anything in the material that you could not read or reconcile.

Then point to the validation pack.
