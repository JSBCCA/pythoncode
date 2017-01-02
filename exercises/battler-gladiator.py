from battler_gladiator_class import Gladiator
from termcolor import colored, cprint
from collections import namedtuple
import math
import os

Battler = namedtuple("Battler", ["name", "lpow", "hpow", "strength", "attr"])
Mario = Battler("Mario", 10, 50, "none", ["none"])
Batman = Battler("Batman", 13, 65, "exploitable weakness", ["none"])
Sans = Battler("Sans", 1, 1, "lust for blood", ["body made of magic"])
battlers = [Sans, Mario, Batman]


def name(player):
    name = input("What is Player " + player + "'s name? ").strip().title()
    if name in battlers:
        return name
    else:
        name(player)


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
for battler in battlers:
    print(battler.name)
print('_' * 52)
name1 = name("One")  # this suddenly isn't working for some reason...
print('\n')
name2 = name("Two")  # this suddenly isn't working for some reason...

health_bar = lambda n: bar(n, 'green')  # can i fix this already??
rage_bar = lambda n: bar(n, 'red')  # can i fix this already??

glad1 = Gladiator(100, 0, 5, 15)  # name1.lpow, .hpow, .strength, .attr
glad2 = Gladiator(100, 0, 6, 16)

print('\n' * 12)
print("Battler Gladiator Combo")
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
