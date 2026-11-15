---
id: engagement/final-report
title: Engagement Final Report
shape: role
last_reviewed: 2026-11-16
sources:
  - https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html
---
# Engagement Final Report

Write the report narrative and build the client report from the validated threat model and the workspace records.

Input: the updated envelope from the validation phase (or the base model if the consultant chose to skip validation), and the workspace. Output: `07-final/narrative.json` and `07-final/report-<name>.html`.

## Work

Follow the [engagement rules](rules.md) and the narrative rules in the [report builder](../helpers/report-builder.md). The report builder's rules on honesty, client wording and never inventing details apply in full.

1. **Confirm the envelope**: the latest `change-review.json` under `threat-model/`, or the one the consultant names. If validation was skipped, say so and say the report will show no client validation.
2. **Complete `07-final/narrative.json`.** `engage.py build` supplies the client, artefact register, workshops, validation record, risk matrix and code access from the workspace, so write only:
   - `title`, `subtitle`, `report_version`, `report_status` (default "Draft for review"), `authors` (from the consultant);
   - `executive_summary`: `system_overview`, `key_components`, `next_steps`;
   - `scope_and_approach`: `approach` (the documents reviewed, the workshops held, the validation call, the frameworks applied), `activities`, `review_coverage`, `limitations`;
   - `records`: titles and impacts for every record; `responsibility` for components; `coverage` and `coverage_note` only where the derived status would mislead; `type` for verification that is a configuration review, design review or vendor assurance request; and, only where the client stated them, `response`, `response_note`, `target_rating`, `owner`, `target_date`, `effort`, `environment`;
   - `test_plan`: the penetration test plan, as the report builder describes: three to seven key attack paths through the most critical components, each with its route, the threats it exercises, the controls to challenge, test cases and what success looks like. Keep test cases to what the client runs or configures; route vendor-run components to assurance requests and list them as out of scope;
   - `assumptions` with the threats that rely on each;
   - `document_control` and `review_triggers`, from the consultant only.
3. **Build the report**:

   ```text
   python3 -I -S -B LIBRARY_ROOT/engagement/tools/engage.py build WORKSPACE <envelope> WORKSPACE/07-final/report-<name>.html [--branding <file>]
   ```

   Reports are never overwritten: use a new name for each build, such as `report-draft-1`. Relay the tool's notes on anything not supplied and on tool or process wording to fix.
4. **Check the result against the envelope**: every open threat appears with a title, impact, coverage and at least one action; every attack path follows recorded flows and cites only recorded threats and controls; no threat is described with a severity word it was not rated with; nothing is described as tested, fixed or approved without evidence.
5. **Set the report phase** to `awaiting_review`.

## Finish

Give the consultant the report path and the review checklist in the [engagement guide](README.md#before-issuing). List what is still "to be agreed" (owners, dates, responses, target ratings), which threats are unrated, and which appendices are thin. Remind them that the file embeds the assessment data and that they set `report_status` to "Final" and rebuild once the review is done.
