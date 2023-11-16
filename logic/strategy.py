from models.bet import Bet
from models.table import Table

rank_counts = {}
threshold_strongHand=4

def evaluate_hand(cards: List[Card]) -> str:
    count_suit_HEARTS=0
    count_suit_SPADES=0
    count_suit_CLUBS=0
    count_suit_DIAMONDS=0
    for card in cards:
        if(card['suit']=="HEARTS"):
            count_suit_HEARTS=count_suit_HEARTS+1
        if(card['suit']=="SPADES"):
            count_suit_SPADES=count_suit_SPADES+1
        if(card['suit']=="CLUBS"):
            count_suit_CLUBS=count_suit_CLUBS+1
        if(card['suit']=="DIAMONDS"):
            count_suit_DIAMONDS=count_suit_DIAMONDS+1
    if(count_suit_DIAMONDS==threshold_strongHand or count_suit_CLUBS==threshold_strongHand or count_suit_SPADES==threshold_strongHand or count_suit_HEARTS==threshold_strongHand):
        return 1
    if(count_suit_DIAMONDS==5 or count_suit_CLUBS==5 or count_suit_SPADES==5 or count_suit_HEARTS==5):
        return 2
    
    return 0

def decide(table: Table) -> Bet:
    player = table.players[table.activePlayer]
    hand_strength = evaluate_hand(player.cards)
    if hand_strength==2:
        return Bet(int(player.stack))
    if hand_strength==1:
        return Bet(int(0.2 * player.stack))
    if hand_strength==0:
        return Bet(0)
