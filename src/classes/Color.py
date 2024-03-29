import math


class Color:
    """ Simple class for manipulating color values"""

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return 'rgb(' + str(math.floor(self.r)) + ',' + str(math.floor(self.g)) + ',' + str(math.floor(self.b)) + ')'

    def __sub__(self, other):
        return Color(self.r - other.r, self.g - other.g, self.b - other.b)

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b


