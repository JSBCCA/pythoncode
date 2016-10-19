def ask(message):
    print(message)
    return input()


def barchart(L):
    """(int, int, int) -> str
    Takes three integers and converts it into a bar chart.

    >>> barchart(4, 9, 7)
    \ ****
    \ *********
    \ *******
    \ ********************

    """
    total = 0
    for i in L:
        total += int(i)
        print(i, "\t" + ("*" * int(i)))
    print(total, "\t" + ("*" * int(total)))


if __name__ == '__main__':
    Q = (ask("What are the numbers? ")).split()
    barchart(Q)
