with open("tale_of.txt", 'r') as file:
    l = file.read().lower().split()  # list of all of our words

new_l = []
for word in l:
    # str.isalpha is function form of the method .isalpha()
    # check word 'word' for non letters
    new_l.append("".join(list(filter(str.isalpha, word))))

# put all words into dictionary
d = {}
# d = {word: int}
for word in l:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

# find the 10 most common words

# get the values
v = list(d.values())
# sort the values
v.sort()
# get the 10th value
tenth_val = v[-10]
# filter dictionary for words w/ higher value than tenth_val
words = list(filter(lambda x: d[x] >= tenth_val, d))
# print out the words to the user
print(words)
