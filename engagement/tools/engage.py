"""Engagement workspace helper for threat modelling engagements.

Run with a trusted interpreter in isolated mode:

    python3 -I -S -B LIBRARY_ROOT/engagement/tools/engage.py COMMAND WORKSPACE [options]

Commands
    init WORKSPACE --client NAME --system NAME [--project NAME] [--code none|partial|full]
        Create the workspace folders and engagement.json.
    scan WORKSPACE
        Register new or changed files under materials/ in materials/register.json.
    extract WORKSPACE
        Extract plain text from .docx, .pptx, .vsdx, .vtt and .srt materials into materials/_text/.
    plan WORKSPACE --architectures a,b --methods m1,m2 --depth quick|deep --by NAME
                   [--scope security|privacy|security-and-privacy] [--risk-matrix FILE]
        Record the confirmed architecture lenses, methods, depth and risk matrix.
    phase WORKSPACE PHASE STATUS [--by NAME] [--note TEXT]
        Set a phase to not_started, in_progress, awaiting_review or complete.
    questions WORKSPACE
        Render 03-questions/workshop-questions.json to Markdown and CSV.
    build WORKSPACE MODEL_JSON OUTPUT_HTML [--pack] [--branding FILE]
        Assemble the report inputs from the workspace and build the HTML report,
        or the client validation pack with --pack.
    status WORKSPACE
        Show where the engagement is and what to do next.

Standard library only. Never touches the network, never executes material content,
never follows symlinks and never overwrites a report.
"""
import csv
import datetime
import hashlib
import html
import importlib.util
import io
import json
import os
import re
import stat
import sys
import zipfile

HERE = os.path.dirname(os.path.realpath(__file__))
LIBRARY_ROOT = os.path.dirname(os.path.dirname(HERE))
PHASES = ["intake", "plan", "questions", "workshops", "model", "validation", "report"]
STATUSES = ["not_started", "in_progress", "awaiting_review", "complete"]
FOLDERS = ["materials/design", "materials/diagrams", "materials/vendor", "materials/workshops", "materials/configuration",
           "materials/code", "materials/other", "materials/_text", "01-intake", "02-plan", "03-questions", "04-workshops",
           "06-validation", "07-final"]
CATEGORY = {"design": "design", "diagrams": "diagram", "vendor": "vendor", "workshops": "workshop",
            "configuration": "configuration", "code": "code", "other": "other"}
CATEGORY_LABEL = {"design": "Design documentation", "diagram": "Architecture diagram", "vendor": "Vendor documentation",
                  "workshop": "Workshop record", "configuration": "Configuration export", "code": "Code repository", "other": "Other"}
