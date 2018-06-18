def createMoveList(side):
	for row in range(side):
		move_list.append([])
		for col in range(side):
			move_list[row].append(' ')

def createBoard(side, move_list):
	for row in range(side):
		for col in range(side):
		
			print(move_list[row][col]+'|', end = '')
		print('\n')

def makeAMove(row, col):
	move_list[row][col] = sign
	createBoard(side, move_list)


def checkOverRow(move_list, sign):
	for row in range(side):
		checkRow = []
		for col in range(side):
			checkRow.append(move_list[row][col])
		if sign*3 in ''.join(checkRow):
			return True
	return False
		

def checkOverCol(move_list, sign):
	for col in range(side):
		checkCol = []
		for row in range(side):
			checkCol.append(move_list[row][col])
		print(''.join(checkCol))
		if sign*3 in ''.join(checkCol):
			return True
	return False

def checkOverDiagonalRight(move_list, sign):
	for sub in range((1 - side), side):
		diagonal = []
		for row in range(side):
			for col in range(side):
				if (row - col) == sub:
					diagonal.append(move_list[row][col])
		#print(diagonal)
		if sign*3 in ''.join(diagonal):
			return True
	return False

def checkOverDiagonalLeft(move_list, sign):
	for tot in range(side - 1, (2*side-2)):
		diagonal = []
		for row in range(side):
			for col in range(side):
				if (row + col) == tot:
					diagonal.append(move_list[row][col])
		#print(diagonal)
		if sign*3 in ''.join(diagonal):
			return True
	return False

def checkOver(move_list,sign):
	
	if checkOverRow(move_list, sign):
		return True
	elif checkOverCol(move_list, sign):
		return True
	elif checkOverDiagonalRight(move_list, sign):
		return True
	elif checkOverDiagonalLeft(move_list, sign):
		return True
	else:
		return False

	






side = int(input('How big do you want the board to be: '))
num_player = int(input('How many players are in the games: ')) 
sign_list = []
for i in range (1, num_player + 1):
	sign_list.append(input('What is the sign for player {}: '.format(i)))
move_list = []
createMoveList(side)
createBoard(side, move_list)
turn = 0
check = False

while check == False:
	for i in range (1, num_player + 1):
		if turn%num_player == (i-1):
			sign = sign_list[i-1]
			move = input('Where do you want to put your sign, player {}: '.format(i)).split()
			row = int(move[0])
			col = int(move[1])
			makeAMove(row, col)
			#print(move_list)
			if checkOver(move_list, sign):
				print('Winner is player {} !'.format(i))
				check = True
				break


	turn += 1




	


