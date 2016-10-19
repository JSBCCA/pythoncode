def find_min_max(values):
    """(list) -> NoneType

    Print the minimum and maximum value from values.
    """

    mini = values[0]
    maxi = values[0]
    for value in values:
        if value > maxi:
            maxi = value
        if value < mini:
            mini = value

    print('The minimum value is {0}'.format(mini))
    print('The maximum value is {0}'.format(maxi))
