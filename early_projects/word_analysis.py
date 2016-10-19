def word_analyze(text):
    letters = ''.join(c for c in text if c.isalpha())
    vowels = ''.join(c for c in text if c.lower() in "aeiou")
    return ("-".join(letters)) + "\nTotal Text Length: " + str(len(
        text)) + "\nNumber of Letters: " + str(len(
            letters)) + "\nNumber of Vowels: " + str(len(vowels))

# text = input("What text would you like to analyze? ")
# letters = ''.join(c for c in text if c.isalpha())
# vowels = ''.join(c for c in text if c.lower() in "aeiou")
# print("-".join(letters), "\nTotal Text Length:", str(len(text)),
#       "\nNumber of Letters:", str(len(letters)), "\nNumber of Vowels:",
#       str(len(vowels)))

# t = input('What text would you like to analyze? ')
# l = (''.join(c for c in t if c.isalpha()))
# print('-'.join(l), '\nTotal Text Length:', str(len(t)), '\nNumber of Letters:',
#       str(len(l)), '\nNumber of Vowels:',
#       str(len(''.join(c for c in t if c.lower() in 'aeiou'))))


def test_word_analyze():
    assert word_analyze("abcdefg") == """a-b-c-d-e-f-g
Total Text Length: 7
Number of Letters: 7
Number of Vowels: 2"""
    assert word_analyze("12345") == """
Total Text Length: 5
Number of Letters: 0
Number of Vowels: 0"""


def test_word_analyze_two():
    assert word_analyze("James Sibert") == """J-a-m-e-s-S-i-b-e-r-t
Total Text Length: 12
Number of Letters: 11
Number of Vowels: 4"""
    assert word_analyze(
        "Base234 Camp888 coding7;") == """B-a-s-e-C-a-m-p-c-o-d-i-n-g
Total Text Length: 24
Number of Letters: 14
Number of Vowels: 5"""


if __name__ == '__main__':
    text = input("What text would you like to analyze? ")
    print(word_analyze(text))
