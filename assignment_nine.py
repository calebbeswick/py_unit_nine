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

def player_turn(hand, new_deck, blackjack):
    card1 = hand[0]
    card2 = hand[1]
    print("Your cards are:")
    print(card1)
    print(card2)
    total = card1.get_rank() + card2.get_rank()
    keep_going = True
    if blackjack:
        keep_going = False
        total = 21
    while keep_going:
        x = input("Would you like to draw another card? (y/n)")
        if x == "y" and total < 21:
            temp_card = new_deck.deal()
            print("Your new card is ", temp_card)
            total = total + temp_card.get_rank()
            print(total)
        elif total > 21 or x == "n":
            keep_going = False
    print("done")
    return total


def dealers_turn(hand, new_deck, blackjack):
    card1 = hand[0]
    card2 = hand[1]
    total = card1.get_rank() + card2.get_rank()
    keep_going = True
    if blackjack:
        keep_going = False
        total = 21
    while keep_going:
        if total < 17:
            temp_card = new_deck.deal()
            total = total + temp_card.get_rank()
        elif total > 17:
            keep_going = False
    return total

def is_blackjack(hand):
    card1 = hand[0]
    card2 = hand[1]
    rank = card1.get_rank()
    rank2 = card2.get_rank()
    if rank == 1 and rank2 == 10:
        blackjack = True
    elif rank == 10 and rank2 == 1:
        blackjack = True
    else:
        blackjack = False


def who_won(user, dealer):
    if user > 21:
        bust = "yes"
    elif user <= 21:
        bust = "no"
    if dealer > 21:
        dealer_bust = "yes"
    elif dealer <= 21:
        dealer_bust = "no"

    if bust == "yes" and dealer_bust == "no":
        print("You lost")
    elif bust == "no" and dealer_bust == "yes":
        print("You won!")
    elif bust == "yes" and dealer_bust == "yes":
        print("You tied!")
    elif bust == "no" and dealer_bust == "no":
        if user > dealer:
            print("You won!")
        elif dealer > user:
            print("Dealer won! You lost!")
        elif dealer == user:
            print("You tied!")

def main():
    new_deck = create_deck()
    hand = deal_cards(new_deck)
    dealer_hand = deal_cards(new_deck)
    user_blackjack = is_blackjack(hand)
    dealer_blackjack = is_blackjack(dealer_hand)
    player_total = player_turn(hand, new_deck, user_blackjack)
    dealer_total = dealers_turn(dealer_hand, new_deck, dealer_hand)
    who_won(player_total, dealer_total)

main()



