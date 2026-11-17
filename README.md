# RigaRada Oracle (Draft 01)

A one-page viewer for the nine RigaRada oracle decks:

| # | Button | Deck | Cards | Card content |
|---|---|---|---|---|
| 1 | US-TH | คนไทยในอเมริกา · Thai Life in America | 605 | One keyword per card, 31 groups |
| 2 | Appearance | รูปลักษณ์หน้าตา | 300 | Name and keywords; the first 90 also have a draft meaning |
| 3 | Health | สุขภาพและโรคภัย | 300 | Name and keywords; the first 90 also have a draft meaning |
| 4 | Occupations | ชื่ออาชีพบนโลก | 300 | Name and keywords; the first 90 also have a draft meaning |
| 5 | Traits | นิสัยความคิดของคน | 300 | Name and keywords; the first 90 also have a draft meaning |
| 6 | US States | รัฐในอเมริกา | 50 | Thai and English name, US Census region |
| 7 | Countries | ประเทศทั่วโลก | 195 | Thai and English name, continent |
| 8 | Thai Provinces | จังหวัดในไทย | 77 | Thai and English name, region |
| 9 | Prognosis | อาการและแนวโน้มสุขภาพ · Health Outlook & Prognosis | 300 | Thai and English name and two keywords, 6 groups of 50 |

Deck 1 uses the keyword list exactly as approved, plus the 41 extra Thai-US keywords requested later (group "Thai-US เพิ่มเติม"), with no meaning added. Exact duplicates were removed, and run-together words were split. Every change is listed in `data/us-th-keywords-notes.md`. Decks 2–5 were extended from 90 to 300 cards each at RigaRada's request. The 210 new cards per deck (35 per group) are appended after the original 90, so the original IDs did not change, and they carry a Thai and English name and two keywords with no meaning yet. No name repeats within a deck. Deck 6 has the 50 states (Washington, D.C. is not a state). Deck 7 has the 193 UN member states plus the two UN observer states, Vatican City and Palestine. Deck 8 has the 76 provinces plus Bangkok, in the six-region grouping. Deck 9 is a separate deck RigaRada asked for on 17 Nov: words that describe how an illness goes rather than what it is (how fast it heals, how hard it is to treat, how severe it is, the outlook, the kind of care, and overall health). None of its names repeat a card in deck 3.

How a reading works:

- **Shuffle first.** Each reading starts with the cards in one face-down pile. Pressing "สับไพ่" shuffles the whole deck and mixes the cards on screen, then lays out every card in the deck on the panel (605 for US-TH, 195 for Countries, and so on) in 10 columns. The panel scrolls up and down and keeps its place after each pick. "สับไพ่ใหม่" shuffles again at any point before the last pick.
- **Tap to pick.** Tap any card on the panel to pick it; there is no sideways scrolling. Tap a picked card in the tray to put it back on the panel. While you pick, the tray already has the shape of the reading: 4 in one row, 6 as 3+3, 9 as 3×3 and 10 in the flat 10-card layout.
- **1, 3, 4, 6, 9 or 10 cards.** The cards turn over as soon as the last one is picked, with no confirmation step. 1 card is "ไพ่ของคุณ" and 3 cards are past, present and future. 4 cards are laid out in one row, 6 cards as two rows of 3 and 9 cards as 3×3, labelled ใบที่ 1, 2, 3 and so on and sized to fit the screen. The 10-card reading is laid flat with every face showing and no card across another, following RigaRada's reference image: 1 in the centre, 2 to its left, 3 above it, 4 to its right, 5 below it, 6 above 2, and 7–10 up the right-hand column from bottom to top. Every card is the same size and the layout fits the screen. On short screens, number badges replace the position names.
- **Large view.** Tap any revealed card to see it large, with its keywords and meaning, and use Previous/Next to move between positions.
- **Keyboard and motion.** Arrow keys and Home/End move between cards on the panel, and Enter or Space picks one. Delete removes a picked card, and Ctrl/⌘+Z undoes. The page follows `prefers-reduced-motion` by default, with a manual override under "ตัวเลือกเพิ่มเติม"; with reduced motion the shuffle happens without animation.

Cards are text only, with no images. The card back is a plain striped pattern with a thin border, with no circle in the middle. Each face shows the Thai name, the English name where there is one, and for decks 6–8 the region or continent. Switching decks starts a new reading with a freshly shuffled deck.

## Status: public

This repo is **public**, and the page is published on GitHub Pages: https://victoradanaith.github.io/rigarada-oracle/

Anyone on the internet can read everything here: the source files in `data/`, the full `index.html`, and the git history.

## ⚠️ Code 2456 only hides the screen. It is not real protection

The page asks for code `2456` before it shows the cards, but that check runs in the browser. The code and every card are written in plain text inside `index.html`, and the repo is public. Anyone can read every card with View Source, from GitHub, or by downloading `data/`, without the code.

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
