# Model workflow

This is a contributor execution contract, not an automated runner or a change to the threat-modeling runbook. Naming a model does not launch it. Invoke each selected stage and report what actually completed. Keep exact prompts, responses and runtime evidence outside tracked content; do not publish private paths, account data, credentials or internal planning material.

## Run mode

State the mode and intended stages before work:

- **Full:** substantial prompt, contract or workflow changes, or an explicit full-lineup request. Run Astra build, Opus second build, independent reviews, then Astra's final decision. Only independent reviews may run in parallel.
- **Review-only:** review an existing candidate with the independent reviewers and Astra's decision; record both builds as skipped.
- **Focused:** a bounded correction may use selected reviewers with reasons for omitted stages. Changes to security guarantees or bypass handling require a Daybreak attempt. An explicit full request overrides this exception.

Contributors without access to a required model record that stage as unavailable; maintainers own the remaining invocations and disposition before merge. This does not waive required stages or authorize a claim that the full lineup completed.

A failed invocation is unavailable, not passed or skipped. Continue useful work while disclosing the missing stage; never silently substitute a model or claim a complete lineup without all required usable results.

## Stages

| Stage | Model | Work |
| --- | --- | --- |
| Build | Astra, `gpt-6-astra` | Read project guidance, implement the approved scope on a descriptive topic branch based on `main` (or the authorized existing PR branch), validate and commit a reviewable candidate. |
| Second build | Opus 5.5, `claude-opus-5-5` | Inspect the actual candidate and sources, correct scope/correctness problems and remove unnecessary prose. Its edits are committed before review; an evidenced no-change result is valid. |
| Independent correctness review | Sol 6.1, `gpt-6.1-sol` | Check prompt behavior, evidence rules, artifacts, lineage, routing and regressions. |
| Independent adversarial review | Daybreak Blue, `gpt-daybreak-blue-latest` | Check trust boundaries, injection paths, authority expansion, false evidence and control bypasses using explicit `daybreak_blue` access. |
| Independent editorial review | Opus 5.5, `claude-opus-5-5` | Check clarity, duplication, placement and plain US English while preserving protections. |
| Additional review when requested | Mythos 5.1, `claude-mythos-5-1` | Perform the caller-requested independent review; record unavailable access without substitution. This supplements the required reviews. |
| Final decision | Astra, `gpt-6-astra` | Read all results, resolve findings against evidence, obtain review of fixes and check the final commit. Recommend disposition; merge only with user authorization and passing required checks. |

Use fresh review sessions with no build-session context or peer findings, including when the editorial reviewer uses the same model as the second builder. Independence here means separate execution and context, not a claim that every stage uses a different model. Give independent reviewers the same frozen SHA, intent, complete diff, full changed files and repository guidance. Do not share another reviewer's findings before their initial result. Reviewers propose fixes without editing the shared branch. Require a recommendation with exact locations, evidence and concrete corrections, separating new regressions from inherited limitations.

## Invocation and evidence

Inspect installed CLI help and model availability before invoking. Select models explicitly. For Codex CLI use `--model gpt-6-astra --cyber-access-program standard` or `--model gpt-6.1-sol --cyber-access-program standard`; Daybreak must use both `--model gpt-daybreak-blue-latest` and `--cyber-access-program daybreak_blue`. Do not infer the access program from the model name or inherited defaults. For Claude Code select `--model claude-opus-5-5` or, when requested and available, `--model claude-mythos-5-1`. Confirm these identifiers against the installed interface; an unavailable identifier is an unavailable stage, not permission to guess a replacement.

Use read-only review sessions with a narrow tool allowlist. Builder permissions cover only the approved repository work. Every stage prompt must state permitted actions, prohibit unrequested delegation and prohibit posting, pushing or merging beyond current authorization. Native Codex delegation may serve Astra/Sol stages only when it exposes the actual requested model and equivalent execution evidence; Daybreak uses an explicit CLI program selection.

For each stage retain: requested model/program, interface version, exact prompt, input and output SHA, session identifier, exit status, completion/error result, and result location. Inspect runtime metadata, not a model's self-description. Record a resolved backend only if exposed; otherwise use “not exposed.” Exit zero alone does not prove the requested work or source checks completed. Keep a stage table with `completed`, `skipped` or `unavailable`, findings, resolution and any re-review coverage. Do not store actual run logs in this repository.

After fixes, commit and send the changed content for re-review. A bounded delta review can extend previous coverage when it names both SHAs and the unchanged scope; broader edits require a fresh independent round. Never say all reviewers reviewed the final SHA when they reviewed earlier content. Reviewer agreement is not evidence of correctness.

## Validate and hand off

After the last edit, apply the [AGENTS.md](AGENTS.md) validation and simplicity rules, including path-matching frontmatter IDs and catalog entries. Review changed contract examples for parseability and internal consistency. Use manual acceptance walkthroughs when behavior needs evaluation, retain actual results outside tracked content and distinguish inspected instructions from executed runs.

Open or update the authorized PR under AGENTS.md. Report changes, actual stage status, validation, limitations and unresolved findings. A recommendation to merge is not authorization, and sending messages or posting reviews also requires explicit authorization.
