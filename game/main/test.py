import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from win_conditions.royal_flush import royale_flush_check

player_one_hand = [[10,"s"],[11,"s"],[12,"s"],[13,"s"],[14,"s"], [5,"d"], [7,"c"]]


royale_flush_check(player_one_hand)