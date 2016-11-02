with open('phone_data.txt', 'r') as file:
    phone_numbers = file.read().splitlines()


# change lines to dictionaries
def first(line):
    "str -> dict"
    for p in phone_numbers:
        if len(p) == 10:
            ...
        elif len(p) == 11:
            ...
        elif len(p) == 12:
            ...
        elif len(p) == 14:
            ...
    return '''{
        x: 555,
        x: 555,
        x: 5555
    }'''


# change dictionaries to strings
def second(d):
    "dict -> str"
    ...
    return '(555) 555-5555'


def test_first():
    assert first("1-476-177-8875") == {
        'area': '476',
        'exchange': '177',
        'subscriber': '8875'
    }
    assert first("8586359388") == {
        'area': '858',
        'exchange': '635',
        'subscriber': '9388'
    }
    assert first("17461538482") == {
        'area': '746',
        'exchange': '153',
        'subscriber': '8482'
    }
    assert first("218-690-7902") == {
        'area': '218',
        'exchange': '690',
        'subscriber': '7902'
    }


def test_second():
    assert second({
        'area': '476',
        'exchange': '177',
        'subscriber': '8875'
    }) == "(476) 177-8875"


if __name__ == '__main__':
    for phone in phone_numbers:
        print(second(first(phone)))
