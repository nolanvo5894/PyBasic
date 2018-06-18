


from checkOver import checkOver
from boardSetUp.boardSetUp import createMoveList, createBoard, makeAMove
	




#MAIN PROGRAM

side = int(input('How big do you want the board to be ?: '))
num_player = int(input('How many players are in the games ?: '))
streak = int(input('How long should the winning streak be ?: ')) 
sign_list = []
for i in range (1, num_player + 1):
	sign_list.append(input('What is the sign for player {}: '.format(i)))

move_list = []
createMoveList(side, move_list)
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
			makeAMove(row, col, sign, side, move_list)
			if checkOver(move_list, sign, side, streak):
				print('Winner is player {} !'.format(i))
				check = True
				break
	turn += 1




	


