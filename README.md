# RigaRada Oracle (Draft 01)

A one-page viewer for the twenty-three RigaRada oracle decks:

| # | Button | Deck | Cards | Card content |
|---|---|---|---|---|
| 1 | US-TH | คนไทยในอเมริกา · Thai Life in America | 605 | One keyword per card, 31 groups |
| 2 | Appearance | รูปลักษณ์หน้าตา | 500 | Name and keywords; the first 90 and the 200 added on 19 Nov also have a draft meaning and image concept |
| 3 | Health | สุขภาพและโรคภัย | 300 | Name and keywords; the first 90 also have a draft meaning |
| 4 | Occupations | ชื่ออาชีพบนโลก | 300 | Name and keywords; the first 90 also have a draft meaning |
| 5 | Traits | นิสัยความคิดของคน | 500 | Name and keywords; the first 90 also have a draft meaning |
| 6 | US States | รัฐในอเมริกา | 50 | Thai and English name, US Census region |
| 7 | Countries | ประเทศทั่วโลก | 195 | Thai and English name, continent |
| 8 | Thai Provinces | จังหวัดในไทย | 77 | Thai and English name, region |
| 9 | Prognosis | อาการและแนวโน้มสุขภาพ · Health Outlook & Prognosis | 300 | Thai and English name and two keywords, 6 groups of 50 |
| 10 | Sacred World | สิ่งศักดิ์สิทธิ์ทั่วโลก · Sacred Figures & Places of the World | 500 | Thai and English name, two keywords and a one-line description on the face, 9 groups |
| 11 | Karma | วิบากกรรม · Karma Across Lifetimes | 500 | Thai and English name and two keywords, 9 groups |
| 12 | Sacred Thailand | สิ่งศักดิ์สิทธิ์ในไทย · Sacred Figures & Places of Thailand | 1,000 | Thai and English name and two keywords, 16 groups |
| 13 | Karma Remedy | วิธีแก้กรรม · Ways to Ease Karma | 500 | Thai and English name and two keywords, 8 groups |
| 14 | Love | ความรักและความสัมพันธ์ · Love & Relationships | 1,000 | Thai and English name and two keywords, 17 groups |
| 15 | Workplace | เรื่องในที่ทำงาน · Work & Career | 500 | Thai and English name and two keywords, 14 groups |
| 16 | Visa & Abroad | สัญชาติ วีซ่า และต่างประเทศ · Visas, Status & Life Abroad | 500 | Thai and English name and two keywords, 13 groups |
| 17 | Housing | ที่อยู่อาศัย · Home & Housing | 500 | Thai and English name and two keywords, 14 groups |
| 18 | Study | การเรียน · Study & Education | 500 | Thai and English name and two keywords, 14 groups |
| 19 | Guidance | การแนะแนวชีวิต · Life Guidance | 500 | Every card starts with one of 7 openings, which are its groups |
| 20 | Timing | ไพ่บอกเวลา · Timing | 500 | Thai and English name and two keywords, 23 groups |
| 21 | Numbers | ตัวเลข 0–999 · Numbers 0–999 | 1,000 | The number, its English words, digit count and digit sum, 10 groups of 100 |
| 22 | Zodiac | ปีนักษัตรและธาตุจีน · Chinese Zodiac & Elements | 500 | Thai and English name and two keywords, 19 groups |
| 23 | Daily Life | ปัญหาอุปสรรคในชีวิตประจำวัน · Everyday Ups & Downs | 500 | 256 obstacles and 244 good turns, 21 groups |

