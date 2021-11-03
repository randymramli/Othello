DISTANCE_FROM_GRID = 20


class Coin:
    '''Class to generate a coin'''
    def __init__(self, x, y, color, size):
        '''Initialize coin with X, Y coordinate and color'''
        self.x = x
        self.y = y
        self.color = color
        self.diameter = size - DISTANCE_FROM_GRID

    def display(self):
        '''Function to draw the coin'''
        fill(self.color)
        ellipse(self.x, self.y, self.diameter, self.diameter)
