import os


def speak(message):
    print(message)
    os.system("say " + str(message.encode("unicode-escape")))


def ask(message):
    print(message)
    os.system("say " + str(message.encode("unicode-escape")))
    return input()


def who():
    color = ask("What is your favorite Color?")
    if color in ["Blue", "Blue.", "blue", "blue."]:
        animal = ask("Dogs or Cats?")
        if animal in ["Dogs", "dogs", "Dogs.", "dogs.", "Either", "either",
                      "Neither", "neither"]:
            glasses = ask("Do you wear glasses?")
            if glasses in ["Yes", "yes", "Yes.", "yes."]:
                speak("You must be Adam.")
            elif glasses in ["No", "no", "No.", "no."]:
                speak("You must be James Hakim.")
            else:
                speak("I don\'t know you.")
        elif animal in ["Cats", "cats"]:
            speak("You must be James Sibert.")
        else:
            speak("I don\'t know you.")

    elif color in ["Green", "green", "Green.", "green."]:
        speak("You must be Eddrick.")

    elif color in ["Dark Gray", "Dark gray", "dark gray", "dark grey",
                   "Dark Grey", "Dark grey", "Dark Gray.", "Dark Grey.",
                   "Grey", "grey", "gray", "Gray", "Gray.", "Grey."]:
        speak("You must be Sean.")

    elif color in ["White", "white", "White.", "white."]:
        glasses = ask("Do you wear glasses?")
        if glasses in ["Yes.", "Yes", "yes.", "yes"]:
            speak("You must be Ricky.")
        else:
            speak("You must be Keegan.")

    elif color in ["Red", "red", "Red.", "red."]:
        glasses = ask("Do you wear glasses?")
        if glasses in ["Yes", "yes", "Yes.", "yes."]:
            speak("You must be Martin.")
        elif glasses in ["No", "no", "No.", "no."]:
            county = ask("What county do you live in?")
            if county in ["Sardis.", "sardis.", "Sardis", "sardis"]:
                speak("You must be Dustin.")
            elif county in ["Water Valley", "Water valley", "water valley",
                            "watervalley", "Water Valley."]:
                speak("You must be Kyle.")
            else:
                speak("I don\'t know you.")
        else:
            speak("I don\'t know you.")

    elif color in ["Black.", "Black", "black.", "black"]:
        vehicle = ask("Do you prefer Cars or Trucks?")
        if vehicle in ["Cars.", "Cars", "cars.", "cars"]:
            speak("You must be Jacob.")
        else:
            speak("You must be Haleem.")

    elif color in ["Yellow.", "Yellow", "yellow.", "yellow"]:
        speak("You must be Addey.")

    elif color in ["Purple.", "Purple", "purple.", "purple"]:
        speak("You must be Onna.")

    elif color in ["Mint Green.", "Mint Green", "Mint green.", "Mint green",
                   "mint green.", "mint green", "Coral.", "Coral", "coral.",
                   "coral", "mint", "Mint"]:
        speak("You must be Nicole.")

    elif color in ["I don\'t have one", "I dont have one",
                   "I don\'t have one.", "I dont have one.", "None", "none",
                   "None.", "none.", "i dont have one", "i dont have one.",
                   "i don\'t have one", "i don\'t have one."]:
        speak("You must be Nate.")

    else:
        speak("I don\'t know you.")
