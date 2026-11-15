"""Fill the Grim Prompter HTML report template.

Usage (from the library, with a trusted interpreter in isolated mode):

    python3 -I -S -B LIBRARY_ROOT/reporting/fill.py MODEL_JSON ENGAGEMENT_JSON BRANDING_JSON OUTPUT_HTML

Embeds the model, the engagement content (narrative, artefacts, workshops, risk matrix)
and the branding into reporting/renderer.html, with the bundled fonts, and writes OUTPUT_HTML.
It validates every input, never overwrites an existing file, uses only the standard
library and never touches the network. Rendering happens in the browser from the
embedded JSON, so the same inputs always produce the same report.
"""
import base64
import datetime
import json
import os
import re
import stat
import sys

HERE = os.path.dirname(os.path.realpath(__file__))
TEMPLATE = os.path.join(HERE, "renderer.html")
MARKERS = ("/*TM_FONTS*/", "/*TM_DATA*/", "/*TM_ENGAGEMENT*/", "/*TM_BRANDING*/")
FONT_DIR = os.path.join(HERE, "fonts")
FONTS = (("Archivo", 600, "archivo-latin-600-normal.woff2"), ("Archivo", 700, "archivo-latin-700-normal.woff2"),
         ("Hanken Grotesk", 400, "hanken-grotesk-latin-400-normal.woff2"), ("Hanken Grotesk", 600, "hanken-grotesk-latin-600-normal.woff2"),
         ("IBM Plex Mono", 400, "ibm-plex-mono-latin-400-normal.woff2"), ("IBM Plex Mono", 500, "ibm-plex-mono-latin-500-normal.woff2"))
MAX_INPUT = 64 * 1024 * 1024
MAX_LOGO = 512 * 1024

REPORTABLE = {
    "TM_REPORT", "TM_TREATMENT_PLAN", "TM_REVIEWED_MODEL", "TM_ANALYSIS", "TM_SYSTEM_MODEL",
    "THREAT_MODEL_REPORT", "THREAT_MODEL_VISUAL", "THREAT_MODEL_DIAGRAM", "UNIFIED_THREAT_MODEL",
    "THREAT_MODEL_FRAGMENT",
}
ENGAGEMENT_KEYS = {"engagement_version", "title", "subtitle", "client", "project", "report_version", "report_date", "authors",
                   "executive_summary", "scope_and_approach", "artefacts", "workshops", "risk_matrix", "options"}
ENGAGEMENT_OPTIONS = {"show_excerpts", "hide_json_download"}
BRANDING_KEYS = {"branding_version", "name", "organisation", "prepared_by", "prepared_for", "logo_file",
                 "logo_data_uri", "classification", "colors", "font_family", "heading_font_family", "footer_text", "disclaimer"}
COLOR_KEYS = {"primary", "accent", "band"}
COLOR_RE = re.compile(r"^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")
FONT_RE = re.compile(r"^[A-Za-z0-9 ,'\"\-]{1,200}$")
DATA_URI_RE = re.compile(r"^data:image/(?:png|jpeg|gif|webp|svg\+xml);base64,[A-Za-z0-9+/=]+$")
LOGO_TYPES = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".gif": "image/gif",
              ".webp": "image/webp", ".svg": "image/svg+xml"}


class InputError(Exception):
    pass


def read_regular(path, limit):
    st = os.lstat(path)
    if stat.S_ISLNK(st.st_mode) or not stat.S_ISREG(st.st_mode):
        raise InputError(f"{path}: not a regular file (symlinks are refused)")
    if st.st_size > limit:
        raise InputError(f"{path}: larger than {limit} bytes")
    with open(path, "rb") as fh:
        return fh.read()


def _no_duplicates(pairs):
    obj = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError(f"duplicate object key {key!r}")
        obj[key] = value
    return obj


def _no_constants(name):
    raise ValueError(f"non-finite number {name} is not allowed")


def load_json(path, what):
    try:
        return json.loads(read_regular(path, MAX_INPUT).decode("utf-8"),
                          object_pairs_hook=_no_duplicates, parse_constant=_no_constants)
    except (OSError, UnicodeDecodeError, ValueError) as exc:
        raise InputError(f"{what} {path}: {exc}") from None


