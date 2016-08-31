def average(values):
    """(list of number) -> number

    Return the average of the numbers in values. Some items in values are None,
    and they are not counted toward the average.

    >>> average([20, 30])
    25.0
    >>> average([None, 20, 30])
    25.0
    """

    count = 0  # The number of values seen so far.
    total = 0  # The sum of the values seen so far.
    n = 0
    x = len(values)
    if values == []:
        return None
    for value in values:
        if value is not None:
            total += value
            count += 1
        elif value is None:
            n += 1
            if n == x:
                return None
            else:
                value = 0
                total += value
    return total / count
