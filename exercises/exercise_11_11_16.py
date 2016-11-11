import random
randnum = "99"  # start with 99
while True:  # loop
    new_randnum = str(random.randint(2, 150))  # set new randint
    print("""{0} little bugs in the code\n{0} little bugs
Take one down, patch it around\n{1} little bugs in the code"""
          .format(randnum, new_randnum))
    randnum = new_randnum  # set new randint to be used again
    if input().lower().strip() == "q":  # ask if they want to quit
        break  # if so, quit
