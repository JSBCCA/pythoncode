def trans(x):
    t = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                      "mnopqrstuvwxyzabcdefghijklMNOPQRSTUVWXYZABCDEFGHIJKL")
    return x.translate(t)


with open("alice_in.txt", 'r') as alice:
    with open("alice_cipher.txt", 'w') as ciph:
        ciph.write(trans(alice.read()))