def short_text(value, field, limit=300):
    if value is None:
        return None
    if not isinstance(value, str) or len(value) > limit:
        raise InputError(f"{field} must be text of at most {limit} characters")
    return value


def check_model(model):
    if not isinstance(model, dict) or not isinstance(model.get("model"), dict):
        raise InputError("model: not a Grim Prompter envelope (no 'model' object)")
    kind = model.get("artifact_type")
    if kind not in REPORTABLE:
        raise InputError(f"model: artifact_type {kind!r} is not reportable; use a quick or deep report, a later stage envelope, or a unified model")
    if model.get("status") == "chunk":
        raise InputError("model: this envelope is one chunk of a sequence; reassemble the full sequence first")
    warnings = []
    if model.get("schema_version") != "1.0":
        warnings.append(f"schema_version is {model.get('schema_version')!r}, not 1.0; the report may be incomplete")
    if model.get("status") != "complete":
        warnings.append(f"model status is {model.get('status')!r}; the report will say so")
    return warnings


def _text(value, where, limit=4000):
    if value is not None and not (isinstance(value, str) and len(value) <= limit):
        raise InputError(f"engagement: {where} must be text of at most {limit} characters")


def _text_list(value, where, limit=4000, count=200):
    if value is None:
        return
    if isinstance(value, str):
        return _text(value, where, limit)
    if not isinstance(value, list) or len(value) > count:
        raise InputError(f"engagement: {where} must be a list of at most {count} text items")
    for item in value:
        _text(item, where, limit)


def _rows(value, where, text_keys, list_keys=(), count=500):
    if value is None:
        return
    if not isinstance(value, list) or len(value) > count:
        raise InputError(f"engagement: {where} must be a list of at most {count} objects")
    for row in value:
        if not isinstance(row, dict) or set(row) - set(text_keys) - set(list_keys):
            raise InputError(f"engagement: each {where} item may use only {sorted(set(text_keys) | set(list_keys))}")
        for key in text_keys:
            _text(row.get(key), f"{where}.{key}")
        for key in list_keys:
            _text_list(row.get(key), f"{where}.{key}", 400)


