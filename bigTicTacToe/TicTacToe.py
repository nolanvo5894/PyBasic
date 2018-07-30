from checkOver import checkOver
from boardSetUp.boardSetUp import createMoveList, createBoard, makeAMove, signSelection





#MAIN PROGRAM
if __name__ == '__main__':
	side = int(input('How big do you want the board to be ?: '))
	num_players = int(input('How many players are in the games ?: '))
	streak = int(input('How long should the winning streak be ?: '))
	sign_list = []
	signSelection(sign_list, num_players)
	move_list = []
	createMoveList(side, move_list)
	createBoard(side, move_list)


	turn = 0
	check = False

	while check == False:
		for i in range (1, num_players + 1):
			if turn%num_players == (i-1):
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
