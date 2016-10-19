x = 'aattgccgt'

# ttaacggca


def sequence(x):
    y = x.lower().split()
    newlist = []
    for z in y:
        for i in z:
            if i == 'a':
                newlist.append('t')
            elif i == 't':
                newlist.append('a')
            elif i == 'c':
                newlist.append('g')
            elif i == 'g':
                newlist.append('c')
    return ''.join(newlist)


print(sequence(x))
