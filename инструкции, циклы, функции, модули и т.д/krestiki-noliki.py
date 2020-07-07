empty_board = {'1': ' 1 ', '2': ' 2 ', '3': ' 3 ',
               '4': ' 4 ', '5': ' 5 ', '6': ' 6 ',
               '7': ' 7 ', '8': ' 8 ', '9': ' 9 '}


def printed(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('---+---+---')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('---+---+---')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


turn = ' X '
for i in range(9):
    printed(empty_board)
    print('Сейчас ходит', turn)
    move = input('В какую клетку?: ')
    empty_board[move] = turn
    if turn == ' X ':
        turn = ' O '
    else:
        turn = ' X '
printed(empty_board)
