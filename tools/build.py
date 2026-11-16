"""Build index.html from data/ (5 decks) and tools/template.html.

Usage: python3 tools/build.py   (run from the repo root)
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
FIELDS = ["id", "category", "name_th", "name_en", "keywords", "meaning", "image_concept"]
DECKS = [
    ("US-TH", "USTH", "คนไทยในอเมริกา", "Thai Life in America", "us-th-draft01.json"),
    ("Appearance", "LOOK", "รูปลักษณ์หน้าตา", "Appearance", "appearance-draft01.txt"),
    ("Health", "HLTH", "สุขภาพและโรคภัย", "Health & Illness", "health-draft01.txt"),
    ("Occupations", "WORK", "ชื่ออาชีพบนโลก", "Occupations of the World", "occupations-draft01.txt"),
    ("Traits", "MIND", "นิสัยความคิดของคน", "Human Traits & Mindsets", "traits-draft01.txt"),
]


def load_txt(path, prefix):
    cards, cat = [], None
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            cat = line[1:].strip()
            continue
        parts = line.split("|")
        assert len(parts) == 5, (path.name, line)
        cards.append(dict(zip(FIELDS, [f"{prefix}-{len(cards) + 1:03d}", cat, *parts])))
    return cards


def load_sheet(path):
    rows = json.loads(path.read_text(encoding="utf-8"))["values"][1:]
    return [dict(zip(FIELDS, r)) for r in rows]


decks = []
for label, prefix, th, en, src in DECKS:
    p = DATA / src
    cards = load_sheet(p) if p.suffix == ".json" else load_txt(p, prefix)
    for c in cards:
        c["keywords"] = [k.strip() for k in c["keywords"].split(",") if k.strip()]
    assert len(cards) == 90, (label, len(cards))
    assert len({c["id"] for c in cards}) == 90, label
    decks.append({"label": label, "th": th, "en": en, "cards": cards})
    print(f"{label}: {len(cards)} cards")

js = json.dumps(decks, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
tpl = (ROOT / "tools/template.html").read_text(encoding="utf-8")
assert tpl.count("/*DECKS*/") == 1
(ROOT / "index.html").write_text(tpl.replace("/*DECKS*/", js), encoding="utf-8")
print("wrote index.html")
