# returns roman numeral of number
def to_numeral(num):
    "int -> string"
    ints = (100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = ""
    for i in range(len(ints)):
        count = int(num / ints[i])
        result += nums[i] * count
        num -= ints[i] * count
    return result


# returns roman numeral of given integer if it is between 1 and 100
def r_numeral(num):
    "int -> string"
    if not str(num).isdigit():
        return "Only numbers please."
    elif not int(num) >= 1 or not int(num) <= 100:
        return "Must be between 1 and 100."
    else:
        return to_numeral(int(num))


# py.test exercise_11_1_16.py --cov=exercise_11_1_16.py --cov-report=html
def test_r_numeral():
    assert r_numeral(0) == "Must be between 1 and 100."
    assert r_numeral(5) == "V"
    assert r_numeral(101) == "Must be between 1 and 100."
    assert r_numeral('dk4sj') == "Only numbers please."


if __name__ == "__main__":
    print(r_numeral(input("Number: ")))
