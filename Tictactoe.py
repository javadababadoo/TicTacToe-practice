from random import randint
from IPython.display import clear_output
from boto.sdb.db.sequence import fib
from statsmodels.sandbox import gam

playerList = []
board = [" "," "," "," "," "," "," "," "," "]
gameOver = False


def enterNames():
    global playerList
    playerList.append(input("Please enter player's one name (X)"))
    playerList.append(input("Please enter player's two name (0)"))

def chooseTurn():
    return randint(0,1)


def askForNewPosition(piece):
    success = False
    while not success:
        try:
            board_position = int(input("Please enter a number for the board position choice: "))
            success = addNewPosition(board_position, piece)
        except ValueError:
            print("Sorry, please enter a valid number")


def addNewPosition(board_position, piece):
    global board
    if 0 <= board_position <= len(board) and board[board_position].strip() == "":
            print("Posicion vacia %s" %board[board_position])
            board[board_position] = piece
            return True
    else:
        print("The position is busy or invalid")
        return False


def printBoard(board):
    clear_output()
    num = -1
    for column in board:
        num+=1
        if num % 3 == 0 and num != 0:
            print("| ")
            print("| %s" %column, end="")
        else:
            print("| %s" %column, end="")
    print("|")


def checkWinner(piece):
    return (board[0] == board[1] == board[2] == piece or
            board[3] == board[4] == board[5] == piece or
            board[6] == board[7] == board[8] == piece or
            board[0] == board[4] == board[8] == piece or
            board[0] == board[3] == board[6] == piece or
            board[1] == board[4] == board[7] == piece or
            board[2] == board[5] == board[8] == piece or
            board[2] == board[4] == board[6] == piece)

def checkFullBoard():
    return not (" " in board[1:])


enterNames()
firstPlayer = chooseTurn()

while not gameOver:
    print("")
    print("Player's %s's turn." %(firstPlayer+1))
    piece = "X" if firstPlayer == 0 else "0"
    askForNewPosition(piece)
    printBoard(board)
    gameOver = checkWinner(piece)
    if gameOver:
        print("Piece: (%s), The player %s has won." % (piece, playerList[firstPlayer]))
    else:
        gameOver = checkFullBoard()
        if gameOver:
            print("The game is a draw")
        else:
            firstPlayer = 1 if firstPlayer == 0 else 0