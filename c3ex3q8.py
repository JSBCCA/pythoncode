def weeks_el(day1, day2):
    """ (int, int) -> int

    Return number of weeks between two days in the same year.

    >>> weeks_el(3, 20)
    2

    >>> weeks_el(9, 61)



    """
    one = (abs(day1 - day2)) // 7
    return (one)


if __name__ == '__main__':
    a = int(input("What number is the first day?"))
    b = int(input("What number is the second day?"))
    print(weeks_el(a, b))
