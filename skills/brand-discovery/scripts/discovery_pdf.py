"""Client discovery PDF kit (optional part of brand-discovery).

    python discovery_pdf.py build questions.json --agency profile.json --out client-discovery-v1.pdf
    python discovery_pdf.py read returned.pdf --questions questions.json --out answers.json
    python discovery_pdf.py answers-template questions.json --out answers.json

`build` makes a branded, fillable PDF from the same questions the operator would
ask by text or on a call. `read` turns a returned copy back into answers and
flags blanks, conflicts and flattened copies. `answers-template` writes the same
answers file, empty, for answers collected by text or call (provenance
"transcribed").

Needs reportlab and pypdf (requirements.txt); the rest of the pipeline does not.
Nothing here sends, hosts or uploads anything: the operator sends the PDF
through their own channel and reads the returned copy locally. Keep agency
profiles, questions, returned PDFs and answers out of public repositories.
"""
import argparse
import datetime as dt
import json
import pathlib
import sys

TEXT = {
    "en": {
        "prepared_for": "Prepared for",
        "how_title": "How to fill this in",
        "how": [
            "Open this file in Adobe Acrobat Reader (free) or your phone's Files app. A browser or email preview may not save your answers.",
            "Tap or type your answers. Skip anything you're unsure of; \"Not sure\" is a fine answer.",
            "Save, then send the file back{contact}. Photos, logos and examples go in the same reply as attachments, not inside this file.",
        ],
        "other": "Other",
        "other_hint": "Tell us",
        "not_sure": "Not sure, help me choose",
        "note": "Anything to add? (optional)",
        "pick_one": "Pick one.",
        "pick_up_to": "Pick up to {n}.",
        "pick_any": "Pick any that apply.",
        "page": "Page {n}",
        "version": "Version {v}",
        "reply_to": " to {who}",
    },
    "es": {
        "prepared_for": "Preparado para",
        "how_title": "Cómo llenarlo",
        "how": [
            "Abre este archivo en Adobe Acrobat Reader (gratis) o en la app Archivos de tu teléfono. La vista previa del navegador o del correo puede no guardar tus respuestas.",
            "Toca o escribe tus respuestas. Si no estás seguro, \"No estoy seguro\" también es una buena respuesta.",
            "Guarda el archivo y mándalo de regreso{contact}. Fotos, logos y ejemplos van en el mismo mensaje como archivos adjuntos, no dentro de este archivo.",
        ],
        "other": "Otro",
        "other_hint": "Cuéntanos",
        "not_sure": "No estoy seguro, ayúdenme a elegir",
        "note": "¿Algo más que agregar? (opcional)",
        "pick_one": "Elige una.",
        "pick_up_to": "Elige hasta {n}.",
        "pick_any": "Elige las que apliquen.",
        "page": "Página {n}",
        "version": "Versión {v}",
        "reply_to": " a {who}",
    },
}

DEFAULT_COLORS = {"ink": "#121212", "muted": "#555555", "accent": "#121212", "line": "#C9C9C9", "paper": "#FFFFFF"}


def load_json(path):
    return json.loads(pathlib.Path(path).read_text(encoding="utf-8"))


def text_for(locale):
    return TEXT.get((locale or "en")[:2], TEXT["en"])


def _circle_arc_stream(size, r, arcs=(0, 1, 2, 3), rotated=False):
    """Radio-button circle for reportlab's appearance streams. reportlab's own
    version scales by size/20, so any radio not 20pt wide is drawn small in the
    corner of its box in every viewer that uses the stored appearance."""
    num = lambda v: f"{v:.4f}".rstrip("0").rstrip(".")
    h, cp, r = num(size * 0.5), num(0.55231 * r), num(r)
    out = [f"{'0.7071 0.7071 -0.7071 0.7071' if rotated else '1 0 0 1'} {h} {h} cm"]
    segments = {
        0: (f"{r} 0 m", f"{r} {cp} {cp} {r} 0 {r} c"),
        1: (f"0 {r} m", f"-{cp} {r} -{r} {cp} -{r} 0 c"),
        2: (f"-{r} 0 m", f"-{r} -{cp} -{cp} -{r} 0 -{r} c"),
        3: (f"0 -{r} m", f"{cp} -{r} {r} -{cp} {r} 0 c"),
    }
    for arc in (0, 1, 2, 3):
        if arc in arcs:
            move, curve = segments[arc]
            if len(out) == 1:
                out.append(move)
            out.append(curve)
    return "\n".join(out)


