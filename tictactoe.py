boardList = [' ' for x in range(10)]
def insertLetter(letter,position):
    boardList[position] = letter

def spaceIsFree(position):
    return boardList[position] == ''

def printBoard(board):
    print('----------------')
    print('|    |    |    |')
    print('| ' + board[1] + '  | ' + board[2] + '  | ' + board[3] + '  |')
    print('|    |    |    |')
    print('----------------')
    print('|    |    |    |')
    print('| ' + board[4] + '  | ' + board[5] + '  | ' + board[6] + '  |')
    print('|    |    |    |')
    print('----------------')
    print('|    |    |    |')
    print('| ' + board[7] + '  | ' + board[8] + '  | ' + board[9] + '  |')
    print('|    |    |    |')
    print('----------------')

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def isWinner(board,letter):
    return (board[1] == letter and board[2] == letter and board[3] == letter) or \
        (board[4] == letter and board[5] == letter and board[6] == letter) or \
        (board[7] == letter and board[8] == letter and board[9] == letter) or \
        (board[1] == letter and board[4] == letter and board[7] == letter) or \
        (board[2] == letter and board[5] == letter and board[8] == letter) or \
        (board[3] == letter and board[6] == letter and board[9] == letter) or \
        (board[1] == letter and board[5] == letter and board[9] == letter) or \
        (board[3] == letter and board[5] == letter and board[7] == letter)

def playerMove():
    runCode = True
    while runCode:
        move = input("Please a position to enter the X between 1 - 9: ")
        try:
            move = int(move)
            if 0 < move < 10:
                if spaceIsFree(move):
                    runCode = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this position is occupied.')
            else:
                print('Please enter a valid position (in between 1 - 9).')
        except:
            print('Please enter a valid input (must always be a number).')
