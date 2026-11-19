"""Build tables.html (clash-year calendar 2000-3000 and birth-year age table) and their sheet TSVs.

Usage: python3 tools/tables.py   (run from the repo root)

Clash levels follow the common Thai four-level scheme:
  100% = the sign opposite the year (chong), 75% = the year's own sign (tai sui),
  50% = the sign in "harm" (hai) with the year, 25% = the sign in "break" (po) with the year.
Schools differ; the page says so.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
Z = ['ชวด', 'ฉลู', 'ขาล', 'เถาะ', 'มะโรง', 'มะเส็ง', 'มะเมีย', 'มะแม', 'วอก', 'ระกา', 'จอ', 'กุน']
A = ['หนู', 'วัว', 'เสือ', 'กระต่าย', 'มังกร', 'งู', 'ม้า', 'แพะ', 'ลิง', 'ไก่', 'สุนัข', 'หมู']
EL = ['ไม้', 'ไฟ', 'ดิน', 'ทอง', 'น้ำ']
HARM = {0: 7, 7: 0, 1: 6, 6: 1, 2: 5, 5: 2, 3: 4, 4: 3, 8: 11, 11: 8, 9: 10, 10: 9}
BREAK = {0: 9, 9: 0, 6: 3, 3: 6, 5: 8, 8: 5, 2: 11, 11: 2, 4: 1, 1: 4, 10: 7, 7: 10}


def sign(y):
    a = (y - 4) % 12
    return a, EL[((y - 4) % 10) // 2]


def label(a):
    return f'{Z[a]} ({A[a]})'


chong = []
for y in range(2000, 3001):
    a, el = sign(y)
    chong.append([y, y + 543, f'{Z[a]} · {A[a]}{el}', label((a + 6) % 12), label(a), label(HARM[a]), label(BREAK[a])])

ages = []
for y in range(1900, 2027):
    a, el = sign(y)
    ages.append([y, y + 543, Z[a], f'{A[a]}{el}'])

exp = ROOT / 'data' / 'sheet-export'
head = ['ค.ศ.', 'พ.ศ.', 'ปีนักษัตร · ธาตุ', 'ชง 100% (ตรงข้าม)', 'ชง 75% (ชงตัวเอง)', 'ชง 50% (ไห่)', 'ชง 25% (ผั่ว)']
(exp / 'chong.tsv').write_text('\n'.join('\t'.join(map(str, r)) for r in [head] + chong) + '\n', encoding='utf-8')
ahead = ['ปีเกิด ค.ศ.', 'ปีเกิด พ.ศ.', 'ปีนักษัตร', 'นักษัตรและธาตุ', 'อายุในปี 2026 (2569)', 'อายุในปี 2027 (2570)']
(exp / 'ages.tsv').write_text('\n'.join('\t'.join(map(str, r)) for r in [ahead] + [r + [2026 - r[0], 2027 - r[0]] for r in ages]) + '\n', encoding='utf-8')

tpl = (ROOT / 'tools' / 'tables-template.html').read_text(encoding='utf-8')
data = json.dumps({'chong': chong, 'ages': ages}, ensure_ascii=False, separators=(',', ':'))
assert tpl.count('/*DATA*/') == 1
(ROOT / 'tables.html').write_text(tpl.replace('/*DATA*/', data), encoding='utf-8')
print(f'{len(chong)} clash years, {len(ages)} birth years; wrote tables.html')
