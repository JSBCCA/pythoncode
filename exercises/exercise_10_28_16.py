import random


def make_dict():
    # make a dictionary of letters with random letter values
    al = 'abcdefghijklmnopqrstuvwxyz'
    shuff = list(al)
    random.shuffle(shuff)
    shuff = ''.join(shuff)
    return {al[i]: shuff[i] for i in range(25)}


def random_translate(text):
    new_str = ''
    dictionary = make_dict()
    # translate text to be your dictionary values
    for c in text:
        if c in dictionary:
            new_str += dictionary[c]
        elif c.lower() in dictionary:
            new_str += dictionary[c.lower()].upper()
        else:
            new_str += c
    return new_str


# py.test exercise_10_28_16.py --cov=exercise_10_28_16.py --cov-report=html
def test_random_translate():
    assert len("Hello") == len(random_translate("Hello"))
    assert len("It's") == len(random_translate("It's"))


if __name__ == '__main__':
    print(random_translate(input("Text: ")))
