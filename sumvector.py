sv1 = {0: 1, 1: 1, 2: 3}
sv2 = {0: 4, 1: 5, 2: 6}


def sparse_add(sv1, sv2):
    """dict, dict -> dict

    Returns a new dictionary that is the sum of the other two.

    >>>sparse_add(sv1, sv2)
    {0: 5, 1: 6, 2: 9}
    """
    newdict = {}
    keys = set(sv1.keys()) | set(sv2.keys())
    for key in keys:
        x = sv1.get(key, 0) + sv2.get(key, 0)
        newdict[key] = x
    return (newdict)


print(sparse_add(sv1, sv2))
