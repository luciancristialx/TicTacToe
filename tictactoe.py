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
        move = int(input("Please select a position to enter the X between 1 - 9: "))
        try:

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

def computerMove():
    possibleMoves = [x for x, letter in enumerate(boardList) if letter == ' ' and x!=0]
    move = 0

    for let in ['O','X']:
        for i in possibleMoves:
            boardCopy = boardList[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornerValues = []
    for i in possibleMoves:
        if i in [1 ,3, 7, 9]:
            cornerValues.append(i)

    if len(cornerValues) > 0:
        move = selectRandom(cornerValues)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesValues = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesValues.append(i)

    if len(edgesValues) > 0:
        move = selectRandom(edgesValues)
        return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def main():
    print("Welcome to TicTacToe!")
    printBoard(boardList)

    while not(isBoardFull(boardList)):
        if not(isWinner(boardList,'O')):
            playerMove()
            printBoard(boardList)
        else:
            print("Sorry you lost the game!")
            break

        if not(isWinner(boardList,'X')):
            move = computerMove()
            if move == 0:
                print("Tie game!")
            else:
                insertLetter('O',move)
                print("Computer place an O on position: ", move)
                printBoard(boardList)
        else:
            print("You win!")
            break

    if isBoardFull(boardList):
        print("Tie game!")

while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        boardList = [' ' for x in range(10)]
        print('------------------------')
        main()
    else:
        break