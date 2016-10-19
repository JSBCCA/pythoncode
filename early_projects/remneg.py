def remove_neg(numlist):
    numremove = []
    for item in numlist:
        if item < 0:
            numremove.append(item)
    for item in numremove:
        numlist.remove(item)
    print(numlist)


remove_neg([9, -4, -5, -6, 11, 8, -3])
