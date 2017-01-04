def trans(x):
    t = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                      "mnopqrstuvwxyzabcdefghijklMNOPQRSTUVWXYZABCDEFGHIJKL")
    return str(x).translate(t)


with open("alice_in.txt", 'r') as alice:
    with open("alice_cipher.txt", 'w') as ciph:
        ciph.write(trans(alice.read()))

# with open("alice_in.txt", 'r') as file:
#     alice = file.read()
#
# ciph = trans(alice)
#
# with open("alice_cipher.txt", 'w') as file:
#     file.write(ciph)
