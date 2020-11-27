from urllib.parse import quote

def default(args):
    return 'https://www.google.com/search?q={}'.format(' '.join(args))

def resolve(args=[]):
    if args:
        try:
            return 'https://www.google.com/search?q={}'.format(quote(' '.join(args[1:])))
        except:
            return 'https://www.google.com/search?q={}'.format(quote(args[0]))
    else:
        return 'https://www.google.com'