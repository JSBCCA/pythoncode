import sys
# open cust_info_login.txt
with open('cust_info_login.txt', 'r') as file:
    customer_login = file.read().strip().split('\n')
cust_login = list(map(lambda c: c.split(' _ '), customer_login))
# save usernames and passwords to a list
users_and_passwords = []
for customer in cust_login:
    unpw = [customer[2], customer[3]]
    users_and_passwords.append(unpw)
# check for username and password
lock = True
while lock is True:
    username = input("Please enter your username. Type 'q' to quit. ").strip()
    if username.lower() == 'q':
        sys.exit()
    password = input("Please enter your password. ").strip()
    if password.lower() == 'q':
        sys.exit()
    for user in users_and_passwords:
        if username == user[0] and password == user[1]:
            lock = False
# ask for new password
lock = True
while lock is True:
    new_pass = input(
        "What would you like your new password to be? Must be 6 characters. ")
    if len(new_pass) == 6:
        # get user position in order to change password
        for item in cust_login:
            if (username in item) and (password in item):
                item.remove(password)
                item.append(new_pass)
        # change password
        with open('cust_info_login.txt', 'w') as file:
            for i in range(len(cust_login)):
                file.write(cust_login[i][0] + ' _ ' + cust_login[i][1] + ' _' +
                           ' ' + cust_login[i][2] + ' _ ' + cust_login[i][3] +
                           '\n')
        print("Password has been changed.")
        lock = False
