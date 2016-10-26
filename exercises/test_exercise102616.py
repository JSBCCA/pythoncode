"""py.test test_exercise102616.py --cov=exercise_10_26_16.py --cov-report=html"""
from exercise_10_26_16 import *


def test_palin():
    assert palin('mom')
    assert palin('wasitaratisaw')
    assert palin('dog') is False
    assert palin('9874^&') is False
    assert palin("Go hang a salami I'm a lasagna hog.")