# ---------------------------------------------------------------- build


def build(questions_path, agency_path, out_path):
    from reportlab.lib.colors import HexColor
    from reportlab.lib.pagesizes import A4, LETTER
    from reportlab.lib.utils import ImageReader, simpleSplit
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas

    spec = load_json(questions_path)
    agency = load_json(agency_path) if agency_path else {}
    t = text_for(spec.get("locale"))
    warnings = []

    colors = {k: HexColor(v) for k, v in {**DEFAULT_COLORS, **(agency.get("colors") or {})}.items()}
    page_w, page_h = A4 if str(spec.get("page_size", "letter")).lower() == "a4" else LETTER
    margin = 54
    width = page_w - 2 * margin

    # Brand fonts are optional; the standard fonts cover English and Spanish.
    regular, bold = "Helvetica", "Helvetica-Bold"
    fonts = agency.get("fonts") or {}
    for key, fallback in (("regular", regular), ("bold", bold)):
        path = fonts.get(key)
        if not path:
            continue
        try:
            pdfmetrics.registerFont(TTFont(f"Brand-{key}", path))
            if key == "regular":
                regular = "Brand-regular"
            else:
                bold = "Brand-bold"
        except Exception as exc:  # unreadable or not a TrueType file
            warnings.append(f"font {key} not used ({exc}); using {fallback}")

    # Logo: a readable PNG or JPG, else the agency name set in type.
    logo = None
    logo_path = ((agency.get("logo") or {}).get("primary")) if agency else None
    if logo_path:
        p = pathlib.Path(logo_path)
        if not p.exists():
            warnings.append(f"logo not found at {p}; using the agency name in type")
        elif p.suffix.lower() not in (".png", ".jpg", ".jpeg"):
            warnings.append(f"logo {p.name} is not PNG or JPG; using the agency name in type")
        else:
            try:
                logo = ImageReader(str(p))
            except Exception as exc:
                warnings.append(f"logo {p.name} could not be read ({exc}); using the agency name in type")

    agency_name = agency.get("name") or "Discovery"
    contact = agency.get("contact") or {}
    reply_who = contact.get("email") or contact.get("instagram") or contact.get("phone")
    client = spec.get("client") or {}
    version = spec.get("version", 1)
    date = spec.get("date") or dt.date.today().isoformat()

    c = canvas.Canvas(str(out_path), pagesize=(page_w, page_h))
    c.setTitle(f"{spec.get('title', 'Questions')} · {client.get('name', '')}".strip(" ·"))
    c.setAuthor(agency_name)
    c.setSubject("Client discovery questionnaire")
    form = c.acroForm
    form.circleArcStream = _circle_arc_stream  # this form only; see the function
    state = {"page": 1, "y": page_h - margin}

    def footer():
        c.setFont(regular, 8.5)
        c.setFillColor(colors["muted"])
        bits = [agency_name] + [v for v in (contact.get("website"), contact.get("email"), contact.get("instagram"), contact.get("phone")) if v]
        c.drawString(margin, margin - 22, "  ·  ".join(bits))
        c.drawRightString(page_w - margin, margin - 22, t["page"].format(n=state["page"]))

    def new_page():
        footer()
        c.showPage()
        state["page"] += 1
        state["y"] = page_h - margin

    def ensure(height):
        if state["y"] - height < margin + 10:
            new_page()

    def para(text, font, size, color, leading=None, indent=0, w=None):
        leading = leading or size * 1.35
        lines = simpleSplit(text, font, size, (w or width) - indent)
        c.setFont(font, size)
        c.setFillColor(color)
        for line in lines:
            c.drawString(margin + indent, state["y"] - size, line)
            state["y"] -= leading
        return len(lines) * leading

    def measure(text, font, size, w, leading=None):
        return len(simpleSplit(text, font, size, w)) * (leading or size * 1.35)

    # Header: agency mark left, client and version right, then an accent rule.
    top = state["y"]
    if logo:
        iw, ih = logo.getSize()
        h = 30
        w = min(iw * h / ih, width * 0.45)
        c.drawImage(logo, margin, top - h, width=w, height=w * ih / iw, mask="auto")
    else:
        c.setFont(bold, 12)
        c.setFillColor(colors["ink"])
        c.drawString(margin, top - 18, agency_name.upper())
    c.setFont(regular, 9)
    c.setFillColor(colors["muted"])
    if client.get("name"):
        c.drawRightString(page_w - margin, top - 10, f"{t['prepared_for']} {client['name']}")
    c.drawRightString(page_w - margin, top - 23, f"{t['version'].format(v=version)} · {date}")
    state["y"] = top - 44
    c.setStrokeColor(colors["accent"])
    c.setLineWidth(2)
    c.line(margin, state["y"], margin + 48, state["y"])
    state["y"] -= 26

    para(spec.get("title", "A few questions before we design"), bold, 22, colors["ink"], leading=27)
    state["y"] -= 6
    if spec.get("intro"):
        para(spec["intro"], regular, 11, colors["ink"], leading=15.5)
        state["y"] -= 10

    # How to fill it in, in a light box.
    contact_txt = t["reply_to"].format(who=reply_who) if reply_who else ""
    steps = [s.format(contact=contact_txt) for s in t["how"]]
    # 14 top padding + 18 title row + each step + 12 bottom padding.
    box_h = 44 + sum(measure(f"{i + 1}.  {s}", regular, 9.5, width - 28, 13) + 3 for i, s in enumerate(steps))
    ensure(box_h + 10)
    c.setFillColor(HexColor("#F4F4F4"))
    c.setStrokeColor(colors["line"])
    c.setLineWidth(0.6)
    c.roundRect(margin, state["y"] - box_h, width, box_h, 6, stroke=1, fill=1)
    state["y"] -= 14
    c.setFont(bold, 10)
    c.setFillColor(colors["ink"])
    c.drawString(margin + 14, state["y"] - 10, t["how_title"])
    state["y"] -= 18
    for i, s in enumerate(steps):
        para(f"{i + 1}.  {s}", regular, 9.5, colors["ink"], leading=13, indent=14, w=width - 14)
        state["y"] -= 3
    state["y"] -= 30

    def widget_style():
        return dict(borderColor=colors["ink"], fillColor=colors["paper"], textColor=colors["ink"], forceBorder=True, borderWidth=1)

    def text_box(name, tooltip, lines, x=None, w=None):
        h = 14 + 13 * max(1, lines - 1) if lines > 1 else 20
        ensure(h + 6)
        form.textfield(
            name=name, tooltip=tooltip, value="", x=x or margin, y=state["y"] - h, width=w or width, height=h,
            fontName="Helvetica", fontSize=10, fieldFlags="multiline" if lines > 1 else "",
            borderStyle="solid", borderColor=colors["line"], fillColor=colors["paper"], textColor=colors["ink"], forceBorder=True,
        )
        state["y"] -= h + 6

    for n, q in enumerate(spec.get("questions", []), start=1):
        qid, qtype = q["id"], q.get("type", "single")
        options = list(q.get("options", []))
        if q.get("not_sure", qtype != "text"):
            options.append({"value": "not_sure", "label": t["not_sure"]})
        has_other = q.get("other", qtype != "text")
        if has_other:
            options.append({"value": "other", "label": t["other"]})

        hint = q.get("help") or (
            t["pick_one"] if qtype == "single" else t["pick_up_to"].format(n=q["max"]) if q.get("max") else t["pick_any"] if qtype == "multi" else ""
        )
        head_h = measure(f"{n}.  {q['prompt']}", bold, 12.5, width, 16.5) + (measure(hint, regular, 9.5, width, 13) if hint else 0)
        first_row = 22 if qtype != "text" else 26
        ensure(head_h + first_row + 8)
        para(f"{n}.  {q['prompt']}", bold, 12.5, colors["ink"], leading=16.5)
        if hint:
            state["y"] -= 2
            para(hint, regular, 9.5, colors["muted"], leading=13)
        state["y"] -= 6

        if qtype == "text":
            text_box(f"q.{qid}", q["prompt"], q.get("lines", 3))
        else:
            for opt in options:
                label = opt["label"]
                label_w = width - 24 - (190 if opt["value"] == "other" else 0)
                lines = simpleSplit(label, regular, 10.5, label_w)
                row_h = max(20, len(lines) * 14 + 6)
                ensure(row_h)
                box_y = state["y"] - 15
                tip = f"{q['prompt']} {label}"
                if qtype == "single":
                    form.radio(name=f"q.{qid}", tooltip=tip, value=opt["value"], selected=False, x=margin, y=box_y,
                               size=12, buttonStyle="circle", shape="circle", **widget_style())
                else:
                    form.checkbox(name=f"q.{qid}.{opt['value']}", tooltip=tip, x=margin, y=box_y, size=12,
                                  checked=False, buttonStyle="check", shape="square", **widget_style())
                c.setFont(regular, 10.5)
                c.setFillColor(colors["ink"])
                for i, line in enumerate(lines):
                    c.drawString(margin + 20, box_y + 2.5 - i * 14, line)
                if opt["value"] == "other":
                    form.textfield(name=f"q.{qid}.other_text", tooltip=f"{q['prompt']} {t['other']}: {t['other_hint']}", value="",
                                   x=margin + width - 190, y=box_y - 3, width=190, height=18, fontName="Helvetica", fontSize=10,
                                   borderStyle="underlined", borderColor=colors["line"], fillColor=colors["paper"],
                                   textColor=colors["ink"], forceBorder=True)
                state["y"] -= row_h
            if q.get("note", False):
                state["y"] -= 2
                ensure(14 + 34)
                para(t["note"], regular, 9.5, colors["muted"], leading=13)
                text_box(f"q.{qid}.note", f"{q['prompt']} {t['note']}", 2)
        for link in q.get("links", []):
            ensure(16)
            c.setFont(regular, 9.5)
            c.setFillColor(colors["accent"])
            label = link.get("label") or link["url"]
            c.drawString(margin, state["y"] - 10, label)
            c.linkURL(link["url"], (margin, state["y"] - 13, margin + c.stringWidth(label, regular, 9.5), state["y"]), relative=0)
            state["y"] -= 16
        state["y"] -= 16

    footer()
    c.save()
    return warnings


