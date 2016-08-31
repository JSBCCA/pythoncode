def celsius_conv(f):  # takes a temperature in degF and converts to degC
    if f == 0:
        return -17.7778
    else:
        return (f - 32.0) * (5.0 / 9.0)
# print (celsius_conv(94))

c_c = celsius_conv


def above_freezing(c):
    """(number) -> bool

    Return True iff temperature c degrees is above freezing.

    >>> above_freezing(5.2)
    True
    >>>above_freezing(-2)
    False
    """
    return c > 0


if __name__ == "__main__":
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = c_c(fahrenheit)
    if above_freezing(celsius):
        print("It is above freezing.")
    else:
        print("It is below freezing.")
