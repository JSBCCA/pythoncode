import random


def gibber_gener():
    low = "abcdefghijklmnopqrstuvwxyz"
    upp = low.upper()
    num = "0123456789"
    sym = "!@#$%&*_+><?"
    gibber = ''
    rand = random.randint(4, 8)
    x = [low, upp, num, sym]
    random.shuffle(x)
    for string in x:
        gibber += random.choice(string)
    for i in range(rand):
        item = random.choice([low, upp, num, sym])
        gibber += random.choice(item)
    print(gibber)


if __name__ == "__main__":
    gibber_gener()
