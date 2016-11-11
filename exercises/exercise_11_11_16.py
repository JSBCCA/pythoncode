from random import randint  # import randint
import sys  # import ability to exit
str_rand_num = "99"  # start with 99
while True:  # start loop
    new_str_rand_num = str(randint(2, 150))  # set new randint
    print(str_rand_num + " little bugs in the code\n" + str_rand_num +
          " little bugs\nTake one down, patch it around\n" + new_str_rand_num +
          " little bugs in the code")  # use both randints
    str_rand_num = new_str_rand_num  # set new randint to be used again
    quit = input().lower().strip()  # ask if they want to quit
    if quit == "q":  # if so,
        sys.exit()  # quit
