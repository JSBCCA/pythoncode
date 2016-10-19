import random
from termcolor import colored, cprint


class Gladiator:
    """A gladiator that fights to the death."""

    def __init__(self, health, rage, damage_low, damage_high):
        self.health = health  # starts at 100
        self.rage = rage  # is a percentage- starts at 0
        self.damage_low = damage_low
        self.damage_high = damage_high

    def __repr__(self):
        return 'Gladiator({0}, {1}, {2}, {3})'.format(
            self.health, self.rage, self.damage_low, self.damage_high)

    def __str__(self):
        return (str(self.name) + " has " + str(self.health) +
                " 'health' (out of 100), " + str(self.rage) + " 'rage', " +
                str(self.damage_low) + " for minimum damage output, and " +
                str(self.damage_high) + " for maximum damage output.")

    def attack(self, other):
        """
        Attacks a provided target- the attack either hits or crits.
        A hit does a random number between 'damage_low' and 'damage_high'
        points of damage.
        A crit does double the damage of a hit.
        The gladiator crits 'rage' percent of the time.
        If he crits, 'rage' is set to 0, otherwise it is increased by 15.
        Attack has a .2 percent chance of missing.
        If 'rage' is at 100 percent, player will enter Rage mode.
        In Rage mode, an attack will do 10x damage in exchange for all 'rage.'
        """
        damage = random.randint(self.damage_low, self.damage_high)
        miss = random.randint(0, 500)
        if self.rage == 100:
            damage *= 10
            self.rage = 0
            print(colored('RAGE-FILLED CRITICAL HIT!', 'red', attrs=['bold']))
        elif self.rage > random.randint(0, 100):
            damage *= 2
            self.rage = 0
            print("Critical hit!!")
        else:
            self.rage += 15
            if self.rage >= 100:
                self.rage = 100
                print(colored('RAGE MODE ENGAGED!!', 'red', attrs=['bold']))
        if miss == 100:
            print("Attack missed!")
        else:
            other.health -= damage
        if other.health < 0:
            other.health = 0
        other.isDead()

    def heal(self):
        """
        Increases the gladiators 'health' by 10, and decreases 'rage' by 10.
        Gladiator can't heal if they're dead, at max 'health', or if they
        have < 10 'rage'. If in Rage mode, can restore 'health' to max in
        exchange for all 'rage'.
        """
        if self.health > 0 and self.health < 100 and self.rage == 100:
            self.health += 100
            self.rage = 0
            print(colored('RAGE HEAL!', 'red', attrs=['bold']))
        elif self.health > 0 and self.health < 100 and self.rage >= 10:
            self.health += 12
            self.rage -= 10
        elif self.health == 100 or self.rage < 10:
            print("Can't heal now!")
        if self.health > 100:
            self.health = 100

    def isDead(self):
        """
        Returns whether or not the gladiator is alive.
        """
        if self.health < 1:
            if self.rage == 100:
                self.health = 1
                return False
            return True
        else:
            return False
