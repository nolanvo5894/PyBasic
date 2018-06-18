def create_move_list(side):
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
	move_list[row][col] = 'x'
	createBoard(side, move_list)


def checkOverRow(move_list):
	for row in range(side):
		checkRow = []
		for col in range(side):
			checkRow.append(move_list[row][col])
		if 'xxx' == ''.join(checkRow):
			print('Winner is here!')

def checkOverCol(move_list):
	for col in range(side):
		checkCol = []
		for row in range(side):
			checkCol.append(move_list[row][col])
		if 'xxx' == ''.join(checkCol):
			print('Winner is here!')

def checkOverDiagonalRight(move_list):
	for sub in range((1 - side), side):
		
		diagonal = []
		for row in range(side):
			for col in range(side):
				if (row - col) == sub:
					diagonal.append(move_list[row][col])
		print(diagonal)
		if 'xxx' in ''.join(diagonal):
			print('Winner is here!')
			break
			
def checkOverDiagonalLeft(move_list):
	for tot in range(side - 1, (2*side-2)):
		
		diagonal = []
		for row in range(side):
			for col in range(side):
				if (row + col) == tot:
					diagonal.append(move_list[row][col])
		print(diagonal)
		if 'xxx' in ''.join(diagonal):
			print('Winner is here!')
			break

def checkOver(move_list):
	checkOverRow(move_list)
	checkOverCol(move_list)
	checkOverDiagonalRight(move_list)
	checkOverDiagonalLeft(move_list)






side = int(input('How big do you want the board to be: ')) 
move_list = []
create_move_list(side)
createBoard(side, move_list)


for i in range(side):
	move = input('Where do you want to put your sign: ').split()
	row = int(move[0])
	col = int(move[1])
	makeAMove(row, col)
	print(move_list)
	checkOver(move_list)
	


