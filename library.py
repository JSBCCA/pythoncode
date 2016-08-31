def ask(m):
    print(m)
    return input()


def lib():
    a = ask("     Books in stock:\n"
            "Harry Potter  - 1 in Stock\n"
            "Percy Jackson - Out of Stock\n"
            "Mind stuff    - 1 in Stock\n").strip().lower()
    if a == "harry potter":
        print("Alright, here is your copy of Harry Potter. Have a nice day!")
    elif a == "percy jackson":
        print("Sorry, we're out of that book... Anything else you want?")
        lib()
    elif a == "mind stuff":
        print("Alright, here is your copy of Mind Stuff. Have a nice day!")
    else:
        print("Sorry, we don't have that book... Anything else you want?")
        lib()


print("Welcome! What book would you like?")
lib()
