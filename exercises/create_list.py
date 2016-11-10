stuff = []
x = True
while x is True:
    y = input("")
    if y.lower() != 'done':
        stuff.append(y)
    else:
        print(stuff)
        print(len(stuff))
        break
