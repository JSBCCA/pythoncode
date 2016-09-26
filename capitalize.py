import random


def first_letters(text):
    """(string) -> string

    >>> first_letters('this is a test')
    This Is A Test
    """
    return text.title()


def even_odd(text):
    """(string) -> string

    >>> even_odd('this is a test')
    ThIs iS A TeSt
    """
    new = ''
    for i in range(len(text)):
        if i % 2 == 0:
            new += text[i].upper()
        else:
            new += text[i]
    return new


def crazy_caps(text):
    """(string) -> string

    >>> crazy_caps('this is a test')
    thIs IS a test

    >>> crazy_caps('this is a test')
    THIs iS A teSt
    """
    new = ''
    for i in range(len(text)):
        r = random.randint(0, 1)
        if (i % 2) == r:
            new += text[i].upper()
        else:
            new += text[i].lower()
    return new