Deck 1 uses the keyword list exactly as approved, plus the 41 extra Thai-US keywords requested later, with no meaning added. On 17 Nov (23:38–23:42) RigaRada circled the categories to merge in four colours, so its 30 posted groups now show as 9: the circled groups became "คน ความรัก และความสัมพันธ์", "บุญ โชคลาภ และชีวิต", "เงิน ธุรกิจ และฐานะ" and "บ้าน ทิศทาง และสถานที่", and the extra Thai-US keywords were placed in the group that fits each one. The mapping is in `tools/keywords.py`; card IDs and order did not change. Exact duplicates were removed, and run-together words were split. Every change is listed in `data/us-th-keywords-notes.md`. Decks 2–5 were extended from 90 to 300 cards each at RigaRada's request. The 210 new cards per deck (35 per group) are appended after the original 90, so the original IDs did not change, and they carry a Thai and English name and two keywords with no meaning yet. No name repeats within a deck. Deck 6 has the 50 states (Washington, D.C. is not a state). Deck 7 has the 193 UN member states plus the two UN observer states, Vatican City and Palestine. Deck 8 has the 76 provinces plus Bangkok, in the six-region grouping. Deck 9 is a separate deck RigaRada asked for on 17 Nov: words that describe how an illness goes rather than what it is (how fast it heals, how hard it is to treat, how severe it is, the outlook, the kind of care, and overall health). None of its names repeat a card in deck 3. Deck 10 (requested 17 Nov, 21:16) covers founders, Buddhas and bodhisattvas, Hindu, Chinese, Japanese and Korean deities, saints and angels, spiritual teachers who have died, sacred images and objects, well-known belief systems, and sacred places outside Thailand. It includes every religion except Islam, and leaves out Thai figures and places, which belong to the separate Thai deck RigaRada asked for at 21:14. Deck 11 (21:25) describes karma from past and present lives, good and bad, across beliefs worldwide. Its cards are belief content for reflection, not statements of fact. Since 18 Nov every card starts with one of the openings RigaRada asked for (23:57 and 00:03): กรรมจาก… ผลบุญจาก… อดีตเคยเป็น… อดีตเคยทำ… สร้างบุญโดย… ถ้า…จะเพิ่มกรรมเรื่อง… อนาคตจะเป็น… อนาคตจะมี… and เป็นคนมีพลังพิเศษในเรื่อง…, and those openings are its nine groups. Deck 12 (21:14, confirmed 18 Nov) is the Thai counterpart of deck 10: important Buddha images and postures, amulets and sacred objects, revered monks who have died, kings and heroes people pay respect to, deities and spirits in Thai belief, shrines and city pillars, temples and stupas by region, Christian, Hindu, Sikh and Chinese places of worship, rites and festivals, and chants. It includes every religion except Islam. Only names whose details could be stated with confidence were kept; living monks are left out. Some deities, such as Brahma, Ganesha and Guanyin, appear in both deck 10 and deck 12, because they are also worshipped in Thailand. Decks 13–18 were requested on 18 Nov between 00:02 and 00:46. Deck 13 (ways to ease karma) has 450 Thai Buddhist and Thai folk-belief cards and 50 from other faiths and traditions worldwide (Islam is left out, as in decks 10 and 12); sacred places name the province or country. The first keyword on each card says what kind of claim it is: ความเชื่อ (a belief or tradition), แนวปฏิบัติ (general good practice), มีงานวิจัยสนับสนุน (a practice with research behind it, such as mindfulness or forest walks) or ข้อเท็จจริง (a plain fact, such as Thailand's 1323 mental-health hotline or seeing a doctor for symptoms). Deck 14 covers love for every gender and orientation, hopes and heartbreak, status, obstacles, what to change, whether to continue, a partner's looks and attitudes, likeness and difference in ethnicity, religion and culture, family, third parties for better and worse, and belief-based remedies. Deck 15 covers job hunting, interviews, results, bosses and colleagues, pay, promotion, transfers and leaving, risks, and belief-based remedies. Deck 16 covers visas, green cards, citizenship, interviews in Thailand and abroad, border control, partner visas, and long-term life in Thailand or abroad. Words such as "แต่งปลอม", "เอกสารปลอม" and "ไม่เนียนถูกจับได้" appear only as reading keywords tagged ผิดกฎหมาย or ความเสี่ยง; the deck gives no method for faking documents or avoiding immigration control, and visa names are given without fees, quotas or current rules, which change and must be checked with official sources. Deck 17 covers buying, selling, renting, loans and budgets, contracts, housemates and landlords, repairs, location and direction, moving, feng shui and household spirits, positive and negative. Deck 18 covers study only: levels from kindergarten to postdoc, applications, exams, interviews, scholarships and research fields, paying for study, workload, ability, classmates and teachers, atmosphere and location, outcomes, and certificates. Within each deck no name repeats; a few short names also appear in an older deck (for example ใจดี in Traits and Love).

## Category picker

US-TH, Appearance, Traits, Sacred World, Karma, Sacred Thailand and decks 13–23 show a "หมวด" dropdown under the deck buttons: "ทุกหมวด" (every card, the default) or one category at a time, with its card count. Choosing a category starts a new reading from that category only. Which decks get the dropdown is set by `CAT_PICK` in `tools/build.py`.

## Sheet export

`python3 tools/build.py` also writes `data/sheet-export/<prefix>.tsv`, one row per card in the main sheet's column order (ID, category, Thai, English, keywords, meaning, image concept). The main Google Sheet can pull a deck with `=IMPORTDATA(".../data/sheet-export/<prefix>.tsv")`.

How a reading works:

