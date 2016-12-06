while True:
    nouns = input("Give 5 nouns separated by commas. ").split(", ")
    if len(nouns) == 5:
        break
while True:
    adjectives = input("Give 5 adjectives separated by commas. ").split(", ")
    if len(adjectives) == 5:
        break
while True:
    verbs = input("Give 6 verbs separated by commas. ").split(", ")
    if len(verbs) == 6:
        break

print("\nRudolph the " + adjectives[0].title() + "-Nosed " + nouns[0].title() +
      "\nHad a very " + adjectives[1] + " nose\nAnd if you ever " + verbs[0] +
      "ed it\nYou would even say it glows\nAll of the other " + nouns[0] +
      "\nUsed to " + verbs[1] + " and call him " + nouns[1] +
      "\nThey never let " + adjectives[2] + " Rudolph\n" + verbs[2] +
      " in any " + nouns[0] + " games\nThen one " + adjectives[3] +
      " Christmas Eve\nSanta " + verbs[3] + ' to say\n"Rudolph, with your ' +
      nouns[2] + " so " + adjectives[4] + "\nWon't you " + verbs[4] + " my " +
      nouns[3] + ' tonight?"\nThen how the reindeer ' + verbs[5] +
      'ed him\nAs they shouted out with glee\n"Rudolph the ' + adjectives[
          0].title() + "-Nosed " + nouns[0] + "\nYou'll go down in " + nouns[4]
      + '!"')
