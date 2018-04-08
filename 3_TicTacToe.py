theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):													### printing the board
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkInput():  # checking correct input is given
	x = input()
	if theBoard[x]=='X' or theBoard[x]=='Y': 	### Input should not be already selected position
		print('This position is already filled. Choose another position')
	elif x in theBoard.keys():					### Input should be within given keys
		return x
	else:
		print('Enter correct place')
		for i in theBoard.keys():
			print(i)

def checkResult(player, board): 				### checking all possible combination
	if (board['top-L'] == player):
		if (board['top-M'] == player) and (board['top-R'] == player):
			return True
		elif (board['mid-M'] == player) and (board['low-R'] == player):
			return True
		elif (board['mid-L'] == player) and (board['low-L']==player):
			return True
	elif (board['top-M'] == player) and (board['mid-M'] == player) and (board['low-M'] == player):
		return True
	elif (board['top-R'] == player):
		if (board['mid-R'] == player) and (board['low-R'] == player):
			return True
		elif (board['mid-M'] == player) and (board['low-L'] == player):
			return True
	elif (board['mid-L'] == player) and (board['mid-M'] == player) and (board['mid-R'] == player):
		return True
	elif (board['low-L'] == player):
		if (board['low-M'] == player) and (board['low-R'] == player):
			return True
		
turn = 'X'

for i in range(9):
	move = None
	printBoard(theBoard)
	print('Turn for '+ turn + '. Move on which space?')
	while move==None:									### keep on asking for input untill correct input is given
		move = checkInput()
	
	theBoard[move] = turn
	if turn == 'X':										### toggling the player
		turn = 'Y'
	else:
		turn = 'X'
		
	if i > 3:											### printing the result
		if checkResult('X', theBoard)==True:
			print('X is winner')
			break
		elif checkResult('Y')==True:
			print('X is winner')
			break
printBoard(theBoard)