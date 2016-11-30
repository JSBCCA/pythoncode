from collections import Counter

with open("tale_of.txt", 'r') as file:
    tale = file.read().split()  # list of all of our words

l = []
for word in tale:
    l.append("".join(filter(str.isalpha, word)))

# Counter makes an ordered dictionary
print(Counter(filter(lambda x: x.istitle() and len(x) > 4, l)).most_common(10))
