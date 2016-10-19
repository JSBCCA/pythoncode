from random import choice, shuffle
from string import digits
# open cust_info.txt and get names and numbers
with open('cust_info.txt', 'r') as file:
    customer_info = file.read().strip().split('\n')
cust_info = list(map(lambda c: c.split(' _ '), customer_info))


# create usernames, first initial and last name
# duplicates have a number on the end
def how_many(username, username_list):
    num = 0
    for item in username_list:
        compare = item.strip(digits)
        if compare == username:
            num += 1
    if num > 0:
        return (num)
    else:
        return ('')
# Ex: Sean Anthony -> santhony
#     Sam Anthony -> santhony1
#     Steve Anthony -> santhony2
names = []
for info in cust_info:
    name = info[0].lower().split()
    names.append(name)
usernames = []
name_num = 0
for n in names:
    new_user = ''
    new_user += n[0][0]
    new_user += n[1]
    new_user += str(how_many(new_user, usernames))
    usernames.append(new_user)
# create passwords, 6 characters long with numbers and/or lowercase letters
passwords = []
items = ["abcdefghijklmnopqrstuvwxyz", "0123456789"]
for person in usernames:
    password = ''
    shuffle(items)
    for string in items:
        password += choice(string)
    for i in range(0, 4):
        password += choice(choice(items))
    passwords.append(password)
# write usernames and passwords to cust_info_login.txt in this format:
# First Last _ customerID _ username _ password
# Ex: Sean Anthony _ 123125 _ santhony _ e4anbq
with open('cust_info_login.txt', 'w') as file:
    for i in range(len(usernames)):
        file.write(customer_info[i] + ' _ ' + usernames[i] + ' _ ' + passwords[
            i] + '\n')
