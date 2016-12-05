# named tuples
from collections import namedtuple

Battler = namedtuple("Battler", ["image", "power", "strength", "attributes"])
# name = Battler(image of them,
#                power level,
#                strong against those that have a(an),
#                weak against those that can exploit a(an))
"""for example, if chara has the attribute 'bloodlust' and sans has the
strength 'bloodlust', sans will beat chara."""
# make characters using the new namedtuple "Battler"
Mario = Battler("mario.jpg", 50, "none", ["none"])
sans = Battler("sans.jpg", 1, "lust for blood", ["body made of magic"])
Chara = Battler("chara.jpg", 99, "none", ["lust for blood"])
Batman = Battler("batman.jpg", 65, "exploitable weakness", ["none"])
Superman = Battler("superman.jpg", 100, "none", ["exploitable weakness"])
Doctor_Strange = Battler("doctor_strange.jpg", 80, "body made of magic",
                         ["exploitable weakness"])
Darth_Vader = Battler("darth_vader.jpg", 82, "none", ["none"])
# some characters can have multiple attributes
Alucard = Battler("alucard.jpg", 85, "none",
                  ["bloodlust", "body made of magic"])

# you can then use these items how you see fit
print(Mario.image)
print(Mario.power)
print(Mario.strength)
if "body made of magic" in Mario.attributes:
    print("Mario loses!")
