# RigaRada Oracle (Draft 01)

A one-page viewer for the eight RigaRada oracle decks:

| # | Button | Deck | Cards | Card content |
|---|---|---|---|---|
| 1 | US-TH | คนไทยในอเมริกา · Thai Life in America | 565 | One keyword per card, 30 groups |
| 2 | Appearance | รูปลักษณ์หน้าตา | 90 | Name, keywords, draft meaning |
| 3 | Health | สุขภาพและโรคภัย | 90 | Name, keywords, draft meaning |
| 4 | Occupations | ชื่ออาชีพบนโลก | 90 | Name, keywords, draft meaning |
| 5 | Traits | นิสัยความคิดของคน | 90 | Name, keywords, draft meaning |
| 6 | US States | รัฐในอเมริกา | 50 | Thai and English name, US Census region |
| 7 | Countries | ประเทศทั่วโลก | 195 | Thai and English name, continent |
| 8 | Thai Provinces | จังหวัดในไทย | 77 | Thai and English name, region |

Deck 1 uses the keyword list exactly as approved, with no meaning added. Exact duplicates were removed, and run-together words were split. Every change is listed in `data/us-th-keywords-notes.md`. Deck 6 has the 50 states (Washington, D.C. is not a state). Deck 7 has the 193 UN member states plus the two UN observer states, Vatican City and Palestine. Deck 8 has the 76 provinces plus Bangkok, in the six-region grouping.

The layout is the same as the RigaRada tarot prototype (`rigarada-mobile-fan-v2.html`):

- **Fan Arc.** Cards lie face down in a fan. Swipe to browse (a swipe never picks a card), and tap the centre card or press "เลือกใบนี้" to pick one card at a time.
- **1, 3 or 10 cards.** The 10-card reading is laid out as a Celtic Cross: 1 in the centre, 2 across 1 (turned 90°), 3 below, 4 left, 5 above, 6 right, and 7–10 up the right-hand column from bottom to top. Every card is the same size and the layout fits the screen. On short screens, number badges replace the position names.
- **Reveal and large view.** A confirmation dialog appears before cards are turned over. Tap any revealed card to see it large, with its keywords and meaning, and use Previous/Next to move between positions.
- **Keyboard and motion.** Arrow keys, Home/End and PageUp/PageDown move through the fan. Enter or Space picks a card, Delete removes it, and Ctrl/⌘+Z undoes. The page follows `prefers-reduced-motion` by default, with a manual override under "ตัวเลือกเพิ่มเติม".

Cards are text only, with no images. Each face shows the Thai name, the English name where there is one, and for decks 6–8 the region or continent. Switching decks starts a new reading with a freshly shuffled deck.

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
