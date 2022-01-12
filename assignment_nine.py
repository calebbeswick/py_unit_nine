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
    card1 = str(card1)
    card2 = str(card2)
    hand.append(card1)
    hand.append(card2)
    print(type(hand))
    return hand

def player_turn(hand, newdeck ):
    card1 = hand[0]
    card2 = hand[1]
    card1 = card.Card.get_rank("A")
    hand[0].Card.get_rank(9)
    print(ranked)



def dealers_turn():
    pass

def is_blackjack(hand):
    card1 = hand[0]
    card2 = hand[1]
    rank = card1.card.get_rank()
    print(rank)

# def who_won():



new_deck = create_deck()
hand = deal_cards(new_deck)
# player_turn(hand, new_deck)
is_blackjack(hand)