# ---------------------------------------------------------------- read


def _name(value):
    if value is None:
        return None
    s = str(value)
    return s[1:] if s.startswith("/") else s


def _pdf_values(pdf_path):
    """Field name -> value, reading both field values and widget states,
    because viewers differ in which one they update."""
    from pypdf import PdfReader

    reader = PdfReader(str(pdf_path))
    fields = reader.get_fields() or {}
    values = {}
    for name, field in fields.items():
        values[name] = field.get("/V")
    for page in reader.pages:
        for ref in page.get("/Annots") or []:
            annot = ref.get_object()
            if annot.get("/Subtype") != "/Widget":
                continue
            parent = annot.get("/Parent")
            parent = parent.get_object() if parent is not None else None
            name = annot.get("/T") or (parent.get("/T") if parent is not None else None)
            state = annot.get("/AS")
            if name is None or state is None or _name(state) == "Off":
                continue
            if values.get(name) in (None, "", "/Off"):
                values[name] = state
    return values, bool(fields)


def blank_answers(spec, provenance):
    return {
        "questions_version": spec.get("version", 1),
        "provenance": provenance,
        "status": "empty",
        "answers": {q["id"]: {"type": q.get("type", "single"), "value": None, "values": [], "other_text": "", "note": "", "state": "blank"} for q in spec.get("questions", [])},
        "flags": [],
    }


