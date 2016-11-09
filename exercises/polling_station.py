# create dictionary to contain votes and choices
vote_count = {}
# find the number of choices and add them to the dictionary
choices_number = int(input("How many choices are there? "))
for cn in range(choices_number):
    choice = input("Choice " + str(cn + 1) + ": ").title()
    vote_count[choice] = 0
# find out how many votes each key has and add them to the dictionary
voters_number = int(input("How many voters are there? "))
for vn in range(voters_number):
    vote = input("Vote " + str(vn + 1) + ": ").title()
    vote_count[vote] += 1
# find the key with the highest amount of votes
highest_voted = max(vote_count, key=vote_count.get)
# print out the winner
print(str(highest_voted) + " wins!")
