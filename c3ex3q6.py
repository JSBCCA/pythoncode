def average(a, b, c):
    """ (number, number, number) -> number

    Precondition: 100 > Numbers > 0.

    Returns the average of three numbers.

    >>>average(40, 99, 87)
    75.33
    >>>average(80, 0, 100)
    60

    """
    return round(((a + b + c) / 3), 2)


if __name__ == '__main__':
    x = int(input("Give grade 1 pls: "))
    y = int(input("Give grade 2 pls: "))
    z = int(input("Give grade 3 pls: "))
    print(average(x, y, z))