def read(pdf_path, questions_path):
    spec = load_json(questions_path)
    out = blank_answers(spec, "pdf-fields")
    out["source"] = pathlib.Path(pdf_path).name
    out["read_at"] = dt.datetime.now().isoformat(timespec="seconds")
    values, has_fields = _pdf_values(pdf_path)
    ours = [k for k in values if str(k).startswith("q.")]
    if not has_fields or not ours:
        out["status"] = "flattened"
        out["provenance"] = "none"
        out["flags"].append({"issue": "no_fields", "message": "This copy has no form fields left (printed or flattened). Transcribe the answers by hand with `answers-template` and mark provenance 'transcribed'."})
        return out

    def text(name):
        v = values.get(name)
        return "" if v is None else str(v).strip()

    for q in spec.get("questions", []):
        qid, qtype = q["id"], q.get("type", "single")
        a = out["answers"][qid]
        if qtype == "text":
            a["value"] = text(f"q.{qid}") or None
        elif qtype == "single":
            v = _name(values.get(f"q.{qid}"))
            a["value"] = None if v in (None, "", "Off") else v
        else:
            picked = []
            for opt in [o["value"] for o in q.get("options", [])] + ["not_sure", "other"]:
                v = _name(values.get(f"q.{qid}.{opt}"))
                if v not in (None, "", "Off"):
                    picked.append(opt)
            a["values"] = picked
        a["other_text"] = text(f"q.{qid}.other_text")
        a["note"] = text(f"q.{qid}.note")
        chosen = a["values"] if qtype == "multi" else [a["value"]] if a["value"] else []
        if not chosen and not a["other_text"] and not a["note"]:
            a["state"] = "blank"
            out["flags"].append({"id": qid, "issue": "blank"})
        elif chosen == ["not_sure"] or (qtype == "multi" and "not_sure" in chosen and len(chosen) == 1):
            a["state"] = "not_sure"
        else:
            a["state"] = "answered"
        if "other" in chosen and not a["other_text"]:
            out["flags"].append({"id": qid, "issue": "other_without_text"})
        if a["other_text"] and "other" not in chosen and qtype != "text":
            out["flags"].append({"id": qid, "issue": "text_without_other", "message": "Wrote in 'Other' without ticking it; treat as their answer only after checking."})
        if qtype == "multi" and q.get("max") and len([v for v in chosen if v != "not_sure"]) > q["max"]:
            out["flags"].append({"id": qid, "issue": "too_many", "max": q["max"]})
        if qtype == "multi" and "not_sure" in chosen and len(chosen) > 1:
            out["flags"].append({"id": qid, "issue": "not_sure_with_answers"})

    for rule in spec.get("conflicts", []):
        def has(qid, value):
            a = out["answers"].get(qid) or {}
            return value == a.get("value") or value in (a.get("values") or [])
        if all(has(qid, value) for qid, value in rule.get("when", [])):
            out["flags"].append({"issue": "conflict", "message": rule.get("message", "These answers pull in different directions; ask one clarifying question.")})

    states = [a["state"] for a in out["answers"].values()]
    out["status"] = "empty" if all(s == "blank" for s in states) else "complete" if "blank" not in states else "partial"
    return out


