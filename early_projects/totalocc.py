def total_occurences(s1, s2, ch):
    """(str, str, str) -> int

    Precondition: len(ch) == 1

    Return the total number of times ch appears in s1 and s2.

    >>> total_occurences('red', 'blue', 'u')
    1
    """
    # total_occurences('Yellow', 'Blue', 'u')
    return (s1 + s2).count(ch)


if __name__ == '__main__':
    one = input('What is string one? ')
    two = input('What is string two? ')
    three = input('What is the letter? ')
    print(total_occurences(one, two, three))
