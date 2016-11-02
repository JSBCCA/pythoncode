with open('phone_data.txt', 'r') as file:
    phone_numbers = file.read().splitlines()


# change lines to dictionaries
def first(line):
    "str -> dict"
    if len(line) == 10:
        new_dict = {'area': str(line[:3]),
                    'exchange': str(line[3:6]),
                    'subscriber': str(line[6:])}
    elif len(line) == 11:
        new_dict = {'area': str(line[1:4]),
                    'exchange': str(line[4:7]),
                    'subscriber': str(line[7:])}
    elif len(line) == 12:
        new_dict = {'area': str(line[:3]),
                    'exchange': str(line[4:7]),
                    'subscriber': str(line[8:])}
    elif len(line) == 14:
        new_dict = {'area': str(line[2:5]),
                    'exchange': str(line[6:9]),
                    'subscriber': str(line[10:])}
    return new_dict


# change dictionaries to strings
def second(d):
    "dict -> str"
    return '(' + d['area'] + ') ' + d['exchange'] + '-' + d['subscriber']


# py.test exercise_10_31_16_redux.py --cov=exercise_10_31_16_redux.py --cov-report=html
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
    with open('new_phone_data.txt', 'w') as file:
        for phone in phone_numbers:
            file.write(second(first(phone)) + '\n')
