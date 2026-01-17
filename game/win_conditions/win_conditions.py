import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from deck.Deck import Deck
from collections import Counter


royal_flush_heart = [[10,"h"],[11,"h"],[12,"h"],[13,"h"],[14,"h"]]
royal_flush_spade = [[10,"s"],[11,"s"],[12,"s"],[13,"s"],[14,"s"]]
royal_flush_club = [[10,"c"],[11,"c"],[12,"c"],[13,"c"],[14,"c"]]
royal_flush_diamond = [[10,"d"],[11,"d"],[12,"d"],[13,"d"],[14,"d"]]

royale_flushes = [royal_flush_heart, royal_flush_spade, royal_flush_club, royal_flush_diamond]
suits = ['h', 's', 'c', 'd']

def royale_flush_check(player_cards):
    for royal_flush in royale_flushes:
        if all(card in player_cards for card in royal_flush):
            print("Royal Flush Found with cards: ", royal_flush)
            return True
    print("No Royal Flush Found")
    return False 



def straight_flush_check(player_cards):
    for suit in suits:
        suited_cards = sorted([card[0] for card in player_cards if card[1] == suit])

        for i in range(len(suited_cards) - 4):
            if suited_cards[i+4] - suited_cards[i] == 4 and len(set(suited_cards[i:i+5])) == 5:
                straight_flush = [[rank, suit] for rank in range(suited_cards[i], suited_cards[i]+5)]
                print("Straight Flush Found with cards: ", straight_flush)
                return True
            
    print("No Straight Flush Found")
    return False



def four_of_a_kind_check(player_cards):
    print(player_cards)
    ranks = [card[0] for card in player_cards]
    # Count the frequency of each rank
    rank_counts = Counter(ranks)
    # Check if any rank has a count of 4
    for count in rank_counts.values():
        print(count)
        if count == 4:
            print("Four of a Kind Found with cards: ", rank_counts, [card for card in player_cards if card[0] == count])
            return True
        
    print("No Four of a Kind Found")
    return False




def flush_check(player_cards):
    suits_count = {'h': 0, 's': 0, 'c': 0, 'd': 0}
    for card in player_cards:
        suits_count[card[1]] += 1
    for suit, count in suits_count.items():
        if count >= 5:
            flush = [card for card in player_cards if card[1] == suit]
            print("Flush Found with cards: ", flush)
            return True
    print("No Flush Found")
    return False

def straight_check(player_cards):
    unique_numbers = sorted(set([card[0] for card in player_cards]))
    for i in range(len(unique_numbers) - 4):
        if unique_numbers[i+4] - unique_numbers[i] == 4:
            straight = [[rank, None] for rank in range(unique_numbers[i], unique_numbers[i]+5)]
            print("Straight Found with cards: ", straight)
            return True
    print("No Straight Found")
    return False
    

def three_of_a_kind_check(player_cards):
    numbers = [x[0] for x in player_cards]
    for number in set(numbers):
        if numbers.count(number) == 3:
            four_of_a_kind = [[number, suit] for suit in suits]
            print("Four of a Kind Found with cards: ", four_of_a_kind)
            return 
    print("No Four of a Kind Found")
    return False

def two_pair(player_cards):
    numbers = [x[0] for x in player_cards]
    pairs = []
    for number in set(numbers):
        if numbers.count(number) == 2:
            pair = [[number, suit] for suit in suits]
            pairs.append(pair)
    if len(pairs) >= 2:
        print("Two Pairs Found with cards: ", pairs[:2])
        return True
    print("No Two Pairs Found")
    print(pairs, len(pairs), numbers)
    return False



def pair(player_cards):
    numbers = [x[0] for x in player_cards]
    pairs = []
    for number in set(numbers):
        if numbers.count(number) == 2:
            pair = [[number, suit] for suit in suits]
            pairs.append(pair)
    if pairs:
        print("Pairs Found with cards: ", pairs)
        return True
    print("No Pairs Found")
    return False


def high_card(player_cards):
    highest_card = max(player_cards, key=lambda x: x[0])
    print("High Card is: ", highest_card)
    return highest_card

def full_house_check(player_cards):
    numbers = [x[0] for x in player_cards]
    three_of_a_kind = None
    pair = None

    for number in set(numbers):
        if numbers.count(number) == 3 and three_of_a_kind is None:
            three_of_a_kind = [[number, suit] for suit in suits]
        elif numbers.count(number) == 2 and pair is None:
            pair = [[number, suit] for suit in suits]

    if three_of_a_kind and pair:
        print("Full House Found with cards: ", three_of_a_kind + pair)
        return True
    print("No Full House Found")
    return False


