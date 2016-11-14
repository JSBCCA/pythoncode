from random import randint
num = randint(1, 100)
guess = 0
while guess != num:
    guess = int(input())
    if guess > num:
        print("too high")
    elif guess < num:
        print("too low")
    elif guess == num:
        print("CORRECT!")
    else:
        print("Unknown Error")
