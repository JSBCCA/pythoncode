import os


def speak(message):
    print(message)
    os.system("say " + str(message.encode("unicode-escape")))


def ask(message):
    print(message)
    os.system("say " + str(message.encode("unicode-escape")))
    return input()


def who():
    color = ask("What is your favorite Color?").lower()
    if color == "blue":
        animal = ask("Dogs or Cats?").lower()
        if animal in ["dogs", "either", "neither"]:
            glasses = ask("Do you wear glasses?").lower()
            if glasses == "yes":
                speak("You must be Adam.")
            elif glasses == "no":
                speak("You must be James Hakim.")
            else:
                speak("I don\'t know you.")
        elif animal == "cats":
            speak("You must be James Sibert.")
        else:
            speak("I don\'t know you.")

    elif color == "green":
        speak("You must be Eddrick.")

    elif color in ["dark grey", "dark gray", 'grey', 'gray']:
        speak("You must be Sean.")

    elif color == 'white':
        glasses = ask("Do you wear glasses?").lower()
        if glasses == 'yes':
            speak("You must be Ricky.")
        else:
            speak("You must be Keegan.")

    elif color == 'red':
        glasses = ask("Do you wear glasses?").lower()
        if glasses == 'yes':
            speak("You must be Martin.")
        elif glasses == 'no':
            speak("You must be Dustin.")

    elif color == 'black':
        speak("You must be Jacob.")

    elif color == 'yellow':
        speak("You must be Addey.")

    elif color == 'purple':
        speak("You must be Onna.")

    elif color in ['mint', 'mint green', 'coral']:
        speak("You must be Nicole.")

    elif color in ['i dont have one', 'i don\'t have one', 'none',
                   'dont have one', 'nothing']:
        speak("You must be Nate.")

    else:
        speak("I don\'t know you.")
