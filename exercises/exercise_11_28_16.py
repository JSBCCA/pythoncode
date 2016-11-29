from urllib.request import urlopen

txtFile = urlopen("http://introcs.cs.princeton.edu/java/data/tale.txt")
string = txtFile.read().decode('utf-8')

# escape all the words into a consistent format
l = string.lower().split()  # list of all of our words

d = {}
for word in l:
    if word in d:
        d[word] += 1
    # elif len(word) > 5:
    # d[word] = 1
    else:
        d[word] = 1
# {word: int, word: int...}

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
