import random

gameboard = [['-','-','-'],['-','-','-'],['-','-','-']]
playerOptions = {'1':['0','0'], '2':['1','0'], '3':['2','0'], '4':['0','1'], '5':['1','1'], '6':['2','1'], '7':['0','2'], '8':['1','2'], '9':['2','2']}

def playerMove(gameboard):
    while True:
        for row in gameboard:
            print(' '.join(row))
        print('Where do you want to move?')
        answer = input('1-9: ')
        while answer not in playerOptions:
            print('Invalid answer')
            answer = input('1-9: ')
        x, y = int(playerOptions[answer][0]), int(playerOptions[answer][1])
        if gameboard[y][x] == '-':
            gameboard[y][x] = 'X'
            break
        else:
            print('you can\'t move there')
            continue

def computerMove(gameboard):
    copy = gameboard
    for i in range(len(copy)):
        for j in range(len(copy[i])):
            if copy[j][i] == 'X' or copy[j][i] == 'O':
                continue
            else:
                copy[j][i] = 'O'
                if checkIfOver(copy, 'O') == 'O':
                    return str(j) + ',' + str(i)
                else:
                    copy[j][i] = '-'
    copy = gameboard
    for i in range(len(copy)):
        for j in range(len(copy[i])):
            if copy[j][i] == 'X' or copy[j][i] == 'O':
                continue
            else:
                copy[j][i] = 'X'
                if checkIfOver(copy, 'X') == 'X':
                    return str(j) + ',' + str(i)
                else:
                    copy[j][i] = '-'
    if gameboard[1][1] == '-':
        return '1,1'
    while True:
        rand = random.randint(1,4)
        if gameboard[0][0] != '-' and gameboard[2][2] != '-' and gameboard[0][2] != '-' and gameboard[2][0] != '-':
            break
        if rand == 1:
            if gameboard[0][0] == '-':
                return '0,0'
            else:
                continue
        elif rand == 2:
            if gameboard[2][2] == '-':
                return '2,2'
            else:
                continue
        elif rand == 3:
            if gameboard[0][2] == '-':
                return '0,2'
            else:
                continue
        elif rand == 4:
            if gameboard[2][0] == '-':
                return '2,0'
            else:
                continue
    while True:
        rand = random.randint(1,4)
        if rand == 1:
            if gameboard[0][1] == '-':
                return '0,1'
            else:
                continue
        elif rand == 2:
            if gameboard[2][1] == '-':
                return '2,1'
            else:
                continue
        elif rand == 3:
            if gameboard[1][2] == '-':
                return '1,2'
            else:
                continue
        elif rand == 4:
            if gameboard[1][0] == '-':
                return '1,0'
            else:
                continue

def checkIfOver(board, letter):
    if board[0][0] == letter and board[0][1] == letter and board[0][2] == letter:
        return board[0][0]
    elif board[1][0] == letter and board[1][1] == letter and board[1][2] == letter:
        return board[1][0]
    elif board[2][0] == letter and board[2][1] == letter and board[2][2] == letter:
        return board[2][0]
    elif board[0][0] == letter and board[1][0] == letter and board[2][0] == letter:
        return board[0][0]
    elif board[0][1] == letter and board[1][1] == letter and board[2][1] == letter:
        return board[0][1]
    elif board[0][2] == letter and board[1][2] == letter and board[2][2] == letter:
        return board[0][2]
    elif board[0][0] == letter and board[1][1] == letter and board[2][2] == letter:
        return board[0][0]
    elif board[2][0] == letter and board[1][1] == letter and board[0][2] == letter:
        return board[2][0]
    else:
        return 'none'

print('Welcome to Tictactoe')
print('1 2 3 \n4 5 6 \n7 8 9')
if input('Is the player going first? ') == 'yes':
    playerMove(gameboard)

while True:
    print('----------------------------')
    computerChosen = computerMove(gameboard)
    y, x = computerChosen.split(',')
    x, y = int(x), int(y)
    gameboard[y][x] = 'O'
    winner = checkIfOver(gameboard, 'O')
    if winner == 'O':
        break
    notFinished = False
    for row in gameboard:
        for each in row:
            if each == '-':
                notFinished = True
    if notFinished == False:
        break
    playerMove(gameboard)
    winner = checkIfOver(gameboard, 'X')
    if winner == 'X':
        break
    notFinished = False
    for row in gameboard:
        for each in row:
            if each == '-':
                notFinished = True
    if notFinished == False:
        break

for row in gameboard:
    print(' '.join(row))

print(winner, 'has won the game!') if winner != 'none' else print('The game was a draw.')