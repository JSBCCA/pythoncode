def find_min(L, b):
    """(list, int) -> int
    Precondition: L[b:] is not empty.
    Return the index of the smallest value in L[b:].

    >>> find_min([3, -1, 7, 5], 0)
    1
    """
    smallest = b
    i = b + 1
    while i != len(L):
        if L[i] < L[smallest]:
            smallest = i
        i = i + 1
    return smallest


def selection_sort(L):
    """(list) -> NoneType
    Reorder the items in L from smallest to largest.

    >>> L = [3, 4, 7, -1, 2, 5]
    >>> selection_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """
    i = 0
    while i != len(L):
        smallest = find_min(L, i)
        L[i], L[smallest] = L[smallest], L[i]
        i = i + 1


def insert(L, b):
    """(list, int) -> NoneType

    Precondition: L[0:b] is already sorted.
    Insert L[b] where it belongs in L[0:b + 1].

    >>> L = [3, 4, -1, 7, 2, 5]
    >>> insert(L, 2)
    >>> L
    [-1, 3, 4, 7, 2, 5]
    """
    i = b
    while i != 0 and L[i - 1] >= L[b]:
        i = i - 1
    value = L[b]
    del L[b]
    L.insert(i, value)


def insertion_sort(L):
    """(list) -> NoneType
    Reorder the items in L from smallest to largest.

    >>> L = [3, 4, -1, 7, 2, 5]
    >>> insertion_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """
    i = 0
    while i != len(L):
        insert(L, i)
        i = i + 1


def merge(L1, L2):
    """(list, list) -> list
    Merge sorted lists L1 and L2 into a new list and return that new list.
    >>> merge([1, 3, 4, 6],[1, 2, 5, 7])
    [1, 1, 2, 3, 4, 5, 6, 7]
    """
    newL = []
    i1 = 0
    i2 = 0
    while i1 != len(L1) and i2 != len(L2):
        if L1[i1] <= L2[i2]:
            newL.append(L1[i1])
            i1 += 1
        else:
            newL.append(L2[i2])
            i2 += 1
    newL.extend(L1[i1:])
    newL.extend(L2[i2:])
    return newL


def merge_sort(L):
    """(list) -> NoneType
    >>> L = [3, 4, -1, 7, 2, 5]
    >>> merge_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """
    workspace = []
    for i in range(len(L)):
        workspace.append([L[i]])
    i = 0
    while i < len(workspace) - 1:
        L1 = workspace[i]
        L2 = workspace[i + 1]
        newL = merge(L1, L2)
        workspace.append(newL)
        i += 2
    if len(workspace) != 0:
        L[:] = workspace[-1][:]


def bubble_sort(L):
    """(list) -> list
    Reorder the items in L from smallest to largest.

    >>> bubble_sort([6, 5, 4, 3, 7, 1, 2])
    [1, 2, 3, 4, 5, 6, 7]
    """
    # keep sorted section at end of list
    # repeated until all is sorted
    for _ in L:
        # traverse the list
        for i in range(len(L) - 1):
            # compare pairs
            if L[i] > L[i + 1]:
                # swap larger elements into the higher position
                # a, b = b, a
                L[i], L[i + 1] = L[i + 1], L[i]
    return L


def bubble_sort2(L):
    """(list) -> NoneType
    Reorder the items in L from smallest to largest.

    >>> bubble_sort([6, 5, 4, 3, 7, 1, 2])
    [1, 2, 3, 4, 5, 6, 7]
    """
    # keep sorted section at beginning of list
    # repeated until all is sorted
    for _ in L:
        # traverse the list
        for i in range(1, len(L)):
            # compare pairs
            if L[i] < L[i - 1]:
                # swap smaller elements into the lower position
                # a, b = b, a
                L[i], L[i - 1] = L[i - 1], L[i]
    return L
