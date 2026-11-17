"""Parse the deck 1 keyword list (data/us-th-keywords-source.txt) into cards.

The source is the keyword list as it was posted, one '# category' line per bullet group.
Items are separated by spaces. Items that are several words, and items that were posted
without a space between them, are handled by the two tables below. Every change is listed
in data/us-th-keywords-notes.md so it can be reviewed.
"""
import re
from pathlib import Path

# Items that contain spaces and stay one card.
PHRASES = [
    "TikTok เกอร์", "นักเทรด Forex", "work and travel", "โดน Pause", "มี House เมท",
    "Friends With Benefits", "One Night Stand", "mass shooting", "ลงทุน Forex ได้", "คน ABC",
]

# Items posted with no space between them, split into separate cards.
SPLITS = {
    "นำเที่ยวส่งอาหาร": ["นำเที่ยว", "ส่งอาหาร"],
    "ขายของแห้งขายของสด": ["ขายของแห้ง", "ขายของสด"],
    "นายหน้าทำงานเกี่ยวกับศาสนามูลนิธิ": ["นายหน้า", "ทำงานเกี่ยวกับศาสนา", "มูลนิธิ"],
    "ยามทหาร": ["ยาม", "ทหาร"],
    "งานราชการงานรัฐวิสาหกิจงานเกี่ยวกับสนามบิน": ["งานราชการ", "งานรัฐวิสาหกิจ", "งานเกี่ยวกับสนามบิน"],
    "แอร์สจ๊วตพนักงานสนามบิน": ["แอร์สจ๊วต", "พนักงานสนามบิน"],
    "โชว์ตัวขายของออนไลน์": ["โชว์ตัว", "ขายของออนไลน์"],
    "แฟชั่นพนักงานขายทั่วไปพนักงานขายแบรนด์เนม": ["แฟชั่น", "พนักงานขายทั่วไป", "พนักงานขายแบรนด์เนม"],
    "ปริญญาตรีปริญญาโท": ["ปริญญาตรี", "ปริญญาโท"],
    "ขี้หลีเจ้าชู้": ["ขี้หลี", "เจ้าชู้"],
    "รอต่อไปได้ควรหยุดรอ": ["รอต่อไปได้", "ควรหยุดรอ"],
    "รู้หน้าไม่รู้ใจนิสัยตรงข้ามกับที่คิด": ["รู้หน้าไม่รู้ใจ", "นิสัยตรงข้ามกับที่คิด"],
    "คนน่ารักคนนิสัยดี": ["คนน่ารัก", "คนนิสัยดี"],
    "ดูแก่คุยเก่ง": ["ดูแก่", "คุยเก่ง"],
    "ใจดีใจอ่อน": ["ใจดี", "ใจอ่อน"],
    "จะโดนไล่ออกออกจากงาน": ["จะโดนไล่ออก", "ออกจากงาน"],
}

# Kept exactly as posted, but worth a second look.
FLAGS = {
    "Citizen": "ต้นฉบับเขียนว่า \"Citizen planking\" แยกเป็น 2 ใบ (Citizen / planking) — planking อาจพิมพ์ผิด",
    "planking": "ดู Citizen",
    "พระยังไม่มีมีพลังงาน": "อาจหมายถึง \"พระยังไม่มีพลังงาน\" หรือ \"พระยังไม่มี / มีพลังงาน\"",
    "ออก": "น่าจะหมายถึงทิศตะวันออก (คงไว้ตามต้นฉบับ)",
    "ตก": "น่าจะหมายถึงทิศตะวันตก (คงไว้ตามต้นฉบับ)",
}


def parse(path: Path):
    cards, dups, cat = [], [], None
    seen = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            cat = line[1:].strip()
            continue
        for p in PHRASES:
            line = line.replace(p, p.replace(" ", " "))
        for tok in re.split(r"[ \t]+", line):
            if not tok:
                continue
            tok = tok.replace(" ", " ")
            for item in SPLITS.get(tok, [tok]):
                if item in seen:
                    dups.append((cat, item))
                    continue
                seen.add(item)
                cards.append({"id": f"USTH-{len(cards) + 1:03d}", "category": cat, "name_th": item,
                              "name_en": "", "keywords": "", "meaning": "", "image_concept": ""})
    return cards, dups


def notes(cards, dups):
    used = {c["name_th"] for c in cards}
    lines = ["# สำรับ 1 · หมายเหตุการแยกคีย์เวิร์ด", "",
             f"ได้ {len(cards)} ใบ (คีย์เวิร์ดไม่ซ้ำ)  ตัดคำซ้ำออก {len(dups)} คำ", "",
             "## คำที่ติดกันในต้นฉบับ แยกเป็นหลายใบ", ""]
    lines += [f"- {k} → {' / '.join(v)}" for k, v in SPLITS.items()]
    lines += ["", "## คำที่มีเว้นวรรค คงไว้เป็นใบเดียว", ""] + [f"- {p}" for p in PHRASES]
    lines += ["", "## คำซ้ำที่ตัดออก (คงใบแรกไว้)", ""] + [f"- {w} (หมวด {c})" for c, w in dups]
    lines += ["", "## ควรตรวจอีกครั้ง", ""] + [f"- {k}: {v}" for k, v in FLAGS.items() if k in used]
    return "\n".join(lines) + "\n"
