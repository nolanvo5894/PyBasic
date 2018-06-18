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