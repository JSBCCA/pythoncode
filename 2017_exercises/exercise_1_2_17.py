# Number of paragraphs

from collections import Counter

with open("alice_in.txt", 'r') as file:
    alice = file.readlines()  # list of all of our words

alice = alice[32:3371]
alice = "".join(alice)
alice = alice.split(" ")

l = []
for word in alice:
    l.append("".join(filter(str.isalpha, word)))

    # lambda x: .isalpha and len(x) > 0, word

print("Number of words: " + str(len(l)))

print("Number of paragraphs: ")

print("Twenty most common words: ")
# Counter makes an ordered dictionary
placeholder_variable = Counter(l).most_common(20)
for i in range(len(placeholder_variable)):
    if placeholder_variable[i] == placeholder_variable[-1]:
        print(str(placeholder_variable[i][0]))
    else:
        print(str(placeholder_variable[i][0]) + ", ", end="")
