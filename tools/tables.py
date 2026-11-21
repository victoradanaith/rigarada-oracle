"""Build tables.html (clash calendar 1950-3000, age table, zodiac compatibility, weekday lucky colours) and their sheet TSVs.

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
for y in range(1950, 3001):
    a, el = sign(y)
    chong.append([y, y + 543, f'{Z[a]} · {A[a]}{el}', label((a + 6) % 12), label(a), label(HARM[a]), label(BREAK[a])])

# compatibility: trine (san he) and six harmony (liu he) suit; clash, harm, break and punishment (xing) don't
TRINE = [{0, 4, 8}, {1, 5, 9}, {2, 6, 10}, {3, 7, 11}]
SIX = {0: 1, 1: 0, 2: 11, 11: 2, 3: 10, 10: 3, 4: 9, 9: 4, 5: 8, 8: 5, 6: 7, 7: 6}
XING = [{2, 5, 8}, {1, 7, 10}, {0, 3}]
SELF_XING = {4, 6, 9, 11}
compat = []
for a in range(12):
    tri = next(g for g in TRINE if a in g) - {a}
    xing = next((g for g in XING if a in g), set()) - {a}
    xs = [label(x) for x in sorted(xing)] + (['ตัวเองกับตัวเอง (ปีเดียวกัน)'] if a in SELF_XING else [])
    compat.append([label(a), ', '.join(label(x) for x in sorted(tri)), label(SIX[a]),
                   label((a + 6) % 12), label(HARM[a]), label(BREAK[a]), ', '.join(xs) or '-'])

# weekday lucky colours by taksa: from the birth-day planet go round the taksa ring, 8 roles
RING = ['อาทิตย์', 'จันทร์', 'อังคาร', 'พุธ', 'เสาร์', 'พฤหัสบดี', 'ราหู', 'ศุกร์']
PCOL = {'อาทิตย์': 'แดง', 'จันทร์': 'เหลือง ครีม', 'อังคาร': 'ชมพู', 'พุธ': 'เขียว', 'พฤหัสบดี': 'ส้ม แสด',
        'ศุกร์': 'ฟ้า น้ำเงิน', 'เสาร์': 'ม่วง', 'ราหู': 'เทา ดำ'}
ROLES = [('บริวาร', 'คนรอบข้าง ลูกน้อง คนในบ้าน'), ('อายุ', 'สุขภาพ อายุยืน'), ('เดช', 'อำนาจ บารมี ความกล้า'),
         ('ศรี', 'โชคลาภ เงินทอง เสน่ห์'), ('มูละ', 'ทรัพย์สิน หลักฐาน มรดก'), ('อุตสาหะ', 'ความขยัน การงาน'),
         ('มนตรี', 'ผู้ใหญ่อุปถัมภ์ คนช่วยเหลือ'), ('กาลกิณี', 'สิ่งไม่ดี ควรเลี่ยง')]
DAYS = [('วันอาทิตย์', 'อาทิตย์'), ('วันจันทร์', 'จันทร์'), ('วันอังคาร', 'อังคาร'), ('วันพุธ (กลางวัน)', 'พุธ'),
        ('วันพุธ (กลางคืน)', 'ราหู'), ('วันพฤหัสบดี', 'พฤหัสบดี'), ('วันศุกร์', 'ศุกร์'), ('วันเสาร์', 'เสาร์')]
colours = []
for day, planet in DAYS:
    i = RING.index(planet)
    colours.append([day] + [PCOL[RING[(i + k) % 8]] for k in range(8)])

ages = []
for y in range(1900, 2027):
    a, el = sign(y)
    ages.append([y, y + 543, Z[a], f'{A[a]}{el}'])

exp = ROOT / 'data' / 'sheet-export'
head = ['ค.ศ.', 'พ.ศ.', 'ปีนักษัตร · ธาตุ', 'ชง 100% (ตรงข้าม)', 'ชง 75% (ชงตัวเอง)', 'ชง 50% (ไห่)', 'ชง 25% (ผั่ว)']
(exp / 'chong.tsv').write_text('\n'.join('\t'.join(map(str, r)) for r in [head] + chong) + '\n', encoding='utf-8')
ahead = ['ปีเกิด ค.ศ.', 'ปีเกิด พ.ศ.', 'ปีนักษัตร', 'นักษัตรและธาตุ', 'อายุในปี 2026 (2569)', 'อายุในปี 2027 (2570)']
(exp / 'ages.tsv').write_text('\n'.join('\t'.join(map(str, r)) for r in [ahead] + [r + [2026 - r[0], 2027 - r[0]] for r in ages]) + '\n', encoding='utf-8')

chead = ['นักษัตร', 'ถูกโฉลก (สามประสาน)', 'คู่มิตร (หกประสาน)', 'ไม่ถูก: ชง (ตรงข้าม)', 'ไม่ถูก: ไห่', 'ไม่ถูก: ผั่ว', 'ไม่ถูก: เฮ้ง']
(exp / 'compat.tsv').write_text('\n'.join('\t'.join(r) for r in [chead] + compat) + '\n', encoding='utf-8')
khead = ['คนเกิด'] + [f'{r} ({m})' for r, m in ROLES]
(exp / 'colours.tsv').write_text('\n'.join('\t'.join(r) for r in [khead] + colours) + '\n', encoding='utf-8')

tpl = (ROOT / 'tools' / 'tables-template.html').read_text(encoding='utf-8')
data = json.dumps({'chong': chong, 'ages': ages, 'compat': compat, 'colours': colours, 'roles': ROLES}, ensure_ascii=False, separators=(',', ':'))
assert tpl.count('/*DATA*/') == 1
(ROOT / 'tables.html').write_text(tpl.replace('/*DATA*/', data), encoding='utf-8')
print(f'{len(chong)} clash years ({chong[0][0]}-{chong[-1][0]}), {len(ages)} birth years, {len(compat)} signs, {len(colours)} birth days; wrote tables.html')
