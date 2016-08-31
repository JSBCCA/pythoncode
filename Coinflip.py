import random


def coinflip():
    flip = random.randint(1, 2)
    if flip == 1:
        print("Heads")
    elif flip == 2:
        print("Tails")
