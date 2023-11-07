from models.rank import Rank
from models.suit import Suit


class Card:
    rank: Rank
    suit: Suit

    def __init__(self, card: dict):
        self.rank = Rank(card['rank'])
        self.suit = Suit(card['suit'])
