with open('sowpods.txt', 'r') as sp:
    contents = sp.read().lower().split()


def five_vowels():
    words = []
    for w in contents:
        if all(v in w for v in 'aeiou'):
            words.append(w)
    print("\nList of words containing all 5 vowels, not including 'y':")
    print(words)


def six_vowels():
    words = []
    for w in contents:
        if all(v in w for v in 'aeiouy'):
            words.append(w)
    print("\nList of words containing all 6 vowels, including 'y':")
    print(words)


def no_vowels():
    words = []
    for w in contents:
        if all(v not in w for v in 'aeiou'):
            words.append(w)
    print("\nList of words containing none of the 5 main vowels:")
    print(words)


def order_vowels():
    words = []
    for w in contents:
        if 'a' in w and 'e' in w and 'i' in w and 'o' in w and 'u' in w:
            if w.index('a') < w.index('e') < w.index('i') < w.index(
                    'o') < w.index('u'):
                words.append(w)
    print("\nList of words containing the main 5 vowels in order:")
    print(words)


def initials():
    words = []
    for w in contents:
        if 'j' in w and 'e' in w and 's' in w:
            if w.index('j') < w.index('e') < w.index('s'):
                words.append(w)
    print("\nList of words containing my 3 initials in order:")
    print(words)


five_vowels()
six_vowels()
no_vowels()
order_vowels()
initials()
