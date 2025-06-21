import card, random

class Deck:
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self):
        self.cards = [card.Card(rank, suit) for suit in self.suits for rank in range(2,15)]
        random.shuffle(self.cards)

    def deal(self, num: int) -> list:
        return [self.cards.pop() for _ in range(num)]
    
    