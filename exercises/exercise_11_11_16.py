import random
r_num = "99"  # start with 99
while True:  # loop
    print("{0} little bugs in the code\n{0} little bugs".format(r_num))
    r_num = str(random.randint(2, 150))  # set new randint
    if input("""Take one down, patch it around
{} little bugs in the code\n""".format(r_num)).lower().strip() == "q":
        break  # option to quit
