"""Tests for the optional discovery PDF kit.

    pip install -r requirements.txt      (add pypdfium2 for the render check)
    python -m unittest test_discovery_pdf -v

PDF tests skip without reportlab and pypdf; the answers-template test runs
without them, because the text-or-call path must work with no dependencies.
"""
import copy
import json
import pathlib
import sys
import tempfile
import unittest

HERE = pathlib.Path(__file__).resolve().parent
ASSETS = HERE.parent / "assets"
sys.path.insert(0, str(HERE))

import discovery_pdf  # noqa: E402

try:
    import reportlab  # noqa: F401
    import pypdf  # noqa: F401
    HAVE_PDF = True
except ImportError:
    HAVE_PDF = False

try:
    import pypdfium2  # noqa: F401
    HAVE_RENDER = True
except ImportError:
    HAVE_RENDER = False

EXAMPLE_QUESTIONS = ASSETS / "questions.example.json"
EXAMPLE_AGENCY = ASSETS / "agency-profile.example.json"

SPANISH = {
    "version": 2,
    "locale": "es",
    "page_size": "a4",
    "client": {"name": "Taquería Doña Inés"},
    "title": "Unas preguntas antes de diseñar",
    "intro": "Cinco minutos. Ya vimos tu página y tu Instagram, así que solo preguntamos lo que no podemos decidir sin ti.",
    "questions": [
        {"id": "lead", "type": "single", "prompt": "¿Qué debe ver la gente primero?",
         "options": [{"value": "product", "label": "La comida, en fotos reales"},
                     {"value": "place", "label": "El lugar y la familia que lo atiende"}], "note": True},
        {"id": "feel", "type": "multi", "max": 2, "prompt": "¿Cómo se debe sentir la página?",
         "options": [{"value": "warm", "label": "Cálida"}, {"value": "simple", "label": "Sencilla"},
                     {"value": "lively", "label": "Alegre"}]},
        {"id": "never", "type": "text", "lines": 3, "prompt": "¿Algo que nunca debamos decir o mostrar?"},
    ],
}


def write_json(folder, name, data):
    path = pathlib.Path(folder) / name
    path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return path


def fill(src, dst, values, mode="both"):
    """Fill a built PDF the way a viewer would. `values` maps field names to a
    string (text field or radio choice) or True (checkbox). mode "v_only" sets
    only field values and "as_only" only widget states, because real viewers
    differ in which one they update."""
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import NameObject, TextStringObject

    writer = PdfWriter(clone_from=PdfReader(str(src)))
    for page in writer.pages:
        for ref in page.get("/Annots") or []:
            annot = ref.get_object()
            parent = annot.get("/Parent")
            parent = parent.get_object() if parent is not None else None
            name = annot.get("/T") or (parent.get("/T") if parent is not None else None)
            if name not in values:
                continue
            value = values[name]
            field_type = annot.get("/FT") or (parent.get("/FT") if parent is not None else None)
            if field_type == "/Tx":
                annot[NameObject("/V")] = TextStringObject(value)
                continue
            on_states = [k for k in annot["/AP"]["/N"].keys() if k != "/Off"]
            if parent is not None and annot.get("/T") is None:  # radio kid
                target = "/" + value
                hit = target in on_states
                if mode != "v_only":
                    annot[NameObject("/AS")] = NameObject(target if hit else "/Off")
                if hit and mode != "as_only":
                    parent[NameObject("/V")] = NameObject(target)
            else:  # checkbox
                if mode != "v_only":
                    annot[NameObject("/AS")] = NameObject(on_states[0])
                if mode != "as_only":
                    annot[NameObject("/V")] = NameObject(on_states[0])
    with open(dst, "wb") as fh:
        writer.write(fh)


def flatten(src, dst):
    """Drop the form and its widgets, like printing to PDF or 'flatten' in a viewer."""
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import NameObject

    writer = PdfWriter(clone_from=PdfReader(str(src)))
    for page in writer.pages:
        if "/Annots" in page:
            del page[NameObject("/Annots")]
    if "/AcroForm" in writer._root_object:
        del writer._root_object[NameObject("/AcroForm")]
    with open(dst, "wb") as fh:
        writer.write(fh)


