def count_dict_dups(dictionary):
    """dict -> int
    Returns a set of the integers that have duplicates.

    >>>count_dict_dups({'red': 1, 'blue': 2, 'green': 1, 'orange': 1})
    1

    >>>count_dict_dups({'a': 2, 'b': 2, 'c': 4, 'd': 4})
    2

    """
    seen_values = set()
    duplicates = set()
    for i in dictionary:
        if dictionary[i] in seen_values:
            duplicates.add(dictionary[i])
        else:
            seen_values.add(dictionary[i])
    return (len(duplicates))
