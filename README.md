# legal-ai-digest

A personal, non-commercial, **read-only** script that builds a private daily digest of public discussions in r/legaltech (and r/Lawyertalk, r/LawFirm) for one person.

- Runs once per day, under 100 Reddit Data API requests per day.
- Uses Reddit's official Data API (script app, read-only OAuth via PRAW).
- Never posts, comments, votes, or sends messages.
- No data resale, sharing, commercialization, or AI/ML model training.
- Data is kept only for the day's summary and is not retained long-term.

## Usage

```bash
pip install praw
export REDDIT_CLIENT_ID=...
export REDDIT_CLIENT_SECRET=...
python digest.py
```

Maintainer: u/Dear_Computer_9622
