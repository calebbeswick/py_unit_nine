import card
import deck

def create_deck():
    new_deck = deck.Deck()
    new_deck.shuffle()
    return new_deck

def deal_hand(new_deck):
    hand = []
    new_deck.pop[0]
    new_deck.pop[1]
