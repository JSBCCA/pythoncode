def palindrome(p):  # remove non-letters, make lower
    np = ''.join(list(filter(lambda c: c.isalpha(), list(p.strip().lower()))))
    return (np == np[::-1]) and (len(np) > 0)  # check if palindrome


if __name__ == '__main__':
    t = input("Give text: ")
    print(palindrome(t))
