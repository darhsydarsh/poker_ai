#this place will hold the main game logic and essences and call other modules

import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from deck.Deck import Deck
from game.win_conditions.win_conditions import *


player_one_hand = []
player_two_hand = []
card_drawn_hand = []


def run():
    
    game_deck = Deck()

    player_one_hand.extend([game_deck.Pick_card() for i in range(2)])
    player_two_hand.extend([game_deck.Pick_card() for i in range(2)])
    card_drawn_hand.extend([game_deck.Pick_card() for i in range(5)])

    print("Player One Hand: ", [game_deck.card_name(card) + card[1] for card in player_one_hand])
    print("Player Two Hand: ", [game_deck.card_name(card) + card[1] for card in player_two_hand])
    print("Cards on Table: ", [game_deck.card_name(card) + card[1] for card in card_drawn_hand])
    player_cards = player_one_hand + card_drawn_hand
    print(player_cards)



    royale_flush_check(player_cards)

run()