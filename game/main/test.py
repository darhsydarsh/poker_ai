import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from win_conditions.win_conditions import *


royale_hand = [[10,"h"],[11,"h"],[12,"h"],[14,"h"],[13,"h"]]
straight_flush_hand = [[6,"s"],[7,"s"],[8,"s"],[9,"s"],[10,"s"]]
four_of_a_kind_hand = [[9,"h"],[9,"s"],[9,"c"],[9,"d"],[3,"h"],[3,"s"],[5,"d"]]



# royale_flush_check(royale_hand)
# straight_flush_check(straight_flush_hand)
# four_of_a_kind_check(four_of_a_kind_hand)
# flush_check(royale_hand)
# straight_check(royale_hand)
# straight_check(straight_flush_hand)
# three_of_a_kind_check(four_of_a_kind_hand)
# two_pair(four_of_a_kind_hand)
# pair(four_of_a_kind_hand)
# high_card(four_of_a_kind_hand)
# full_house_check(four_of_a_kind_hand)

four_of_a_kind_check(four_of_a_kind_hand)
