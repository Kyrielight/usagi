from urllib.parse import quote

def default(args):
    return 'https://www.google.com/search?q={}'.format(quote(' '.join(args)))

def resolve(args=[]):
    if len(args) > 1:
        return 'https://www.google.com/search?q={}'.format(quote(' '.join(args[1:])))
    else:
        return 'https://www.google.com'