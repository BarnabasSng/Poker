"""Class module for a player. Contains information such as amount of chips available"""

class Player:
    """Class representing a poker player"""

    def __init__(self, chips):
        self.hand = []
        self.chips = chips
        self.current_bet = 0
        self.folded = False

    def bet(self, amount):
        """Function to bet a specified amount of chips"""
        self.chips -= amount
        self.current_bet += amount

    def fold(self):
        """Function to fold out of this round"""
        
        self.folded = True
