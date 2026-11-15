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

| Section | Contents | Comes from |
| --- | --- | --- |
| Executive summary | What the system is and does, key components, key next steps, headline counts, summary table, basis and limits | Narrative from the engagement file; everything else from the model |
| Technical summary | Architecture diagram with threats, controls and verification on each component; overview table; component and flow inventory | Model |
| Threats | Framework mapping table; threat details; attack trees and conflicts when present | Model (mappings come from method findings) |
| Controls | Controls in place with status, limitations and the threats they address | Model |
| Recommendations | Proposed treatments with alternatives and trade-offs; requirements and decisions when present | Model |
| Verification required | Planned tests with pass, fail and inconclusive criteria | Model |
| Scope and approach | Scope, approach, methods applied, inspection coverage, limitations, open unknowns | Model, plus approach narrative from the engagement file |
| Appendix A: Artefacts | Artefact register with versions; sources and revisions cited by evidence; files inspected; evidence ledger | Engagement file and model |
| Appendix B: Workshops | Date, title, attendees, purpose, outcomes | Engagement file |
| Appendix C: Risk matrix | The matrix, rating definitions, rated threats placed on it, risk register | Engagement file and model |

The architecture diagram is drawn from the model's flow records, arranged in flow order from the actors. Each component carries markers for its threats, controls and verification tests. Hover over a marker to see what it is; select it to open that entry. Select a component to highlight its connections. Flows that cross a trust boundary are dashed. Use the checkboxes to hide a layer and the zoom buttons to resize.

When the engagement file leaves something out, the report says so and falls back to the model where it can: the scope description for the summary, the components with the most open threats, and the recommendations for the first open threats.

## Engagement file

Start from [`engagement-template.json`](engagement-template.json); [`examples/sample-engagement.json`](examples/sample-engagement.json) is a complete fictional one. All values are plain text.

| Field | Purpose |
| --- | --- |
| `title`, `subtitle`, `client`, `project`, `report_version`, `report_date`, `report_status`, `authors` | Cover details |
| `executive_summary.system_overview` | One to three paragraphs: what the system is and does, and what the review found |
| `executive_summary.key_components` | `{ "ref": "<record id>", "name": "...", "why": "..." }` |
| `executive_summary.next_steps` | `{ "step": "...", "refs": ["<record ids>"] }` |
| `scope_and_approach.approach` | Paragraphs on how the engagement was delivered |
| `scope_and_approach.activities` | `{ "phase": "...", "description": "..." }` |
| `scope_and_approach.review_coverage` | Paragraph on which code and documentation was reviewed in full, partly or not at all |
| `scope_and_approach.limitations` | Limitations in client wording; replaces the limitations text recorded in the model |
| `artefacts` | `{ "name", "type", "version", "date", "source", "notes" }` |
| `workshops` | `{ "date", "title", "attendees": [], "purpose", "outcomes": [] }` |
| `risk_matrix` | `name`, `version`, `source`, `likelihood` and `consequence` levels (`label`, `description`), `cells` (one row per likelihood level, one rating label per consequence level) and `ratings` (`label`, `color`, `description`, highest first) |
| `options` | `show_excerpts` (code excerpts in the evidence references, default off) and `include_data_download` (a button to download the underlying data, default off) |

The agent drafts the summary narrative from the model and cites record ids, so you can check each statement. Workshops, artefact versions and the risk matrix are never invented: supply them in the request or in files you name.

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