TEXT_NATIVE = {".txt", ".md", ".csv", ".json", ".yaml", ".yml", ".xml", ".tf", ".drawio", ".puml", ".mmd"}
AGENT_NATIVE = {".pdf", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
MAX_MEMBER = 50 * 1024 * 1024
MAX_TEXT = 20 * 1024 * 1024
NEXT = {
    "intake": "Add client material to materials/, run scan and extract, then ask the agent: /engagement intake",
    "plan": "Review 01-intake/initial-understanding.md, ask the agent: /engagement plan, then confirm it with engage.py plan",
    "questions": "With the plan confirmed, ask the agent: /engagement questions",
    "workshops": "Run the workshops, save each transcript or notes file in materials/workshops/, then: /engagement workshop",
    "model": "When the open questions that block modelling are answered: /engagement model",
    "validation": "Review the base model, build the validation pack (/engagement validation-pack), hold the client call, then: /engagement validate",
    "report": "Ask the agent: /engagement report, then review it against the checklist before issuing",
}


class Problem(Exception):
    pass


def today():
    return datetime.date.today().isoformat()


def inside(root, path):
    root = os.path.realpath(root)
    full = os.path.realpath(path)
    if full != root and not full.startswith(root + os.sep):
        raise Problem(f"{path} is outside the workspace")
    return full


def read_json(path, default=None):
    if not os.path.exists(path):
        if default is not None:
            return default
        raise Problem(f"{path} not found")
    st = os.lstat(path)
    if stat.S_ISLNK(st.st_mode) or not stat.S_ISREG(st.st_mode):
        raise Problem(f"{path} is not a regular file")
    with open(path, "r", encoding="utf-8") as fh:
        try:
            return json.load(fh)
        except json.JSONDecodeError as exc:
            raise Problem(f"{path}: {exc}") from None


def write_json(path, value):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(value, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    os.replace(tmp, path)


def load_state(ws):
    state = read_json(os.path.join(ws, "engagement.json"))
    if state.get("engagement_workspace_version") != "1.0":
        raise Problem("engagement.json is not an engagement workspace file")
    return state


def save_state(ws, state, event=None):
    if event:
        state.setdefault("log", []).append({"date": today(), "event": event})
    write_json(os.path.join(ws, "engagement.json"), state)


def options(argv, allowed, flags=()):
    """Split argv into positionals and --key value options."""
    positional, opts, i = [], {}, 0
    while i < len(argv):
        arg = argv[i]
        if arg.startswith("--"):
            key = arg[2:]
            if key in flags:
                opts[key] = True
            elif key in allowed and i + 1 < len(argv):
                opts[key] = argv[i + 1]
                i += 1
            else:
                raise Problem(f"unknown or incomplete option {arg}")
        else:
            positional.append(arg)
        i += 1
    return positional, opts


# ---------------------------------------------------------------- init

def cmd_init(argv):
    pos, opts = options(argv, {"client", "system", "project", "code"})
    if len(pos) != 1 or not opts.get("client") or not opts.get("system"):
        raise Problem("usage: init WORKSPACE --client NAME --system NAME [--project NAME] [--code none|partial|full]")
    ws = os.path.abspath(pos[0])
    code = opts.get("code", "none")
    if code not in ("none", "partial", "full"):
        raise Problem("--code must be none, partial or full")
    if os.path.exists(os.path.join(ws, "engagement.json")):
        raise Problem("this folder already holds an engagement")
    for folder in FOLDERS:
        os.makedirs(os.path.join(ws, folder), exist_ok=True)
    state = {
        "engagement_workspace_version": "1.0",
        "client": opts["client"], "system": opts["system"], "project": opts.get("project"),
        "created": today(), "code_access": code,
        "plan": {"architectures": [], "methods": [], "depth": None, "review_scope": "security",
                 "risk_matrix_file": None, "confirmed_by": None, "confirmed_on": None},
        "phases": {p: {"status": "not_started", "updated": None, "by": None, "note": None} for p in PHASES},
        "log": [],
    }
    save_state(ws, state, "Engagement workspace created")
    write_json(os.path.join(ws, "materials", "register.json"), {"register_version": "1.0", "materials": []})
    with open(os.path.join(ws, "materials", "README.txt"), "w", encoding="utf-8") as fh:
        fh.write("Put client material in the matching folder, then run engage.py scan and extract.\n\n"
                 "design/         architecture and design documents, security requirements, data flow descriptions\n"
                 "diagrams/       architecture, network and data-flow diagrams (PDF, PNG, SVG, VSDX, draw.io)\n"
                 "vendor/         third-party product documentation, security whitepapers, SOC 2 or ISO reports, contracts\n"
                 "workshops/      workshop and validation-call transcripts or notes (VTT, SRT, DOCX, TXT, MD)\n"
                 "configuration/  configuration exports and screenshots that show how something is actually set up\n"
                 "code/           one folder per repository copy, when source code is available\n"
                 "other/          anything else\n")
    print(f"created {ws}")
    print("next: " + NEXT["intake"])


# ---------------------------------------------------------------- scan

def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def git_revision(repo):
    """Read the checked-out commit without running git."""
    try:
        head = open(os.path.join(repo, ".git", "HEAD"), encoding="utf-8").read().strip()
        if head.startswith("ref: "):
            ref = os.path.join(repo, ".git", *head[5:].split("/"))
            if os.path.isfile(ref):
                return open(ref, encoding="utf-8").read().strip()[:12] + f" ({head[5:].split('/')[-1]})"
            return head[5:]
        return head[:12]
    except OSError:
        return None


def cmd_scan(argv):
    if len(argv) != 1:
        raise Problem("usage: scan WORKSPACE")
    ws = os.path.abspath(argv[0])
    load_state(ws)
    reg_path = os.path.join(ws, "materials", "register.json")
    register = read_json(reg_path, {"register_version": "1.0", "materials": []})
    items = register["materials"]
    by_file = {m["file"]: m for m in items}
    seen, added, changed = set(), [], []

    def next_id():
        nums = [int(m["id"][2:]) for m in items if re.fullmatch(r"M-\d+", m.get("id", ""))]
        return f"M-{(max(nums) if nums else 0) + 1:03d}"

    def record(rel, category, digest, size, version=None):
        seen.add(rel)
        entry = by_file.get(rel)
        if entry is None:
            entry = {"id": next_id(), "file": rel, "category": category,
                     "title": os.path.splitext(os.path.basename(rel))[0].replace("_", " ").replace("-", " "),
                     "version": version, "date": None, "source": None, "sha256": digest, "bytes": size,
                     "added": today(), "text_file": None, "read": "not_read", "notes": "", "status": "current"}
            items.append(entry)
            by_file[rel] = entry
            added.append(entry)
        elif entry.get("sha256") != digest:
            entry.update({"sha256": digest, "bytes": size, "status": "changed", "read": "not_read"})
            if version:
                entry["version"] = version
            changed.append(entry)
        elif entry.get("status") == "missing":
            entry["status"] = "current"

    mat = os.path.join(ws, "materials")
    for top in sorted(os.listdir(mat)):
        folder = os.path.join(mat, top)
        if top.startswith("_") or not os.path.isdir(folder) or os.path.islink(folder):
            continue
        category = CATEGORY.get(top, "other")
        if category == "code":
            for repo in sorted(os.listdir(folder)):
                full = os.path.join(folder, repo)
                if os.path.isdir(full) and not os.path.islink(full):
                    rev = git_revision(full)
                    record(f"materials/code/{repo}", "code", rev or "unversioned", 0, rev)
            continue
        for base, dirs, files in os.walk(folder):
            dirs[:] = sorted(d for d in dirs if not os.path.islink(os.path.join(base, d)))
            for name in sorted(files):
                full = os.path.join(base, name)
                st = os.lstat(full)
                if stat.S_ISLNK(st.st_mode) or not stat.S_ISREG(st.st_mode) or name.startswith("."):
                    continue
                rel = os.path.relpath(full, ws).replace(os.sep, "/")
                record(rel, category, sha256(full), st.st_size)
    for entry in items:
        if entry["file"] not in seen and entry.get("status") != "missing":
            entry["status"] = "missing"
    write_json(reg_path, register)
    print(f"{len(items)} materials registered: {len(added)} new, {len(changed)} changed")
    for entry in added + changed:
        print(f"  {entry['id']}  {entry['category']:<13} {entry['file']}  [{entry['status']}]")
    missing = [m for m in items if m.get("status") == "missing"]
    for entry in missing:
        print(f"  {entry['id']}  missing: {entry['file']}")
    untitled = [m["id"] for m in items if not m.get("version") or not m.get("date")]
    if untitled:
        print("fill in version and date in materials/register.json for: " + ", ".join(untitled[:20]))


# ---------------------------------------------------------------- extract

TAG = re.compile(r"<[^>]+>")


def zip_text(path, pattern):
    """Return (member name, xml text) pairs for members matching pattern, with size caps."""
    out = []
    with zipfile.ZipFile(path) as zf:
        infos = zf.infolist()
        if len(infos) > 5000:
            raise Problem("archive has too many members")
        names = [i for i in infos if re.fullmatch(pattern, i.filename)]

        def order(info):
            m = re.search(r"(\d+)\.xml$", info.filename)
            return int(m.group(1)) if m else 0

        for info in sorted(names, key=order):
            if info.file_size > MAX_MEMBER:
                raise Problem(f"{info.filename} is too large")
            out.append((info.filename, zf.read(info).decode("utf-8", "replace")))
    return out


def paragraphs(xml, para_end, run_pattern):
    lines = []
    for chunk in re.split(para_end, xml):
        text = "".join(html.unescape(TAG.sub("", m)) for m in re.findall(run_pattern, chunk, flags=re.S))
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            lines.append(text)
    return lines


def number(member):
    return re.search(r"(\d+)", member.split("/")[-1]).group(1)


def extract_docx(path):
    lines = []
    for _, xml in zip_text(path, r"word/document\.xml"):
        xml = re.sub(r"<w:tab\s*/>", "<w:t>\t</w:t>", xml)

        def row(match):
            cells = []
            for cell in re.findall(r"<w:tc[ >].*?</w:tc>", match.group(0), flags=re.S):
                cells.append(" ".join(paragraphs(cell, r"</w:p>", r"<w:t(?:\s[^>]*)?>(.*?)</w:t>")))
            return "<w:p><w:r><w:t>" + html.escape(" | ".join(cells)) + "</w:t></w:r></w:p>"

        xml = re.sub(r"<w:tr[ >].*?</w:tr>", row, xml, flags=re.S)
        lines += paragraphs(xml, r"</w:p>", r"<w:t(?:\s[^>]*)?>(.*?)</w:t>")
    return lines


def extract_pptx(path):
    lines = []
    for name, xml in zip_text(path, r"ppt/slides/slide\d+\.xml"):
        lines.append("## Slide " + number(name))
        lines += paragraphs(xml, r"</a:p>", r"<a:t(?:\s[^>]*)?>(.*?)</a:t>")
    for name, xml in zip_text(path, r"ppt/notesSlides/notesSlide\d+\.xml"):
        notes = paragraphs(xml, r"</a:p>", r"<a:t(?:\s[^>]*)?>(.*?)</a:t>")
        if notes:
            lines.append("## Notes " + number(name))
            lines += notes
    return lines


def extract_vsdx(path):
    lines = ["(Shape text only. Connectors, arrows and layout are not captured: read an image or PDF export of the diagram as well.)"]
    for name, xml in zip_text(path, r"visio/pages/page\d+\.xml"):
        lines.append("## Page " + number(name))
        for m in re.findall(r"<Text(?:\s[^>]*)?>(.*?)</Text>", xml, flags=re.S):
            text = re.sub(r"\s+", " ", html.unescape(TAG.sub("", m))).strip()
            if text:
                lines.append("- " + text)
    return lines


STAMP = re.compile(r"(\d{1,2}:)?\d{1,2}:\d{2}[.,]\d{1,3}\s*-->\s*\S+")


def extract_captions(path):
    """WebVTT or SRT to '[time] Speaker: text' lines, merging consecutive cues from one speaker."""
    with open(path, "r", encoding="utf-8-sig", errors="replace") as fh:
        raw = fh.read(MAX_TEXT)
    lines, time, speaker, buf, last = [], None, None, [], None

    def flush():
        nonlocal buf, last
        text = re.sub(r"\s+", " ", " ".join(buf)).strip()
        if text:
            if speaker and speaker == last and lines:
                lines[-1] += " " + text
            else:
                lines.append(f"[{time}] {speaker + ': ' if speaker else ''}{text}")
                last = speaker
        buf = []

    for line in raw.splitlines():
        line = line.strip()
        if STAMP.search(line):
            flush()
            time = line.split("-->")[0].strip().split(".")[0].split(",")[0]
            speaker = None
            continue
        if not line or line.upper().startswith("WEBVTT") or line.isdigit() or line.startswith(("NOTE", "STYLE")) or re.fullmatch(r"[0-9a-f-]{8,}(/\d+-\d+)?", line):
            continue
        voice = re.match(r"<v\s+([^>]+)>(.*)", line)
        if voice:
            speaker, line = voice.group(1).strip(), voice.group(2)
        elif time and not buf and re.match(r"^[A-Z][\w .'-]{1,40}:\s", line):
            speaker, line = line.split(":", 1)[0].strip(), line.split(":", 1)[1]
        buf.append(html.unescape(TAG.sub("", line)))
    flush()
    return lines


EXTRACTORS = {".docx": extract_docx, ".pptx": extract_pptx, ".vsdx": extract_vsdx, ".vtt": extract_captions, ".srt": extract_captions}


def cmd_extract(argv):
    if len(argv) != 1:
        raise Problem("usage: extract WORKSPACE")
    ws = os.path.abspath(argv[0])
    reg_path = os.path.join(ws, "materials", "register.json")
    register = read_json(reg_path)
    done, native, skipped = 0, [], []
    for entry in register["materials"]:
        if entry.get("status") == "missing" or entry["category"] == "code":
            continue
        ext = os.path.splitext(entry["file"])[1].lower()
        source = inside(ws, os.path.join(ws, entry["file"]))
        if ext in TEXT_NATIVE:
            entry["text_file"] = entry["file"]
        elif ext in AGENT_NATIVE:
            entry["text_file"] = None
            native.append(entry)
        elif ext in EXTRACTORS:
            target_rel = f"materials/_text/{entry['id']}-{re.sub(r'[^A-Za-z0-9._-]+', '_', os.path.basename(entry['file']))}.txt"
            target = os.path.join(ws, target_rel)
            if entry.get("text_file") == target_rel and os.path.exists(target) and entry.get("status") != "changed":
                continue
            try:
                lines = EXTRACTORS[ext](source)
            except (zipfile.BadZipFile, KeyError, OSError, Problem) as exc:
                skipped.append((entry, str(exc)))
                continue
            text = "\n".join(lines)[:MAX_TEXT]
            with open(target, "w", encoding="utf-8") as fh:
                fh.write(text + "\n")
            entry["text_file"] = target_rel
            if entry.get("status") == "changed":
                entry["status"] = "current"
            done += 1
            print(f"  {entry['id']}  {len(lines):>5} lines  {target_rel}")
        else:
            skipped.append((entry, "no extractor for this file type; export it to PDF, DOCX or text"))
    write_json(reg_path, register)
    print(f"extracted {done} file(s)")
    if native:
        print("read directly by the agent (PDF or image): " + ", ".join(e["id"] for e in native))
    for entry, why in skipped:
        print(f"  {entry['id']}  not extracted: {entry['file']} ({why})")


# ---------------------------------------------------------------- plan, phase, status

def library_ids(folder):
    path = os.path.join(LIBRARY_ROOT, folder)
    return sorted(os.path.splitext(n)[0] for n in os.listdir(path) if n.endswith(".md") and n != "README.md")


def cmd_plan(argv):
    pos, opts = options(argv, {"architectures", "methods", "depth", "scope", "risk-matrix", "by"})
    if len(pos) != 1 or not opts.get("architectures") or not opts.get("depth") or not opts.get("by"):
        raise Problem("usage: plan WORKSPACE --architectures a,b --methods m1,m2 --depth quick|deep --by NAME [--scope ...] [--risk-matrix FILE]")
    ws = os.path.abspath(pos[0])
    state = load_state(ws)
    archs = [a.strip() for a in opts["architectures"].split(",") if a.strip()]
    methods = [m.strip() for m in opts.get("methods", "").split(",") if m.strip()]
    known_a, known_m = library_ids("quick"), library_ids("methods")
    bad = [a for a in archs if a not in known_a] + [m for m in methods if m not in known_m]
    if bad:
        raise Problem("not in the library: " + ", ".join(bad) + "\n  architectures: " + ", ".join(known_a) + "\n  methods: " + ", ".join(known_m))
    if opts["depth"] not in ("quick", "deep"):
        raise Problem("--depth must be quick or deep")
    scope = opts.get("scope", "security")
    if scope not in ("security", "privacy", "security-and-privacy"):
        raise Problem("--scope must be security, privacy or security-and-privacy")
    matrix = opts.get("risk-matrix")
    if matrix:
        full = inside(ws, os.path.join(ws, matrix))
        read_json(full)
        matrix = os.path.relpath(full, ws).replace(os.sep, "/")
    state["plan"] = {"architectures": archs, "methods": methods, "depth": opts["depth"], "review_scope": scope,
                     "risk_matrix_file": matrix, "confirmed_by": opts["by"], "confirmed_on": today()}
    state["phases"]["plan"].update({"status": "complete", "updated": today(), "by": opts["by"]})
    save_state(ws, state, f"Plan confirmed by {opts['by']}: {', '.join(archs)}; methods {', '.join(methods) or 'none'}; {opts['depth']}")
    print("plan recorded")
    if not matrix:
        print("note: no risk matrix recorded, so threats will not be rated. Copy the client's matrix into the workspace and rerun with --risk-matrix.")


def cmd_phase(argv):
    pos, opts = options(argv, {"by", "note"})
    if len(pos) != 3 or pos[1] not in PHASES or pos[2] not in STATUSES:
        raise Problem(f"usage: phase WORKSPACE {{{'|'.join(PHASES)}}} {{{'|'.join(STATUSES)}}} [--by NAME] [--note TEXT]")
    ws = os.path.abspath(pos[0])
    state = load_state(ws)
    if pos[2] == "complete" and not opts.get("by"):
        raise Problem("a phase is completed by a named consultant: add --by NAME")
    state["phases"][pos[1]].update({"status": pos[2], "updated": today(), "by": opts.get("by"), "note": opts.get("note")})
    save_state(ws, state, f"{pos[1]} set to {pos[2]}" + (f" by {opts['by']}" if opts.get("by") else ""))
    print(f"{pos[1]}: {pos[2]}")


def cmd_status(argv):
    if len(argv) != 1:
        raise Problem("usage: status WORKSPACE")
    ws = os.path.abspath(argv[0])
    state = load_state(ws)
    register = read_json(os.path.join(ws, "materials", "register.json"), {"materials": []})
    cats = {}
    for m in register["materials"]:
        if m.get("status") != "missing":
            cats[m["category"]] = cats.get(m["category"], 0) + 1
    plan = state["plan"]
    print(f"{state['client']} / {state['system']}  (code access: {state['code_access']})")
    print("materials: " + (", ".join(f"{n} {c}" for c, n in sorted(cats.items())) or "none registered"))
    print("plan: " + (f"{', '.join(plan['architectures'])}; methods {', '.join(plan['methods']) or 'none'}; {plan['depth']}; "
                      f"risk matrix {plan['risk_matrix_file'] or 'not set'}; confirmed by {plan['confirmed_by']}" if plan["confirmed_by"] else "not confirmed"))
    qpath = os.path.join(ws, "03-questions", "workshop-questions.json")
    if os.path.exists(qpath):
        qs = read_json(qpath).get("questions", [])
        counts = {}
        for q in qs:
            counts[q.get("status", "open")] = counts.get(q.get("status", "open"), 0) + 1
        print("questions: " + ", ".join(f"{n} {s}" for s, n in sorted(counts.items())))
    nxt = None
    for p in PHASES:
        info = state["phases"][p]
        print(f"  {p:<11} {info['status']:<16} {info.get('updated') or '':<11} {info.get('by') or ''}")
        if nxt is None and info["status"] != "complete":
            nxt = p
    print("next: " + (NEXT[nxt] if nxt else "all phases complete"))


# ---------------------------------------------------------------- questions

def cmd_questions(argv):
    if len(argv) != 1:
        raise Problem("usage: questions WORKSPACE")
    ws = os.path.abspath(argv[0])
    state = load_state(ws)
    folder = os.path.join(ws, "03-questions")
    data = read_json(os.path.join(folder, "workshop-questions.json"))
    questions = data.get("questions", [])
    for q in questions:
        if not re.fullmatch(r"Q-\d{3}", str(q.get("id", ""))) or not q.get("question"):
            raise Problem("every question needs an id like Q-001 and question text")
    order = {"must": 0, "should": 1, "could": 2}
    sessions = []
    for q in questions:
        if q.get("session", "General") not in sessions:
            sessions.append(q.get("session", "General"))
    md = [f"# Workshop questions: {state['client']}, {state['system']}", ""]
    if data.get("summary"):
        md += [str(data["summary"]), ""]
    open_n = sum(1 for q in questions if q.get("status", "open") == "open")
    md += [f"{len(questions)} questions, {open_n} open. Priority: **must** blocks the threat model, **should** changes a finding, **could** adds detail.", ""]
    for session in sessions:
        rows = sorted((q for q in questions if q.get("session", "General") == session), key=lambda q: (order.get(q.get("priority"), 3), q["id"]))
        audience = sorted({q["audience"] for q in rows if q.get("audience")})
        md += [f"## {session}", ""]
        if audience:
            md += ["Who should attend: " + ", ".join(audience), ""]
        for q in rows:
            mark = {"answered": "[x]", "partly": "[~]"}.get(q.get("status", "open"), "[ ]")
            md.append(f"- {mark} **{q['id']}** ({q.get('priority', 'should')}) {q['question']}")
            if q.get("why"):
                md.append(f"  - Why it matters: {q['why']}")
            if q.get("listen_for"):
                md.append(f"  - Listen for: {q['listen_for']}")
            if q.get("refs"):
                md.append(f"  - Relates to: {', '.join(q['refs'])}")
            if q.get("answer"):
                md.append(f"  - Answer ({q.get('answered_in', 'recorded')}): {q['answer']}")
        md.append("")
    with open(os.path.join(folder, "workshop-questions.md"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(md))
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["ID", "Session", "Audience", "Priority", "Question", "Why it matters", "Listen for", "Relates to", "Status", "Answer"])
    for q in questions:
        row = [q["id"], q.get("session", "General"), q.get("audience", ""), q.get("priority", "should"), q["question"], q.get("why", ""),
               q.get("listen_for", ""), " ".join(q.get("refs", [])), q.get("status", "open"), q.get("answer", "")]
        writer.writerow([("'" + c if isinstance(c, str) and c[:1] in "=+-@\t" else c) for c in row])
    with open(os.path.join(folder, "workshop-questions.csv"), "w", encoding="utf-8-sig", newline="") as fh:
        fh.write(buf.getvalue())
    print(f"wrote 03-questions/workshop-questions.md and .csv ({len(questions)} questions, {open_n} open)")


# ---------------------------------------------------------------- build

NARRATIVE_KEYS = {"title", "subtitle", "report_version", "report_date", "report_status", "authors", "executive_summary",
                  "scope_and_approach", "records", "assumptions", "document_control", "review_triggers", "test_plan", "options"}


def names(people):
    out = []
    for p in people or []:
        if isinstance(p, dict):
            bits = [p.get("name"), p.get("role"), p.get("organisation")]
            out.append(", ".join(b for b in bits if b))
        elif p:
            out.append(str(p))
    return out


def report_inputs(ws, pack):
    state = load_state(ws)
    register = read_json(os.path.join(ws, "materials", "register.json"), {"materials": []})
    narrative = read_json(os.path.join(ws, "07-final", "narrative.json"), {})
    unknown = set(narrative) - NARRATIVE_KEYS
    if unknown:
        raise Problem(f"07-final/narrative.json has keys the report does not use: {sorted(unknown)}")
    eng = {"engagement_version": "1.0", "client": state["client"], "project": state.get("project") or state["system"],
           "title": f"{state['system']} threat model", "code_access": state["code_access"]}
    eng.update(narrative)
    eng["artefacts"] = [{
        "id": m["id"], "name": m.get("title") or m["file"], "type": CATEGORY_LABEL.get(m["category"], "Other"), "category": m["category"],
        "version": m.get("version"), "date": m.get("date"), "source": m.get("source"), "notes": m.get("notes") or None,
        "file": m["file"], "text_file": m.get("text_file"), "reviewed": m.get("read", "not_read")}
        for m in register["materials"] if m.get("status") != "missing"]
    workshops = []
    wdir = os.path.join(ws, "04-workshops")
    for name in sorted(os.listdir(wdir)) if os.path.isdir(wdir) else []:
        if name.endswith(".json"):
            w = read_json(os.path.join(wdir, name))
            workshops.append({"date": w.get("date"), "title": w.get("title"), "attendees": names(w.get("attendees")),
                              "purpose": w.get("purpose"), "outcomes": [str(o) for o in w.get("outcomes", [])]})
    eng["workshops"] = workshops
    vpath = os.path.join(ws, "06-validation", "validation.json")
    if os.path.exists(vpath) and not pack:
        v = read_json(vpath)
        eng["validation"] = {
            "sessions": [{"date": s.get("date"), "title": s.get("title"), "attendees": names(s.get("attendees"))} for s in v.get("sessions", [])],
            "items": [{"ref": i.get("ref"), "outcome": i.get("outcome"), "note": i.get("note")} for i in v.get("items", [])]}
    matrix = state["plan"].get("risk_matrix_file")
    if matrix:
        eng["risk_matrix"] = read_json(inside(ws, os.path.join(ws, matrix)))
    if pack:
        opts = dict(eng.get("options") or {})
        opts["pack"] = "validation"
        eng["options"] = opts
        eng["report_status"] = "Draft for validation"
    return eng


def model_ids(path):
    """Record ids present in a model envelope, found without assuming its exact shape."""
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError):
        return set()
    found = set()

    def walk(node):
        if isinstance(node, dict):
            if isinstance(node.get("id"), str):
                found.add(node["id"])
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)
    walk(data)
    return found


