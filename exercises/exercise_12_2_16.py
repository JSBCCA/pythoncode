# color
from termcolor import cprint

# height of tree
while True:
    height = int(input(
        """How tall should the Christmas Tree be? (Odd numbers only.
Must be greater than 2, and less than 40.)\n"""))
    if (height % 2 != 0) and (height > 2) and (height < 40):
        break
# use even numbers?

# tree
print("\n")
asterisks = 1
space = height - 1
color = "yellow"
while asterisks < (height * 2):
    cprint((" " * space) + ("*" * asterisks), color)
    color = "green"
    asterisks += 2
    space -= 1
# add special characters as ornaments?

# tree trunk
if height < 10:
    cprint((" " * (height - 1)) + "T", "red")
elif (height > 10) and (height < 14):
    cprint((" " * (height - 2)) + "IHI", "red")
elif (height > 14) and (height < 20):
    cprint((" " * (height - 3)) + "IHHHI", "red")
    cprint((" " * (height - 3)) + "IHHHI", "red")
elif (height > 20) and (height < 24):
    cprint((" " * (height - 4)) + "IHHHHHI", "red")
    cprint((" " * (height - 4)) + "IHHHHHI", "red")
elif (height > 24) and (height < 28):
    cprint((" " * (height - 4)) + "IHHHHHI", "red")
    cprint((" " * (height - 4)) + "IHHHHHI", "red")
    cprint((" " * (height - 4)) + "IHHHHHI", "red")
elif (height > 28) and (height < 34):
    cprint((" " * (height - 5)) + "IHHHHHHHI", "red")
    cprint((" " * (height - 5)) + "IHHHHHHHI", "red")
    cprint((" " * (height - 5)) + "IHHHHHHHI", "red")
elif (height > 34) and (height < 38):
    cprint((" " * (height - 6)) + "IHHHHHHHHHI", "red")
    cprint((" " * (height - 6)) + "IHHHHHHHHHI", "red")
    cprint((" " * (height - 6)) + "IHHHHHHHHHI", "red")
else:
    cprint((" " * (height - 6)) + "IHHHHHHHHHI", "red")
    cprint((" " * (height - 6)) + "IHHHHHHHHHI", "red")
    cprint((" " * (height - 6)) + "IHHHHHHHHHI", "red")
    cprint((" " * (height - 6)) + "IHHHHHHHHHI", "red")
