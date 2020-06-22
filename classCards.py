class Cards:
	def __init__(self, value, suit):
		if suit not in Cards.suit:
			raise ValueError(f"{suit} doen't exist.")
		if value not in Cards.value:
			raise ValueError(f'{value} is INVALID.')
		self.suit = suit
		self.value = value
	def __repr__(self):
		return f'{self.value} of {self.suit}'