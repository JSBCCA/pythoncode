def triple(n):
    """ (number) -> number

    Returns triple a given number.

    >>> triple(9)
    27

    >>> triple(-5)
    -15

    >>> triple(1.1)
    3.3

    """
    one = n * 3
    return (one)


if __name__ == '__main__':
    blah = int(input("Give a number pls: "))
    print(triple(blah))
