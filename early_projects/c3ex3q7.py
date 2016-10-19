def best3av(a, b, c, d):
    """ (number, number, numbern number) -> number

    Precondition: 100 > Numbers > 0.

    Returns the average of the highest three numbers.

    >>>average(40, 99, 87, 0)
    75.33
    >>>average(80, 10, 100, 40)
    73.33

    """
    One = min(a, b, c, d)
    Two = (a + b + c + d - One)
    Three = Two / 3
    return round(Three, 2)


if __name__ == '__main__':
    w = int(input("Give grade 1 pls: "))
    x = int(input("Give grade 2 pls: "))
    y = int(input("Give grade 3 pls: "))
    z = int(input("Give grade 4 pls: "))
    print(best3av(w, x, y, z))
