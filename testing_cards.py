import card
import deck

# new_card = card.Card(9, "Hearts")
# print(new_card.suit)
#
# other_card = card.Card(5, "Clubs")
# print(other_card.rank)

new_deck = deck.Deck()
print(new_deck.cards[-1].rank + " of " + new_deck.cards[-1].suit)
