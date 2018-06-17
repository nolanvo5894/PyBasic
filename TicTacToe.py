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


#def checkOver(move_list)

side = int(input('How big do you want the board to be: ')) #3
move_list = []
create_move_list(side)
createBoard(side, move_list)


for i in range(3):
	move = input('Where do you want to put your sign: ').split()
	row = int(move[0])
	col = int(move[1])
	makeAMove(row, col)
	print(move_list)



