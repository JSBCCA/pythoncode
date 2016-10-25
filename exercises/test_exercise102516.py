"""py.test testname.py --cov=name.py --cov-report=html"""
from exercise_10_25_16 import *


def test_one_lower():
    text = 'dog'
    pgt = pig_latin(text)
    assert pgt == 'Ogday'


def test_multi_lower():
    text = 'dog and cat'
    pgt = pig_latin(text)
    assert pgt == 'Ogday anday atcay'


def test_one_upper():
    text = 'JAMES'
    pgt = pig_latin(text)
    assert pgt == 'Amesjay'


def test_multi_upper():
    text = 'JAMES IS COOL'
    pgt = pig_latin(text)
    assert pgt == 'Amesjay isay oolcay'


def test_one_lower_one_upper():
    text = 'super POWER'
    pgt = pig_latin(text)
    assert pgt == 'Upersay owerpay'


def test_one_symbols():
    text = '%$^58'
    pgt = pig_latin(text)
    assert pgt == 'Invalid.'


def test_multi_symbols():
    text = '74328* 897*^#'
    pgt = pig_latin(text)
    assert pgt == 'Invalid.'


def test_one_and_symbols():
    text = 'dog (*&*^)'
    pgt = pig_latin(text)
    assert pgt == 'Invalid.'


def test_multi_mix():
    text = 'i aM a BAd sPElLeR'
    pgt = pig_latin(text)
    assert pgt == 'Iay amay aay adbay ellerspay'


def test_mix():
    text = 'BeAr'
    pgt = pig_latin(text)
    assert pgt == 'Earbay'


def test_invalid():
    text = 'kljfjU&*^%'
    pgt = pig_latin(text)
    assert pgt == 'Invalid.'


def test_vowel():
    text = 'air'
    pgt = pig_latin(text)
    assert pgt == 'Airay'


def test_second_vowel():
    text = 'big umbrella'
    pgt = pig_latin(text)
    assert pgt == 'Igbay umbrellaay'


def test_first_two():
    text = 'that'
    pgt = pig_latin(text)
    assert pgt == 'Atthay'


def test__second_first_two():
    text = 'In what'
    pgt = pig_latin(text)
    assert pgt == 'Inay atwhay'


def test_regular():
    text = 'house'
    pgt = pig_latin(text)
    assert pgt == 'Ousehay'
