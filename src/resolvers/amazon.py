def resolve(args=[]):
    if args:
        return 'https://www.amazon.com/s?k={}'.format('+'.join(args[1:]))
    else:
        return 'https://www.amazon.com'