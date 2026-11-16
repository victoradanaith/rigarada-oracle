# RigaRada Oracle (Draft 01)

A one-page viewer for the five RigaRada oracle decks, 90 cards each:

| # | Button | Deck |
|---|---|---|
| 1 | US-TH | คนไทยในอเมริกา · Thai Life in America |
| 2 | Appearance | รูปลักษณ์หน้าตา |
| 3 | Health | สุขภาพและโรคภัย |
| 4 | Occupations | ชื่ออาชีพบนโลก |
| 5 | Traits | นิสัยความคิดของคน |

Cards are text only, with no images. Each card shows its ID, category, Thai and English name, keywords, draft meaning and image concept. You can filter by category, search, and draw one card at random.

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
