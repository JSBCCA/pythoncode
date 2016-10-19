# triangle
"""for i in range(7):
    for j in range(i + 1):
        print("T", end='')
    print() """

# backwards triangle
x = 7
for i in range(x):
    for j in range(x - i):
        print(" ", end="")
    for j in range(i + 1):
        print("T", end='')
    print()
