def resolve(args=[]):
    if len(args) > 1:
        return 'https://www.amazon.com/s?k={}'.format('+'.join(args[1:]))
    else:
        return 'https://www.amazon.com'