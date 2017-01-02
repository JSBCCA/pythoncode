# Number of words
# Number of paragraphs
# 20 most common words

from collections import Counter

with open("alice_in.txt", 'r') as file:
    alice = file.read().split()  # list of all of our words

l = []
for word in alice:
    l.append("".join(filter(str.isalpha, word)))

# Counter makes an ordered dictionary
print("Number of words: " + str(len(l)))
print("Number of paragraphs: ")
print("Twenty most common words: ")
placeholder_variable = Counter(l).most_common(20)
for i in range(len(placeholder_variable)):
    if placeholder_variable[i] == placeholder_variable[-1]:
        print(str(placeholder_variable[i][0]))
    else:
        print(str(placeholder_variable[i][0]) + ", ", end="")
