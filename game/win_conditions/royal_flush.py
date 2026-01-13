import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from deck.Deck import Deck


royal_flush_heart = [[10,"h"],[11,"h"],[12,"h"],[13,"h"],[14,"h"]]
royal_flush_spade = [[10,"s"],[11,"s"],[12,"s"],[13,"s"],[14,"s"]]
royal_flush_club = [[10,"c"],[11,"c"],[12,"c"],[13,"c"],[14,"c"]]
royal_flush_diamond = [[10,"d"],[11,"d"],[12,"d"],[13,"d"],[14,"d"]]

royale_flushes = [royal_flush_heart, royal_flush_spade, royal_flush_club, royal_flush_diamond]


def royale_flush_check(player_cards):
    for royal_flush in royale_flushes:
        if all(card in player_cards for card in royal_flush):
            print("Royal Flush Found with cards: ", royal_flush)
            return True
    print("No Royal Flush Found")
    return False 

