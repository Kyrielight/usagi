from urllib.parse import quote

def resolve(args=[]):
    if len(args) > 1:
        return 'https://www.facebook.com/search/top/?q={}'.format(quote(' '.join(args[1:])))
    else:
        return 'https://www.facebook.com'