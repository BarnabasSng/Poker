"""Class module for a game of poker"""

import deck
import player

class Game:
    """Class to represent a round of poker"""

    def __init__(self, num_of_players: list):
        self.players = [player.Player(500) for _ in range(num_of_players)]
        self.deck = deck.Deck()
        self.community_cards = []
        self.pot = 0
        self.current_bet = 0

    # def deal_hole_cards(self):
        # for player in self.players:
        #     player.hand = 