# ---------------------------------------------------------------- cli


def _importable(module):
    import importlib.util
    return importlib.util.find_spec(module) is not None


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build", help="make the branded fillable PDF")
    b.add_argument("questions")
    b.add_argument("--agency", help="agency profile JSON (optional: without it the PDF uses plain type)")
    b.add_argument("--out", required=True)
    r = sub.add_parser("read", help="read a returned PDF into answers JSON")
    r.add_argument("pdf")
    r.add_argument("--questions", required=True)
    r.add_argument("--out", required=True)
    tpl = sub.add_parser("answers-template", help="empty answers JSON for answers taken by text or call")
    tpl.add_argument("questions")
    tpl.add_argument("--out", required=True)
    args = ap.parse_args(argv)

    if args.cmd in ("build", "read"):
        missing = [m for m in ("reportlab", "pypdf") if not _importable(m)]
        if missing:
            setup = pathlib.Path(__file__).resolve().parents[2] / "client-site-pipeline" / "scripts" / "setup.mjs"
            requirements = pathlib.Path(__file__).with_name("requirements.txt")
            print(f"The PDF kit needs {' and '.join(missing)}. Install them with:\n  node \"{setup}\"\n"
                  f"or: python -m pip install --user -r \"{requirements}\"\n"
                  "Without them, ask the same questions by text or on a call and use `answers-template`.", file=sys.stderr)
            return 2

    if args.cmd == "build":
        warnings = build(args.questions, args.agency, args.out)
        for w in warnings:
            print(f"note: {w}")
        print(f"wrote {args.out}")
    elif args.cmd == "read":
        result = read(args.pdf, args.questions)
        pathlib.Path(args.out).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"{result['status']}: {len(result['flags'])} flag(s) -> {args.out}")
    else:
        result = blank_answers(load_json(args.questions), "transcribed")
        pathlib.Path(args.out).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"wrote {args.out} (fill it in from the call or messages; keep provenance 'transcribed')")
    return 0


if __name__ == "__main__":
    sys.exit(main())
