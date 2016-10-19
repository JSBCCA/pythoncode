def absoadd(n, m):
    """(num, num) -> num

    Gives the absolute value of the difference of two numbers.

    >>> absoadd(5, 6)
    11
    """
    first = abs(n - m)
    return (first)


if __name__ == '__main__':
    a = int(input("just gimme number: "))
    b = int(input("just gimme number: "))
    print(absoadd(a, b))
