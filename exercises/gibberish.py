import random

with open('sowpods.txt', 'r') as sp:
    content = sp.read().split()


def rand_word():
    rand = random.choice(content)
    return rand.lower()


def rand_sentence():
    sentence_len = random.randint(4, 13)
    sen = ''
    sen += rand_word().title()
    for i in range(sentence_len - 1):
        sen += " " + rand_word()
    sen += '. '
    return sen


def gibber_gener():
    rand_amount = random.randint(4, 8)
    para = input("Number of paragraphs: ")
    if para.isnumeric():
        para = int(para)
        for i in range(para):
            print('\n')
            x = ''
            for i in range(rand_amount):
                x += rand_sentence()
            print(x.strip())
    else:
        gibber_gener()


gibber_gener()
