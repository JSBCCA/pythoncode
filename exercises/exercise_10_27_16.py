def square_dict(num):
    new_dict = {}
    if str(num).isdigit():
        for n in range(1, num + 1):
            new_dict[n] = n * n
        return new_dict
    return {}


# py.test exercise_10_27_16.py --cov=exercise_10_27_16.py --cov-report=html
def test_square_dict():
    assert square_dict(4) == {1: 1, 2: 4, 3: 9, 4: 16}
    assert square_dict(0) == {}
    assert square_dict(-1) == {}
    assert square_dict('dog') == {}


if __name__ == '__main__':
    print(square_dict(10))
