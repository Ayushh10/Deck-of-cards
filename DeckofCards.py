from random import shuffle
class Cards():
	suits = ['Hearts','Diamonds','Spades','Clubs']
	values = ['A','K','Q','J','2','3','4','5','6','7','8','9','10']
	def __init__(self, value, suit):
		if suit not in Cards.suits:
			raise ValueError(f"{suit} is INVALID.")
		if value not in Cards.values:
			raise ValueError(f"{value} is INVALID.")
		self.value = value
		self.suit = suit
	def __repr__(self):
		return f'{self.value} of {self.suit}'

class Deck():
     
     def __init__(self):
           self.cards = [Cards(value, suit) for suit in Cards.suits for value in Cards.values]

     def __repr__(self):
          return f'Deck of {len(self.cards)} cards.'
    	
     def count(self):
          return len(self.cards)

     def _deal(self, num):
          count = self.count()
          if count <= 0:
                raise ValueError('All cards have been dealt.')
          deal = min([count,num])
          cards = self.cards[-deal:]
          self.cards = self.cards[:-deal]
          return cards

     def deal_card(self):
          return self._deal(1)[0]   #[0] returns a singe item instead of a list

     def deal_hand(self, hand_size):
          return self._deal(hand_size)

     def shuffle(self):
          if self.count() < 52:
               raise ValueError("ONLY FULL DECK IS SHUFFLED")
          shuffle(self.cards)

    	

