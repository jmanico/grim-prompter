# Agent Instructions

Grim Prompter is a threat modeling prompt library for AI coding agents. `README.md` is the entry point, `start-here.md` is the first-run guide, `runbook.md` is the operating contract every prompt follows, and `skills/threat-model/SKILL.md` is the shared Claude Code and Codex skill.

- Prompts live in `quick/`, `deep/`, `methods/`, `helpers/`, `privacy/` and `reference/`. HTML report rendering lives in `reporting/`. `catalog.md` lists every prompt.
- Prompts are written for coding agents working under `runbook.md`: read-only project inspection, evidence cited by `path:start-end`, artifacts written to the run folder, and stage hand-offs through files. Don't reintroduce chat-window or copy-and-paste instructions.
- Each prompt's frontmatter `id` is its path without `.md`. Keep ids, links and `catalog.md` in step when adding, moving or removing a prompt.
- Write method instructions in original words. Do not copy text, tables or figures from method sources.
- Keep the project simple: plain Markdown prompts and embedded JSON contracts. Do not introduce an application, framework or test harness. The one exception is `reporting/`: a single self-contained HTML renderer and a standard-library `fill.py`. Keep it dependency-free and offline, insert model text only as text (never `innerHTML`), and keep section ids in step across `renderer.html`, `fill.py` and `reporting/README.md`.
- Never publish private system material, credentials, customer data or internal planning documents. Never fabricate system facts or execution results.
- Validate changes with `git diff --check` and check that every local link and referenced file exists. There is no application build or test suite.
- Follow [MODELS.md](MODELS.md) for the contributor model workflow, recording actual stages and keeping execution evidence outside tracked content.
- Use a descriptive topic branch, commit reviewable changes and open a pull request against `main`. Merge only when the user has authorized it and all configured required checks pass. Never bypass repository protection.
