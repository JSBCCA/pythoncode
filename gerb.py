males = input("What are the names of the males?")  # {stuff, stuff}
females = input("What are the names of the females?")


def mating_pairs(males, females):
    """set, set -> set(tuple, tuple)

    Returns a set of pairs; two tuples containing both a male and a female.

    >>>mating_pairs({'male1', 'male2'}, {'female1', 'female2'})
    {('male1', 'female1'), ('male2', 'female2')}

    >>>mating_pairs({'1', '2', '3'}, {'a', 'b', 'c'})
    {('1', 'a'), ('2', 'b'), ('3', 'c')}
    """
    settup = set()
    while len(males) > 0 and len(females) > 0:
        newlist = []
        y = males.pop()
        newlist.append(y)
        z = females.pop()
        newlist.append(z)
        settup.add((y, z))
    print(settup)


mating_pairs(males, females)
