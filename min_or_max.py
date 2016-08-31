def min_or_max_index(L, B):
    """list, bool -> tuple

    If bool is True, return a tuple holding the min from a list and its index.
    If bool is False, return a tuple holding the max from a list and its index.

    >>>min_index([1, 4, 6, 78, 3])
    (1, 0)
    """
    min_val = L[0]
    max_val = L[0]
    min_i = 0
    max_i = 0
    for i in range(len(L)):
        if L[i] < min_val:
            min_val = L[i]
            min_i = i
        elif L[i] > max_val:
            max_val = L[i]
            max_i = i
    if B is True:
        return (min_val, min_i)
    elif B is False:
        return (max_val, max_i)
    else:
        print("Something went wrong.")


print(min_or_max_index([9, 5, 6, 4, 28], True))

print(min_or_max_index([9, 5, 6, 4, 28], False))
