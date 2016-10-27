def square_dict(num):
    return dict((n, n * n) for n in range(1, int(num) + 1))


# py.test exercise_10_27_16.py --cov=exercise_10_27_16.py --cov-report=html
def test_square_dict():
    assert square_dict(3) == {1: 1, 2: 4, 3: 9}
    assert square_dict(0) == {}
    assert square_dict(-1) == {}


if __name__ == '__main__':
    print(square_dict(input("Number: ")))
