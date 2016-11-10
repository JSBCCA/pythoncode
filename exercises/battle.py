chars = {
    'the human': [10, 'good'],
    'toriel': [80, 'good'],
    'sans': [1, 'good'],
    'papyrus': [20, 'good'],
    'alphys': [8, 'good'],
    'mettaton': [30, 'good'],
    'mettaton ex': [47, 'good'],
    'muffet': [38.8, 'good']
    'flowey': [3, 'evil'],
    'asgore': [80, 'good'],
    'undyne': [50, 'good'],
    'asriel dreemurr': [9999, 'snevil'],
    'chara': [99, 'evil']
}

first = input("First battler: ").lower().strip()
second = input("Second battler: ").lower().strip()

if (chars[first][0] == 1) and (chars[second][1] == 'evil'):
    print(first + " wins!")
elif (chars[second][0] == 1) and (chars[first][1] == 'evil'):
    print(second + " wins!")
elif chars[second][0] < chars[first][0]:
    print(first.title() + " wins!")
elif chars[second][0] > chars[first][0]:
    print(second.title() + " wins!")
else:
    print("It's a tie!")
