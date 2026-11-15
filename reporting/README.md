# HTML report

Turn a finished threat model into one self-contained HTML report you can open in a browser, click through and print to PDF. It is built from the run's JSON envelope (`quick-report.json`, `05-report.json` or another reportable envelope) plus a short engagement file.

```text
/threat-model report
/threat-model report for threat-model/2026-11-15-deep-api, client Acme, workshops in notes/workshops.md, risk matrix risk/matrix.json
/threat-model deep api with STRIDE per element and ATT&CK, using risk/matrix.json as the rating rubric, with html report
```

Codex uses `$threat-model` with the same words. The agent follows [the report builder](../helpers/report-builder.md): it drafts the engagement file, then runs `fill.py` to embed the model, engagement file, branding and fonts into [`renderer.html`](renderer.html). The browser draws the report from the embedded JSON.

Output goes into the run folder as `report-<name>.html` and `report-<name>.engagement.json`. Existing files are never overwritten.

## Structure

The report is built so the reader finishes with three answers: what the current threats are, whether today's controls cover them, and what they need to do.

| Section | Contents | Comes from |
| --- | --- | --- |
| Executive summary | Narrative; three verdicts (threats, controls, actions); threats-at-a-glance table with risk now and target, control coverage and required actions; key components; next steps; basis | Narrative and annotations from the engagement file; counts, coverage and links from the model |
| Technical summary | Architecture diagram grouped by trust zone with threat, control and verification markers and a written key; overview table; inventory | Model |
| Threats | Framework mapping; one self-contained entry per threat (what could happen, why it matters, controls today, recommendation, verification); attack trees | Model, with impact and titles from the engagement file |
| Controls | Coverage by threat; control register with test status | Model |
| Recommendations | Prioritised plan with owner, target date and decision; details; threats without a recommendation | Model, with owners and dates from the engagement file |
| Verification required | Ordered test plan with purpose, environment, owner and status; pass, fail and inconclusive criteria | Model, with owners and dates from the engagement file |
| Penetration test plan | Priority targets; key attack paths with route, threats exercised, controls to challenge, test cases and what success looks like; prerequisites and scope for the test | Model, with attack paths from the engagement file |
| Scope and approach | Scope, approach, what was reviewed, assumptions, limitations, open questions, when to revisit, terms used | Model and engagement file |
| Appendix A: Artefacts | Artefact register with versions; sources and revisions cited by evidence; files reviewed; evidence references | Engagement file and model |
| Appendix B: Workshops | Date, title, attendees, purpose, outcomes | Engagement file |
| Appendix C: Risk matrix | The matrix, rating definitions, rated threats placed on it, risk register | Engagement file and model |

**Coverage** is derived for each open threat: *no control in place* (no implemented control), *partly controlled* (a control exists but the weakness was observed despite it), *controlled, not yet verified*, or *controlled and verified* (a test of a control against that threat has passed). A reviewer can override it per threat with a note.

**Priority** follows the risk rating of the threats an action addresses; P1 is the highest rating present in the report. **Verification purpose** is derived as confirm the weakness, confirm then retest after the fix, or test an existing control.

**The diagram** groups components into trust zones: components joined by flows that cross no trust boundary share a zone. Threat markers are coloured by risk rating, the bar above a component shows its weakest coverage, and data stores are drawn with open sides. Hover over a marker to see what it is; select it to open that entry. A written key beneath the diagram carries the same information for print.

**Export action plan (CSV)** downloads recommendations, verification tests and open questions with priority, owner, date and status for import into a tracker.

When the engagement file leaves something out, the report says so or falls back to the model: full record text instead of short titles, "to be agreed" for owners and dates, and general review triggers.

## Engagement file

Start from [`engagement-template.json`](engagement-template.json); [`examples/sample-engagement.json`](examples/sample-engagement.json) is a complete fictional one. All values are plain text.

