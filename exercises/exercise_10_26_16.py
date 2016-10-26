def palindrome(t):  # remove non-letters, make lower
    nt = ''.join(list(filter(lambda c: c.isalpha(), list(t.strip().lower()))))
    if (str(nt) == str(nt)[::-1]) and (len(nt) > 0):  # check for palindrome
        return True
    else:
        return False


if __name__ == '__main__':
    yours = input("Insert your palindrome: ")
    print(palindrome(yours))
