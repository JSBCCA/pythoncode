def binary_search(L, v):
    """(list, object) -> int

    Return the index of the first occurrence of value in L, or return -1
    if value is not in L.

    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 1)
    0
    """
    i = 0
    j = len(L) - 1
    while i != j + 1:
        m = (i + j) // 2
        if L[m] < v:
            i = m + 1
        else:
            j = m - 1
    if 0 <= i < len(L) and L[i] == v:
        return i
    else:
        return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
