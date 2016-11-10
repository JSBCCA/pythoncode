import random
ranks, suits = list('A123456789TJQK'), list('SDCH')
deck = []
for suit in suits:
    for num in ranks:
        deck.append(num + suit)
random.shuffle(deck)
print(deck)
