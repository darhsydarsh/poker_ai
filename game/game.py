#this place will hold the main game logic and essences and call other modules

import game.deck as deck


player_one_hand = []
player_two_hand = []
card_drawn_hand = []


def run():
    
    given_deck = deck.deck.copy()
       

    player_one_hand.extend([deck.card_pick(given_deck) for i in range(2)])
    player_two_hand.extend([deck.card_pick(given_deck) for i in range(2)])
    card_drawn_hand.extend([deck.card_pick(given_deck) for i in range(5)])

    print("Player One Hand: ", [deck.card_name(card) + card[1] for card in player_one_hand])
    print("Player Two Hand: ", [deck.card_name(card) + card[1] for card in player_two_hand])
    print("Cards on Table: ", [deck.card_name(card) + card[1] for card in card_drawn_hand])

    