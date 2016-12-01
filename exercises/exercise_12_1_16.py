# 140 character or less snippets that should be full sentences
from random import choice

with open("tale_of.txt", 'r') as file:
    tale = file.readlines()

temptale = []
for line in tale:
    temptale.append(line.replace("Mr.", "Mister").replace(
        "Mrs.", "Missus").replace("Dr.", "Doctor"))

tale = "".join(temptale[106:16155])
splittale = tale.split(".")

tale = []
for sentence in splittale:
    tale.append(sentence.replace("\n", " "))


def random_snippet():
    while True:
        t = choice(tale).strip() + "."
        if (len(t) > 7) and (len(t) < 141):
            return t


print('<' + random_snippet() + '>')
while True:
    pause = input("").upper().strip()
    if pause == "Q":
        break
    else:
        print('<' + random_snippet() + '>')
