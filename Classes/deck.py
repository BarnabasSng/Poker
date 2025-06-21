"""Class module for a deck of 52 cards"""

import random
import card

class Deck:
    """Class representing a deck of 52 cards"""

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self):
        self.cards = [card.Card(rank, suit) for suit in self.suits for rank in range(2,15)]
        random.shuffle(self.cards)

    def deal(self, num: int) -> list:
        """Function to deal specified number of cards"""

        return [self.cards.pop() for _ in range(num)]
