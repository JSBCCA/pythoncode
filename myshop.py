# Glitch-fixing placeholder


def myshop(popcorn=0,
           coke=0,
           cookies=0, ):
    one = popcorn * 5.05
    two = coke * 2.19
    three = cookies * 1.50
    four = (one + two + three)
    five = round((four * 1.07), 2)
    if five > 0:
        print("\nHere is your receipt. [$" + str(five) + "]. Also...")
    else:
        print("Oh, did you change your mind? Well then...\n")
