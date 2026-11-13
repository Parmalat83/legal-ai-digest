"""legal-ai-digest: personal, non-commercial, read-only Reddit digest.

Once per day, reads recent public posts (and top comments) from a few
legal-tech subreddits via Reddit's official Data API and writes them to a
local JSON file, which is then summarized privately for a single user.

Read-only: no posting, commenting, voting, or messaging. No data resale,
no AI model training. Fewer than 100 API requests per day.
"""
import json
import os
import time

import praw

SUBREDDITS = ["legaltech", "Lawyertalk", "LawFirm"]
POSTS_PER_SUB = 25
COMMENTS_PER_POST = 5
WINDOW_SECONDS = 24 * 3600


def main():
    reddit = praw.Reddit(
        client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_CLIENT_SECRET"],
        user_agent="script:legal-ai-digest:v0.1 (by u/Dear_Computer_9622)",
    )
    reddit.read_only = True
    cutoff = time.time() - WINDOW_SECONDS
    out = []
    for name in SUBREDDITS:
        for post in reddit.subreddit(name).new(limit=POSTS_PER_SUB):
            if post.created_utc < cutoff:
                continue
            post.comment_sort = "top"
            post.comments.replace_more(limit=0)
            out.append({
                "subreddit": name,
                "title": post.title,
                "url": f"https://www.reddit.com{post.permalink}",
                "score": post.score,
                "num_comments": post.num_comments,
                "created_utc": post.created_utc,
                "selftext": post.selftext[:4000],
                "top_comments": [c.body[:1000] for c in post.comments[:COMMENTS_PER_POST]],
            })
    with open("digest_input.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(out)} posts")


if __name__ == "__main__":
    main()
