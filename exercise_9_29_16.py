with open('sowpods.txt', 'r') as sow:
    content = sow.read().split()

for word in ['BASE', 'CAMP', 'CODING', 'ACADEMY']:
    print("Index of " + word + ":", content.index(word))

con_str = "".join(content)
for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    print(ch + ":", con_str.count(ch))
