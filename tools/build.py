"""Build index.html from data/ (24 decks) and tools/template.html.

Usage: python3 tools/build.py   (run from the repo root)
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
sys.path.insert(0, str(ROOT / "tools"))
from keywords import parse as parse_keywords, notes as keyword_notes  # noqa: E402

FIELDS = ["id", "category", "name_th", "name_en", "keywords", "meaning", "image_concept"]
# label, id prefix, Thai name, English name, source file, show category on the card face
DECKS = [
    ("US-TH", "USTH", "คนไทยในอเมริกา", "Thai Life in America", "us-th-keywords-source.txt", False),
    ("Appearance", "LOOK", "รูปลักษณ์หน้าตา", "Appearance", "appearance-draft01.txt", False),
    ("Health", "HLTH", "สุขภาพและโรคภัย", "Health & Illness", "health-draft01.txt", False),
    ("Occupations", "WORK", "ชื่ออาชีพบนโลก", "Occupations of the World", "occupations-draft01.txt", False),
    ("Traits", "MIND", "นิสัยความคิดของคน", "Human Traits & Mindsets", "traits-draft01.txt", False),
    ("US States", "STAT", "รัฐในอเมริกา", "US States", "us-states-draft01.txt", True),
    ("Countries", "CTRY", "ประเทศทั่วโลก", "Countries of the World", "countries-draft01.txt", True),
    ("Thai Provinces", "PROV", "จังหวัดในไทย", "Thai Provinces", "thai-provinces-draft01.txt", True),
    ("Prognosis", "PROG", "อาการและแนวโน้มสุขภาพ", "Health Outlook & Prognosis", "prognosis-draft01.txt", False),
    ("Sacred World", "SACR", "สิ่งศักดิ์สิทธิ์ทั่วโลก", "Sacred Figures & Places of the World", "sacred-world-draft01.txt", False),
    ("Karma", "KARM", "วิบากกรรม", "Karma Across Lifetimes", "karma-draft01.txt", False),
    ("Sacred Thailand", "THSC", "สิ่งศักดิ์สิทธิ์ในไทย", "Sacred Figures & Places of Thailand", "sacred-thailand-draft01.txt", False),
    ("Karma Remedy", "REME", "วิธีแก้กรรม", "Ways to Ease Karma", "karma-remedy-draft01.txt", False),
    ("Love", "LOVE", "ความรักและความสัมพันธ์", "Love & Relationships", "love-draft01.txt", False),
    ("Workplace", "JOBS", "เรื่องในที่ทำงาน", "Work & Career", "workplace-draft01.txt", False),
    ("Visa & Abroad", "VISA", "สัญชาติ วีซ่า และต่างประเทศ", "Visas, Status & Life Abroad", "visa-abroad-draft01.txt", False),
    ("Housing", "HOME", "ที่อยู่อาศัย", "Home & Housing", "housing-draft01.txt", False),
    ("Study", "STDY", "การเรียน", "Study & Education", "study-draft01.txt", False),
    ("Guidance", "GUID", "การแนะแนวชีวิต", "Life Guidance", "guidance-draft01.txt", False),
    ("Timing", "TIME", "ไพ่บอกเวลา", "Timing", "timing-draft01.txt", False),
    ("Numbers", "NUMB", "ตัวเลข 0–999", "Numbers 0–999", "numbers-draft01.txt", False),
    ("Zodiac", "ZODI", "ปีนักษัตรและธาตุจีน", "Chinese Zodiac & Elements", "zodiac-draft01.txt", False),
    ("Daily Life", "DALY", "ปัญหาอุปสรรคในชีวิตประจำวัน", "Everyday Ups & Downs", "daily-draft01.txt", False),
    ("Caution", "WARN", "สิ่งที่ต้องระวังในชีวิต", "Cautions & Misfortunes", "caution-draft01.txt", False),
]

# decks that get a category dropdown (every card, or one category at a time)
CAT_PICK = {"USTH", "SACR", "KARM", "THSC", "REME", "LOVE", "JOBS", "VISA", "HOME", "STDY", "LOOK", "MIND", "GUID", "TIME", "NUMB", "ZODI", "DALY", "WARN"}
# decks whose one-line description (the meaning field) is printed on the card face
SHOW_DESC = {"SACR"}
# decks whose category is the opening phrase of every card name; the page colours that phrase differently
LEAD_CAT = {"GUID"}


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


decks = []
for label, prefix, th, en, src, show_cat in DECKS:
    path = DATA / src
    if src == "us-th-keywords-source.txt":
        cards, dups = parse_keywords(path)
        (DATA / "us-th-keywords-notes.md").write_text(keyword_notes(cards, dups), encoding="utf-8")
    else:
        cards = load_txt(path, prefix)
    for c in cards:
        c["keywords"] = [k.strip() for k in c["keywords"].split(",") if k.strip()]
    ids = [c["id"] for c in cards]
    names = [c["name_th"] for c in cards]
    assert cards and len(set(ids)) == len(ids), label
    assert len(set(names)) == len(names), (label, sorted({n for n in names if names.count(n) > 1}))
    deck = {"label": label, "th": th, "en": en, "showCat": show_cat, "cards": cards}
    if prefix in CAT_PICK:
        deck["catPick"] = True
    if prefix in SHOW_DESC:
        deck["showDesc"] = True
    if prefix in LEAD_CAT:
        deck["leadCat"] = True
    decks.append(deck)
    print(f"{label}: {len(cards)} cards, {len({c['category'] for c in cards})} categories")

# one TSV per deck for the main Google Sheet (columns A-G), pulled in with IMPORTDATA
EXPORT = DATA / "sheet-export"
EXPORT.mkdir(exist_ok=True)
for (label, prefix, *_), d in zip(DECKS, decks):
    rows = ["\t".join([c["id"], c["category"] or "", c["name_th"], c["name_en"] or "", ",".join(c["keywords"]), c.get("meaning") or "", c.get("image_concept") or ""]) for c in d["cards"]]
    assert not any("\t" in v for c in d["cards"] for v in (c["name_th"], c["name_en"] or "", c["category"] or ""))
    (EXPORT / f"{prefix.lower()}.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")

js = json.dumps(decks, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
tpl = (ROOT / "tools/template.html").read_text(encoding="utf-8")
assert tpl.count("/*DECKS*/") == 1
(ROOT / "index.html").write_text(tpl.replace("/*DECKS*/", js), encoding="utf-8")
print("wrote index.html")
