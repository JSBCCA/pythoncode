def palin(p):
    np = list(filter(str.isalpha, p.lower()))  # remove non-letters
    return np == np[::-1] and len(np) > 0  # check if palindrome


if __name__ == '__main__':
    t = input("Text: ")
    print(palin(t))
