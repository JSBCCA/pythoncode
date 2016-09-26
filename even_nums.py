def even_list(string):
    string = filter(str.isnumeric, string.split(" "))
    string = map(int, string)
    even_string = list(filter(lambda n: n % 2 == 0, string))
    return even_string


def test_even_list():
    assert even_list('5 4 6 8 99') == [4, 6, 8]
    assert even_list('1 0 0 6') == [0, 0, 6]
    assert even_list('53 5 7') == []
    assert even_list('2 4 6') == [2, 4, 6]
    assert even_list('abc def') == []
    assert even_list('2, 3, 4') == [4]


if __name__ == '__main__':
    string = input("Enter a series of space separated integers:\n").strip()
    print(even_list(string))
