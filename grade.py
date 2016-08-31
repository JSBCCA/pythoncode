def ask(message):
    """ Prints a message and returns input"""
    print(message)
    return input()


def remove(numlist):
    """Removes negative numbers and numbers above 100 from a list"""
    numremove = []
    for item in numlist:
        if item < 0 or item > 100:
            numremove.append(item)
    for item in numremove:
        numlist.remove(item)
    return (numlist)


def average(num):
    """Gets the average of the numbers in a list"""
    total = 0
    for n in num:
        total += n
    return (total / (len(num)))


def lettergrade(n):
    """Converts a number to a letter grade"""
    if n < 60:
        print("F " + str(n))
    elif 70 > n >= 60:
        print("D " + str(n))
    elif 80 > n >= 70:
        print("C " + str(n))
    elif 90 > n >= 80:
        print("B " + str(n))
    elif 100 >= n >= 90:
        print("A " + str(n))
    else:
        print("Sorry, something went wrong!")


ltr = lettergrade

if __name__ == '__main__':

    assignment_list = []
    a = ask("How many students do you have?")
    while True:
        grades = []
        name = (ask(
            "What is the name of this assignment? (Enter 'Q' to quit).").strip(
            ).lower())
        if name == "q":
            break
        for c in range(int(a)):
            c = -1
            while c < 0 or c > 100:
                c = int(ask("Enter grade:"))
                grades.append(c)
                remove(grades)
        assignment_list.append([name, grades])
    for i in assignment_list:
        name = i[0]
        grades = i[1]
        print(name)
        print("Average: ", end='')
        ltr(int(average(grades)))
        print("Highest: ", end='')
        ltr(max(grades))
        print("Lowest: ", end='')
        ltr(min(grades))

    # rades = [7, 8, 9]
    # for rade in rades:
    # print(rade)
