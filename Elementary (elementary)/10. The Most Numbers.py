def checkio(*args):
    if args:
        return max(args) - min(args)
    else:
        return 0


if __name__ == '__main__':
    checkio(-0.07)
