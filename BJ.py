# this is the program for a simplified game of Black Jack between 1 Dealer and 1 Player.
# both the player and the dealer tries to increase their points up to but not higher than 21 by drawing cards from the Deck.
# number cards carry the same amount of points as their numbers. All face cards carry 10 points and are treated the same. The 'A' card can carry either 1 or 11 points, whichever is better for its drawer.
# the Deck's original card list is made up of 52 numbers ranging from 1 to 10, each appears 4 times, and 4 'A's.
# whoever gets higher than 21 points bursts and lose the game.
# the one who get exactly 21 points first win with a Black Jack.
# the one who burst first loses.
# if no one bursts, the one with the higher number of points win.
# the player can choose when to stop taking in card in his/her turn.
# the dealer have to keep taking in card until its point is >= 17.

import random

# create a Deck class with:
	# attribute 'cardList' that keeps track of the list of cards in the Deck.
	# attribute 'cardNumber' that keeps track of the number of cards in the Deck.
	# method throwOut to deal the card to either the Dealer or the Player.
	# method showCardList that prints out the list of all cards in the Deck.
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

# create a Dealer class with:
	# attribute 'score' which keeps track of the dealer's number of points.
	# attribute 'hand' which keeps track of the list of cards on the dealer's hand.
	# method takeIn for taking in a card from the Deck.
	# method checkBurst to see if the Dealer's point > 21.
	# method checkBJ to see if the Dealer's point == 21.

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

# create a Player class with:
	# attribute 'score' which keeps track of the dealer's number of points.
	# attribute 'hand' which keeps track of the list of cards on the player's hand.
	# attribute 'fund' which stores the amount of money the player has.
	# method takeIn for taking in a card from the Deck.
	# method checkBurst to see if the Dealer's point > 21.
	# method checkBJ to see if the Dealer's point == 21.

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


# the function for the main game.
def game():

	if myPlayer.checkBJ():
		print('You won with a BJ')
		myPlayer.fund += bet
		return
	else:

		# Ask the player whether to hit or stand


		playerChoice = input('Press h for hit and s for stand: ')


		# If player choose 'Hit', deal cards until:
			# Player chooses 'Stand'
			# or Player gets BJ.
			# or Player bursts.

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


		# The dealer's turn comes after the player's turn.
		# The dealer first must take in cards until its score >= 17
		# Then:
			# If it gets a BJ, player loses.
			# Else if it gets a burst, player wins.
			# Else the dealer's score and the player's score are compared, the one with the higher score wins. Equal score means a tie.

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

	# player is asked if he/she wants to start a game and how much money he/she has
	play = 'y'
	fund = float(input('How much money do you have? '))
	myPlayer = Player(fund)

	# if player agrees to start a game, a Deck is created and the player is asked for the amount of money he/she wants to bet on that game.
	# the game loop starts
	while play == 'y':
		myDeck = Deck()
		myPlayer.score = 0
		bet = float(input('How much money do you want to bet? '))
		myDealer = Dealer()

		# Start by dealing cards to the dealer and the player
		# Player takes in 2 cards
		myPlayer.takeIn(myDeck.throwOut())
		myPlayer.takeIn(myDeck.throwOut())
		print(f'Your score is {myPlayer.score}')
		# # Dealer takes in 2 cards
		myDealer.takeIn(myDeck.throwOut())
		myDealer.takeIn(myDeck.throwOut())
		# The main game starts.
		game()
		# Let the player knows his/her fund after the game based on the outcome of the game.
		print(f'You have {myPlayer.fund} in your fund')
		# Ask player if he/she wants to play another game.
		play = input('Do you want to keep playing? Press y for yes and n for no: ')
