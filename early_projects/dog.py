# false = dominant: dark eyes, upright ears, short coat
# true = recessive: light eyes, floppy ears, long coat
# and


def dog():
    dad_ears = input("Does the dad dog have upright ears?\n")
    mom_ears = input("Does the mom dog have upright ears?\n")

    if (dad_ears == "yes") or (mom_ears == "yes"):
        puppy_ears = "upright"
    elif (dad_ears == "no") and (mom_ears == "no"):
        puppy_ears = "floppy"
    else:
        puppy_ears = "unknown"
    dad_eyes = input("Does the dad dog have dark eyes?\n")
    mom_eyes = input("Does the mom dog have dark eyes?\n")

    if (dad_eyes == "yes") or (mom_eyes == "yes"):
        puppy_eyes = "dark"
    elif (dad_eyes == "no") and (mom_eyes == "no"):
        puppy_eyes = "light"
    else:
        puppy_eyes = "unknown"
    dad_coat = input("Does the dad dog have a short coat?\n")
    mom_coat = input("Does the mom dog have a short coat?\n")
    if (dad_coat == "yes") or (mom_coat == "yes"):
        puppy_coat = "short"
    elif (dad_coat == "no") and (mom_coat == "no"):
        puppy_coat = "long"
    else:
        puppy_coat = "unknown"

    print("The puppy will have " + puppy_eyes + " eyes, " + puppy_ears +
          " ears, and a " + puppy_coat + " coat.")


dog()
