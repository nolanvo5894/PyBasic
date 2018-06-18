def checkOverRow(move_list, sign, side, streak):
	for row in range(side):
		checkRow = []
		for col in range(side):
			checkRow.append(move_list[row][col])
		if sign*streak in ''.join(checkRow):
			return True
	return False
		

def checkOverCol(move_list, sign, side, streak):
	for col in range(side):
		checkCol = []
		for row in range(side):
			checkCol.append(move_list[row][col])
		if sign*streak in ''.join(checkCol):
			return True
	return False

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