| Field | Purpose |
| --- | --- |
| `title`, `subtitle`, `client`, `project`, `report_version`, `report_date`, `report_status`, `authors` | Cover details |
| `executive_summary.system_overview` | One to three paragraphs: what the system is and does, and what the review found |
| `executive_summary.key_components` | `{ "ref": "<record id>", "name": "...", "why": "..." }` |
| `executive_summary.next_steps` | `{ "step": "...", "refs": ["<record ids>"] }` |
| `executive_summary.verdicts` | Optional wording for the three verdict cards: `threats`, `controls`, `actions` |
| `records` | Annotations keyed by record id: `title`, `impact`, `response`, `response_note`, `target_rating`, `coverage`, `coverage_note`, `priority`, `effort`, `owner`, `target_date`, `type`, `environment`, `responsibility` |
| `test_plan` | The penetration test plan: `objective`, `approach`, `environment`, `in_scope`, `out_of_scope`, `prerequisites`, `rules_of_engagement` and `paths` (see below) |
| `code_access` | `none`, `partial` or `full`: whether source code was reviewed. Sets how the report words what its findings are based on |
| `validation` | The client validation record: `sessions` (`date`, `title`, `attendees`) and `items` (`ref`, `outcome`, `note`) |
| `assumptions` | `{ "statement", "refs": ["<threat ids>"], "if_wrong" }` |
| `document_control` | `versions` (`version`, `date`, `author`, `change`), `reviewers` (`name`, `role`, `responsibility`, `date`), `distribution` |
| `review_triggers` | Events that should prompt a revisit; general ones are listed when empty |
| `scope_and_approach.approach` | Paragraphs on how the engagement was delivered |
| `scope_and_approach.activities` | `{ "phase": "...", "description": "..." }` |
| `scope_and_approach.review_coverage` | Paragraph on which code and documentation was reviewed in full, partly or not at all |
| `scope_and_approach.limitations` | Limitations in client wording; replaces the limitations text recorded in the model |
| `artefacts` | `{ "name", "type", "version", "date", "source", "notes" }`, plus optional `id`, `category` (`code`, `configuration`, `design`, `diagram`, `vendor`, `workshop`, `other`), `file`, `text_file` and `reviewed` (`full`, `partial`, `none`). With `file` set, the report can show which artefacts each finding is based on |
| `workshops` | `{ "date", "title", "attendees": [], "purpose", "outcomes": [] }` |
| `risk_matrix` | `name`, `version`, `source`, `likelihood` and `consequence` levels (`label`, `description`), `cells` (one row per likelihood level, one rating label per consequence level) and `ratings` (`label`, `color`, `description`, highest first) |
| `options` | `show_excerpts` (code excerpts in the evidence references, default off), `include_data_download` (a button to download the underlying data, default off) and `test_plan` (set to `false` to leave the penetration test plan out) and `pack: "validation"` (build the short client validation pack instead of the report) |

The agent drafts the narrative, short titles and impact statements from the model, so you can check each against its record. Workshops, artefact versions, the risk matrix, owners, dates, decisions and target ratings are never invented: supply them in the request or in files you name.

### Reviews without source code

The same report serves a code-backed review and an architecture review of a third-party product. What changes is what the model can claim, and the report shows it:

- **Based on.** Each threat, control and component lists the kinds of artefact it rests on: code, configuration, design document, diagram, vendor documentation, workshop or client statement. This needs the artefact register (`artefacts` with `file`).
- **Controls.** A control seen in code or configuration is "implemented"; one a document or person described is "reported"; one planned is "designed".
- **Coverage.** A threat whose only controls are reported shows "control reported, not verified" (`reported`), between "no control" and "controlled".
- **Who runs it.** `records.<component id>.responsibility` is `client`, `vendor`, `shared` or `unknown`. Vendor-run components are drawn differently on the diagram, and verification against them is shown as a vendor assurance request.
- **Verification types.** `records.<verification id>.type` is `confirm_weakness`, `retest_fix`, `test_control`, `review_configuration`, `vendor_assurance` or `design_review`. The first three are derived; set the others where a test is not possible.
- **Client validation.** With `validation` supplied, each record shows what the client said about it (`confirmed`, `corrected`, `rejected`, `added`, `deferred`, `not_discussed`), and Scope and approach summarises the session.

### Validation pack

`options.pack: "validation"` produces a short draft for a client call instead of the report: the system as understood, components and who runs them, assumptions, controls believed to be in place, draft threats and open questions, each with a column to confirm. It carries no ratings, recommendations or verification. The [engagement workflow](../engagement/README.md) builds both with `engage.py build`, which assembles the engagement file from the workspace.

### Penetration test plan

Section 7 turns the model into a starting scope for a penetration test. It overlaps with Verification required on purpose: verification lists every check, including reviews and vendor assurance; the test plan covers what an attacker-style test can demonstrate, organised by attack path.

