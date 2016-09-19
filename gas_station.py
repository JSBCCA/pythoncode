def price(x, y):
    one = (int(input("How many gallons?: "))) * x
    two = round((one), 2)
    print("Here is your receipt.\n " + str(y).title() + " - $" + str(two) +
          "\nThank you for shopping with us!")


def gas():
    gas = input("Welcome!\nWhat kind of gas would you like?\nRegular : $2.09\n"
                "Midgrade : $2.29\nPremium : $2.49\n").strip().lower()
    if gas == "regular":
        price(2.09, gas)
    elif gas == "midgrade":
        price(2.29, gas)
    elif gas == "premium":
        price(2.49, gas)
    else:
        print("Well, have a nice day!")


gas()
