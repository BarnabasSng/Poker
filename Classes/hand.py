"""Class module for a hand of 5 cards"""

import card

class Hand:
    """Class to represent a hand of 5 cards of a player, 2 hole cards and 3 community cards.
    Hand rankings are as follows: Straight Flush, Four of a kind, Full House, Flush, Straight, Three of a Kind,
    Two Pair, Pair, High Card"""

    def __init__(self, cards: list[card.Card]):
        """Cards are sorted in descending order"""
        self.cards = cards
        cards.sort(reverse=True)
        self.ranks = [card.rank for card in self.cards]
        self.suits = [card.suit for card in self.cards]

    def is_straight(self) -> bool:
        """Function to check if hand contains a straight"""
        if len(set(self.ranks)) == 5:
            if self.ranks[0] - self.ranks[-1] == 4:
                return True
            elif self.ranks == [14,5,4,3,2]:
                return True
        return False
    
    def is_flush(self) -> bool:
        """Function to check if hand contains a flush"""
        return True if len(set(self.suits)) == 1 else False
    
    def is_straight_flush(self) -> bool:
        """Function to check if hand contains a straight flush"""
        return self.is_straight() and self.is_flush()
    
    def is_pair(self) -> bool:
        """Function to check if hand contains a pair"""
        return True if len(set(self.ranks)) <= 4 else False
    
    def is_three_of_a_kind(self) -> bool:
        """Function to check if hand contains a three of a kind"""
        for rank in set(self.ranks):
            if self.ranks.count(rank) >= 3:
                return True
        return False
    
    def is_four_of_a_kind(self) -> bool:
        """Function to check if hand contains a four of a kind"""
        for rank in set(self.ranks):
            if self.ranks.count(rank) == 4:
                return True
        return False
        
    def is_two_pair(self) -> bool:
        """Function to check if hand contains a two pair"""
        count = 0
        for rank in set(self.ranks):
            if self.ranks.count(rank) >= 2:
                count += 1
        return count==2
    
    def is_full_house(self) -> bool:
        """Function to check if hand contains a full house"""
        return self.is_two_pair() and len(self.ranks) == 2
    
    def evaluate_hand(self) -> tuple:
        """Function to evaluate the strength of a hand. The function returns a tuple of numbers,
        where the first number is the ranking of the hand (Straight flush has highest rank 8, High card has rank 0)
        and the following numbers are the kicker cards depending on the type of hand"""
        if self.is_straight_flush():
            return (8,self.ranks[0])
        if self.is_four_of_a_kind():
            four_of_a_kind = [rank for rank in self.ranks if self.ranks.count(rank) == 4].pop()
            kicker = [rank for rank in self.ranks if rank != four_of_a_kind].pop()
            return (7, four_of_a_kind, kicker)
