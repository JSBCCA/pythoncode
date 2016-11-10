import random
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
possible_cards = ['S', 'D', 'C', 'H']
deck = []
for suit in possible_cards:
    for card in ranks:
        deck.append(card + suit)
random.shuffle(deck)
print(deck)
