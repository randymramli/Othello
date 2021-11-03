from random import randint


class ComputerAI():
    def __init__(self, legal_moves, size):
        self.legal_moves = legal_moves
        self.size = size
   
    def best_position(self):
        self.side_pos()
        legal_moves_amount = len(self.legal_moves)

        move = None
        if self.corner_position() is not None:
            move = self.corner_position()
        elif self.side_pos() is not None:
            move = self.side_pos()
        else:
            if legal_moves_amount > 0:
                move = self.legal_moves[0]
        return move
            
    def corner_position(self):
        corner_positions = [(0, 0), (0, self.size - 1), (self.size - 1, 0),
                            (self.size - 1, self.size - 1)]
        for location in corner_positions:
            if self.legal_moves.count(location) > 0:
                return location
    
    def side_pos(self):
        side_position = []
        for i in range(0, self.size):
            side_position.append((0, i))
            side_position.append((i, 0))
            side_position.append((self.size - 1, i))
            side_position.append((i, self.size - 1))
        for position in side_position:
            if self.legal_moves.count(position) > 0:
                return position
