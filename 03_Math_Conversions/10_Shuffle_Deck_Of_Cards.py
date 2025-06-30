import itertools
import random

# Define the suits and ranks
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# Create the full deck using Cartesian product
deck = list(itertools.product(ranks, suits))

# Shuffle the deck
random.shuffle(deck)

# Display the shuffled deck
print("Shuffled deck of cards:")
for card in deck:
    print(card[0], "of", card[1])
