import random
cardnumbers={0:"A",1:"2",2:"3",3:"4",4:"5",5:"6",6:"7",7:"8",8:"9",9:"10",10:"J",11:"Q",12:"K"}

class Card:
    """ A class to describe cards in a pack """
    def __init__(self, number: int):
        self._card_number = number

    def get_suit(self):
        """ return a string 'C', 'S', 'H', 'D' """
        return"SHDC"[self._card_number // 13]
        pass

    def get_value(self):
        """ return a string 'A'..'10', 'J', 'Q', 'K' """
        return cardnumbers[int(self._card_number) % 13]

    def get_short_name(self) -> str:
        """ return card name eg '10D' '8C' 'AH' """
        return self.get_value(),self.get_suit()
        pass

    def get_long_name(self):
        """ return card name eg 'Ten of Diamonds' """
        return ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"][self._card_number % 13],"of",["Spades","Hearts","Diamonds","Clubs"][self._card_number//13]
        pass


class Deck:
    """ A class to contain a pack of cards with methods for shuffling, adding or removing cards etc. """
    def __init__(self):
        self._card_list = []
        for i in range(52):
            self._card_list.append(Card(i))

    def length(self):
        """ returns the number of cards still in the deck """
        return len(self._card_list)
        pass

    def shuffle_deck(self):
        """ shuffles the cards """
        random.shuffle(self._card_list)

    def take_top_card(self):
        """ removes the top card from the deck and returns it (as a card object) """
        return self._card_list.pop(0)
        pass

    def add_card(self, new_card):
        """ add a card to the bottom of the deck """
        self._card_list.append(new_card)


card = Card(14)
print(card.get_suit())
print(card.get_short_name())
print(card.get_long_name())
deck = Deck()
deck.shuffle_deck()
for _ in range(deck.length()):
    card = deck.take_top_card()
    print(card.get_long_name())