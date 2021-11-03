BLACK = 0
WHITE = 255


class GameController:
    '''Class to check who wins or lose'''
    def __init__(self, width, height, size):
        self.width = width
        self.height = height
        self.player_wins = False
        self.computer_wins = False
        self.size = size
        self.total_coin = size * size
        self.game_over = False
        self.flip_list = []
        self.Black_count = 0
        self.White_count = 0
        self.winner_score = 0
        self.lose_score = 0
        self.fin_message = ''

    def end_game(self, board_array, coin_storage):
        """Carries out necessary actions if computer or player wins"""
        current_coin = len(coin_storage)
        if current_coin == self.total_coin:
            self.game_over = True
        if self.game_over is True:
            black_count, white_count = self.count_colours(board_array)
            if black_count > white_count:
                self.winner = "Black"
                self.winner_score = black_count
                self.lose_score = white_count
            elif white_count > black_count:
                self.winner = "White"
                self.winner_score = white_count
                self.lose_score = black_count
            else:
                self.winner_score = black_count
                self.lose_score = white_count
            return black_count


    def count_colours(self,board_array):
        for x in range(self.row_amount):
            for y in range(self.column_amount):
                if board_array[x][y] is not None:
                    if board_array[x][y].color == BLACK:
                        self.Black_count += 1
                    else:
                        self.White_count += 1
                        
        return Black_count, White_count
    

    def legal_moves(self, board_array, color, x, y):
        self.flip_list = []
        if color == BLACK:
            other_color = WHITE
        else:
            other_color = BLACK
        neighbor_coord = [(1, 0), (0, 1), (-1, 1), (1, -1), (1, 1),
                          (-1, -1), (-1, 0), (0, -1)]
        for x_neighbor, y_neighbor in neighbor_coord:
            new_x = int(x + x_neighbor)
            new_y = int(y + y_neighbor)
            if self.onboard(new_x, new_y):
                location = board_array[new_x][new_y]

                while location is not None and location.color == other_color:
                    new_x = int(new_x + x_neighbor)
                    new_y = int(new_y + y_neighbor)
                    if not self.onboard(new_x, new_y):
                        break
                    location = board_array[new_x][new_y]

                if location is not None and location.color == color:
                    while new_x != x or new_y != y:
                        new_x = int(new_x - x_neighbor)
                        new_y = int(new_y - y_neighbor)
                        if new_x != x or new_y != y:
                            self.flip_list.append((new_x, new_y))
        if len(self.flip_list) == 0:
            return False
        return True

    def onboard(self, X, Y):
        '''Function to check if coordinate is in board or no'''
        return X >= 0 and X < self.size and Y >= 0 and Y < self.size

    def get_legal_moves(self, board_array, color):
        legal_moves = []
        for x in range(self.size):
            for y in range(self.size):
                location = board_array[x][y]
                if location is None and\
                   self.legal_moves(board_array, color, x, y):
                    legal_moves.append((x, y))
        return legal_moves
    
    def display_winner(self):
        if self.winner is None:
            message = "TIE, {0} - {1}".format(self.win_score, self.lose_score)
        else:
            message = "{} Wins, {} - {}".format(self.winner, self.win_score,
                                                self.lose_score)
        self.display_mssg(message)

    def display_mssg(self, message):
        """Displays the end game message"""
        textSize(32)
        tw = textWidth(message)
        ta = textAscent()
        td = textDescent()

        stroke(0)
        strokeWeight(4)
        fill(WHITE)
        rectMode(CENTER)
        rect(MSSG_SIZE, MSSG_SIZE, tw + 20, ta + td + 20)

        fill(50)
        textAlign(CENTER, CENTER)
        text(message, MSSG_SIZE, MSSG_SIZE)
