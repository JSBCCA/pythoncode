def total_len(s1, s2):
    """ (str, str) -> int

    Return sum of the lengths of s1 and s2.

    >>> total_len("bob", "go")
    5

    >>>total_len("hey", "and")
    6

    """
    return (len(s1 + s2))


print(total_len("hello", "guy"))
