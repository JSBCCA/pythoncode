from collections import Counter

with open("alice_in.txt", 'r') as file:
    alice = file.readlines()  # list of all of our words

alice = alice[32:3371]
alice = "".join(alice)
alice = alice.split(" ")

l = []
for word in alice:
    if len(word) > 0:
        l.append("".join(filter(str.isalpha, word)))

print("Number of words: " + str(len(l)))

print("Number of paragraphs: ?")

print("Twenty most common words: ")

# Counter makes an ordered dictionary
twenty = Counter(l).most_common(20)

for i in range(len(twenty)):
    if twenty[i] == twenty[-1]:
        print(str(twenty[i][0]))
    else:
        print(str(twenty[i][0]) + ", ", end="")
