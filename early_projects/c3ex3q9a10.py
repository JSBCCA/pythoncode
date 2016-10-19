def square(n):
    """ (int) -> int

    Return a number squared.

    >>> square(7)
    49

    >>> square(12)
    144


    """
    return (n * n)


if __name__ == '__main__':
    a = int(input("Give a number:"))
    print(square(a))
