from urllib.parse import quote

def search(args=None):
    if args:
        return 'https://www.facebook.com/search/top/?q={}'.format(quote(' '.join(args)))
    else:
        return 'https://www.facebook.com'

