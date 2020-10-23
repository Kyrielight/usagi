def usa(args=None):
        if args:
            return 'https://www.amazon.com/s?k={}'.format('+'.join(args))
        else:
            return 'https://www.amazon.com'
    
def japan(args=None):
    if args:
        return 'https://www.amazon.co.jp/s?k={}'.format('+'.join(args))
    else:
        return 'https://www.amazon.co.jp'