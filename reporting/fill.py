"""Fill the Grim Prompter HTML report template.

Usage (from the library, with a trusted interpreter in isolated mode):

    python3 -I -S -B LIBRARY_ROOT/reporting/fill.py MODEL_JSON CONFIG_JSON BRANDING_JSON OUTPUT_HTML

Embeds the three JSON documents into reporting/renderer.html and writes OUTPUT_HTML.
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
MARKERS = ("/*TM_DATA*/", "/*TM_CONFIG*/", "/*TM_BRANDING*/")
MAX_INPUT = 64 * 1024 * 1024
MAX_LOGO = 512 * 1024

REPORTABLE = {
    "TM_REPORT", "TM_TREATMENT_PLAN", "TM_REVIEWED_MODEL", "TM_ANALYSIS", "TM_SYSTEM_MODEL",
    "THREAT_MODEL_REPORT", "THREAT_MODEL_VISUAL", "THREAT_MODEL_DIAGRAM", "UNIFIED_THREAT_MODEL",
    "THREAT_MODEL_FRAGMENT",
}
SECTIONS = {
    "cover", "notice", "inspection-coverage", "executive-summary", "scope", "system", "diagram",
    "threats", "risks", "controls", "requirements", "treatments", "verification", "decisions",
    "gaps", "conflicts", "methods", "attack-trees", "attack-paths", "changes", "evidence",
    "visualizations", "appendix",
}
SECTION_OPTIONS = {"compact", "filter", "top_threats", "top_gaps", "order", "expanded",
                   "show_excerpts", "include_raw_json", "max_nodes"}
CONFIG_KEYS = {"report_config_version", "template", "title", "subtitle", "description", "sections", "options"}
GLOBAL_OPTIONS = {"interactive", "show_excerpts"}
BRANDING_KEYS = {"branding_version", "name", "organisation", "prepared_by", "prepared_for", "logo_file",
                 "logo_data_uri", "classification", "colors", "font_family", "footer_text", "disclaimer"}
COLOR_KEYS = {"primary", "accent", "text", "bg", "surface", "muted", "border"}
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


def check_config(cfg):
    if not isinstance(cfg, dict):
        raise InputError("config: must be a JSON object")
    unknown = set(cfg) - CONFIG_KEYS
    if unknown:
        raise InputError(f"config: unknown keys {sorted(unknown)}")
    if cfg.get("report_config_version") != "1.0":
        raise InputError("config: report_config_version must be \"1.0\"")
    for k in ("template", "title", "subtitle", "description"):
        short_text(cfg.get(k), f"config.{k}")
    sections = cfg.get("sections")
    if not isinstance(sections, list) or not sections:
        raise InputError("config: sections must be a nonempty list")
    seen = set()
    for item in sections:
        sid = item if isinstance(item, str) else (item.get("id") if isinstance(item, dict) else None)
        if sid not in SECTIONS:
            raise InputError(f"config: unknown section {sid!r}; allowed: {sorted(SECTIONS)}")
        if sid in seen:
            raise InputError(f"config: section {sid!r} listed twice")
        seen.add(sid)
        if isinstance(item, dict):
            extra = set(item) - {"id", "title", "options"}
            if extra:
                raise InputError(f"config: section {sid!r} has unknown keys {sorted(extra)}")
            short_text(item.get("title"), f"section {sid} title", 120)
            opts = item.get("options", {})
            if not isinstance(opts, dict) or set(opts) - SECTION_OPTIONS:
                raise InputError(f"config: section {sid!r} options must use {sorted(SECTION_OPTIONS)}")
            flt = opts.get("filter")
            if flt is not None and not (isinstance(flt, dict) and all(isinstance(v, list) and all(isinstance(x, str) for x in v) for v in flt.values())):
                raise InputError(f"config: section {sid!r} filter must map field names to lists of strings")
    opts = cfg.get("options", {})
    if not isinstance(opts, dict) or set(opts) - GLOBAL_OPTIONS or not all(isinstance(v, bool) for v in opts.values()):
        raise InputError(f"config: options must be booleans from {sorted(GLOBAL_OPTIONS)}")


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
            raise InputError(f"branding.colors.{k} must be a hex colour such as #1f3a5f")
    if brand.get("font_family") is not None and not (isinstance(brand["font_family"], str) and FONT_RE.match(brand["font_family"])):
        raise InputError("branding.font_family may contain only letters, digits, spaces, commas, quotes and hyphens")
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
    model_path, config_path, brand_path, out_path = argv[1:]
    try:
        model = load_json(model_path, "model")
        config = load_json(config_path, "config")
        brand = load_json(brand_path, "branding")
        warnings = check_model(model)
        check_config(config)
        brand = check_branding(brand, brand_path)
        if not out_path.endswith(".html"):
            raise InputError("output must end with .html")
        parent = os.path.dirname(os.path.abspath(out_path))
        if not os.path.isdir(parent) or os.path.islink(out_path):
            raise InputError("output folder must exist and the output must not be a symlink")
        template = read_regular(TEMPLATE, 4 * 1024 * 1024).decode("utf-8")
        pieces, rest = [], template
        for marker in MARKERS:
            if rest.count(marker) != 1 or template.count(marker) != 1:
                raise InputError(f"renderer.html must contain {marker} exactly once")
            head, rest = rest.split(marker)
            pieces.append(head)
        config = dict(config)
        config["generated_at"] = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
        config["source_file"] = os.path.basename(model_path)
        html = pieces[0] + embed(model) + pieces[1] + embed(config) + pieces[2] + embed(brand) + rest
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
          f"threats {len(m.get('threats', []))}, treatments {len(m.get('treatments', []))}, gaps {len(m.get('gaps', []))}, evidence {len(m.get('evidence', []))}")
    print("sections: " + ", ".join(s if isinstance(s, str) else s["id"] for s in config["sections"]))
    for w in warnings:
        print(f"warning: {w}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
