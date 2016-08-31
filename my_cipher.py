def translate_to():
    t = str.maketrans("abcdefghijklmnopqrstuvwxyz", "xyzabcdefghijklmnopqrstuv"
                      "w")
    x = str(input("What do you want to translate? (all lowercase): "))
    print(x.translate(t))
