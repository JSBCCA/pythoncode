def KtoM(k):
    """ (number) -> number

    Returns miles from kilometers.

    >>> KtoM(5)
    3.106855

    >>> KtoM(9)
    5.592339

    """
    return k * 0.621371


if __name__ == '__main__':
    blah = int(input("Give a distance in Kilometers pls: "))
    print(KtoM(blah))
