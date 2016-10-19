def count_values(dictionary):
    """

    """
    seen_values = set()
    for i in dictionary:
        seen_values.add(dictionary[i])
    return len(seen_values)


print(count_values({'red': 1, 'green': 1, 'blue': 2, 'yellow': 3, 'purp': 2}))