def page_text(pdf_path):
    from pypdf import PdfReader
    return "\n".join(p.extract_text() or "" for p in PdfReader(str(pdf_path)).pages)


def image_count(pdf_path):
    from pypdf import PdfReader
    total = 0
    for page in PdfReader(str(pdf_path)).pages:
        xobjects = (page.get("/Resources") or {}).get("/XObject") or {}
        total += sum(1 for x in xobjects.values() if x.get_object().get("/Subtype") == "/Image")
    return total


class AnswersTemplateWithoutDependencies(unittest.TestCase):
    def test_template_is_transcribed_and_complete(self):
        spec = json.loads(EXAMPLE_QUESTIONS.read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmp:
            out = pathlib.Path(tmp) / "answers.json"
            self.assertEqual(discovery_pdf.main(["answers-template", str(EXAMPLE_QUESTIONS), "--out", str(out)]), 0)
            data = json.loads(out.read_text(encoding="utf-8"))
        self.assertEqual(data["provenance"], "transcribed")
        self.assertEqual(data["status"], "empty")
        self.assertEqual(list(data["answers"]), [q["id"] for q in spec["questions"]])

    @unittest.skipIf(HAVE_PDF, "only meaningful without the PDF dependencies")
    def test_build_without_dependencies_explains_instead_of_crashing(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = pathlib.Path(tmp) / "kit.pdf"
            self.assertEqual(discovery_pdf.main(["build", str(EXAMPLE_QUESTIONS), "--out", str(out)]), 2)
            self.assertFalse(out.exists())


@unittest.skipUnless(HAVE_PDF, "reportlab and pypdf not installed (optional)")
class BuildAndRead(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = pathlib.Path(self._tmp.name)
        self.spec = json.loads(EXAMPLE_QUESTIONS.read_text(encoding="utf-8"))

    def tearDown(self):
        self._tmp.cleanup()

    def build(self, spec=None, agency=EXAMPLE_AGENCY, name="kit.pdf"):
        questions = write_json(self.tmp, name + ".questions.json", spec or self.spec)
        out = self.tmp / name
        warnings = discovery_pdf.build(questions, agency, out)
        return out, questions, warnings

    def agency(self, **changes):
        data = json.loads(EXAMPLE_AGENCY.read_text(encoding="utf-8"))
        for key, value in changes.items():
            data[key] = {**(data.get(key) or {}), **value} if isinstance(value, dict) else value
        return write_json(self.tmp, "agency.json", data)

    # -- creation

    def test_fields_match_the_questions(self):
        from pypdf import PdfReader
        pdf, _, warnings = self.build()
        self.assertEqual(warnings, [])
        fields = PdfReader(str(pdf)).get_fields()
        for q in self.spec["questions"]:
            qid, qtype = q["id"], q.get("type", "single")
            if qtype == "single":
                self.assertEqual(fields[f"q.{qid}"].get("/FT"), "/Btn", qid)
            elif qtype == "multi":
                for value in [o["value"] for o in q["options"]] + ["not_sure", "other"]:
                    self.assertIn(f"q.{qid}.{value}", fields)
            else:
                self.assertEqual(fields[f"q.{qid}"].get("/FT"), "/Tx", qid)
            if qtype != "text":
                self.assertIn(f"q.{qid}.other_text", fields)
            self.assertEqual(f"q.{qid}.note" in fields, bool(q.get("note")), qid)

    def test_every_widget_has_a_tooltip_and_sits_on_the_page(self):
        from pypdf import PdfReader
        pdf, _, _ = self.build()
        reader = PdfReader(str(pdf))
        for page in reader.pages:
            width, height = float(page.mediabox.width), float(page.mediabox.height)
            for ref in page.get("/Annots") or []:
                annot = ref.get_object()
                if annot.get("/Subtype") != "/Widget":
                    continue
                parent = annot.get("/Parent")
                tip = annot.get("/TU") or (parent.get_object().get("/TU") if parent is not None else None)
                self.assertTrue(tip, "widget without a tooltip (screen readers read it)")
                x1, y1, x2, y2 = [float(v) for v in annot["/Rect"]]
                self.assertTrue(0 <= x1 < x2 <= width and 40 <= y1 < y2 <= height, annot["/Rect"])

    def test_radio_appearance_is_centered_in_its_box(self):
        """reportlab scales radio circles by size/20; ours must fill the box."""
        from pypdf import PdfReader
        pdf, _, _ = self.build()
        for ref in PdfReader(str(pdf)).pages[0]["/Annots"]:
            annot = ref.get_object()
            if annot.get("/T") is None and annot.get("/Parent") is not None:
                x1, y1, x2, _ = [float(v) for v in annot["/Rect"]]
                half = (x2 - x1) / 2
                for state, stream in annot["/AP"]["/N"].items():
                    data = stream.get_object().get_data().decode("latin1")
                    self.assertIn(f"1 0 0 1 {half:g} {half:g} cm", data, state)
                break
        else:
            self.fail("no radio widget on page 1")

    def test_long_questionnaire_breaks_pages(self):
        spec = copy.deepcopy(self.spec)
        extra = copy.deepcopy(spec["questions"][3])
        for i in range(6):
            q = copy.deepcopy(extra)
            q["id"] = f"proof{i}"
            spec["questions"].append(q)
        pdf, questions, _ = self.build(spec, name="long.pdf")
        from pypdf import PdfReader
        self.assertGreater(len(PdfReader(str(pdf)).pages), 3)
        self.assertEqual(discovery_pdf.read(pdf, questions)["status"], "empty")

    # -- branding

    def test_missing_logo_falls_back_to_type(self):
        pdf, _, warnings = self.build(agency=self.agency(logo={"primary": str(self.tmp / "nope.png")}))
        self.assertTrue(any("not found" in w for w in warnings), warnings)
        self.assertEqual(image_count(pdf), 0)
        self.assertIn("EXAMPLE STUDIO", page_text(pdf))

    def test_svg_logo_falls_back_to_type(self):
        svg = self.tmp / "logo.svg"
        svg.write_text("<svg xmlns='http://www.w3.org/2000/svg'/>", encoding="utf-8")
        pdf, _, warnings = self.build(agency=self.agency(logo={"primary": str(svg)}))
        self.assertTrue(any("not PNG or JPG" in w for w in warnings), warnings)
        self.assertEqual(image_count(pdf), 0)

    def test_corrupt_png_falls_back_to_type(self):
        bad = self.tmp / "logo.png"
        bad.write_bytes(b"not an image")
        pdf, _, warnings = self.build(agency=self.agency(logo={"primary": str(bad)}))
        self.assertTrue(any("could not be read" in w for w in warnings), warnings)
        self.assertIn("EXAMPLE STUDIO", page_text(pdf))

    def test_png_logo_is_drawn(self):
        from PIL import Image
        logo = self.tmp / "logo.png"
        Image.new("RGBA", (240, 60), (18, 18, 18, 255)).save(logo)
        pdf, _, warnings = self.build(agency=self.agency(logo={"primary": str(logo)}))
        self.assertEqual(warnings, [])
        self.assertEqual(image_count(pdf), 1)
        self.assertNotIn("EXAMPLE STUDIO", page_text(pdf))

    def test_no_agency_profile(self):
        pdf, questions, warnings = self.build(agency=None)
        self.assertEqual(warnings, [])
        text = page_text(pdf)
        self.assertIn("DISCOVERY", text)
        self.assertNotIn("example.com", text.replace("https://example.com/", ""))
        self.assertEqual(discovery_pdf.read(pdf, questions)["status"], "empty")

    def test_two_agencies_brand_separately(self):
        a, _, _ = self.build(agency=self.agency(name="North Studio", contact={"email": "hi@north.test"}), name="a.pdf")
        b, _, _ = self.build(agency=self.agency(name="South Media", contact={"email": "hola@south.test"}), name="b.pdf")
        ta, tb = page_text(a), page_text(b)
        self.assertIn("NORTH STUDIO", ta)
        self.assertIn("hi@north.test", ta)
        self.assertNotIn("South", ta)
        self.assertIn("SOUTH MEDIA", tb)
        self.assertNotIn("North", tb)

    def test_unreadable_brand_font_falls_back(self):
        bad = self.tmp / "brand.ttf"
        bad.write_bytes(b"nope")
        pdf, _, warnings = self.build(agency=self.agency(fonts={"regular": str(bad), "bold": None}))
        self.assertTrue(any("font regular not used" in w for w in warnings), warnings)
        self.assertTrue(pdf.exists())

    def test_truetype_brand_font_when_available(self):
        candidates = [pathlib.Path(p) for p in ("C:/Windows/Fonts/arial.ttf", "/Library/Fonts/Arial.ttf",
                                                "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")]
        font = next((p for p in candidates if p.exists()), None)
        if not font:
            self.skipTest("no TrueType font on this machine")
        pdf, _, warnings = self.build(agency=self.agency(fonts={"regular": str(font), "bold": str(font)}))
        self.assertEqual(warnings, [])
        self.assertIn("Who do you most want to reach", page_text(pdf))

    # -- Spanish

    def test_spanish_text_and_answers_keep_accents(self):
        pdf, questions, _ = self.build(SPANISH, name="es.pdf")
        text = page_text(pdf)
        for phrase in ("Cómo llenarlo", "¿Qué debe ver la gente primero?", "Taquería Doña Inés",
                       "No estoy seguro, ayúdenme a elegir", "Elige hasta 2.", "Página 1"):
            self.assertIn(phrase, text)
        filled = self.tmp / "es-filled.pdf"
        fill(pdf, filled, {"q.lead": "place", "q.lead.note": "La señora Inés abrió en 1998, pero no lo pongas así.",
                           "q.feel.warm": True, "q.never": "Nada de \"auténtico\". Ñ y acentos bien escritos."})
        result = discovery_pdf.read(filled, questions)
        self.assertEqual(result["answers"]["lead"]["value"], "place")
        self.assertEqual(result["answers"]["lead"]["note"], "La señora Inés abrió en 1998, pero no lo pongas así.")
        self.assertEqual(result["answers"]["never"]["value"], "Nada de \"auténtico\". Ñ y acentos bien escritos.")
        self.assertEqual(result["status"], "complete")

    # -- saving and reading back

    def complete_answers(self):
        return {
            "q.visitor": "events", "q.visitor.note": "Catering is most of our money.",
            "q.action": "other", "q.action.other_text": "Text us on WhatsApp",
            "q.lead": "product",
            "q.proof.photos": True, "q.proof.reviews": True,
            "q.feel.warm": True, "q.feel.traditional": True,
            "q.reference.look": True, "q.reference.easy": True,
            "q.never": "Never call it fusion.",
        }

    def check_complete(self, result):
        a = result["answers"]
        self.assertEqual(result["status"], "complete", result["flags"])
        self.assertEqual(a["visitor"]["value"], "events")
        self.assertEqual(a["visitor"]["note"], "Catering is most of our money.")
        self.assertEqual(a["action"]["value"], "other")
        self.assertEqual(a["action"]["other_text"], "Text us on WhatsApp")
        self.assertEqual(a["lead"]["value"], "product")
        self.assertEqual(a["proof"]["values"], ["photos", "reviews"])
        self.assertEqual(a["feel"]["values"], ["warm", "traditional"])
        self.assertEqual(a["reference"]["values"], ["look", "easy"])
        self.assertEqual(a["never"]["value"], "Never call it fusion.")
        self.assertEqual(result["flags"], [])
        self.assertEqual(result["provenance"], "pdf-fields")

    def test_round_trip_field_values_and_widget_states(self):
        pdf, questions, _ = self.build()
        filled = self.tmp / "filled.pdf"
        fill(pdf, filled, self.complete_answers())
        self.check_complete(discovery_pdf.read(filled, questions))

    def test_round_trip_when_viewer_sets_only_widget_states(self):
        pdf, questions, _ = self.build()
        filled = self.tmp / "as-only.pdf"
        fill(pdf, filled, self.complete_answers(), mode="as_only")
        self.check_complete(discovery_pdf.read(filled, questions))

    def test_round_trip_when_viewer_sets_only_field_values(self):
        pdf, questions, _ = self.build()
        filled = self.tmp / "v-only.pdf"
        fill(pdf, filled, self.complete_answers(), mode="v_only")
        self.check_complete(discovery_pdf.read(filled, questions))

    def test_pypdf_writer_fill_reads_back(self):
        """Fill through pypdf's own form API, the path most scripts would use."""
        from pypdf import PdfReader, PdfWriter
        pdf, questions, _ = self.build()
        writer = PdfWriter(clone_from=PdfReader(str(pdf)))
        for page in writer.pages:
            writer.update_page_form_field_values(page, {"q.never": "Keep the mural photo.", "q.visitor": "/lunch"},
                                                 auto_regenerate=False)
        filled = self.tmp / "pypdf.pdf"
        with open(filled, "wb") as fh:
            writer.write(fh)
        result = discovery_pdf.read(filled, questions)
        self.assertEqual(result["answers"]["never"]["value"], "Keep the mural photo.")
        self.assertEqual(result["answers"]["visitor"]["value"], "lunch")
        self.assertEqual(result["status"], "partial")

    # -- flags

    def flags(self, result):
        return {(f.get("id"), f["issue"]) for f in result["flags"]}

    def test_blank_copy_is_empty_with_a_flag_per_question(self):
        pdf, questions, _ = self.build()
        result = discovery_pdf.read(pdf, questions)
        self.assertEqual(result["status"], "empty")
        self.assertEqual(self.flags(result), {(q["id"], "blank") for q in self.spec["questions"]})

    def test_partial_not_sure_and_problem_answers(self):
        pdf, questions, _ = self.build()
        filled = self.tmp / "messy.pdf"
        fill(pdf, filled, {
            "q.visitor": "not_sure",
            "q.action": "other",                                 # ticked Other, wrote nothing
            "q.lead.other_text": "Our grandma's recipes",       # wrote in Other, did not tick it
            "q.proof.photos": True, "q.proof.reviews": True, "q.proof.press": True, "q.proof.years": True,
            "q.feel.not_sure": True, "q.feel.warm": True,
        })
        result = discovery_pdf.read(filled, questions)
        flags = self.flags(result)
        self.assertEqual(result["answers"]["visitor"]["state"], "not_sure")
        self.assertIn(("action", "other_without_text"), flags)
        self.assertIn(("lead", "text_without_other"), flags)
        self.assertIn(("proof", "too_many"), flags)
        self.assertIn(("feel", "not_sure_with_answers"), flags)
        self.assertIn(("reference", "blank"), flags)
        self.assertEqual(result["status"], "partial")

    def test_conflict_rules(self):
        pdf, questions, _ = self.build()
        filled = self.tmp / "conflict.pdf"
        fill(pdf, filled, {"q.feel.simple": True, "q.feel.lively": True,
                           "q.lead": "credibility", "q.proof.none_yet": True})
        messages = [f["message"] for f in discovery_pdf.read(filled, questions)["flags"] if f["issue"] == "conflict"]
        self.assertEqual(len(messages), 2)
        self.assertTrue(any("Simple and lively" in m for m in messages))
        self.assertTrue(any("credibility" in m for m in messages))

    def test_flattened_copy_goes_to_transcription(self):
        pdf, questions, _ = self.build()
        filled, flat = self.tmp / "filled.pdf", self.tmp / "flat.pdf"
        fill(pdf, filled, self.complete_answers())
        flatten(filled, flat)
        result = discovery_pdf.read(flat, questions)
        self.assertEqual(result["status"], "flattened")
        self.assertEqual(result["provenance"], "none")
        self.assertEqual([f["issue"] for f in result["flags"]], ["no_fields"])
        self.assertTrue(all(a["value"] is None and a["values"] == [] for a in result["answers"].values()))

    def test_foreign_pdf_with_other_fields_counts_as_flattened(self):
        from reportlab.pdfgen import canvas
        other = self.tmp / "other.pdf"
        c = canvas.Canvas(str(other))
        c.drawString(50, 740, "Someone else's form")
        c.acroForm.textfield(name="name", x=50, y=700, width=200, height=20)
        c.showPage()
        c.save()
        _, questions, _ = self.build()
        self.assertEqual(discovery_pdf.read(other, questions)["status"], "flattened")

    # -- CLI

    def test_cli_build_and_read(self):
        out, answers = self.tmp / "cli.pdf", self.tmp / "answers.json"
        self.assertEqual(discovery_pdf.main(["build", str(EXAMPLE_QUESTIONS), "--agency", str(EXAMPLE_AGENCY),
                                             "--out", str(out)]), 0)
        self.assertEqual(discovery_pdf.main(["read", str(out), "--questions", str(EXAMPLE_QUESTIONS),
                                             "--out", str(answers)]), 0)
        self.assertEqual(json.loads(answers.read_text(encoding="utf-8"))["status"], "empty")

    # -- rendering

    @unittest.skipUnless(HAVE_RENDER, "pypdfium2 not installed (test-only)")
    def test_choices_show_where_they_were_made(self):
        """Render through pdfium's form layer, the way viewers draw widgets:
        a chosen radio or checkbox is dark at its center, an unchosen one isn't."""
        import pypdfium2 as pdfium
        from pypdf import PdfReader
        pdf, _, _ = self.build()
        filled = self.tmp / "shown.pdf"
        fill(pdf, filled, {"q.visitor": "events", "q.proof.photos": True})
        scale, ink = 4, {}
        doc = pdfium.PdfDocument(str(filled))
        try:
            doc.init_forms()
            for index, page in enumerate(PdfReader(str(filled)).pages):
                image = doc[index].render(scale=scale, may_draw_forms=True).to_pil().convert("L")
                height = float(page.mediabox.height)
                for ref in page.get("/Annots") or []:
                    annot = ref.get_object()
                    parent = annot.get("/Parent")
                    name = annot.get("/T") or (parent.get_object().get("/T") if parent is not None else None)
                    on = [k for k in (annot.get("/AP") or {}).get("/N", {}).keys() if k != "/Off"]
                    if not on or annot.get("/FT", parent.get_object().get("/FT") if parent is not None else None) != "/Btn":
                        continue
                    x1, y1, x2, y2 = [float(v) for v in annot["/Rect"]]
                    cx, cy = int((x1 + x2) / 2 * scale), int((height - (y1 + y2) / 2) * scale)
                    box = [image.getpixel((cx + dx, cy + dy)) for dx in range(-3, 4) for dy in range(-3, 4)]
                    ink[f"{name}={on[0][1:]}"] = sum(1 for px in box if px < 128)
        finally:
            doc.close()
        self.assertGreater(ink["q.visitor=events"], 20, "chosen radio shows no dot")
        self.assertEqual(ink["q.visitor=families"], 0, "unchosen radio shows a dot")
        photos = next(v for k, v in ink.items() if k.startswith("q.proof.photos="))
        reviews = next(v for k, v in ink.items() if k.startswith("q.proof.reviews="))
        self.assertGreater(photos, 5, "ticked checkbox shows no mark")
        self.assertEqual(reviews, 0, "unticked checkbox shows a mark")

    @unittest.skipUnless(HAVE_RENDER, "pypdfium2 not installed (test-only)")
    def test_pages_render_with_fields(self):
        import pypdfium2 as pdfium
        for spec, name in ((self.spec, "en.pdf"), (SPANISH, "es-render.pdf")):
            pdf, _, _ = self.build(spec, name=name)
            doc = pdfium.PdfDocument(str(pdf))
            try:
                self.assertGreaterEqual(len(doc), 1)
                for i in range(len(doc)):
                    image = doc[i].render(scale=1, may_draw_forms=True).to_pil().convert("L")
                    dark = sum(1 for px in image.getdata() if px < 128)
                    self.assertGreater(dark, 500, f"{name} page {i + 1} looks blank")
            finally:
                doc.close()


if __name__ == "__main__":
    unittest.main()
