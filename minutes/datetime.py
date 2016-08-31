import datetime

for y in range(100):
    with open('minutes{0}.txt'.format(y), 'r') as file:
        emp = []
        x = 0
        while True:
            contents = file.read().split('###')
            emp.append(contents)
    print(emp)
"""for i in contents:
    x = x + float(i)
if 'M' in emp:
    if x > 2500:
        print(dat + ": You have exceeded your cap.")
    else:
        print(dat + ": You have not exceeded your cap.")
elif 'L' in emp:
    if x > 2000:
        print(dat + ": You have exceeded your cap.")
    else:
        print(dat + ": You have not exceeded your cap.")
elif 'H' in emp:
    if x > 3000:
        print(dat + ": You have exceeded your cap.")
    else:
        print(dat + ": You have not exceeded your cap.")"""
