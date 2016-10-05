from random import randint, choice, shuffle
password = ''
rand = randint(4, 8)
items = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQrstuvwXYZ",
         "0123456789", "!@#$%&*_+>:;\/<?"]
shuffle(items)
for string in items:
    password += choice(string)
for i in range(rand):
    password += choice(choice(items))
print(password)
