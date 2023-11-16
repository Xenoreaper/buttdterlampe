from models.bet import Bet
from models.table import Table

def decide(table: Table) -> Bet:
    player = table.players[table.activePlayer]
    bet_amount = int(0.7 * player.stack) 
