import myshop


def movie(name):
    two = round((9.99 * 1.07), 2)
    print("Here is your Ticket and movie receipt.\n[Ticket for", name,
          " - $" + str(two) + "]\nEnjoy the film!")


def concession():
    print("  Refreshments:\n"
          "Popcorn - $5.05\n"
          "Coke    - $2.19\n"
          "Cookies - $1.50\n"
          "Alright, you want to buy-\n")
    a = int(input("How many Popcorn buckets? ").strip())
    b = int(input("How many Cokes? ").strip())
    c = int(input("How many Cookies? ").strip())
    myshop.myshop(a, b, c)


def theater():
    name = input("Hello! What is your name?").strip().capitalize()
    film = input("Thank you for coming, " + name + "! " + "Welcome to "
                 "the Malco Theater!\n"
                 "What film would you like to go see today?\n"
                 "      Films:\n"
                 "The Avengers: 8:00\n"
                 "Frozen:       7:00\n"
                 "Star Wars:    7:30\n"
                 "Harry Potter: 5:00\n"
                 "Shrek:        4:30\n"
                 "\n"
                 "  Tickets: $9.99").strip().lower()
    if film == "the avengers":
        would = input("Would you like to buy some concessions?").strip().lower(
        )
        if would == "yes":
            concession()
            movie(film.title())
        else:
            print("Just the movie then? Alright.")
            movie(film.title())
    elif film == "frozen":
        would = input("Would you like to buy some concessions?").strip().lower(
        )
        if would == "yes":
            concession()
            movie(film.title())
        else:
            print("Just the movie then? Alright.")
            movie(film.title())
    elif film == "star wars":
        would = input("Would you like to buy some concessions?").strip().lower(
        )
        if would == "yes":
            concession()
            movie(film.title())
        else:
            print("Just the movie then? Alright.")
            movie(film.title())
    elif film == "harry potter":
        would = input("Would you like to buy some concessions?").strip().lower(
        )
        if would == "yes":
            concession()
            movie(film.title())
        else:
            print("Just the movie then? Alright.")
            movie(film.title())
    elif film == "shrek":
        would = input("Would you like to buy some concessions?").strip().lower(
        )
        if would == "yes":
            concession()
            movie(film.title())
        else:
            print("Just the movie then? Alright.")
            movie(film.title())
    else:
        print("Oh, did you change your mind...? Well then, have a nice day!")


theater()
