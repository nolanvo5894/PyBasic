def createMoveList(side, move_list):
	for row in range(side):
		move_list.append([])
		for col in range(side):
			move_list[row].append(' ')

def createBoard(side, move_list):
	for row in range(side):
		for col in range(side):
			print(move_list[row][col]+'|', end = '')
		print('\n')

def makeAMove(row, col, sign, side, move_list):
	move_list[row][col] = sign
	createBoard(side, move_list)

def signSelection(sign_list, num_players):
	for i in range (1, num_players + 1):
		sign_list.append(input('What is the sign for player {}: '.format(i)))