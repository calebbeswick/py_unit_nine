import card
import deck



def create_deck():
    newdeck = deck.Deck()
    newdeck.shuffle()
    return newdeck

def deal_cards(new_deck):
    hand = []
    card1 = new_deck.deal()
    card2 = new_deck.deal()
    hand.append(card1)
    hand.append(card2)
    return hand

def player_turn(hand, newdeck):
    card1 = hand[0]
    card2 = hand[1]
    print(card1)
    print(card2)
    total = card1.get_rank() + card2.get_rank()
    print(total)






# def dealers_turn():
#     pass
#
# def is_blackjack(hand):
#     card1 = hand[0]
#     card2 = hand[1]
#     rank = card1.card.get_rank()
#     print(rank)

# def who_won():



new_deck = create_deck()
hand = deal_cards(new_deck)
player_turn(hand, new_deck)



