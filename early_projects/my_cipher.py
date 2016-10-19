def translate_to():
    t = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
                      "klmnopqrstuvwxyzabcdefghijKLMNOPQRSTUVWXYZABCDEFGHIJ")
    x = str(input("What do you want to translate? (all lowercase): "))
    print(x.translate(t))


translate_to()

# s
# e
# k
