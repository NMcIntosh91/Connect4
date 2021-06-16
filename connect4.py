#from termcolor import colored

def setUpField(width, placeHolder):
	f = []
	for col in range(width):
		row = []
		for r in range(width):
			row.append(placeHolder)
		f.append(row)
	return f

#Displays game field
def printField(noOfTurns):
	print("Turn Number " + str(noOfTurns) + "\n")
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

#Allows player to choose a column - ERROR HANDLING HOMEWORK
def chooseColumn(board, playerNo):
	turnEnd = False
	while turnEnd == False:
		#playerColor = colored("X", 'red')
		playerColor = "X"
		wid = len(board)
		
		try:
			column = int(input("Player " + str(playerNo) + "- Choose a row: " + "\n")) - 1

			if board[wid - 1][column] == placeHolder:
					for i in range(0, wid):
						if(board[i][column] == placeHolder):
							if playerNo == 2:
								#playerColor = colored("0", 'yellow')
								playerColor = "0"
							board[i][column] = " " + str(playerColor) + " "
							turnEnd = True
							break
			else:
				print("Player " + str(playerNo) + "- This columnn is full. Please choose another column.")
			
		except ValueError:
			print("Player " + str(playerNo) + "- You have entered an incorrect value.")
		except IndexError:
			print("Player " + str(playerNo) + "- You have selected outside of the suggested range")
		except Exception as e:
			print(str(e))
		finally:
			print("Player " + str(playerNo) + "- Please enter a valid input")

#Checks if a plyaer has made 4 in a row
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

#Runs the game
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

field = [] #The game field
width = 7 #The width of the game field
player = 1 #Determines which Player's turn it is
endTurn = False 
placeHolder = " * "
field = setUpField(width, placeHolder)
gameLoop(field, player, endTurn)






	