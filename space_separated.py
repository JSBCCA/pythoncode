def space_sep(txt):
    sym = "1234567890)(*&^%$#@!-=_+][}{\\|;:\'\"/?>.<,"
    return (sorted(set((''.join(c for c in txt
                                if c not in sym)).split()) - set("")))

# txt = input("Enter your space separated entries:\n").strip().lower()
# sym = "1234567890)(*&^%$#@!-=_+][}{\\|;:\'\"/?>.<,"
# print(sorted(set((''.join(c for c in txt if c not in sym)).split()) - set("")))

# print(sorted(set((''.join(
#     c for c in (input('Enter your space separated entries:\n').strip().lower())
#     if c not in '1234567890)(*&^%$#@!-=_+][}{\\|;:\'\"/?>.<,')).split()) - set(
#         '')))


def test_space_sep():
    assert space_sep("a b c") == ['a', 'b', 'c']
    assert space_sep("123245") == []
    assert space_sep("abc, and") == ['abc', 'and']


def test_space_sep_two():
    assert space_sep("!!!aaaaaaa") == ['aaaaaaa']
    assert space_sep("a1b2, 5678 and ; 67 for") == ['ab', 'and', 'for']
    assert space_sep("once upon a time,") == ['a', 'once', 'time', 'upon']


if __name__ == '__main__':
    txt = input("Enter your space separated entries:\n").strip().lower()
    print(space_sep(txt))
