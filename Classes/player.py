class Player:
    def __init__(self, chips):
        self.hand = []
        self.chips = chips
        self.current_bet = 0
        self.folded = False

    def bet(self, amount):
        self.chips -= amount
        self.current_bet += amount

    def fold(self):
        self.folded = True
