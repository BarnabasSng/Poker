class Card:
    def __init__(self, rank: int, suit: str):
        self.rank = rank
        self.suit = suit

    def return_readable_rank(rank: int) -> str:
        jqka_dict = {11:'Jack', 12:'Queen', 13 : 'King', 14:'Ace'}
        if rank in jqka_dict:
            return jqka_dict[rank]
        return rank

    def __str__(self):
        return f"{self.return_readable_rank(self.rank)} of {self.suit}"

    def __repr__(self):
        return f"Card(rank={self.rank},suit={self.suit})"