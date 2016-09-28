"""
4) Print out the list of words containing all 5 vowels in order.
5) Print out the list of words containing your initials.
(Letters must be in order, but not necessarily consecutive.)
"""

with open('sowpods.txt', 'r') as sp:
    content = sp.read().lower().split()


def five_vowels():
    words = []
    for w in content:
        if all(v in w for v in 'aeiou'):
            words.append(w)
    print("\nList of words containing all 5 vowels, not including 'y':")
    print(words)


def six_vowels():
    words = []
    for w in content:
        if all(v in w for v in 'aeiouy'):
            words.append(w)
    print("\nList of words containing all 6 vowels, including 'y':")
    print(words)


def no_vowels():
    words = []
    for w in content:
        if all(v not in w for v in 'aeiou'):
            words.append(w)
    print("\nList of words containing none of the 5 main vowels:")
    print(words)


def order_vowels():
    words = []
    for word in content:
        for w in word:
            if w == 'a':
                # ...
                words.append(word)
    print(
        "\nList of words containing all 5 vowels in order, not including 'y':")
    print(words)


def initials():
    words = []
    for word in content:
        for w in word:
            if w == 'j':
                # ...
                words.append(word)
    print("\nList of words containing my 3 initials in order:")
    print(words)


five_vowels()
six_vowels()
no_vowels()
order_vowels()
initials()
