import random
names = ["CHARLIE", "TED", "BILL", "JUDY", "KATIE", "CATHERINE", "BOB",
         "JOSEPH", "STEVE", "HOLLY", "MARY", "MARTY"]
while True:
    year = random.randint(10, 85)
    name = random.choice(names)
    things = [("NO, NOT SINCE 19" + str(year) + "!"),
              ("SOMEONE HUSH THAT DOG!"),
              ("SORRY " + name + ", I DON'T HAVE ANY MORE COOKIES!"),
              ("* War Flashbacks *")]
    x = input()
    if x.isupper() is False:
        print("\nHUH?! SPEAK UP, SONNY!")
    elif x == "BYE" or x == "BYE!":
        break
    elif x.isupper() is True:
        print("\n" + random.choice(things))
