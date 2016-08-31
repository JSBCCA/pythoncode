w = 99
x = " bottles"
y = " bottle"


def wa():
    if 0 < w < 2:
        return y
    else:
        return x


def za():
    if 0 < z < 2:
        return y
    else:
        return x


while w > 0:

    z = w - 1

    print(str(w) + str(wa()) + " of Coke on the wall, " + str(w) + str(wa(
    )) + " of Coke; take one down, pass it\n around, " + str(z) + str(za()) +
          " of Coke on the wall!")

    w -= 1
