from board import Board
from coin import Coin
from game_controller import GameController

WIDTH = 800
HEIGHT = 800
# window sizes are made constant
SIZE = 8
BLACK = 0
WHITE = 255
DELAY_TIME = 10
delay_count = 0
player_turn = False
answer = ''

gc = GameController(WIDTH, HEIGHT, SIZE)
board = Board(SIZE, WIDTH, HEIGHT)


def setup():
    '''Function to setup the board'''
    size(WIDTH, HEIGHT)
    background(34, 139, 35)
    board.game_start()
    answer = input('enter your name')
    if answer:
        print('hi ' + answer)
    elif answer == '':
        print('[empty string]')
    else:
        print(answer)
        # Canceled dialog will print None
    print("Your turn")


def input(message):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)


def draw():
    global delay_count
    global player_turn
    global answer

    if not board.display(answer):
        # Take computer's turn
        if board.color == WHITE:
            if delay_count == DELAY_TIME:
                delay_count = 0
                player_turn = True
                board.comp_move()
            elif delay_count == 0:
                print("Computer's turn.")
                delay_count += 1
            else:
                delay_count += 1
        # Checks of user has valid move
        else:
            if player_turn:
                print("Your turn.")
                board.player_move()
                player_turn = False


def mousePressed():
    '''Function to check input from mouse'''
    if board.color == BLACK:
        if (mouseX >= 0) and (mouseX < WIDTH) and \
           (mouseY >= 0) and (mouseY < HEIGHT):
            board.check_coin(mouseX, mouseY)
        else:
            pass
