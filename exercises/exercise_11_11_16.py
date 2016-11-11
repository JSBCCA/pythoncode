from random import randint
import sys
# start with 99
str_rand_num = "99"
# loop
while True:
    # set new randint
    new_str_rand_num = str(randint(2, 150))
    # use both randints
    print(str_rand_num + """ little bugs in the code
""" + str_rand_num + " little bugs\nTake one down, patch it around\n" +
          new_str_rand_num + " little bugs in the code")
    # change new randint to be used again
    str_rand_num = new_str_rand_num
    # ask if they want to quit
    quit = input().lower().strip()
    if quit == "q":
        sys.exit()
