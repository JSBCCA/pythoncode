Data = ['data0.txt', 'data1.txt', 'data2.txt', 'data3.txt', 'data4.txt',
        'data5.txt', 'data6.txt', 'data7.txt', 'data8.txt', 'data9.txt']

for dat in Data:
    with open(dat, 'r') as file:
        emp = []
        x = 0
        contents = file.read().split()
        emp.append(contents[0])
        for i in contents[1:]:
            x = x + float(i)
        if 'M' in emp:
            if x > 600000:
                print(dat + ": You have exceeded your cap.")
            else:
                print(dat + ": You have not exceeded your cap.")
        elif 'L' in emp:
            if x > 300000:
                print(dat + ": You have exceeded your cap.")
            else:
                print(dat + ": You have not exceeded your cap.")
        elif 'H' in emp:
            if x > 900000:
                print(dat + ": You have exceeded your cap.")
            else:
                print(dat + ": You have not exceeded your cap.")
