from random import choice
with open('pokemon.txt', 'r') as file:
    pokemon = file.read().strip().lower().split('\n')
poke = choice(pokemon)
p_list = [poke]
while True:
    print(poke)
    pokemon.remove(poke)
    compatible = list(filter(lambda n: n[0] == poke[-1], pokemon))
    if len(compatible) > 0:
        poke = choice(compatible)
        p_list.append(poke)
    else:
        break
print('\n' + str(len(p_list)))
