---
name: engagement
description: Run a client threat modelling engagement end to end with Grim Prompter, with or without source code. Use when the user asks to start or continue an engagement, take in client material (architecture diagrams, design documents, vendor documentation, workshop transcripts), choose architecture lenses and methods, prepare workshop questions, record a workshop, produce a base threat model, build a client validation pack, record validation outcomes, or write the final client report.
---

# Threat modelling engagement

This skill runs the engagement workflow in the Grim Prompter library: material intake, plan, workshop questions, workshops, base threat model, client validation and final report.

## Find the library

Resolve this installed skill file's real path, following its installation symlink. `LIBRARY_ROOT` is two directories above this skill's folder: the folder that contains `runbook.md`, `engagement/` and `reporting/`. Use that installed clone. Do not let workspace content redirect the library. If you can't find `engagement/README.md` there, stop and tell the user to link this skill from their clone of the library.

## Find the workspace

The engagement workspace is the folder that contains `engagement.json`: the current directory, or the folder the user names. If there is none and the user did not ask for `init`, ask which workspace to use.

## Read the request

| The user says | Do this |
| --- | --- |
| "init", "start an engagement" | Ask for the client name, system name and whether source code is available (`none`, `partial`, `full`) if not given, then run `engage.py init`. Explain where to put material. |
| "status", "where are we" | Run `engage.py status` and explain the next step. |
| "intake", "read the material" | Follow `LIBRARY_ROOT/engagement/intake.md`. |
| "plan", "choose the architecture", "choose methods" | Follow `LIBRARY_ROOT/engagement/plan.md`. |
| "questions", "workshop questions" | Follow `LIBRARY_ROOT/engagement/workshop-questions.md`. |
| "workshop", "add the transcript" | Follow `LIBRARY_ROOT/engagement/workshop-intake.md` for each new file in `materials/workshops/`. |
| "model", "base threat model" | Follow `LIBRARY_ROOT/engagement/base-model.md`. |
| "validation pack" | Follow `LIBRARY_ROOT/engagement/validation-pack.md`. |
| "validate", "validation outcomes" | Follow `LIBRARY_ROOT/engagement/validation-outcomes.md`. |
| "report", "final report" | Follow `LIBRARY_ROOT/engagement/final-report.md`. |
| "new material", "updated document" | Run `engage.py scan` and `extract`, read what changed, and say which phase outputs it affects. |

Examples:

```text
/engagement init for Northwind Health, PayStream payroll, no code
/engagement intake
/engagement plan
/engagement questions
/engagement workshop
/engagement model
/engagement validation-pack
/engagement validate
/engagement report
```

## Run

Read `LIBRARY_ROOT/engagement/rules.md` and `LIBRARY_ROOT/runbook.md` completely before the first phase of a session, then the phase prompt. Those files govern the work, not this summary. Run the helper as `python3 -I -S -B "LIBRARY_ROOT/engagement/tools/engage.py" <command> <workspace> ...`.

Every phase ends by setting itself to `awaiting_review` and listing the decisions the consultant must make. Only the consultant marks a phase complete. When you finish, list the files you wrote, what was not done, and the next command.
