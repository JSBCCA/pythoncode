# assign first item to dictionary, give value of 1
# go through items
# if item name isn't equal to any dictionary, set it to a new dictionary
# if item name equals existing dictionary, set that dictionary's value to +=1
# after everything, print dictionaries

people = {}
with open('tweeters.txt') as file:
    for line in file:
        person = line.strip()
        people[person] = people.get(person, 0) + 1

with open('tweets.txt', 'a') as file:
    for i in people:
        file.write(str(i) + ': ' + str(people[i]) + '\n')
