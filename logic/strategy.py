from models.bet import Bet
from models.table import Table


#def decide(table: Table) -> Bet:

 #   return Bet(20)


def decide(table: Table) -> Bet:
    # Deine Implementierung hier
    return Bet(bet=table.players[table.activePlayer].stack)
