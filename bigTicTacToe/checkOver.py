# this module helps to check if a game of TicTacToe is over

# checking if the winning streak is achieved in a row by printing out all rows as strings and see if the streak is in any row.
def checkOverRow(move_list, sign, side, streak):
	for row in range(side):
		checkRow = []
		for col in range(side):
			checkRow.append(move_list[row][col])
		if sign*streak in ''.join(checkRow):
			return True
	return False

# checking if the winning streak is achieved in a row by printing out all columns as strings and see if the streak is in any column.
def checkOverCol(move_list, sign, side, streak):
	for col in range(side):
		checkCol = []
		for row in range(side):
			checkCol.append(move_list[row][col])
		if sign*streak in ''.join(checkCol):
			return True
	return False

# checking if the winning streak is achieved in any negative slope diagonal by printing out all of these diagonal as strings and see if the streak is in any of them.
# to create a list of diagonals, the function takes advantage of the fact that the (row index - column index) is the same for all cells in a diagonal.
def checkOverDiagonalRight(move_list, sign, side, streak):
	for sub in range((1 - side), side):
		diagonal = []
		for row in range(side):
			for col in range(side):
				if (row - col) == sub:
					diagonal.append(move_list[row][col])
		if sign*streak in ''.join(diagonal):
			return True
	return False

# checking if the winning streak is achieved in any positive slope diagonal by printing out all of these diagonal as strings and see if the streak is in any of them.
# to create a list of diagonals, the function takes advantage of the fact that the (row index + column index) is the same for all cells in a diagonal.
def checkOverDiagonalLeft(move_list, sign, side, streak):
	for tot in range(side - 1, (2*side-2)):
		diagonal = []
		for row in range(side):
			for col in range(side):
				if (row + col) == tot:
					diagonal.append(move_list[row][col])
		if sign*streak in ''.join(diagonal):
			return True
	return False

# the big checkOver function that combine the 4 smaller subfunctions above
# this function returns True if any subfunctions finds the winning streak, otherwise it returns False to the game loop so that the game continues.
def checkOver(move_list,sign, side, streak):

	if checkOverRow(move_list, sign, side, streak):
		return True
	elif checkOverCol(move_list, sign, side, streak):
		return True
	elif checkOverDiagonalRight(move_list, sign, side, streak):
		return True
	elif checkOverDiagonalLeft(move_list, sign, side, streak):
		return True
	else:
		return False
