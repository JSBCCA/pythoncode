import os
import time

icao = {'a': 'alfa',
        'b': 'bravo',
        'c': 'charlie',
        'd': 'delta',
        'e': 'echo',
        'f': 'foxtrot',
        'g': 'golf',
        'h': 'hotel',
        'i': 'india',
        'j': 'juliett',
        'k': 'kilo',
        'l': 'lima',
        'm': 'mike',
        'n': 'november',
        'o': 'oscar',
        'p': 'papa',
        'q': 'quebec',
        'r': 'romeo',
        's': 'sierra',
        't': 'tango',
        'u': 'uniform',
        'v': 'victor',
        'w': 'whiskey',
        'x': 'x-ray',
        'y': 'yankee',
        'z': 'zulu',
        ' ': '  '}

text = input("""Please type out what you want translated with no numbers.
""").lower()


def speak_ICAO(words, time_one, time_two):
    listtext = []
    newtext = ''
    for i in text:
        if i in icao:
            listtext.append(icao[i])
        newtext += icao[i] + ' '
    print(newtext)
    for i in listtext:
        if i == " ":
            time.sleep(time_one)
        elif i == "  ":
            time.sleep(time_two)
        else:
            os.system("say " + i)


speak_ICAO(text)
