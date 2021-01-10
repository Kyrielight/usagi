from urllib.parse import quote

KOTOBANK_MAIN = "https://kotobank.jp/"
KOTOBANK_WORD_SEARCH = KOTOBANK_MAIN + "word/{}"

def word_search(args=[]):
    if len(args) < 1:
        return KOTOBANK_MAIN
    else:
        return KOTOBANK_WORD_SEARCH.format(quote(' '.join(args[1:])))