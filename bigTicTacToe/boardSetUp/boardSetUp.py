#functions to create the board and print out the board, let user select the sign they want to use in the game,
#let users make a move, and then store the move in a list.

#function to let user select a sign for the game, for example 'x' or 'o' or 's'
def signSelection(sign_list, num_players):
	for i in range (1, num_players + 1):
		sign_list.append(input('What is the sign for player {}: '.format(i)))

#function to create a board of size sidexside and a list of all cells with row index and column index (a list of list actually)
def createBoard(side, move_list):
	for row in range(side):
		for col in range(side):
			print(move_list[row][col]+'|', end = '')
		print('\n')

#function to create a list of list to store moves made by players.
def createMoveList(side, move_list):
	for row in range(side):
		move_list.append([])
		for col in range(side):
			move_list[row].append(' ')

#function to let user make a move by putting their in a selected cell.
def makeAMove(row, col, sign, side, move_list):
	move_list[row][col] = sign
	createBoard(side, move_list)
