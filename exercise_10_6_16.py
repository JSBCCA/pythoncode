with open('users.txt', 'r') as file:
    users = file.read().strip().split('\n')

with open('compromised.txt', 'r') as file:
    compromised = file.read().strip().split('\n')

file = open('compromised_users.txt', 'w')
for i in users:
    if i in compromised:
        file.write(i + '\n')
file.close()
