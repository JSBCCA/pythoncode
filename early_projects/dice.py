def rolldie():
    import random

    roll = random.randint(1, 6)
    print("You got a: ")
    print(" _____")
    if roll == 1:
        print("|     |\n" "|  *  |\n" "|     |")

    elif roll == 2:
        print("|*    |\n" "|     |\n" "|    *|")

    elif roll == 3:
        print("|*    |\n" "|  *  |\n" "|    *|")

    elif roll == 4:
        print("|*   *|\n" "|     |\n" "|*   *|")

    elif roll == 5:
        print("|*   *|\n" "|  *  |\n" "|*   *|")

    elif roll == 6:
        print("|*   *|\n" "|*   *|\n" "|*   *|")
    print(" -----")


r = rolldie
# r() = rolldie()
