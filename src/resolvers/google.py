from urllib.parse import quote

def default(args):
    return 'https://www.google.com/search?q={}'.format(quote(' '.join(args)))

def search(args=[]):
    if len(args) > 1:
        return 'https://www.google.com/search?q={}'.format(quote(' '.join(args[1:])))
    else:
        return 'https://www.google.com'

def youtube_search(args=[]):
    if len(args) > 1:
        return 'https://www.youtube.com/results?search_query={}'.format(quote(' '.join(args[1:])))
    else:
        return 'https://www.youtube.com'