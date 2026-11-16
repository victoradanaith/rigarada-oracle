# RigaRada Oracle (Draft 01)

A one-page viewer for the five RigaRada oracle decks, 90 cards each:

| # | Button | Deck |
|---|---|---|
| 1 | US-TH | คนไทยในอเมริกา · Thai Life in America |
| 2 | Appearance | รูปลักษณ์หน้าตา |
| 3 | Health | สุขภาพและโรคภัย |
| 4 | Occupations | ชื่ออาชีพบนโลก |
| 5 | Traits | นิสัยความคิดของคน |

The layout is the same as the RigaRada tarot prototype (`rigarada-mobile-fan-v2.html`):

- **Fan Arc.** Cards lie face down in a fan. Swipe to browse (a swipe never picks a card), and tap the centre card or press "เลือกใบนี้" to pick one card at a time.
- **1, 3 or 10 cards.** The 10-card reading is laid out as a Celtic Cross: 1 in the centre, 2 across 1 (turned 90°), 3 below, 4 left, 5 above, 6 right, and 7–10 up the right-hand column from bottom to top. Every card is the same size and the layout fits the screen. On short screens, number badges replace the position names.
- **Reveal and large view.** A confirmation dialog appears before cards are turned over. Tap any revealed card to see it large, with its keywords and meaning, and use Previous/Next to move between positions.
- **Keyboard and motion.** Arrow keys, Home/End and PageUp/PageDown move through the fan. Enter or Space picks a card, Delete removes it, and Ctrl/⌘+Z undoes. The page follows `prefers-reduced-motion` by default, with a manual override under "ตัวเลือกเพิ่มเติม".

Cards are text only, with no images. Each face shows the Thai and English name. Switching decks starts a new reading with a freshly shuffled deck.

## Status: public

This repo is **public**, and the page is published on GitHub Pages: https://victoradanaith.github.io/rigarada-oracle/

Anyone on the internet can read everything here: the source files in `data/`, the full `index.html`, and the git history.

## ⚠️ Code 2456 only hides the screen. It is not real protection

The page asks for code `2456` before it shows the cards, but that check runs in the browser. The code and all 450 cards are written in plain text inside `index.html`, and the repo is public. Anyone can read every card with View Source, from GitHub, or by downloading `data/`, without the code.

The code only keeps casual visitors from seeing the cards straight away. Don't put anything in this repo that must stay secret.

## Files

- `index.html` is the whole site, with the data built in. Open it straight in a browser; there are no dependencies.
- `data/` holds the sources: `us-th-draft01.json` (a snapshot of the Google Sheet) and `*-draft01.txt` for decks 2–5.
- `tools/build.py` and `tools/template.html` rebuild `index.html` from `data/`:

```bash
python3 tools/build.py
```

The meanings are prompts for reflection. They don't predict outcomes and aren't medical, legal or immigration advice.
