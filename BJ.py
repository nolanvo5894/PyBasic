import random



class Deck:
	cardList = list(range(1,10))*4
	def __init__ (self, cardNumber):
		self.cardNumber = cardNumber

	def throwOut(self):
		cardThrow = random.choice(self.cardList)
		print(f'New card is {cardThrow}')
		self.cardNumber -= 1
		self.cardList.remove(cardThrow)
		return cardThrow

	def showCardList(self):
	 	print (self.cardList)

myDeck = Deck(52)



# need to add the secret card later
class Dealer():
	def __init__ (self):
		self.score = 0
		self.hand = []
	#card = myDeck.throwOut()
	#need to take in twice at the start of the game

	def takeIn(self, card): 
		self.hand.append(card)
		self.score += card 

	def checkBurst(self):
		return self.score > 21

	def checkBJ(self):
		return self.score == 21

	def checkScore(self):
		return self.score



myDealer = Dealer()
myDealer.takeIn(myDeck.throwOut())
myDeck.showCardList()

print(myDealer.hand)
print(myDealer.checkBurst())
print(myDealer.checkBJ())
print(myDealer.checkScore())



		