- **Shuffle first.** Each reading starts with the cards in one face-down pile. Pressing "สับไพ่" shuffles the whole deck and mixes the cards on screen, then lays out every card in the deck on the panel (605 for US-TH, 195 for Countries, and so on) in 10 columns. The panel scrolls up and down and keeps its place after each pick. "สับไพ่ใหม่" shuffles again at any point before the last pick.
- **Tap to pick.** Tap any card on the panel to pick it; there is no sideways scrolling. Tap a picked card in the tray to put it back on the panel. While you pick, the tray already has the shape of the reading: 4 in one row, 6 as 3+3, 9 as 3×3 and 10 in the flat 10-card layout.
- **1, 2, 3, 4, 6, 9, 10 or 30 cards.** A spread larger than the chosen category is greyed out, and the page drops to the largest spread that fits. The cards turn over as soon as the last one is picked, with no confirmation step. 1 card is "ไพ่ของคุณ" and 3 cards are past, present and future. 2 cards sit side by side, 30 cards three to a row (the page scrolls). 4 cards are laid out in one row, 6 cards as two rows of 3 and 9 cards as 3×3, labelled ใบที่ 1, 2, 3 and so on and sized to fit the screen. The 10-card reading is laid flat with every face showing and no card across another, following RigaRada's reference image: 1 in the centre, 2 to its left, 3 above it, 4 to its right, 5 below it, 6 above 2, and 7–10 up the right-hand column from bottom to top. Every card is the same size and the layout fits the screen. On short screens, number badges replace the position names.
- **Large view.** Tap any revealed card to see it large, with its keywords and meaning, and use Previous/Next to move between positions.
- **Keyboard and motion.** Arrow keys and Home/End move between cards on the panel, and Enter or Space picks one. Delete removes a picked card, and Ctrl/⌘+Z undoes. The page follows `prefers-reduced-motion` by default, with a manual override under "ตัวเลือกเพิ่มเติม"; with reduced motion the shuffle happens without animation.

Cards are text only, with no images. The card back is a plain striped pattern with a thin border, with no circle in the middle. Each face shows the Thai name, the English name where there is one, and for decks 6–8 the region or continent. Switching decks starts a new reading with a freshly shuffled deck.

## Status: public

This repo is **public**, and the page is published on GitHub Pages: https://victoradanaith.github.io/rigarada-oracle/

Anyone on the internet can read everything here: the source files in `data/`, the full `index.html`, and the git history.

## ⚠️ Code 59 only hides the screen. It is not real protection

The page asks for code `59` before it shows the cards, but that check runs in the browser. The code and every card are written in plain text inside `index.html`, and the repo is public. Anyone can read every card with View Source, from GitHub, or by downloading `data/`, without the code.

The code only keeps casual visitors from seeing the cards straight away. Don't put anything in this repo that must stay secret.

## Files

- `index.html` is the whole site, with the data built in. Open it straight in a browser; there are no dependencies.
- `data/` holds the sources: `us-th-keywords-source.txt` (the deck 1 keyword list, one `#` line per group) and `*-draft01.txt` for decks 2–8 (`# category`, then `Thai|English|keywords|meaning|image concept` per card).
- `tools/keywords.py` turns the deck 1 list into cards and writes `data/us-th-keywords-notes.md`.
- `tools/build.py` and `tools/template.html` rebuild `index.html` from `data/`:

```bash
python3 tools/build.py
```

The meanings are prompts for reflection. They don't predict outcomes and aren't medical, legal or immigration advice.

## Clash-year and age tables (19 Nov)

`tables.html` (linked under the card options) has two tables behind the same code. The clash-year calendar lists every year from 2000 to 3000 with its พ.ศ. year, sign and element, and the four signs that clash with it, using the four-level scheme common in Thai sources: 100% is the sign opposite the year, 75% the year's own sign, 50% the sign in "harm" (ไห่) with it and 25% the sign in "break" (ผั่ว) with it. Other schools split the levels differently, and the Chinese year starts around 4 February, not 1 January; the page says both. The age table lists birth years 1900–2026 with พ.ศ., sign and element (such as ม้าทอง) and the age reached in a chosen year. `python3 tools/tables.py` builds the page from `tools/tables-template.html` and writes `data/sheet-export/chong.tsv` and `ages.tsv` for the main sheet.

Decks 19–23 (19 Nov, 00:44–02:55): Guidance cards begin ต้องทำสิ่งนี้เพราะ… / ห้ามทำสิ่งนี้เพราะ… / ถ้าทำสิ่งนี้แล้วจะดีเพราะ… / ถ้าทำสิ่งนี้แล้วจะแย่เพราะ… / ไม่ทำสิ่งนี้ก็ได้เพราะ… / ถ้าทำสิ่งนี้แล้วจะ… / ถ้าไม่ทำสิ่งนี้แล้วจะ…. Timing mixes general phrases (เร็วๆ นี้, อีกนานมาก), within N hours, days, weeks, months and years, weekdays and parts of the day, months, dates, the lunar calendar, seasons, festivals, the next 12 years and life stages. Zodiac has one group per sign (the sign, its five elements, 12 things it should do and 11 it should not) plus the elements, the generating and restraining cycles, element correspondences, each sign's element, direction and month, harmonies and clashes, and clash-year remedies; its advice is belief, tagged ความเชื่อ. Numbers runs 0–999 with no meanings. Daily Life covers travel, weather, home, money, work, technology, health, food, people, paperwork, animals, shopping, family, school, holidays, mood and community. Appearance and Traits each gained 200 cards (about 33 per group), appended so earlier IDs did not change.
