def linear_search(lst, value):
    """(list, object) -> int

    Return the index of the first occurence of value in lst, or return -1 if
    value is not in lst.

    >>>linear_search([2, 5, 1, -3], 5)
    1

    >>>linear_search([2, 4, 2], 2)
    0

    >>>linear_search([], 5)
    -1
    """
    lst.append(value)
    i = 0
    while lst[i] != value:
        i = i + 1
    lst.pop()
    if i == len(lst):
        return -1
    else:
        return i
