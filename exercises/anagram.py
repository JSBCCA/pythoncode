from random import shuffle, choice
import time
import sys

original = ['purple', 'blue', 'green', 'yellow', 'orange', 'red', 'pink',
            'white', 'gray', 'black', 'brown', 'ant', 'horse', 'dog', 'cat',
            'food', 'house', 'cheese', 'pizza', 'hamburger', 'shark', 'bird',
            'bat', 'baseball', 'football', 'video', 'game', 'hero', 'infinity',
            'car', 'television', 'smart', 'telephone', 'cow', 'tornado', 'art',
            'fire', 'water', 'earthquake', 'flood', 'dolphin', 'crow', 'shoe',
            'sock', 'pants', 'shirt', 'hand', 'foot', 'tooth', 'legend', 'fly',
            'snow', 'queen', 'king', 'clown', 'terrorist', 'airplane', 'truck',
            'cone', 'brush', 'finger', 'hair', 'rabbit', 'table', 'bottle',
            'can', 'bag', 'sword', 'gun', 'chicken', 'school', 'lock', 'eagle',
            'hum', 'rainbow', 'rain', 'bow', 'radio', 'toothbrush', 'liquid',
            'gas', 'solid', 'plasma', 'play', 'player', 'prayer', 'earth',
            'wind', 'air', 'oxygen', 'clean', 'tomato', 'potato', 'volcano',
            'piano', 'pray', 'fort', 'rock', 'pop', 'bee', 'bug', 'penguin',
            'fish', 'beast', 'whale', 'hammer', 'crack', 'dark', 'light',
            'heavy', 'pun', 'pond', 'punish', 'zero', 'thousand', 'hundred',
            'alpha', 'omega', 'cream', 'oblivion', 'dragon', 'chaos', 'point',
            'money', 'shield', 'super', 'dairy', 'okay', 'tree', 'plant',
            'leaf', 'nuclear', 'family', 'code', 'program', 'president', 'ice',
            'agent', 'prince', 'princess', 'boat', 'submarine', 'sandwich',
            'elephant', 'home', 'cookie', 'soda', 'doll', 'nice', 'count',
            'indigo', 'violet', 'violent', 'bark', 'branch', 'olive', 'pasta',
            'file', 'ocean', 'sea', 'pirate', 'ninja', 'dinosaur', 'bowl',
            'plate', 'spoon', 'fork', 'knife', 'spork', 'spatula', 'spaghetti',
            'board', 'abroad', 'girl', 'boy', 'man', 'woman', 'child', 'adult',
            'parent', 'son', 'sun', 'daughter', 'organ', 'trumpet', 'guitar',
            'violin', 'trombone', 'bone', 'skeleton', 'meme', 'internet',
            'drum', 'strum', 'stomach', 'piccolo', 'flute', 'symbol', 'digit',
            'ship', 'robot', 'mouse', 'house', 'alone', 'create', 'fight',
            'flashlight', 'deodorant', 'star', 'sky', 'vision', 'vampire',
            'past', 'door', 'present', 'future', 'time', 'space', 'coffin',
            'ghost', 'zombie', 'heaven', 'chocolate', 'candy', 'sweet',
            'rude', 'forgive', 'computer', 'apocalypse', 'jupiter', 'mercury',
            'brutal', 'flower', 'genius', 'window', 'muscle', 'miniscule',
            'humongous', 'homunculus', 'terrifying', 'reindeer', 'incredible',
            'watermelon', 'apricot', 'pumpkin', 'royalty', 'country', 'ear']

wordlist = []
mode = input("Easy, Medium, or Hard? ").lower().strip()
if mode == "easy":
    for i in original:
        if len(i) < 6:
            wordlist.append(i)
    time.sleep(1)
    print("\n" * 25)
elif mode == "medium":
    for i in original:
        if (len(i) >= 5) and (len(i) < 7):
            wordlist.append(i)
    time.sleep(1)
    print("\n" * 25)
elif mode == "hard":
    for i in original:
        if len(i) > 7:
            wordlist.append(i)
    time.sleep(1)
    print("\n" * 25)
elif mode == 'q':
    sys.exit()
else:
    for i in original:
        if len(i) < 6:
            wordlist.append(i)
    time.sleep(1)
    print("\n" * 25)

while True:
    x = False
    if len(wordlist) == 0:
        print("You win! Congratulations!")
        sys.exit()
    word_true = choice(wordlist)
    word_ana = list(word_true)
    while x is False:
        shuffle(word_ana)
        if word_ana != list(word_true):
            x = True
    word_ana = ''.join(word_ana)
    guess = False
    print("Word anagram: " + str(word_ana))
    while guess != word_true:
        guess = input("Guess the word! ").strip().lower()
        if guess == 'q':
            sys.exit()
        elif guess == word_true:
            print("Correct!")
            wordlist.remove(word_true)
            time.sleep(2)
            print("\n" * 25)
        elif set(guess) != set(word_true):
            print("Come on, you're not even trying...")
