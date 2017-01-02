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
print(Counter(l).most_common(20))
print('hi')
