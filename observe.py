def find_dups(L):
    """(list(nums)) -> set(nums)

    Returns a set of the numbers that appear multiple times in a list.

    >>>find_dups([7, 8, 7, 9])
    (7)

    >>>find_dups([5, 9, 5, 6, 3, 6])
    (5, 6)

    """
    duplicates = {}
    setdup = set()
    for i in L:
        duplicates[i] = duplicates.get(i, 0) + 1
        if duplicates[i] > 1:
            setdup.add(i)
    return (setdup)


find_dups([5, 5, 6, 5, 4, 3, 7, 4, 2])
