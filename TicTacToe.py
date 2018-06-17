def create_move_list(side):
	for row_index in range(side):
		for col_index in range(side):
			move_list[str(row_index) + str(col_index)] = ' '

def createBoard(side, move_list):
	for row_index in range(side):
		for col_index in range(side):
			print(move_list[str(row_index) + str(col_index)]+'|', end = '')
		print('\n')

def makeAMove(move):
	move_list[move] = 'x'
	createBoard(side, move_list)

#def checkOver(move_list)

side = int(input('How big do you want the board to be: '))
move_list = {}
create_move_list(side)
createBoard(side, move_list)


for i in range(3):
	move = input('Where do you want to put your sign: ')
	makeAMove(move)
	print(move_list)



