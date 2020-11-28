from urllib.parse import quote

NSFW_FLAG = "&include_over_18=on"
SEARCH_URL = "https://www.reddit.com/search?q={}{}"
SUBREDDIT_URL = "https://reddit.com/r/{}"
SUBREDDITS_URL = "https://www.reddit.com/subreddits"
REDDIT_URL = "https://reddit.com"


def subreddit(args=[]):
    if args[0][2:]:
        return SUBREDDIT_URL.format(args[0][2:])
    else:
        return SUBREDDITS_URL


def search(args=[]):
    if len(args) > 1:
        nsfw = True if "18" in args[0] or "nsfw" in args[0] else False
        return SEARCH_URL.format(quote(" ".join(args[1:])), NSFW_FLAG if nsfw else "")
    else:
        return REDDIT_URL
