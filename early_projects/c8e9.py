def sfl(L):
    """ (list) -> bool
    Precondition: len(L) >= 2

    Return True if and only if first item of the list is same as last.

    >>> sfl([3, 4, 2, 8, 3])
    True

    >>> sfl([a, b, c])
    False

    """
    return (L[0] == L[-1])


def is_longer(L1, L2):
    """ (list, list) -> bool
    Return True if and only if the length of L1 is longer than L2.

    >>> is_longer([1, 2, 3], [4, 5])
    True

    >>> is_longer([a, b, c], [d, e, f])
    False

    """
    return len(L1) > len(L2)


if __name__ == '__main__':
    a = input("What is the list? ").split()
    b = input("Another please: ").split()
    c = input("One more: ").split()
    d = is_longer(b, c)
    e = sfl(a)
    if e is True:
        print("The items at the beginning and end of List 1 are the same.")
    else:
        print("The items at the beginning and end of List 1 are not the"
              " same.")
    if d is True:
        print("The second list is longer than the third.")
    else:
        print("The second list is not longer than the third.")
