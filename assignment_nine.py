import card
import deck

def create_deck():
    newdeck = deck.Deck()
    newdeck.shuffle()
    return newdeck

def deal_cards(new_deck):
    hand = []
    card1 = new_deck.pop()
    card2 = new_deck.pop()
    print(card1)
    print(card2)
    return hand

# def player_turn(player_hand, newdeck ):
#     new_deck = create_deck()
#     deal_cards(new_deck)
#
# def dealers_turn():
#     pass

def is_blackjack(hand):
    card1 = hand.pop(0)
    card2 = hand.pop(1)
    rank = card1.card.get_rank()
    print(rank)

# def who_won():



new_deck = create_deck()
card1 = deal_cards(new_deck)

