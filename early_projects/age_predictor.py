def age_predict():
    name = input("What is your name?\n")
    print("Hello " + name + " it is nice to meet you!")
    x = True
    while x:
        age = input("How old are you " + name + "?\n")
        if age.isnumeric():
            x = False
        else:
            print("Please try again.")
    age_date = ((100 - (int(age))) + 2016)
    print(name + " will turn 100 in the year " + str(age_date) + "!")
    if ((int(age) % 2) == 0):
        print(age + " is an even number!")
    else:
        print(age + " is an odd number :(")

    if ((age_date % 3) == 0):
        print("The year " + str(age_date) + " is divisible by three!")
    else:
        print("The year " + str(age_date) + " is not divisible by three :(")
    print("The first letter of your name repeated " + age + " times is " + (
        name[0] * int(age)))


age_predict()
