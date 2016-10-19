def int_list():
    howmany = int(input("How many inputs? "))
    nums = []
    for i in range(howmany):
        x = int(input("Input: "))
        nums.append(x)
    print(nums)


int_list()
