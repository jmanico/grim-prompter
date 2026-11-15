# Running a threat modelling engagement

This guide takes a consultant through a client threat modelling engagement from first material to issued report. It works with or without source code: an architecture review of a third-party product from documents and workshops follows the same steps as a code-backed review of an in-house application.

You drive it with an AI coding agent (Claude Code or Codex) and one small helper tool. The agent reads the material, drafts each output and stops at every decision point for you. You make the decisions.

## The process at a glance

| # | Phase | You do | The agent produces | You decide |
| --- | --- | --- | --- | --- |
| 0 | Set up | Create the workspace; drop in client material | Workspace folders | Whether code is available |
| 1 | Intake | `/engagement intake` | Evidence bundle; initial understanding of the system | Is the understanding right? What else to request? |
| 2 | Plan | `/engagement plan`, then confirm | Recommended architecture lenses, methods, depth, rating approach | Lenses, methods, depth, risk matrix, privacy |
| 3 | Workshop questions | `/engagement questions` | Prioritised question list by session and audience | Which questions, which sessions, who attends |
| 4 | Workshops | Run them; save transcripts; `/engagement workshop` | Workshop records; answered questions; updated understanding | Enough to model, or another workshop? |
| 5 | Base threat model | `/engagement model` | Draft threat model with controls, recommendations, verification | Is the draft fit to show the client? |
| 6 | Validation | `/engagement validation-pack`; hold the call; `/engagement validate` | Validation pack and agenda; outcomes; updated model | Accept corrections, ratings and decisions |
| 7 | Final report | `/engagement report` | Client report with a penetration test plan (HTML, prints to PDF); action plan and test plan (CSV) | Review, complete owners and dates, issue |

Nothing moves to the next phase on its own. Each phase ends "awaiting review", and you mark it complete by name.

## Set up once

1. Clone this library and link both skills into your agent (check for existing links first):

   ```bash
   git clone https://github.com/raa-appsec/grim-prompter ~/grim-prompter
   mkdir -p ~/.claude/skills
   ln -s ~/grim-prompter/skills/threat-model ~/.claude/skills/threat-model
   ln -s ~/grim-prompter/skills/engagement ~/.claude/skills/engagement
   ```

   For Codex, link into `~/.agents/skills/` instead. Start a new agent session afterwards.
