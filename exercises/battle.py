chars = {
    'frisk': [10, 'good'],
    'dummy': [0, '???'],
    'mad dummy': [80, '???'],
    'glad dummy': [5, 'good'],
    'toriel': [80, 'good'],
    'napstablook': [10, 'good'],
    'sans': [1, 'good'],
    'papyrus': [20, 'good'],
    'alphys': [8, 'good'],
    'mettaton': [30, 'good'],
    'mettaton ex': [47, 'good'],
    'mettaton neo': [90, 'good'],
    'muffet': [38.8, '???']
    'flowey': [3, 'evil'],
    'photoshop flowey': [9999, 'evil'],
    'asgore': [80, 'good'],
    'undyne': [50, 'good'],
    'undyne the undying': [99, 'good'],
    'asriel dreemurr': [9999, 'snevil'],
    'asriel': [20, 'good'],
    'chara': [99, 'evil'],
    'gaster': [2, '???']
}
# 197

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
