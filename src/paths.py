#pylint:disable=unused-wildcard-import,undefined-variable,import-error,anomalous-backslash-in-string

import re
from resolvers import *

PATHS = {
    'a(?:\ .+)?': amazon.resolve,
    'f(?:\ .+)?': facebook.resolve,
    'g(?:\ .+)?': google.search,
    'j[wksn]?(?:\ .+)?': jisho.resolve,
    'kb(?:\ .+)?': kotobank.word_search,
    'r\/\w*': reddit.subreddit,
    're?((18)|(nsfw))? .+': reddit.search,
    't@.+': twitter.at,
    'yt(?:\ .+)?': google.youtube_search,
}

def resolve_path(command, default=google.default):
    for key, path in PATHS.items():
        if re.match(r"^{}$".format(key), command.strip(), re.IGNORECASE):
            return path
    return default