2. You need Python 3 on your machine. The helper uses only the standard library and never touches the network.
3. Optional: add your branding file as described in the [reporting guide](../reporting/README.md#branding).

In the commands below, `engage` stands for:

```bash
python3 -I -S -B ~/grim-prompter/engagement/tools/engage.py
```

You can run these yourself or ask the agent to; `/engagement status` tells you where you are and what comes next.

## Phase 0: set up the engagement

```bash
engage init ~/engagements/northwind-paystream --client "Northwind Health" --system "PayStream payroll" --code none
```

`--code` is `none`, `partial` or `full`. It records whether source code is available and changes how the report words its findings.

Put the client's material into the workspace:

| Folder | What goes there |
| --- | --- |
| `materials/design/` | Architecture and design documents, security requirements, data flow descriptions |
| `materials/diagrams/` | Architecture, network and data-flow diagrams |
| `materials/vendor/` | Third-party product documentation, security papers, audit reports, contracts |
| `materials/workshops/` | Workshop and validation-call transcripts or notes |
| `materials/configuration/` | Configuration exports and screenshots that show how something is actually set up |
| `materials/code/<repo>/` | A copy of each repository, when code is available |
| `materials/other/` | Anything else |

Then open your agent in the workspace folder.

**File formats.** Word, PowerPoint, Visio, WebVTT and SRT files are converted to text by `engage extract`. PDFs and images are read directly by the agent. Text, Markdown, CSV, Mermaid and draw.io files are read as they are. Export anything else (Excel, for example) to PDF or text first. For Visio, also supply a PDF or image export: the text extract has the shape labels but not the arrows.

> **Decision point 1: code access.** If you have code for some components only, use `partial`. The model will record which components were backed by code and will not let one component's code stand as evidence for another.

## Phase 1: intake

```text
/engagement intake
```

The agent registers the material, reads all of it, and writes two files in `01-intake/`:

- `initial-understanding.md`: what the system is, components and who runs them, data, trust boundaries, the controls the material describes, contradictions, and a numbered list of what the material does not tell us.
- `SYSTEM_UNDER_REVIEW.md`: the evidence bundle, with every fact tied to a document and line. Later phases build on it.

It also asks you to complete document titles, versions and dates in `materials/register.json`. These appear in the report's Appendix A.

> **Decision point 2: is the understanding right?** Read `initial-understanding.md` critically. Edit it directly where it is wrong. Decide what extra material to request (a vendor audit report, a configuration export, a diagram export). Then mark the phase complete:
>
> ```bash
> engage phase WORKSPACE intake complete --by "Your Name"
> ```

## Phase 2: plan

```text
/engagement plan
```

The agent recommends, in `02-plan/plan.md`:

- **Architecture lenses**: one primary and up to two secondary, from the library's 36 (for example `multi-tenant-saas`, `identity-federation`, `enterprise-integration`, `hybrid-multicloud`, `api`, `microservices`). Each lens brings its own threat patterns.
- **Methods**: from the library's 29 (for example STRIDE per element, attack trees, ATT&CK or CAPEC mapping, LINDDUN), with what each will and will not give you on this evidence.
- **Depth**: quick (one pass plus a challenge) or deep (six stages).
- **Rating**: whether a client risk matrix is available.

> **Decision point 3: lenses, methods, depth and rating.** Change anything you disagree with, then record the plan. This is the only way the plan is set:
>
> ```bash
> engage plan WORKSPACE --architectures multi-tenant-saas,identity-federation --methods stride-per-element --depth quick --risk-matrix 02-plan/risk-matrix.json --by "Your Name"
> ```
>
> Guidance:
> - Fewer lenses and methods give a tighter model. Add a method only if the client will use its output.
> - Without code, mapping methods (ATT&CK, CAPEC) will cover only some threats. STRIDE works well on a design.
> - **Risk matrix.** Threats are rated only with the client's matrix and likelihood and consequence the client agreed. Copy the matrix into `02-plan/` in the format of [`reporting/examples/risk-matrix-5x5.json`](../reporting/examples/risk-matrix-5x5.json). Without one, the report shows threats as "not yet rated".
> - **Privacy.** If the system holds personal data and privacy was not in the brief, decide whether to raise it with the client. Add `--scope security-and-privacy` only if it is in scope.

## Phase 3: workshop questions

```text
/engagement questions
```

Run this after you have reviewed the initial understanding and confirmed the plan. The agent turns every unknown, contradiction, unconfirmed control and unknown owner into a question, adds what each chosen lens needs to know, and writes `03-questions/workshop-questions.md` (and `.csv`):

- grouped into sessions by theme, with who should attend;
- prioritised: **must** (the model cannot be drawn without it), **should** (would change a finding), **could** (adds detail);
- each with why it matters and what to listen for;
- a "Material to request" list.

> **Decision point 4: the question list.** Edit `workshop-questions.json` (remove, reword, add), run `engage questions WORKSPACE` to re-render, and plan the sessions. Send the client the questions or keep them as your facilitation guide. Mark the phase complete.

## Phase 4: workshops

Run the workshops and record them. After each one, save the transcript or your notes in `materials/workshops/` (name files with the date, such as `2026-11-04-architecture-walkthrough.vtt`) and run:

```text
/engagement workshop
```

The agent writes a record of the session in `04-workshops/` (who said what, tagged as fact, control, decision, assumption, correction or open question), marks which questions were answered, adds the new facts to the evidence bundle, and updates `04-workshops/summary.md`.

If you only have notes, write them as "Name: what they said" lines so statements can be attributed. Add attendee roles in your request if the transcript does not state them.

> **Decision point 5: ready to model?** The summary lists the **must** questions still open. Hold another workshop, chase the client by email (save the reply in `materials/workshops/` and rerun), or proceed and accept that each open question becomes a stated gap in the model. Mark the phase complete.

## Phase 5: base threat model

```text
/engagement model
```

The agent runs the library's quick or deep analysis with your plan, on the evidence bundle, and writes a run folder under `threat-model/`. For a quick run it also challenges its own result. It then drafts short titles, impact statements and component owners in `07-final/narrative.json`.

What you get depends on the evidence:

| | With code or configuration | Documents and workshops only |
| --- | --- | --- |
| Threats | "Observed" where the weakness was seen; otherwise design concerns | All design concerns, each showing what it is based on |
| Controls | "Implemented" where seen; "tested" with test evidence | "Reported" (described by the client or vendor) or "designed" (planned) |
| Coverage of a threat | No control, partly controlled, controlled, or verified | No control, or "control reported, not verified" |
| Verification | Tests in an isolated environment | Configuration reviews, process walkthroughs, design reviews, vendor assurance requests |

> **Decision point 6: is the draft fit to show the client?** Review the model before the client sees it. The agent gives you a review list: threats resting on a single statement, reported controls a configuration export could confirm, components with unknown owners, and gaps blocking a rating. Ask the agent to correct anything wrong, citing the evidence. Mark the phase complete.

## Phase 6: validation with the client

```text
/engagement validation-pack
```

This builds `06-validation/validation-pack.html`, a short draft for the call: the architecture diagram, components and who runs them, assumptions, the controls we believe are in place, the draft threats and the open questions, each with a column for the client to confirm. It has no ratings or recommendations. It also writes `agenda.md` with the items that most need an answer.

Hold the call, record it, save the transcript in `materials/workshops/`, then:

```text
/engagement validate
```

The agent records the outcome for each item discussed (confirmed, corrected, rejected, added, deferred, not discussed) and updates the threat model. Record identities are kept, so T-003 before the call is T-003 after it, and the report shows what changed.

> **Decision point 7: accept the outcomes.** Check that:
> - corrections were applied as the client stated them;
> - a rejected threat was retired for a sound reason. If you disagree with the client, keep it open and say so in the report;
> - nothing was marked confirmed merely because nobody objected;
> - ratings match what was agreed, and unrated threats say what they are waiting on;
> - a control the client confirmed in words is still "reported"; only a configuration export or code makes it "implemented".
>
> Mark the phase complete. You can skip validation, but the report will then show no client validation.

## Phase 7: final report

```text
/engagement report
```

The agent writes the narrative and builds `07-final/report-<name>.html`. Open it in a browser. It prints to PDF (A4 landscape) from the button in the sidebar and exports the action plan as CSV. See the [reporting guide](../reporting/README.md) for its structure.

The report includes a **penetration test plan** (section 7): the priority targets, and the key attack paths to test with their routes, the controls each should challenge, test cases and what success looks like. The agent drafts the paths from the model; you add effort, environment and rules of engagement. It exports as its own CSV for the test team. To leave it out, set `"options": {"test_plan": false}` in `narrative.json`.

Supply, in your request or by editing `07-final/narrative.json`: report title and version, authors, owners and target dates for recommendations and tests, target ratings, the reviewers for document control, and your branding file. Anything you leave out shows as "to be agreed".

### Before issuing

> **Decision point 8: review and issue.** A person reviews every report before it goes out. Check:
>
> 1. **Executive summary**: the narrative is accurate and reads as your work. The three verdicts match your own view.
> 2. **Each threat**: the title, scenario and impact are right; the coverage status is fair; the recommendation is one you would stand behind.
> 3. **Severity**: no severity word appears for an unrated threat. Ratings match the matrix in Appendix C.
> 4. **Controls**: nothing is called implemented or tested without evidence.
> 5. **Diagram**: trust zones and owners are right. Zone names are inferred from the model; correct the model if one is wrong.
> 6. **Penetration test plan**: each attack path is one you would hand to a tester; test cases stay within what the client may authorise; third-party permission is flagged where needed.
> 7. **Scope and limitations**: what was not reviewed is stated, including missing vendor assurance.
> 8. **Appendices**: document versions and dates (A), workshop attendees and dates (B), and the client's matrix (C) are correct.
> 9. **Wording**: no tool, process or internal wording. The build prints a warning listing any it finds.
> 10. **Confidentiality**: the HTML file embeds the full assessment data. Send it only to people who may see all of it, or send the PDF.
>
> When satisfied, set `"report_status": "Final"` in `narrative.json`, rebuild under a new name, and mark the phase complete.

## Key decision points in one place

| # | Decision | When | Why it matters |
| --- | --- | --- | --- |
| 1 | Code access: none, partial or full | Set-up | Sets what can be called observed, and how the report words its basis |
| 2 | Accept the initial understanding | After intake | Everything later builds on it; errors here become wrong threats |
| 3 | Lenses, methods, depth, risk matrix, privacy | Plan | Sets which threat patterns are considered and whether threats can be rated |
| 4 | The workshop question list | Before workshops | Decides what you will know when you model |
| 5 | Ready to model | After workshops | Open "must" questions become gaps in the client's report |
| 6 | Draft fit for the client | After the base model | Your credibility on the validation call |
| 7 | Accept validation outcomes and ratings | After the call | Turns a draft into a model the client owns |
| 8 | Review and issue | Before sending | Nothing is issued without a named reviewer |

## New or changed material mid-engagement

Drop it into `materials/` and say `/engagement new material`. The agent registers it, reads what changed and tells you which outputs it affects. If the base model already exists, the change goes through the same update step as validation, so record identities are kept.

## What the workflow will not do

- **Invent.** Attendees, dates, versions, owners, ratings, decisions, test results and vendor certifications come from the material or from you.
- **Upgrade evidence.** A control stays "reported" until a configuration export or code shows it. A design concern stays a design concern until it is observed or tested.
- **Assess a vendor's internals.** A third-party product is modelled as the vendor documents it, at the boundary the client controls. Missing vendor assurance is reported as a gap.
- **Run tests.** Verification is planned, with pass and fail criteria. Running it needs authorisation and an isolated environment.
- **Advance on its own.** Every phase waits for you.

## Worked example

[`examples/northwind-payroll/`](examples/northwind-payroll/) is a complete fictional engagement without code: a SaaS payroll product integrated with a client's HRIS, identity provider, general ledger and bank. It holds the material, the register, every phase's output, the base model, the validation record and the updated model. Rebuild its pack and report with:

```bash
cd ~/grim-prompter
engage build engagement/examples/northwind-payroll engagement/examples/northwind-payroll/threat-model/2026-11-06-quick-multi-tenant-saas/quick-report.json engagement/examples/northwind-payroll/06-validation/validation-pack.html --pack
engage build engagement/examples/northwind-payroll engagement/examples/northwind-payroll/threat-model/2026-11-14-change/change-review.json engagement/examples/northwind-payroll/07-final/report.html
```

The example's model and phase files were written by hand to show the expected shape of each output. Use it to see what good looks like, not as evidence of what an agent will produce unaided.

## Files in this folder

| File | Purpose |
| --- | --- |
| [`rules.md`](rules.md) | Rules every phase follows: workspace, evidence conventions, reviews with and without code, vendor components, workshop statements |
| [`intake.md`](intake.md), [`plan.md`](plan.md), [`workshop-questions.md`](workshop-questions.md), [`workshop-intake.md`](workshop-intake.md), [`base-model.md`](base-model.md), [`validation-pack.md`](validation-pack.md), [`validation-outcomes.md`](validation-outcomes.md), [`final-report.md`](final-report.md) | One prompt per phase |
| [`tools/engage.py`](tools/engage.py) | Workspace helper: `init`, `scan`, `extract`, `plan`, `phase`, `questions`, `build`, `status` |

## Limits to know about

- Diagrams supplied only as images are read by the agent and can be misread, especially arrows and groupings. The validation pack puts the diagram first for that reason.
- The architecture diagram in the report is drawn from the model's flows and trust boundaries, not copied from the client's diagram.
- Business impact, owners, target ratings and component owners are held in `narrative.json` alongside the model, not inside it. Keep the file with the engagement.
- Very large systems (dozens of components) will produce long reports and a dense diagram; split the engagement by subsystem.
