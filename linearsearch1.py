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
    i = 0
    while i != len(lst) and lst[i] != value:
        i = i + 1
    if i == len(lst):
        return -1
    else:
        return i


def reverse_linear_search(lst, value):
    """(list, object) -> int

    Return the index of the first occurence of value in lst, or return -1 if
    value is not in lst.

    >>>reverse_linear_search([2, 5, 1, -3], 5)
    1

    >>>reverse_linear_search([2, 4, 2], 2)
    2

    >>>reverse_linear_search([], 5)
    -1
    """
    i = len(lst) - 1
    while i != -1 and lst[i] != value:
        i = i + 1
    if i == -1:
        return -1
    else:
        return i
