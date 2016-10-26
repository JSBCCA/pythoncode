"""py.test test_exercise102616.py --cov=exercise_10_26_16.py --cov-report=html"""
from exercise_10_26_16 import *


def test_palindrome():
    text = 'mom'
    pt = palindrome(text)
    assert pt is True


def test_multi_palindrome():
    text = 'wasitaratisaw'
    pt = palindrome(text)
    assert pt is True


def test_false():
    text = 'dog'
    pt = palindrome(text)
    assert pt is False


def test_symbols():
    text = '9874^&'
    pt = palindrome(text)
    assert pt is False


def test_palin_with_symbols():
    text = "Go hang a salami I'm a lasagna hog."
    pt = palindrome(text)
    assert pt is True
