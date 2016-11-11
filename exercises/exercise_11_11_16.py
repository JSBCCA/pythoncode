import random
str_rand_num = "99"  # start with 99
while True:  # loop
    new_str_rand_num = str(random.randint(2, 150))  # set new randint
    print(str_rand_num + " little bugs in the code\n" + str_rand_num +
          " little bugs\nTake one down, patch it around\n" + new_str_rand_num +
          " little bugs in the code")
    str_rand_num = new_str_rand_num  # set new randint to be used again
    if input().lower().strip() == "q":  # ask if they want to quit
        break  # if so, quit
