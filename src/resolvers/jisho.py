from urllib.parse import quote

JISHO_URL = "https://jisho.org/search/"
WORDS = quote(" #words")
KANJI = quote(" #kanji")
SENTENCES = quote(" #sentences")
NAMES = quote(" #names")

def resolve(args=[]):
    if len(args) > 1:
        root_arg = args[0].lower() 
        rest_arg = ' '.join(args[1:])

        if root_arg == "jw":
            return _words(rest_arg)
        elif root_arg == "jk":
            return _kanji(rest_arg)
        elif root_arg == "js":
            return _sentences(rest_arg)
        elif root_arg == "jn":
            return _names(rest_arg)
        else:
            return _all(rest_arg)
    else:
        return "https://jisho.org"

def _all(args):
    return JISHO_URL + quote(args)

def _words(args):
    return JISHO_URL + quote(args) + WORDS

def _kanji(args):
    return JISHO_URL + quote(args) + KANJI

def _sentences(args):
    return JISHO_URL + quote(args) + SENTENCES

def _names(args):
    return JISHO_URL + quote(args) + NAMES