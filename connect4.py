def setUpField(width, placeHolder):
	f = []
	for col in range(width):
		row = []
		for r in range(width):
			row.append(placeHolder)
		f.append(row)
	return f

def printField(noOfTurns):
	print("Turn Number " + str(noOfTurns))
	print()
	width = len(field)
	for i in range(width):
		if i == 6:
			print(" " + str(width) + " ")
		else:
			print(" " + str(i + 1) + " ", end="")

	for row in range(width - 1, -1, -1):
		for col in range(0, width):
			if col == width - 1:
				print(field[row][col])
			else:
				print(field[row][col], end="")
	print()

def chooseColumn(board, playerNo):
	turnEnd = False
	while turnEnd == False:
		playerColor = "X"
		wid = len(board)
		column = int(input("Player " + str(playerNo) + "- Choose a row: ")) - 1
		print()
			
		if column >= 0 and column <= wid - 1:
			if board[wid - 1][column] == placeHolder:
				for i in range(0, wid):
					if(board[i][column] == placeHolder):
						if playerNo == 2:
							playerColor = "0"
						board[i][column] = " " + str(playerColor) + " "
						turnEnd = True
						break
			else:
				print("This is row cannot be selected as it is full. Please choose again.")
		else: 
			print("Please enter a valid row.")


def checkWinner(board):
	width = len(board)
	winnerFound = False
	for row in range(0, width):
		for col in range(0, width - 3):
			if board[row][col] != placeHolder:
				if board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3]:
					winnerFound = True
					break

	if winnerFound == False:
		for row in range(3, width):
			for col in range(0, width):
				if board[row][col] != placeHolder:
					if board[row][col] == board[row - 1][col] == board[row - 2][col] == board[row - 3][col]:
						winnerFound = True
						break

	if winnerFound == False:
		for row in range(width - 3):
			for col in range(width - 3):
				if board[row][col] != placeHolder:
					if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]:
						winnerFound = True 
						break

	if winnerFound == False:
		for row in range(width - 3):
			for col in range(width - 3):
				if board[row][col] != placeHolder:
					if board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3]:
						winnerFound = True
						break

	return winnerFound

def gameLoop(board, playerNo, turnEnd):
	isWin = False
	turnNumber = 1
	while(turnNumber <= 49 and isWin == False):
		if playerNo == 1:
			chooseColumn(board, playerNo)
			isWin = checkWinner(board)

			if isWin == False: playerNo = 2
		else: 
			chooseColumn(board, playerNo)
			isWin = checkWinner(board)
			if isWin == False: playerNo = 1

		printField(turnNumber)
		turnNumber += 1

	print("Game Over!")

	if isWin:
		print("Player " + str(playerNo) + " is the Winner")
	else:
		print("Draw!")



field = []
player = 1
width = 7
endTurn = False
placeHolder = " * "
field = setUpField(width, placeHolder)
gameLoop(field, player, endTurn)






	