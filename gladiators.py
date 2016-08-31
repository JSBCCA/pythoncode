from gladiator_class import Gladiator
from termcolor import colored, cprint
import math
import os

os.system("printf '\\e[8;23;52t'")


def ask(message):
    print(message)
    return input()


def first():
    name1 = ask("What is Player one's name?").strip().title()
    if name1 in ['James', 'Ragnarok', 'Infinity', 'Oblivion', 'Perseus',
                 'Excalibur', 'Big the Cat', 'Zero', 'Shadow', 'Omega',
                 'Edgar', 'Neo', 'Sibert', 'Pruitt', 'Bullock', 'Peyton',
                 'Taylor', 'Roxas', 'Sarah', 'Xemnas', 'Silver', 'Baka', 'X']:
        print('\nWow, cool name!')
        return name1
    else:
        return name1


def second():
    name2 = ask("What is Player two's name?").strip().title()
    if name2 in ['James', 'Ragnarok', 'Infinity', 'Oblivion', 'Perseus',
                 'Excalibur', 'Big the Cat', 'Zero', 'Shadow', 'Omega',
                 'Edgar', 'Neo', 'Sibert', 'Pruitt', 'Bullock', 'Peyton',
                 'Taylor', 'Roxas', 'Sarah', 'Xemnas', 'Silver', 'Baka', 'X']:
        print('\nWow, cool name!')
        return name2
    else:
        return name2


print('\n' * 20)
print('_' * 52)
name1 = first()
print('\n')
name2 = second()


def bar(n, color):
    num_colored = math.ceil(n / 10)
    num_space = 10 - num_colored
    return colored(" " * num_colored, color, attrs=['reverse']) +\
                  (" " * num_space)


health_bar = lambda n: bar(n, 'green')
rage_bar = lambda n: bar(n, 'red')


def showstuff(g1, g2):
    linef = "{0:<21}  {1:<21}"
    linef2 = "{0:<35} {1:<35}"
    print(linef.format(str(name1), str(name2)))
    print(linef2.format(("Health: {0} " + str(g1.health)).format(health_bar(
        g1.health)), ("Health: {0} " + str(g2.health)).format(health_bar(
            g2.health))))
    print(linef2.format(("Rage:   {0} " + str(g1.rage)).format(rage_bar(
        g1.rage)), ("Rage:   {0} " + str(g2.rage)).format(rage_bar(g2.rage))))
    print('\n\n')


def play1turn():
    x = input(str(name1) + ": Attack or heal? ").strip().lower()
    if x in ['attack', 'a']:
        print("\n\n" + str(name1) + " attacks!")
        return glad1.attack(glad2)
    elif x in ['heal', 'h']:
        print("\n\n" + str(name1) + " tries to heal!")
        return glad1.heal()
    else:
        print("Sorry, try again.")
        play1turn()


def play2turn():
    y = input(str(name2) + ": Attack or heal? ").strip().lower()
    if y in ['attack', 'a']:
        print("\n\n" + str(name2) + " attacks!")
        return glad2.attack(glad1)
    elif y in ['heal', 'h']:
        print("\n\n" + str(name2) + " tries to heal!")
        return glad2.heal()
    else:
        print("Sorry, try again.")
        play2turn()

#  Game where two gladiators fight to the death; controlled via input.
# 'name', 'health', 'rage', 'lowest damage', 'highest damage'
# 'health' starts at 100, 'rage' is a percentage that starts at 0.

glad1 = Gladiator(100, 0, 5, 15)
glad2 = Gladiator(100, 0, 6, 16)

print('\n' * 12)
print("""   _____ _           _ _       _
  / ____| |         | (_)     | |
 | |  __| | __ _  __| |_  __ _| |_ ___  _ __
 | | |_ | |/ _` |/ _` | |/ _` | __/ _ \| '__|
 | |__| | | (_| | (_| | | (_| | || (_) | |
  \_____|_|\__,_|\__,_|_|\__,_|\__\___/|_|   """)
print('_' * 52)
print('\n' * 6)

showstuff(glad1, glad2)
while (glad1.isDead() or glad2.isDead()) is False:
    play1turn()
    print('\n' + ('_' * 52))
    showstuff(glad1, glad2)
    if glad1.isDead() is True:
        print(str(name2) + " wins!!")
        break
    elif glad2.isDead() is True:
        print(str(name1) + " wins!!")
        break

    play2turn()
    print('\n' + ('_' * 52))
    showstuff(glad1, glad2)
    if glad1.isDead() is True:
        print(str(name2) + " wins!!")
        break
    elif glad2.isDead() is True:
        print(str(name1) + " wins!!")
        break