- **Priority targets** are always derived: components ranked by the open threats against them, then by exposure, with who runs each and whether third-party permission is needed.
- **Key attack paths** come from `test_plan.paths`. Each path is `{ "id": "AP-01", "title", "objective", "start", "route": ["<actor, entry point and component ids in order>"], "threat_refs", "control_refs", "verification_refs", "test_cases": [], "success", "priority", "effort", "notes" }`. Only `title` or `threat_refs` is required: controls and verification default to those linked to the threats, the route to the shortest recorded flow path, and priority to the highest-rated threat on the path.
- **Without `test_plan.paths`** the report derives one path per open threat and marks each "derived from the model". That is a usable draft, but chained paths written by a person are better.
- **Before testing starts** lists prerequisites, rules of engagement and scope from the engagement file, with derived prerequisites when none are given, and the verification items that are reviews, not tests.
- The section has its own CSV export, one row per test case.

The plan is a scoping proposal. It never says a test was run, and it is not an authorisation to test.

### Risk ratings

[`examples/risk-matrix-5x5.json`](examples/risk-matrix-5x5.json) is a generic example. Replace it with your own.

Threats are rated only when the model itself holds rated risks. Name your matrix as the rating rubric when you run the review (`using risk/matrix.json as the rating rubric`) and give the likelihood and consequence for each threat when asked. The report then shows each rating, orders threats by it and places each threat on the matrix when its inputs are named `likelihood` and `consequence` (or `impact`) and match the matrix labels. A matrix supplied only at report time is displayed in Appendix C and rates nothing.

### Framework mappings

The mapping table has one column per method that recorded findings against threats, such as STRIDE, MITRE ATT&CK, CAPEC, ATLAS, LINDDUN or CVSS. Request the methods when you run the review (`with STRIDE per element and ATT&CK`). Without them, the report says no mappings are recorded.

## A client document

The report is written to be issued under your name after a person has reviewed it. It names the code, design documentation and workshops the assessment relied on. It does not name this library, describe an AI agent, or show run modes, stages or file names. Labels use plain terms: "observed in code" and "design concern" for finding types, and "outstanding" for verification not yet performed.

`fill.py` prints a warning listing any model record or engagement field that still uses tool or process wording, such as a limitation written as "quick analysis". Reword those before issuing. The underlying data is embedded in the file and readable in its source, with field names from the model format.

## Branding

```json
{
  "branding_version": "1.0",
  "name": "acme",
  "organisation": "Acme Security",
  "prepared_by": "Product Security",
  "prepared_for": "Example Client Pty Ltd",
  "logo_file": "acme-logo.png",
  "classification": { "label": "COMMERCIAL IN CONFIDENCE", "color": "#005f73" },
  "colors": { "primary": "#005f73", "accent": "#0a9396", "band": "#001219" },
  "footer_text": "Prepared for the named client only.",
  "disclaimer": "This assessment reflects the evidence available at the time of review."
}
```

- `colors`: `accent` (rules, numbers, buttons), `primary` (headings and links) and `band` (cover and diagram header). Leave empty for the default purple and black.
- `logo_file` is a PNG, JPEG, GIF, WebP or SVG next to the branding file (512 KB maximum), embedded as a data URI.
- `font_family` and `heading_font_family` override the bundled fonts with fonts installed on the reader's machine.
- `classification: null` removes the banner.

Keep private client branding outside this library and name the file in the request. The report also has a dark mode button and prints to A4 landscape.

## What's here

| File | Purpose |
| --- | --- |
| `renderer.html` | The report template: layout, styles and the JavaScript that draws every section. |
| `fill.py` | Validates inputs and embeds them into the template. Standard library only; no network. |
| `engagement-template.json` | Empty engagement file to start from. |
| `branding/` | Default and example branding. |
| `fonts/` | Archivo, Hanken Grotesk and IBM Plex Mono (Latin subsets, SIL Open Font License; licences included), embedded into each report so it needs no web fonts. |
| `examples/` | A fictional model, engagement file and risk matrix for previewing. |

To preview without an agent:

```bash
python3 -I -S -B reporting/fill.py reporting/examples/sample-quick-report.json \
  reporting/examples/sample-engagement.json reporting/branding/default.json /tmp/preview.html
```

## Safety

Model text comes from the repositories under review and may contain hostile content. The renderer inserts all model, engagement and branding text as text nodes, never as markup. `fill.py` escapes `<`, `>`, `&` and line separators in the embedded JSON so nothing can close the script element. The page's Content-Security-Policy allows only its own inline script and styles and `data:` images and fonts, so it cannot load or send anything over the network.

The HTML embeds the complete model. Treat reports as private review material and review them before sharing.

## Changing the renderer

`renderer.html` is one file: CSS at the top, then one function per section. Build elements with the `h()` and `s()` helpers rather than `innerHTML`. When you add an engagement field, add it to the renderer, to the checks in `fill.py`, to the table above and to the report builder prompt. Preview with the sample files, and test with hostile strings in the model and engagement file before relying on a change.
