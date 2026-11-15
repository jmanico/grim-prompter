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
| `records` | Annotations keyed by record id: `title`, `impact`, `response`, `response_note`, `target_rating`, `coverage`, `coverage_note`, `priority`, `effort`, `owner`, `target_date`, `type`, `environment` |
| `assumptions` | `{ "statement", "refs": ["<threat ids>"], "if_wrong" }` |
| `document_control` | `versions` (`version`, `date`, `author`, `change`), `reviewers` (`name`, `role`, `responsibility`, `date`), `distribution` |
| `review_triggers` | Events that should prompt a revisit; general ones are listed when empty |
| `scope_and_approach.approach` | Paragraphs on how the engagement was delivered |
| `scope_and_approach.activities` | `{ "phase": "...", "description": "..." }` |
| `scope_and_approach.review_coverage` | Paragraph on which code and documentation was reviewed in full, partly or not at all |
| `scope_and_approach.limitations` | Limitations in client wording; replaces the limitations text recorded in the model |
| `artefacts` | `{ "name", "type", "version", "date", "source", "notes" }` |
| `workshops` | `{ "date", "title", "attendees": [], "purpose", "outcomes": [] }` |
| `risk_matrix` | `name`, `version`, `source`, `likelihood` and `consequence` levels (`label`, `description`), `cells` (one row per likelihood level, one rating label per consequence level) and `ratings` (`label`, `color`, `description`, highest first) |
| `options` | `show_excerpts` (code excerpts in the evidence references, default off) and `include_data_download` (a button to download the underlying data, default off) |

The agent drafts the narrative, short titles and impact statements from the model, so you can check each against its record. Workshops, artefact versions, the risk matrix, owners, dates, decisions and target ratings are never invented: supply them in the request or in files you name.

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