def check_engagement(eng):
    if not isinstance(eng, dict):
        raise InputError("engagement: must be a JSON object")
    unknown = set(eng) - ENGAGEMENT_KEYS
    if unknown:
        raise InputError(f"engagement: unknown keys {sorted(unknown)}")
    if eng.get("engagement_version") != "1.0":
        raise InputError("engagement: engagement_version must be \"1.0\"")
    for key in ("title", "subtitle", "client", "project", "report_version", "report_date"):
        _text(eng.get(key), key, 300)
    _text_list(eng.get("authors"), "authors", 200, 50)
    summary = eng.get("executive_summary") or {}
    if not isinstance(summary, dict) or set(summary) - {"system_overview", "key_components", "next_steps"}:
        raise InputError("engagement: executive_summary may use only system_overview, key_components and next_steps")
    _text_list(summary.get("system_overview"), "executive_summary.system_overview", 4000, 12)
    _rows(summary.get("key_components"), "executive_summary.key_components", ("ref", "name", "why"), count=20)
    _rows(summary.get("next_steps"), "executive_summary.next_steps", ("step",), ("refs",), count=20)
    approach = eng.get("scope_and_approach") or {}
    if not isinstance(approach, dict) or set(approach) - {"approach", "activities"}:
        raise InputError("engagement: scope_and_approach may use only approach and activities")
    _text_list(approach.get("approach"), "scope_and_approach.approach", 4000, 20)
    _rows(approach.get("activities"), "scope_and_approach.activities", ("phase", "description"), count=50)
    _rows(eng.get("artefacts"), "artefacts", ("name", "type", "version", "date", "source", "notes"))
    _rows(eng.get("workshops"), "workshops", ("date", "title", "purpose"), ("attendees", "outcomes"), count=200)
    opts = eng.get("options") or {}
    if not isinstance(opts, dict) or set(opts) - ENGAGEMENT_OPTIONS or not all(isinstance(v, bool) for v in opts.values()):
        raise InputError(f"engagement: options must be booleans from {sorted(ENGAGEMENT_OPTIONS)}")
    matrix = eng.get("risk_matrix")
    if matrix is None:
        return
    if not isinstance(matrix, dict) or set(matrix) - {"name", "version", "source", "likelihood", "consequence", "cells", "ratings"}:
        raise InputError("engagement: risk_matrix may use only name, version, source, likelihood, consequence, cells and ratings")
    for key in ("name", "version", "source"):
        _text(matrix.get(key), f"risk_matrix.{key}", 600)
    _rows(matrix.get("likelihood"), "risk_matrix.likelihood", ("label", "description"), count=10)
    _rows(matrix.get("consequence"), "risk_matrix.consequence", ("label", "description"), count=10)
    _rows(matrix.get("ratings"), "risk_matrix.ratings", ("label", "color", "description"), count=10)
    for rating in matrix.get("ratings") or []:
        if rating.get("color") is not None and not COLOR_RE.match(rating["color"]):
            raise InputError("engagement: risk_matrix.ratings colours must be hex values such as #d6401c")
    rows, cols = matrix.get("likelihood") or [], matrix.get("consequence") or []
    cells = matrix.get("cells")
    if not (isinstance(cells, list) and len(cells) == len(rows)
            and all(isinstance(r, list) and len(r) == len(cols) and all(isinstance(c, str) and len(c) <= 60 for c in r) for r in cells)):
        raise InputError("engagement: risk_matrix.cells needs one row per likelihood level and one rating label per consequence level")
    labels = {str(r.get("label", "")).strip().lower() for r in matrix.get("ratings") or []}
    if labels and any(c.strip().lower() not in labels for r in cells for c in r):
        raise InputError("engagement: every risk_matrix cell must use a label defined in risk_matrix.ratings")


def font_css():
    rules = []
    for family, weight, name in FONTS:
        path = os.path.join(FONT_DIR, name)
        if not os.path.isfile(path):
            continue
        b64 = base64.b64encode(read_regular(path, 1024 * 1024)).decode("ascii")
        rules.append(f'@font-face{{font-family:"{family}";font-style:normal;font-weight:{weight};font-display:swap;'
                     f'src:url(data:font/woff2;base64,{b64}) format("woff2")}}')
    return "\n".join(rules)


def check_branding(brand, brand_path):
    if not isinstance(brand, dict):
        raise InputError("branding: must be a JSON object")
    unknown = set(brand) - BRANDING_KEYS
    if unknown:
        raise InputError(f"branding: unknown keys {sorted(unknown)}")
    for k in ("name", "organisation", "prepared_by", "prepared_for", "footer_text"):
        short_text(brand.get(k), f"branding.{k}")
    short_text(brand.get("disclaimer"), "branding.disclaimer", 1000)
    colors = brand.get("colors", {})
    if not isinstance(colors, dict) or set(colors) - COLOR_KEYS:
        raise InputError(f"branding.colors keys must be from {sorted(COLOR_KEYS)}")
    for k, v in colors.items():
        if not isinstance(v, str) or not COLOR_RE.match(v):
            raise InputError(f"branding.colors.{k} must be a hex colour such as #7500c0")
    for key in ("font_family", "heading_font_family"):
        if brand.get(key) is not None and not (isinstance(brand[key], str) and FONT_RE.match(brand[key])):
            raise InputError(f"branding.{key} may contain only letters, digits, spaces, commas, quotes and hyphens")
    cls = brand.get("classification")
    if cls is not None:
        if not isinstance(cls, dict) or set(cls) - {"label", "color"}:
            raise InputError("branding.classification must be {\"label\": ..., \"color\": ...} or null")
        short_text(cls.get("label"), "branding.classification.label", 80)
        if cls.get("color") is not None and not COLOR_RE.match(str(cls["color"])):
            raise InputError("branding.classification.color must be a hex colour")
    out = dict(brand)
    logo_file = out.pop("logo_file", None)
    if logo_file:
        if not isinstance(logo_file, str) or os.path.isabs(logo_file) or ".." in logo_file.replace("\\", "/").split("/"):
            raise InputError("branding.logo_file must be a relative path inside the branding file's folder")
        ext = os.path.splitext(logo_file)[1].lower()
        if ext not in LOGO_TYPES:
            raise InputError(f"branding.logo_file must be one of {sorted(LOGO_TYPES)}")
        raw = read_regular(os.path.join(os.path.dirname(os.path.abspath(brand_path)), logo_file), MAX_LOGO)
        out["logo_data_uri"] = f"data:{LOGO_TYPES[ext]};base64," + base64.b64encode(raw).decode("ascii")
    uri = out.get("logo_data_uri")
    if uri is not None and not (isinstance(uri, str) and DATA_URI_RE.match(uri) and len(uri) < MAX_LOGO * 2):
        raise InputError("branding.logo_data_uri must be a base64 data URI for png, jpeg, gif, webp or svg")
    return out