def cmd_build(argv):
    pos, opts = options(argv, {"branding"}, flags=("pack",))
    if len(pos) != 3:
        raise Problem("usage: build WORKSPACE MODEL_JSON OUTPUT_HTML [--pack] [--branding FILE]")
    ws = os.path.abspath(pos[0])
    model, out = os.path.abspath(pos[1]), os.path.abspath(pos[2])
    inside(ws, model)
    inside(ws, out)
    eng = report_inputs(ws, bool(opts.get("pack")))
    if opts.get("pack"):
        eng.pop("test_plan", None)
    if opts.get("pack") and isinstance(eng.get("records"), dict):
        # The pack describes the draft model, so drop annotations for records it does not hold.
        ids = model_ids(model)
        if ids:
            eng["records"] = {k: v for k, v in eng["records"].items() if k in ids}
    eng_path = re.sub(r"\.html$", "", out) + ".engagement.json"
    if os.path.exists(eng_path) or os.path.exists(out):
        raise Problem(f"{os.path.basename(out)} or its engagement file already exists; choose a new name")
    write_json(eng_path, eng)
    spec = importlib.util.spec_from_file_location("tm_fill", os.path.join(LIBRARY_ROOT, "reporting", "fill.py"))
    fill = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fill)
    branding = opts.get("branding") or os.path.join(LIBRARY_ROOT, "reporting", "branding", "default.json")
    code = fill.main(["fill.py", model, eng_path, branding, out])
    if code != 0:
        os.remove(eng_path)
        raise Problem("the report was not built; fix the problem above and run build again")
    print(f"inputs: {eng_path}")


COMMANDS = {"init": cmd_init, "scan": cmd_scan, "extract": cmd_extract, "plan": cmd_plan, "phase": cmd_phase,
            "status": cmd_status, "questions": cmd_questions, "build": cmd_build}


def main(argv):
    if len(argv) < 2 or argv[1] not in COMMANDS:
        print(__doc__.strip(), file=sys.stderr)
        return 2
    try:
        COMMANDS[argv[1]](argv[2:])
    except Problem as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
