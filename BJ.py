import random

class Deck:
	cardList = list(range(1,11))*4
	for i in range(4):
		cardList.append('A')


	def __init__ (self):
		self.cardNumber = len(self.cardList)

	def throwOut(self):
		cardThrow = random.choice(self.cardList)
		print(f'New card is {cardThrow}')
		self.cardNumber -= 1
		self.cardList.remove(cardThrow)
		return cardThrow

	def showCardList(self):
	 	print (self.cardList)

class Dealer():
	def __init__ (self):
		self.score = 0
		self.hand = []
	

	def takeIn(self, card): 
		self.hand.append(card)
		if card == 'A':
			self.score += 11
		else:	
			self.score += card

	def checkBurst(self):
		return self.score > 21

	def checkBJ(self):
		return self.score == 21

	
class Player():
	def __init__ (self, fund):
		self.score = 0
		self.hand = []
		self.fund = fund

	def takeIn(self, card): 
		self.hand.append(card)
		if card == 'A':
			if (self.score + 11) <= 21:
				self.score += 11
			else:
				self.score += 1
		else:
			self.score += card 

	def checkBurst(self):
		if self.score > 21 and 'A' in self.hand:
			self.score -= 10
			self.hand.remove('A')
			return False
		else:
			return self.score > 21


	def checkBJ(self):
		return self.score == 21

	
def game():

	if myPlayer.checkBJ():
		print('You won with a BJ')
		myPlayer.fund += bet
		return 
	else:


	# Ask the player whether to hit or stand


		playerChoice = input('Press h for hit and s for stand: ')


		# If player choose 'Hit', deal cards until:
			# Player chooses 'Stand'.
			# Player gets BJ.
			# Player bursts.

		if playerChoice == 'h':
			while playerChoice != 's' and myPlayer.checkBJ() != True and myPlayer.checkBurst() != True:
				myPlayer.takeIn(myDeck.throwOut())
				if myPlayer.checkBJ():
					print('You won with a BJ')
					myPlayer.fund += bet
					return 
				if myPlayer.checkBurst():
					print('You burst. Try again')
					myPlayer.fund -= bet
					return 
				print(f'Your current score is {myPlayer.score}')
				playerChoice = input('Press H for Hit and S for Stand: ')
				if playerChoice == 's':
					dealerTurn()

		else:
			dealerTurn()



def dealerTurn():
	print(myDealer.hand)
	while myDealer.score < 17:
		myDealer.takeIn(myDeck.throwOut())
	print(f"Dealer's score is {myDealer.score}")
	if myDealer.checkBJ():
		print('Dealer won with BJ')
		myPlayer.fund -= bet
	elif myDealer.checkBurst():
		print('Dealer burst! Player won!')
		myPlayer.fund += bet
	else:
		if myPlayer.score == myDealer.score:
			print('Tie!')
		elif myPlayer.score > myDealer.score:
			print('Player won!')
			myPlayer.fund += bet
		else:
			print('Dealer won!')
			myPlayer.fund -= bet



if __name__ == '__main__':

	# myDeck = Deck()
	# print(myDeck.cardList)

	play = 'y'
	fund = float(input('How much money do you have? '))
	myPlayer = Player(fund)


	while play == 'y':
		myDeck = Deck()
		myPlayer.score = 0
		bet = float(input('How much money do you want to bet? '))
		myDealer = Dealer()

		# Start the game by dealing cards to the dealer and the player

		myPlayer.takeIn(myDeck.throwOut())
		myPlayer.takeIn(myDeck.throwOut())
		print(f'Your score is {myPlayer.score}')

		myDealer.takeIn(myDeck.throwOut())
		myDealer.takeIn(myDeck.throwOut())

		game()
		print(f'You have {myPlayer.fund} in your fund')
		play = input('Do you want to keep playing? Press y for yes and n for no: ')



	








		


