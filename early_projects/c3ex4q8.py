def repeat(s, n):
    """ (str, int) -> str

    Return s repeated n times; if n is negative, return empty string.

    >>> repeat('yes', 4)
    'yesyesyesyes'

    >>>repeat('no', 0)
    ''

    """
    return (s * n)


print(repeat("Hello ", 5))
