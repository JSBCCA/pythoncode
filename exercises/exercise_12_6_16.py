while True:
    v = input('Give 8 verbs separated by commas. ').split(', ')
    if len(v) == 8:
        break
while True:
    n = input('Give 6 nouns separated by commas. ').split(', ')
    if len(n) == 6:
        break
while True:
    a = input('Give 5 adjectives separated by commas. ').split(', ')
    if len(a) == 5:
        break

print('\nRudolph the ' + a[0].title() + '-Nosed ' + n[0].title() +
      '\nHad a very ' + a[1] + ' nose\nAnd if you ever ' + v[0] +
      'ed it\nYou would even say it ' + v[1] + 's\nAll of the other ' + n[0] +
      '\nUsed to ' + v[2] + ' and call him ' + n[1] + '\nThey never let ' + a[
          2] + ' Rudolph\n' + v[3] + ' in any ' + n[0] + ' games\nThen one ' +
      a[3] + ' Christmas Eve\nSanta ' + v[4] + ' to say\n"Rudolph, with your '
      + n[2] + ' so ' + a[4] + "\nWon't you " + v[5] + ' my ' + n[3] +
      ' tonight?"\nThen how the reindeer ' + v[6] + 'ed him\nAs they ' + v[7] +
      'ed out with ' + n[4] + '\n"Rudolph the ' + a[0].title() + '-Nosed ' + n[
          0] + "\nYou'll go down in " + n[5] + '!"')
