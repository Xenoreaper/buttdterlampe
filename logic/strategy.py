from models.bet import Bet
from models.table import Table


#def decide(table: Table) -> Bet:

 #   return Bet(20)


def decide(table: Table) -> Bet:
    player = table.players[table.activePlayer]
    bet_amount = int(0.2 * player.stack)  # Setzt 20% des Chip-Stacks
