def pal(p):  # str.isalpha is function form of the method .isalpha()
    np = list(filter(str.isalpha, p.lower()))  # remove non-letters
    return np == np[::-1] and len(np) > 0  # check if palindrome


# py.test test_exercise102616.py --cov=exercise_10_26_16.py --cov-report=html
def test_palin():
    assert pal('mom')
    assert pal('dog') is False
    assert pal('9874^&') is False
    assert pal("Go hang a salami I'm a lasagna hog.")


if __name__ == '__main__':
    t = input("Text: ")
    print(pal(t))
