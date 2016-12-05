from gladiator_class import Gladiator
from termcolor import colored, cprint
import math
import os


def name(player):
    name = input("What is Player " + player + "'s name? ").strip().title()
    return name


def bar(n, color):
    num_colored = math.ceil(n / 10)
    num_space = 10 - num_colored
    return colored(" " * num_colored, color, attrs=['reverse']) +\
                  (" " * num_space)


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


def playerturn(glad1, glad2, name):
    x = input(str(name) + ": Attack or heal? ").strip().lower()
    if x in ['attack', 'a']:
        print("\n\n" + str(name) + " attacks!")
        return glad1.attack(glad2)
    elif x in ['heal', 'h']:
        print("\n\n" + str(name) + " tries to heal!")
        return glad1.heal()
    else:
        print("Sorry, try again.")
        playerturn()

#  Game where two gladiators fight to the death; controlled via input.
# 'name', 'health', 'rage', 'lowest damage', 'highest damage'
# 'health' starts at 100, 'rage' is a percentage that starts at 0.

os.system("printf '\\e[8;23;52t'")

print('\n' * 20)
print('_' * 52)
name1 = name("One")
print('\n')
name2 = name("Two")

health_bar = lambda n: bar(n, 'green')
rage_bar = lambda n: bar(n, 'red')

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

    playerturn(glad1, glad2, name1)
    print('\n' + ('_' * 52))
    showstuff(glad1, glad2)
    if glad1.isDead() is True:
        print(str(name2) + " wins!!")
        break
    elif glad2.isDead() is True:
        print(str(name1) + " wins!!")
        break

    playerturn(glad2, glad1, name2)
    print('\n' + ('_' * 52))
    showstuff(glad1, glad2)
    if glad1.isDead() is True:
        print(str(name2) + " wins!!")
        break
    elif glad2.isDead() is True:
        print(str(name1) + " wins!!")
        break
