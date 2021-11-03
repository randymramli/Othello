from coin import Coin
from game_controller import GameController
from computerAI import ComputerAI

BLACK = 0
WHITE = 255


class Board:
    '''Class to generate the board for othello'''
    def __init__(self, size, width, height):
        '''Initialize the board with the size and
        desired number of rows and columns'''
        self.size = size
        self.width = width
        self.height = height
        self.spacing = width//size
        self.gc = GameController(width, height, size)
        # count the size of the square based on window size and
        # amount of column and rows
        self.board_array = []
        self.color = BLACK
        self.game_over = False
        self.coin_storage = set()
        self.prev_move = False

    def game_start(self):
        
        for _i in range(self.size):
            current_list = []
            for _j in range(self.size):
                current_list.append(None)
            self.board_array.append(current_list)
            
        mid_bot_row = self.size // 2
        mid_top_row = mid_bot_row - 1
        mid_right_col = self.size // 2
        mid_left_col = mid_right_col - 1
        # array index of the first 4 coins

        left_x = (mid_left_col * self.spacing) + self.spacing//2
        right_x = (mid_right_col * self.spacing) + self.spacing//2
        top_y = (mid_top_row * self.spacing) + self.spacing//2
        bot_y = (mid_bot_row * self.spacing) + self.spacing//2
        # coordinates of the first 4 coins

        self.board_array[mid_top_row][mid_left_col] = Coin(left_x, top_y, 255, self.spacing)
        self.board_array[mid_top_row][mid_right_col] = Coin(right_x, top_y, 0, self.spacing)
        self.board_array[mid_bot_row][mid_left_col] = Coin(left_x, bot_y, 0, self.spacing)
        self.board_array[mid_bot_row][mid_right_col] = Coin(right_x, bot_y, 255, self.spacing)

    def display(self, answer):
        '''Draw the board on to the screen'''
        X = 0
        Y = 0
        stroke(0, 0, 0)
        strokeWeight(4)
        while (X < self.width):
            line(X, Y, X, self.height)
            X += self.spacing
        while (Y < self.height):
            line(0, Y, self.width, Y)
            Y += self.spacing
            
        # use while loop to draw the grids
        for x in range(self.size):
            for y in range(self.size):
                if self.board_array[x][y] is not None:
                    self.board_array[x][y].display()
        
        black_count = self.gc.end_game(self.board_array, self.coin_storage)
        if self.gc.game_over is True:
            self.gc.display_winner()
            if self.score is True:
                self.add_score("scores.txt", user_name, black_count)
                self.score = False
            return True

    def check_coin(self, mouseX, mouseY):
        self.coin_storage.add((mouseX, mouseY))
        self.midpoint = self.spacing / 2
        Y = int(mouseX // self.spacing)
        print(Y)
        X = int(mouseY // self.spacing)
        print(Y)
        legal_moves = self.gc.get_legal_moves(self.board_array, self.color)
        print("legal1: ",legal_moves)
        if self.gc.legal_moves(self.board_array, self.color, X, Y):
            print('flip=', self.gc.flip_list)
            self.place_coin(X, Y)


    def player_move(self):
        if self.gc.game_over is False:
            legal_moves = self.gc.get_legal_moves(self.board_array, self.color)
            if len(legal_moves) == 0:
                if self.prev_move is True:
                    self.gc.game_over = True
                else:
                    self.prev_move = True
                print("No more valid moves")
                self.color = WHITE
            else:
                self.prev_move = False

    def comp_move(self):
        if self.gc.game_over is False:
            legal_moves = self.gc.get_legal_moves(self.board_array, self.color)
            print("legal2: ",legal_moves)
            if len(legal_moves) != 0:
                comp_move = ComputerAI(legal_moves, self.size)
                x, y = comp_move.best_position()
                if self.gc.legal_moves(self.board_array, self.color, x, y):
                    print("2nd flip: ",self.gc.flip_list)
                    self.place_coin(x, y)
                    self.prev_move = False
            else:
                if self.prev_move is True:
                    self.gc.game_over = True
                else:
                    self.prev_move = True
                print("No more valid moves")

    def place_coin(self, array_column, array_row):
        # formulas to find where to draw the coins
        X_pos = (array_column * self.spacing) + self.midpoint
        Y_pos = (array_row * self.spacing) + self.midpoint
        print(array_column, array_row, X_pos, Y_pos)
        print('---')
        self.board_array[array_row][array_column] = Coin(X_pos, Y_pos, self.color, self.spacing)
        if self.color == BLACK:
            self.color = WHITE
        else:
            self.color = BLACK
        self.flip_coins()

    def update(self, black, white):
        '''Function to check on the winner'''
        Total_square = self.row_amount * self.column_amount
        if black + white == Total_square:
            self.gc.game_over = True

    def flip_coins(self):
        for x, y in self.gc.flip_list:
            if self.board_array[x][y].color == WHITE:
                self.board_array[x][y].color = BLACK
            else:
                self.board_array[x][y].color = WHITE
    
    
    def add_score(self, file_name, user_name, black_count):
        try:
            open_file = open(file_name, "r+")
            score_data = []
            result = user_name + " " + str(black_count)
            for line in open_file:
                score_data.append(line)
            if len(score_data) == 0:
                open_file.write(result)
            else:
                first_line_words = score_data[0].split()
                prev_score = int(first_line_words[len(first_line_words) - 1])
                if black_count > prev_score:
                    open_file.seek(0)
                    result += "\n"
                    for line in score_data:
                        result += line
                    open_file.write(result)
                else:
                    result = "\n" + result
                    open_file.write(result)
                open_file.close()
        except:
            print(file_name, "does not exist")
