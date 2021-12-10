import card
import deck

new_card = card.Card("9", "Hearts")
print(new_card.suit)

other_card = card.Card("9", "Clubs")
print(other_card)
if new_card > other_card:
    print("First card is bigger")
else:
    print("Second card is bigger")

new_deck = deck.Deck()
new_deck.shuffle()
print(new_deck.cards[-1].rank + " of " + new_deck.cards[-1].suit)