def embed(obj):
    text = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    # Inside JSON these characters only occur within strings, so escaping keeps the JSON valid
    # and makes it impossible to close the <script> element or open a comment.
    return (text.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
            .replace("\u2028", "\\u2028").replace("\u2029", "\\u2029"))


def main(argv):
    if len(argv) != 5:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    model_path, eng_path, brand_path, out_path = argv[1:]
    try:
        model = load_json(model_path, "model")
        eng = load_json(eng_path, "engagement")
        brand = load_json(brand_path, "branding")
        warnings = check_model(model)
        check_engagement(eng)
        brand = check_branding(brand, brand_path)
        if not out_path.endswith(".html"):
            raise InputError("output must end with .html")
        parent = os.path.dirname(os.path.abspath(out_path))
        if not os.path.isdir(parent) or os.path.islink(out_path):
            raise InputError("output folder must exist and the output must not be a symlink")
        template = read_regular(TEMPLATE, 4 * 1024 * 1024).decode("utf-8")
        pieces, rest = [], template
        for marker in MARKERS:
            if template.count(marker) != 1 or rest.count(marker) != 1:
                raise InputError(f"renderer.html must contain {marker} exactly once, in order")
            head, rest = rest.split(marker)
            pieces.append(head)
        eng = dict(eng)
        eng["generated_at"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
        eng["source_file"] = os.path.basename(model_path)
        html = (pieces[0] + font_css() + pieces[1] + embed(model) + pieces[2] + embed(eng)
                + pieces[3] + embed(brand) + rest)
        with open(out_path, "x", encoding="utf-8") as fh:
            fh.write(html)
    except FileExistsError:
        print(f"error: {out_path} already exists; choose a new name (reports are never overwritten)", file=sys.stderr)
        return 1
    except (InputError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    m = model["model"]
    print(f"wrote {out_path}")
    print(f"model {model.get('model_id')} rev {model.get('revision')} ({model.get('artifact_type')}, {model.get('status')}); "
          f"threats {len(m.get('threats', []))}, controls {len(m.get('controls', []))}, recommendations {len(m.get('treatments', []))}, "
          f"verification {len(m.get('verification', []))}, gaps {len(m.get('gaps', []))}")
    summary = eng.get("executive_summary") or {}
    missing = [name for name, present in (
        ("executive summary narrative", summary.get("system_overview")), ("key components", summary.get("key_components")),
        ("next steps", summary.get("next_steps")), ("approach narrative", (eng.get("scope_and_approach") or {}).get("approach")),
        ("artefact register (Appendix A)", eng.get("artefacts")), ("workshops (Appendix B)", eng.get("workshops")),
        ("risk matrix (Appendix C)", eng.get("risk_matrix"))) if not present]
    if missing:
        print("not supplied, shown as such in the report: " + "; ".join(missing))
    if not any(r.get("status") == "rated" for r in m.get("risks", []) if isinstance(r, dict)):
        print("note: the model has no rated risks, so threats appear as unrated")
    for w in warnings:
        print(f"warning: {w}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
