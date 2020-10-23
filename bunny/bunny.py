from urllib.parse import quote

from .commands import amazon
from .commands import facebook

class BunnyCommands(object):

    @staticmethod
    def a(args=None):
        return amazon.usa(args)
    
    @staticmethod
    def aj(args=None):
        return amazon.japan(args)
    
    @staticmethod
    def f(args=None):
        return BunnyCommands.fb(args)

    @staticmethod
    def fb(args=None):
        return facebook.search(args)

    @staticmethod
    def g(args=None):
        if args:
            return 'https://www.google.com/search?q={}'.format(quote(' '.join(args)))
        else:
            return 'https://www.google.com'
