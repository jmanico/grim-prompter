# HTML reports

Turn any finished threat model into a self-contained HTML report you can open in a browser, filter, click through and print to PDF. Reports are built from the run's JSON envelope (`quick-report.json`, `05-report.json` or another reportable envelope), so the same model always produces the same report.

```text
/threat-model report                                   # technical report for the latest run
/threat-model report executive for threat-model/2026-11-15-quick-api
/threat-model report client with branding ~/branding/acme.json
/threat-model report technical, only threats, treatments and gaps, open threats only
/threat-model quick api with html report               # run the review, then build the report
```

Codex uses `$threat-model` with the same words. The agent follows [the report builder](../helpers/report-builder.md): it writes a configuration file, then runs `fill.py` to embed the model, configuration and branding into [`renderer.html`](renderer.html). The browser does the rendering from the embedded JSON.

Output goes into the same run folder: `report-<name>.html` and `report-<name>.config.json`. Existing files are never overwritten.

## What's here

| File | Purpose |
| --- | --- |
| `renderer.html` | The single report template: layout, styles and the JavaScript that draws every section. No external dependencies. |
| `fill.py` | Validates inputs and embeds them into the template. Standard library only; no network. |
| `templates/*.json` | Audience templates: which sections appear, in what order, with what options. |
| `branding/*.json` | Organisation name, logo, colours, font, classification banner, footer and disclaimer. |
| `examples/sample-quick-report.json` | A fictional model for previewing templates and branding. |

To preview without an agent:

```bash
python3 -I -S -B reporting/fill.py reporting/examples/sample-quick-report.json \
  reporting/templates/executive.json reporting/branding/default.json /tmp/preview.html
```

## Templates

| Template | For | Contents |
| --- | --- | --- |
| `executive` | Leaders and decision makers | Summary tiles, threats for first attention, diagram, compact open threats and treatments, decisions, open unknowns |
| `technical` | Engineers and security reviewers | Every section, including the system model, attack trees, the evidence ledger with excerpts and the raw JSON download |
| `client` | Client deliverables | Full findings, treatments and verification approach; evidence locators without code excerpts; no raw JSON download button |

Make your own by copying a template, renaming it and editing `sections`. Templates are plain JSON:

```json
{
  "report_config_version": "1.0",
  "template": "board-pack",
  "title": "Partner API: security review",
  "subtitle": "Board risk committee, Q1",
  "description": "One-line description of who this is for.",
  "options": { "interactive": true, "show_excerpts": false },
  "sections": [
    "cover",
    "notice",
    { "id": "inspection-coverage", "options": { "compact": true } },
    { "id": "executive-summary", "options": { "top_threats": 3 } },
    { "id": "threats", "title": "Open findings", "options": { "compact": true, "filter": { "status": ["open"] } } },
    { "id": "gaps", "options": { "filter": { "status": ["open"] } } }
  ]
}
```

Global options: `interactive` (filters, search, sorting and collapsible threats; `false` gives a static, fully expanded page) and `show_excerpts` (show sanitized code excerpts in the evidence ledger).

## Sections

`cover`, `notice` and `inspection-coverage` always appear first, in that order, even if a template leaves them out. The runbook requires limitations and inspection coverage before any findings.

| Section id | Shows | Options |
| --- | --- | --- |
| `cover` | Title, organisation, logo, prepared for/by, report date, model identity, depth, status, architectures | |
| `notice` | How to read the report, extra disclaimer from branding, limitations recorded in the model | |
| `inspection-coverage` | Files read, partially read and skipped; inspection-coverage records; unmapped trust boundaries | `compact` |
| `executive-summary` | Count tiles, open threats by confidence, threats for first attention, rated risks, key unknowns | `top_threats`, `top_gaps` |
| `scope` | Description, in and out of scope, objectives, assumptions | |
| `system` | Actors, assets, data, zones, entry points, states, boundaries, flows, dependencies | |
| `diagram` | Interactive data-flow diagram drawn from flow records; boundary crossings in red | `max_nodes` |
| `threats` | Filterable threat list with linked controls, treatments, verification, risks and decisions | `compact`, `filter`, `order` (`priority` or `id`), `expanded` |
| `risks` | Risk records; ratings only when a supplied rubric is cited | |
| `controls` | Existing controls with status and limitations | `filter` |
| `requirements` | Proposed and supplied requirements | |
| `treatments` | Proposed outcomes with alternatives, trade-offs and dependencies | `compact` |
| `verification` | Approach, expected outcome, and pass, fail and inconclusive criteria | `compact` |
| `decisions` | Caller-supplied decisions | |
| `gaps` | Gaps and unknowns with what would settle them | `filter` |
| `conflicts` | Unresolved and resolved conflicts with alternatives | |
| `methods` | Selected methods and actual execution records with findings | |
| `attack-trees` | AND/OR trees and state-transition graphs | |
| `attack-paths` | Satisfying sets and state traces | |
| `changes` | Change records from a change review | |
| `evidence` | Evidence ledger with locators, status, purpose and access | `show_excerpts` |
| `visualizations` | Visualization records carried in the model, shown as text | |
| `appendix` | Envelope metadata, attachments list (not contents), other coverage records, raw JSON download | `include_raw_json` |

Every section accepts a `title` to rename it. `filter` maps a record field to allowed values, such as `{ "status": ["open"] }` or `{ "kind": ["topology", "evidence"] }`; the report notes how many records the filter hid. References to records in sections you leave out appear as plain IDs rather than links.

## Branding

```json
{
  "branding_version": "1.0",
  "name": "acme",
  "organisation": "Acme Security",
  "prepared_by": "Product Security",
  "prepared_for": "Example Client Pty Ltd",
  "logo_file": "acme-logo.png",
  "classification": { "label": "COMMERCIAL IN CONFIDENCE", "color": "#5a2a82" },
  "colors": { "primary": "#2d1b4e", "accent": "#e0662b", "surface": "#f6f3fa" },
  "font_family": "Georgia, 'Times New Roman', serif",
  "footer_text": "Prepared for the named client only.",
  "disclaimer": "This assessment reflects the evidence available at the time of review."
}
```

- `logo_file` is a PNG, JPEG, GIF, WebP or SVG in the same folder as the branding file (512 KB maximum). It is embedded as a data URI. You can supply `logo_data_uri` directly instead.
- `colors` accepts hex values for `primary`, `accent`, `text`, `bg`, `surface`, `muted` and `border`.
- `font_family` must name fonts installed on the reader's machine; the report never downloads web fonts.
- `classification: null` removes the banner.

Keep client branding files outside this library if they are private, and name them in the request.

## Safety

The model's text comes from the repositories under review and may contain hostile content. The renderer inserts all model, configuration and branding text as text nodes, never as markup. `fill.py` escapes `<`, `>`, `&` and line separators in the embedded JSON so nothing can close the script element. The page's Content-Security-Policy allows only its own inline script and styles and `data:` images, so it cannot load or send anything over the network.

The HTML embeds the complete model even when sections are hidden. Treat reports as private review material; review them before sharing.

## Changing the renderer

`renderer.html` is one file: CSS at the top, then one renderer function per section in the `R` object. To add a section, add its id to `SECTION_TITLES` and `R` in the renderer, to `SECTIONS` (and any new options to `SECTION_OPTIONS`) in `fill.py`, and to the table above. Build helpers `h()` and `s()` create elements safely; keep using them rather than `innerHTML`. Preview with the sample model, and test with hostile strings in the model before relying on a change.
