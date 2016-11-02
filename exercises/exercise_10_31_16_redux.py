with open('phone_data.txt', 'r') as file:
    phone_numbers = file.read().splitlines()


# change lines to dictionaries
def parse(line):
    "str -> dict"
    line = line.replace("-", "")
    if len(line) > 10:
        line = line[1:]
    new_dict = {'area': line[:3],
                'exchange': line[3:6],
                'subscriber': line[6:]}
    return new_dict


# change dictionaries to strings
def format_phone(d):
    "dict -> str"
    return '(' + d['area'] + ') ' + d['exchange'] + '-' + d['subscriber']


# py.test exercise_10_31_16_redux.py --cov=exercise_10_31_16_redux.py --cov-report=html
def test_parse():
    assert parse("1-476-177-8875") == {
        'area': '476',
        'exchange': '177',
        'subscriber': '8875'
    }
    assert parse("8586359388") == {
        'area': '858',
        'exchange': '635',
        'subscriber': '9388'
    }
    assert parse("17461538482") == {
        'area': '746',
        'exchange': '153',
        'subscriber': '8482'
    }
    assert parse("218-690-7902") == {
        'area': '218',
        'exchange': '690',
        'subscriber': '7902'
    }


def test_format_phone():
    assert format_phone({
        'area': '476',
        'exchange': '177',
        'subscriber': '8875'
    }) == "(476) 177-8875"


if __name__ == '__main__':
    with open('new_phone_data.txt', 'w') as file:
        for phone in phone_numbers:
            file.write(format_phone(parse(phone)) + '\n')
